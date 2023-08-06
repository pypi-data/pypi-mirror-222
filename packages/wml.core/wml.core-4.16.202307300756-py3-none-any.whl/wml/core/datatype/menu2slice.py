"""Menu-scoped mappings between menu codes and slice codes.
"""
from copy import copy
from tqdm import tqdm

from mt import tp, pd, logg


def merge2base_taxtree_df(
    base_taxtree_df: pd.DataFrame,
    l_menuCodes: tp.List[str],
    logger: tp.Optional[logg.IndentedLoggerAdapter] = None,
) -> pd.DataFrame:
    """Merges a list of menu codes to a taxtree dataframe of base terms.

    Parameters
    ----------
    base_taxtree_df : pandas.DataFrame
        The input taxtree dataframe containing columns ``['code', 'parent_code']``. There must be
        no cycle among the code relationships. All codes must be base terms only and must have
        exactly 5 alphanumeric letters.
    l_menuCodes : list
        list of menu codes to be merged from
    logger : mt.logg.IndentedLoggerAdapter, optional
        logger for debugging purposes

    Returns
    -------
    sealed_taxtree_df : pandas.DataFrame
        The output taxtree dataframe containing columns ``['code', 'parent_code']``. Menu codes
        are assigned as children of their base terms. Each base term 'X1234' also comes with a
        child called 'X1234/' to represent all other children.
    root_code : str
        the root code
    """

    # clean up a bit
    columns = ["code", "parent_code"]
    base_taxtree_df = base_taxtree_df[columns].drop_duplicates().copy()

    # find the root codes
    set1 = set(base_taxtree_df["parent_code"].tolist())
    set2 = set(base_taxtree_df["code"].tolist())
    l_rootCodes = sorted(list(set1 - set2))
    l_baseCodes = sorted(list(set1 | set2))

    if len(l_rootCodes) == 0:
        raise ValueError("No root code detected.")
    if len(l_rootCodes) > 1:
        raise ValueError(f"Multiple root codes detected: {l_rootCodes}.")
    root_code = l_rootCodes[0]

    # add all the base codes with slash
    data = [(base_code + "/", base_code) for base_code in l_baseCodes]

    # add all the menu codes
    l_newMenuCodes = []
    l_newBaseCodes = []
    for menu_code in l_menuCodes:
        if menu_code in l_baseCodes:
            l_newMenuCodes.append(menu_code)
            continue
        parent_code = menu_code[:5]
        if parent_code not in l_baseCodes:
            if parent_code not in l_newBaseCodes:
                l_newBaseCodes.append(parent_code)
        if menu_code != parent_code:
            data.append((menu_code, parent_code))
        l_newMenuCodes.append(menu_code)

    n_newBaseCodes = len(l_newBaseCodes)
    if n_newBaseCodes > 0:
        msg = f"Added new {n_newBaseCodes} baseterms to root code {root_code}."
        logg.warn(msg, logger=logger)
        for base_code in l_newBaseCodes:
            data.append((base_code, root_code))
            data.append((base_code + "/", base_code))

    # make a new dataframe
    df = pd.DataFrame(columns=columns, data=data)
    sealed_taxtree_df = (
        pd.concat([base_taxtree_df, df]).sort_values(columns).reset_index(drop=True)
    )

    return sealed_taxtree_df, root_code


def merge2sealed_taxtree_df(
    sealed_taxtree_df: pd.DataFrame,
    l_menuCodes: tp.List[str],
    logger: tp.Optional[logg.IndentedLoggerAdapter] = None,
) -> pd.DataFrame:
    """Merges a list of menu codes to a sealed taxtree dataframe.

    Parameters
    ----------
    sealed_taxtree_df : pandas.DataFrame
        The input taxtree dataframe containing columns ``['code', 'parent_code']``. It must be
        an output dataframe by invoking :func:`merge2base_taxtree_df`.
    l_menuCodes : list
        list of menu codes to be merged from
    logger : mt.logg.IndentedLoggerAdapter, optional
        logger for debugging purposes

    Returns
    -------
    unsealed_taxtree_df : pandas.DataFrame
        The output taxtree dataframe containing columns ``['code', 'parent_code']``. For each menu
        code 'X1234BLABLAH`, its base term `X1234` is compared against the dataframe. If the base
        term does not exist, the menu code is not merged. If the the base term does exist, the menu
        code is assigned as a child of the 'X1234/' code.
    root_code : str
        the root code
    """

    # clean up a bit
    columns = ["code", "parent_code"]
    sealed_taxtree_df = sealed_taxtree_df[columns].drop_duplicates().copy()

    # build a list of all full codes
    l_fullCodes = sealed_taxtree_df["code"].tolist()
    l_fullCodes += sealed_taxtree_df["parent_code"].tolist()
    l_fullCodes = set(l_fullCodes)

    # find the root codes
    df = sealed_taxtree_df[sealed_taxtree_df["code"].str.len() == 5]
    l_parentCodes = df["parent_code"].drop_duplicates().tolist()
    l_codes = df["code"].drop_duplicates().tolist()
    set1 = set([x[:5] for x in l_parentCodes])
    set2 = set([x[:5] for x in l_codes])
    l_rootCodes = sorted(set1 - set2)
    l_baseCodes = sorted(set1 | set2)

    if len(l_rootCodes) == 0:
        raise ValueError("No root code detected.")
    if len(l_rootCodes) > 1:
        raise ValueError(f"Multiple root codes detected: {l_rootCodes}.")
    root_code = l_rootCodes[0]

    # add all the menu codes
    l_newMenuCodes = []
    l_newBaseCodes = []
    data = []
    for menu_code in l_menuCodes:
        if menu_code in l_fullCodes:
            l_newMenuCodes.append(menu_code)
            continue
        parent_code = menu_code[:5]
        if parent_code not in l_baseCodes:
            if parent_code not in l_newBaseCodes:
                l_newBaseCodes.append(parent_code)
        data.append((menu_code, parent_code + "/"))
        l_newMenuCodes.append(menu_code)

    n_newBaseCodes = len(l_newBaseCodes)
    if n_newBaseCodes > 0:
        msg = f"Added new {n_newBaseCodes} baseterms to root code {root_code}."
        logg.warn(msg, logger=logger)
        for base_code in l_newBaseCodes:
            data.append((base_code, root_code))
            data.append((base_code + "/", base_code))

    # make a new dataframe
    df = pd.DataFrame(columns=columns, data=data)
    unsealed_taxtree_df = (
        pd.concat([sealed_taxtree_df, df]).sort_values(columns).reset_index(drop=True)
    )

    return unsealed_taxtree_df, root_code


class Menu2SliceCodeMappings:
    """Menu-scoped mappings between menu codes and slice codes.

    As agreed with Cristina in the data team as of 2023/03/03.

    Parameters
    ----------
    taxtree_df : pandas.DataFrame
        The taxtree dataframe containing columns ``['code', 'parent_code']``. There must be no
        cycle among the code relationships. All codes must be base terms only.
    menuCode_df : pandas.DataFrame
        The dataframe of menu codes consisting of 2 columns ``['menu_id', 'menu_code']``. If a menu
        code appears in multiple menu ids, items from that menu code can be used in all those
        menus.
    missing_codes : {'warn', 'raise'}
        policy to deal with codes not living in the tree. 'warn' means to raise a warning message.
        'raise' means to raise a ValueError
    logger : mt.logg.IndentedLoggerAdapter, optional
        logger for debugging purposes

    Attributes
    ----------
    l_menuIds : list
        the global list of menu ids in the ascending order
    l_menuCodes : list
        the global list of menu codes in the ascending order
    dl_menuCodes : dict
        a dictionary mapping each menu id to a list of menu codes
    dl_mtaxCodes : dict
        a dictionary mapping each menu id to a list of mtax codes. A mtax code is a code on the
        taxonomy, such that the set of all mtax codes of a given menu id is disjoint and has
        minimum length.
    ddl_mtaxCodes : dict
        a dictionary of dictionaries mapping each (menu_id, menu_code) pair to a list of mtax
        codes.
    taxtree : wml.core.datatype.taxtree.Taxtree
        the taxonomy tree augmented with the global menu codes
    taxtree_df : pandas.DataFrame
        dataframe with  columns ``['taxcode', 'parent_taxcode']`` containing nodes on the taxonomy
        tree
    """

    def __init__(
        self,
        taxtree_df: pd.DataFrame,
        menuCode_df: pd.DataFrame,
        missing_codes: str = "warn",
        logger: tp.Optional[logg.IndentedLoggerAdapter] = None,
    ):
        from .taxtree import load_taxtree

        self.logger = logger

        menuCode_df["menu_id"] = menuCode_df["menu_id"].astype(int)
        self.l_menuIds = sorted(menuCode_df["menu_id"].drop_duplicates().tolist())

        # menu codes
        self.dl_menuCodes = {}
        for menu_id in self.l_menuIds:
            df2 = menuCode_df[menuCode_df["menu_id"] == menu_id]
            l_menuCodes = sorted(df2["menu_code"].drop_duplicates().tolist())
            self.dl_menuCodes[menu_id] = l_menuCodes

        # determine which merge function depending on whether there is a 'X1234/' kind of code
        is_sealed = False
        for code in taxtree_df["code"]:
            if code.endswith("/"):
                is_sealed = True
                break
        if is_sealed:
            msg = "Sealed taxtree dataframe with {} rows detected.".format(
                len(taxtree_df)
            )
            logg.info(msg, logger=logger)
            merge_func = merge2sealed_taxtree_df
        else:
            msg = "Base taxtree dataframe with {} rows detected.".format(
                len(taxtree_df)
            )
            logg.info(msg, logger=logger)
            merge_func = merge2base_taxtree_df

        # merge the menu codes to the taxtree dataframe
        self.l_menuCodes = sorted(menuCode_df["menu_code"].drop_duplicates().tolist())
        taxtree_df, root_code = merge_func(taxtree_df, self.l_menuCodes, logger=logger)

        # merge the root code to the taxtree dataframe
        df = pd.DataFrame(columns=["code", "parent_code"], data=[(root_code, None)])
        taxtree_df = pd.concat([taxtree_df, df])

        # make the tree
        taxtree_df.columns = ["taxcode", "parent_taxcode"]
        self.taxtree_df = taxtree_df
        self.taxtree = load_taxtree(self.taxtree_df)

        # mtax codes
        self.dl_mtaxCodes = {}
        self.ddl_mtaxCodes = {}
        thingy = tqdm(
            self.dl_menuCodes.items(),
            total=len(self.dl_menuCodes),
            desc="Project menus",
            unit="menu",
        )
        for menu_id, l_menuCodes in thingy:
            l_mtaxCodes = self.disjoint(l_menuCodes, missing_codes=missing_codes)
            dl_mtaxCodes = self.project_disjoint(
                l_menuCodes, l_mtaxCodes, disable_logging=True
            )
            self.dl_mtaxCodes[menu_id] = l_mtaxCodes
            self.ddl_mtaxCodes[menu_id] = dl_mtaxCodes

    def disjoint(
        self, l_codes: tp.List[str], missing_codes: str = "warn"
    ) -> tp.List[str]:
        """Disjoints a list of codes so that every pair of codes is disjoint.

        Parameters
        ----------
        l_codes : list
            list of input codes. Each code must live in the tree.
        missing_codes : {'warn', 'raise'}
            policy to deal with codes not living in the tree. 'warn' means to raise a warning
            message. 'raise' means to raise a ValueError

        Returns
        -------
        l_disjointCodes : dict
            the output sorted list of disjoint codes

        Raises
        ------
        ValueError
            if an input code does not live in the tree and the policy is to raise.
        """

        l_indices = []
        l_notFoundCodes = []
        for code in l_codes:
            idx = self.taxtree.find(code.encode())
            if idx < 0:
                l_notFoundCodes.append(code)
            else:
                l_indices.append(idx)

        if l_notFoundCodes:
            if missing_codes == "raise":
                raise ValueError("Detected codes not in the taxtree", l_notFoundCodes)
            elif missing_codes == "warn":
                logg.warn("Ignored codes not found in the taxtree:", logger=self.logger)
                logg.warn(l_notFoundCodes, logger=self.logger)
            else:
                raise ValueError(
                    f"Unknown value for 'missing_codes': '{missing_codes}'."
                )

        l_disjointIndices = self.taxtree.disjoint(l_indices)
        l_disjointCodes = [
            copy(self.taxtree.taxcode(idx).decode()) for idx in l_disjointIndices
        ]
        return sorted(l_disjointCodes)

    def project(self, code: str, l_disjointCodes: tp.List[str]) -> tp.List[str]:
        """Projects a code to a list of disjoint codes.

        Parameters
        ----------
        code : str
            an input code to project. It must live in the tree.
        l_disjointCodes : dict
            list of disjoint codes where the input code is projected to. No checking is conducted
            to ensure the codes are disjoint.

        Returns
        -------
        l_projectedCodes : list
            a subset of `l_disjointCodes` representing the list of projected codes
        """

        idxA = self.taxtree.find(code.encode())

        # upward projection
        for disjoint_code in l_disjointCodes:
            idxB = self.taxtree.find(disjoint_code.encode())
            if self.taxtree.coveredBy(idxA, idxB):
                return [disjoint_code]

        # downward projection
        l_projectedCodes = []
        for disjoint_code in l_disjointCodes:
            idxB = self.taxtree.find(disjoint_code.encode())
            if self.taxtree.covers(idxA, idxB):
                l_projectedCodes.append(disjoint_code)
        return l_projectedCodes

    def project_disjoint(
        self,
        l_codes: tp.List[str],
        l_disjointCodes: tp.List[str],
        disable_logging: bool = False,
    ) -> tp.Dict[str, tp.List[str]]:
        """Projects a list of codes to a list of disjoint codes.

        Each disjoint code is assigned to all input codes which are its descendants, and to the
        closest ancestor input code, if it exists.

        Parameters
        ----------
        l_codes : list
            list of input codes to project. Each code must live in the tree.
        l_disjointCodes : dict
            list of disjoint codes where the input code is projected to. No checking is conducted
            to ensure the codes are disjoint.
        disable_logging : bool
            whether or not to disable the use of self.logger

        Returns
        -------
        dl_projectedCodes : dict
           a dictionary mapping each input code to a subset of `l_disjointCodes`
        """

        logger = None if disable_logging else self.logger

        msg = "Projecting {} codes to the disjoint set".format(len(l_codes))
        with logg.scoped_info(msg, logger=logger):
            l_indices = [copy(self.taxtree.find(code.encode())) for code in l_codes]
            l_dones = [False] * len(l_codes)

            l_disjointIndices = [
                copy(self.taxtree.find(code.encode())) for code in l_disjointCodes
            ]

            dl_projectedCodes = {code: [] for code in l_codes}

            # upward projections
            msg = "Upward projecting {} indices...".format(len(l_disjointIndices))
            logg.info(msg, logger=logger)
            for i, idxA in enumerate(l_disjointIndices):
                disjoint_code = l_disjointCodes[i]

                # find descendant input codes
                for j, idxB in enumerate(l_indices):
                    if l_dones[j]:
                        continue

                    if self.taxtree.coveredBy(idxB, idxA):
                        l_dones[j] = True
                        code = l_codes[j]
                        dl_projectedCodes[code].append(disjoint_code)

            # downward projections
            msg = "Downward projecting {} indices...".format(len(l_disjointIndices))
            logg.info(msg, logger=logger)
            for i, idxA in enumerate(l_disjointIndices):
                disjoint_code = l_disjointCodes[i]

                j = -1
                idxB = idxA
                while not self.taxtree.isRoot(idxB):
                    try:
                        j = l_indices.index(idxB)
                        break
                    except ValueError:
                        idxB = self.taxtree.parent(idxB)
                        continue

                if j >= 0 and not l_dones[j]:
                    code = l_codes[j]
                    dl_projectedCodes[code].append(disjoint_code)

        thingy = (
            l_codes
            if logger is None
            else tqdm(l_codes, total=len(l_codes), desc="Sorting projected codes")
        )
        for code in thingy:
            l_projectedCodes = dl_projectedCodes[code]
            dl_projectedCodes[code] = sorted(l_projectedCodes)

        return dl_projectedCodes

    def project_menus(
        self, l_disjointCodes: tp.List[str]
    ) -> tp.Tuple[pd.DataFrame, pd.DataFrame]:
        """Projects every menu's list of menu codes to a list of disjoint codes.

        The projection is done using :func:`project_disjoint` per menu.

        Parameters
        ----------
        l_disjointCodes : dict
            list of disjoint codes where the input code is projected to. No checking is conducted
            to ensure the codes are disjoint.

        Returns
        -------
        menu2slice_df : pandas
            a sorted dataframe of 3 columns ``['menu_id', 'menu_code', 'slice_codes']`` telling for
            each menu and each menu code, which slice codes it maps to
        slice2menu_df : pandas
            a sorted dataframe of 3 columns ``['menu_id', 'slice_code', 'menu_code']`` telling for
            each menu and each slice code, which menu code it maps to
        """

        # TODO: parallelise me

        data = []
        data2 = []
        things = tqdm(
            self.dl_menuCodes.items(),
            total=len(self.dl_menuCodes),
            unit="menu",
            desc="menu2slice",
        )
        for menu_id, l_menuCodes in things:
            dl_projectedCodes = self.project_disjoint(
                l_menuCodes, l_disjointCodes, disable_logging=True
            )
            for menu_code, l_sliceCodes in dl_projectedCodes.items():
                data2.append((menu_id, menu_code, l_sliceCodes))
                for slice_code in l_sliceCodes:
                    data.append((menu_id, slice_code, menu_code))

        menu2slice_df = pd.DataFrame(
            columns=["menu_id", "menu_code", "slice_codes"], data=data2
        )

        columns = ["menu_id", "slice_code", "menu_code"]
        slice2menu_df = (
            pd.DataFrame(columns=columns, data=data)
            .sort_values(columns)
            .reset_index(drop=True)
        )

        return menu2slice_df, slice2menu_df
