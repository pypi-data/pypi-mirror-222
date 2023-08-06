"""Extra functions about a taxtree."""

from mt import tp, np, pd

from .base import Taxtree


class LeafsetMapper:
    """Given a taxtree, mapping each set of tree nodes to a set of leaf taxcodes as a bool ndarray.

    Parameters
    ----------
    tt : Taxtree
        an input taxtree

    Attributes
    ----------
    N : int
        number of tree taxcodes
    M : int
        number of leaf taxcodes
    l_taxcodes : list
        a sorted list of leaf taxcodes
    df : pandas.DataFrame
        a dataframe with columns ['taxcode', 'leaf_set']. Each row represents a taxcode of the tree
        and its associated set of leaf taxcodes as a bool ndarray.
    """

    def __init__(self, tt: Taxtree):
        self.N = tt.nbElems()  # number of taxcodes

        # construct the taxcode list and make the map that goes from tree idx to list idx of each leaf
        l_leaves = []
        for i in range(self.N):
            if tt.isLeaf(i):
                l_leaves.append((tt.taxcode(i), i))
        l_leaves = sorted(l_leaves, key=lambda x: x[0])
        self.l_taxcodes = [x[0].decode() for x in l_leaves]
        mapLeaf_tree2list = {x[1]: i for i, x in enumerate(l_leaves)}
        self.M = len(l_leaves)  # number of leaf taxcodes

        # make the dataframe
        l_arrays = [None] * self.N

        def visit(i: int) -> np.ndarray:
            if l_arrays[i] is not None:
                return l_arrays[i]
            if tt.isLeaf(i):
                arr = np.eye(1, self.M, mapLeaf_tree2list[i], dtype=np.bool)[0]
            else:
                arr = np.zeros(self.M, dtype=np.bool)
                for j in tt.children(i):
                    arr |= visit(j)
            l_arrays[i] = arr
            return arr

        data = []
        for i in range(self.N):
            data.append((tt.taxcode(i).decode(), visit(i)))
        self.df = pd.DataFrame(columns=["taxcode", "leaf_set"], data=data)

    def compute_leafset(self, x) -> np.ndarray:
        """Maps a taxcodeset into an bool ndarray representing the set of leaf taxcodes.

        Parameters
        ----------
        x : str or list
            a valid tree taxcode or a valid taxcodeset where all the taxcodes exist in the tree

        Returns
        -------
        numpy.ndarray
            a bool ndarray representing the set of leaf taxcodes. See also :attr:`l_taxcodes`.
        """

        if isinstance(x, str):  # turn it into a list
            if "[" in x:
                import json

                x = json.loads(x)
            else:
                x = [x]
        elif not isinstance(x, list):
            raise ValueError(
                "Only a list or a str is accepted. Got type '{}'.".format(type(x))
            )

        df = self.df[self.df["taxcode"].isin(x)]
        if len(df) == 0:
            return np.zeros(self.M, dtype=np.bool)

        if len(df) == 1:
            return df["leaf_set"].iloc[0]

        union_arr = np.zeros(self.M, dtype=np.bool)
        for _, arr in df["leaf_set"].iteritems():
            union_arr |= arr

        return union_arr
