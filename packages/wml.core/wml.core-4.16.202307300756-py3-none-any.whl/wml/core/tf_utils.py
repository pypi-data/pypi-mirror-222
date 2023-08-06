"""Useful TensorFlow-based util functions. The module requires tensorflow or tensorflow-gpu package."""


from mt.base.deprecated import deprecated_func
from mt.gpu import detect_machine, get_mem_info
from mt import tf  # to monkey-patch tf, if required


__all__ = [
    "is_tx2",
    "num_gpus",
    "tf_major_version",
    "tf1",
    "get_keras_session",
    "set_keras_session",
    "disable_eager_execution",
    "import_keras",
    "set_gpu_alloc_policy",
]


def is_tx2():
    """Detects if the machine is a TX2 without using TensorFlow.

    Returns
    -------
    bool
        whether or not we are on a TX2

    Notes
    -----
    You can also use :func:`mt.gpu.detect_machine` which is more general.
    """

    return detect_machine() in ["arm64-tx2", "arm64-j43", "arm64-j45", "arm64-n45"]


def num_gpus():
    """Counts the number of GPU devices that we can use.

    Returns
    -------
    int
        the number of GPU devices detected
    """

    return len(get_mem_info()["gpus"])


def tf_major_version():
    """Checks if TensorFlow has been installed and which major version are we on.

    Returns
    -------
    int
        -1 if no TensorFlow is imported. 0 to 2 corresponding to the major version.
    """
    try:
        import tensorflow as tf

        if tf.__version__ < "1.0.0":
            return 0
        if tf.__version__ < "2.0.0":
            return 1
        return 2
    except ImportError:
        return -1


def disable_eager_execution():
    """Disables eager execution if you are with TF2 or does nothing if not."""

    if tf_major_version() >= 2:
        import tensorflow as tf

        tf.compat.v1.disable_eager_execution()  # need to disable eager in TF2.x


def _import_tf1():
    tf_major = tf_major_version()
    if tf_major < 1:
        raise OSError(
            "Unsupported TensorFlow, major version {}. You need to install TensorFlow minimum version 1.15.".format(
                tf_major
            )
        )
    import tensorflow as tf

    return tf if tf_major < 2 else tf.compat.v1


tf1 = _import_tf1()


def import_keras(use_tf=True):
    """Imports keras, whether it is keras.io or tf.keras depends on the 'use_tf' boolean argument."""
    if use_tf:
        import tensorflow.keras as keras
    else:
        import keras
    return keras


def get_keras_session(use_tf=True):
    """Gets the current keras session, whether it is for keras.io or tf.keras depends on the 'use_tf' boolean argument."""
    if use_tf:
        return tf1.keras.backend.get_session()
    else:
        import keras.backend as K

        return K.get_session()


def set_keras_session(session, use_tf=True):
    """Sets the current keras session, whether it is for keras.io or tf.keras depends on the 'use_tf' boolean argument."""
    if use_tf:
        return tf1.keras.backend.set_session(session)
    else:
        import keras.backend as K

        return K.set_session(session)


def set_gpu_alloc_policy(
    target,
    gpu_max_memory=1024 * 1024 * 1024,
    allow_growth=True,
    interactive_session=False,
    logger=None,
):
    """Sets a policy for allocating gpu memory depending on the target. See notes.

    Parameters
    ----------
    target : {'mlkeras', 'tf1keras', 'tf2'}
        target session type to set a gpu memory allocation policy. See notes.
    gpu_max_memory : int or None
        maximum memory in bytes to be used by the GPU. If None is specified, we let TF decide.
    allow_growth : bool
        allow GPU allocation to grow dynamically or not
    interactive_session : bool
        whether or not to use a tf1.InteractiveSession. Only available if TF2+ is installed and target is 'tf1keras' or 'mlkeras'.
    logger : mt.logg.IndentedLoggerAdapter, optional
        the logger (optional)

    Notes
    -----
    If target is 'mlkeras', we create and return a new keras.Session with the policy defined by `gpu_max_memory` and `allow_growth`.
    If target is 'tf1keras', we create and return a new tf1.Session with the policy defined by `gpu_max_memory` and `allow_growth`.
    If target is 'tf2', we set the policy defined by `gpu_max_memory` on the current uninitialised tf2 config, but we return None. Argument `allow_growth` has no effect in this case.

    Raises
    ------
    ValueError
        if the target is not in the above list
    """

    if target in ["mlkeras", "tf1keras"]:
        use_tf = target == "tf1keras"
        if logger:
            logger.info("Current memory usage:")
            mem = get_mem_info(True)
        else:
            mem = get_mem_info(False)
        if len(mem["gpus"]) == 0:
            if logger:
                logger.warning(
                    "There is no GPU to set the policy for a '{}' session.".format(
                        target
                    )
                )
            return get_keras_session(use_tf=use_tf)  # current session

        if gpu_max_memory is None:
            config = tf1.ConfigProto(device_count={"CPU": 1, "GPU": len(mem["gpus"])})
            config.gpu_options.allow_growth = allow_growth
            if logger:
                logger.debug(
                    "Setting a {} session {} allowing growth on {} gpus.".format(
                        target, "with" if allow_growth else "without", len(mem["gpus"])
                    )
                )
        else:
            min_mem_total = min((gpu["mem_total"] for gpu in mem["gpus"]))
            fraction = gpu_max_memory / min_mem_total

            config = tf1.ConfigProto(device_count={"CPU": 1, "GPU": len(mem["gpus"])})
            config.gpu_options.per_process_gpu_memory_fraction = fraction
            config.gpu_options.allow_growth = allow_growth
            if logger:
                logger.debug(
                    "Setting a {} session with max gpu memory {} bytes {} allowing growth on {} gpus.".format(
                        target,
                        gpu_max_memory,
                        "with" if allow_growth else "without",
                        len(mem["gpus"]),
                    )
                )

        SessionType = (
            tf1.Session
            if tf_major_version() < 2 or not interactive_session
            else tf1.InteractiveSession
        )
        return set_keras_session(SessionType(config=config), use_tf=use_tf)

    if target == "tf2":
        if tf_major_version() < 2:
            raise ImportError("TensorFlow v2+ is not installed. Please install it.")

        if gpu_max_memory is None:
            if allow_growth:
                import tensorflow.config.experimental as tce

                gpus = tce.list_physical_devices("GPU")
                if gpus:
                    if logger:
                        logger.debug(
                            "Setting allowing growth in TF2 {} gpus.".format(len(gpus))
                        )
                    for gpu in gpus:
                        tce.set_memory_growth(gpu, True)
                else:
                    if logger:
                        logger.warning("There is no GPU to set the TF2 policy.")
            else:
                if logger:
                    logger.warning(
                        "There is nothing to do to set the GPU policy for TF2.".format(
                            target
                        )
                    )
        else:
            mega = 1024 * 1024
            memory_limit = (gpu_max_memory + mega - 1) // mega

            import tensorflow.config.experimental as tce

            gpus = tce.list_physical_devices("GPU")
            if gpus:
                if logger:
                    logger.debug(
                        "Setting in TF2 max gpu memory {} MBs on {} gpus.".format(
                            memory_limit, len(gpus)
                        )
                    )
                for gpu in gpus:
                    tce.set_virtual_device_configuration(
                        gpu, [tce.VirtualDeviceConfiguration(memory_limit=memory_limit)]
                    )
            else:
                if logger:
                    logger.warning("There is no GPU to set the TF2 policy.")

        return None

    raise ValueError(
        "Target must be in ['mlkeras', 'tf1keras', 'tf2']. Got '{}'.".format(target)
    )
