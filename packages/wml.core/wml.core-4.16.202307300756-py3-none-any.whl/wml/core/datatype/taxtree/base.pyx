# distutils: language = c++

import numpy as np
cimport numpy as np
import pandas as pd

from libcpp.utility cimport pair
from libcpp.set cimport set
from libcpp.vector cimport vector
from libcpp.deque cimport deque
from libcpp.string cimport string

# C/C++ typedefs
ctypedef vector[int] vect_int
ctypedef set[int] set_int
ctypedef pair[string,string] pair_str


cdef class Taxtree:
    """A growing taxonomy tree

    Notes
    -----
    It is guaranteed that children ids are greather than parent id for all nodes.
    """

    # C/C++ vars

    cdef int c_nbNodes
    cdef vect_int c_idxParent
    cdef vector[vect_int] c_idxChildren
    cdef vector[string] c_taxcode

    # methods

    def __cinit__(self):
        self.c_nbNodes = 0

    cpdef int nbElems(self):
        """Returns the number of elements in the tree."""
        return self.c_nbNodes

    cdef int alloc(self):
        cdef int nb = self.c_nbNodes+1
        self.c_nbNodes = nb
        self.c_idxParent.resize(nb)
        self.c_idxChildren.resize(nb)
        self.c_taxcode.resize(nb)
        return nb-1

    cpdef bint exists(self, const string& taxcode):
        """Checks if a taxcode exists in the tree."""
        cdef int idx
        for idx in range(self.c_nbNodes):
            if self.c_taxcode[idx] == taxcode:
                return True
        return False

    cpdef int find(self, const string& taxcode):
        """Finds the tree index of a given taxcode.

        Parameters
        ----------
            taxcode : bytes
                the taxcode

        Returns
        -------
            idx : int
                the tree index or -1 for not found
        """
        cdef int idx
        for idx in range(self.c_nbNodes):
            if self.c_taxcode[idx] == taxcode:
                return idx
        return -1

    cpdef int insert(self, const string& taxcode, const string& parentCode):
        """Inserts a new taxcode to the taxtree.

        Parameters
        ----------
            taxcode : bytes
                the taxcode
            parentCode : bytes
                the parent taxcode

        Returns
        -------
            idx : int
                the newly inserted tree index
        """
        cdef int idx
        if self.c_nbNodes == 0:
            self.alloc()
            self.c_idxParent[0] = -1
            self.c_taxcode[0] = taxcode
            return 0

        idxParent = self.find(parentCode)
        if idxParent < 0:
            raise ValueError("Parent node with taxcode '{}' does not exist.".format(parentCode.decode()))
        idx = self.alloc()
        self.c_idxParent[idx] = idxParent
        self.c_idxChildren[idxParent].push_back(idx)
        self.c_taxcode[idx] = taxcode
        return idx

    cpdef int parent(self, int idx):
        """Gets the parent index of a given taxcode index."""
        return self.c_idxParent[idx]

    cpdef vect_int children(self, int idx):
        """Gets the list of child indices of a given taxcode index."""
        return self.c_idxChildren[idx]

    cpdef string taxcode(self, int idx):
        """Gets the taxcode of a given tree index."""
        return self.c_taxcode[idx]

    cpdef bint isLeaf(self, int idx):
        """Checks if a given tree index is a leaf node."""
        return self.c_idxChildren[idx].empty()

    cpdef bint isRoot(self, int idx):
        """Checks if a given tree index is the root node."""
        return self.c_idxParent[idx] == -1

    cpdef vect_int reversedPath(self, int idx):
        """Gets the reversed path to the root node of a tree index."""
        cdef vect_int p
        cdef int i = idx
        while i != -1:
            p.push_back(i)
            i = self.c_idxParent[i]
        return p

    cpdef int ancestorLevel(self, int idx, int ancestorIdx):
        cdef int i = idx
        cdef int j = 0
        while i != -1:
            if i == ancestorIdx:
                return j
            i = self.c_idxParent[i]
            j += 1
        return -1

    cpdef int lca(self, int idxA, int idxB):
        """Finds the least common ancestor of two tree indices."""
        cdef vect_int pA, pB
        cdef int i
        if idxA == idxB:
            return idxA
        pA = self.reversedPath(idxA)
        pB = self.reversedPath(idxB)
        while not pA.empty() and not pB.empty():
            if pA.back() == pB.back():
                i = pA.back()
                pA.pop_back()
                pB.pop_back()
            else:
                break
        return i

    cpdef bint separated(self, int idxA, int idxB):
        """Checks if two indices are separated or not."""
        idxC = self.lca(idxA, idxB)
        return (idxC != idxA) and (idxC != idxB)

    cpdef bint covers(self, int idxA, int idxB):
        """Checks if the first index covers the second index."""
        idxC = self.lca(idxA, idxB)
        return idxC == idxA

    cpdef bint coveredBy(self, int idxA, int idxB):
        """Checks if the first index is covered by the second index."""
        idxC = self.lca(idxA, idxB)
        return idxC == idxB

    cpdef vect_int coveredElems(self, int idx, bint leafOnly=False):
        """Finds all elements covered by a given element.

        Parameters
        ----------
        idx : int
            index of the input element
        leafOnly : bool
            whether to only return leaf nodes or not

        Returns
        -------
        res : list
            list of elements covered by the given element
        """
        cdef vect_int t1, t2
        cdef int i
        t1.push_back(idx)
        while not t1.empty():
            i = t1.back()
            t1.pop_back()
            if not leafOnly or self.c_idxChildren[i].empty():
                t2.push_back(i)
            if not self.c_idxChildren[i].empty():
                t1.insert(t1.end(), self.c_idxChildren[i].begin(), self.c_idxChildren[i].end())

        return t2

    cpdef vect_int minimumCoverSet(self, vect_int& core_set):
        """Returns the minimum cover set that contains the elements in the core set."""
        cdef set_int curSet
        cdef int i, j, k
        cdef vect_int path

        # root node
        curSet.insert(0)

        for i in core_set:
            if curSet.count(i) > 0:
                continue

            # go up until either we hit -1 or an element of curSet
            path.clear()
            k = i
            while True:
                j = self.c_idxParent[k]
                if j == -1: # reached above the root and found no element of curSet
                    path.clear()
                    break
                path.push_back(j)
                if curSet.count(j) > 0:
                    break
                k = j

            # go down via path and expand curSet along the way
            while not path.empty():
                j = path.back() # parent
                path.pop_back()

                curSet.erase(j)
                for k in self.c_idxChildren[j]:
                    curSet.insert(k)

        # extract data out
        path.clear()
        for k in curSet:
            path.push_back(k)
        return path

    cpdef vect_int find_relatives(self, int idxA, int idxD):
        """Finds the relatives in the following problem.

        Given a pair of ancestor code and descendant code, there is a unique path P that goes from
        the ancestor to the descendant (excluding the descendant). The goal is to find every code
        which is a child of one of codes in P and is different from the descendant.

        Parameters
        ----------
        idA : int
            the tree index of the ancestor code
        idD : int
            the tree index of the descendant code

        Returns
        -------
        res : list
            list of elements (in tree index) satisfying the problem above. The list can be empty.
        """

        cdef vect_int relatives

        if idxA == idxD:
            return relatives

        idxP = self.c_idxParent[idxD]
        relatives = self.find_relatives(idxA, idxP)
        for idx in self.c_idxChildren[idxP]:
            if idx == idxD:
                continue
            relatives.push_back(idx)

        return relatives


    cdef void disjoint_process(self, int idxA, vect_int& l_disjointIndices):
        cdef vect_int rels

        for idxB in l_disjointIndices:
            idxC = self.lca(idxA, idxB)

            if idxC == idxA:  # new code covers old code
                rels = self.find_relatives(idxA, idxB)
                for idxC in rels:
                    self.disjoint_process(idxC, l_disjointIndices)
                return

            if idxC == idxB:  # old code covers new code
                for i in range(len(l_disjointIndices)):
                    if l_disjointIndices[i] == idxB:
                        l_disjointIndices[i] = idxA
                        break
                rels = self.find_relatives(idxB, idxA)
                for idxC in rels:
                    l_disjointIndices.push_back(idxC)
                return

        l_disjointIndices.push_back(idxA)


    cpdef vect_int disjoint(self, vect_int& l_indices):
        """Disjoints a list of tree indices so that every pair of indices is disjoint.

        Parameters
        ----------
        l_indices : list
            list of input tree indices.

        Returns
        -------
        l_disjointIndices : dict
            the output list of disjoint indices
        """
        cdef vect_int l_disjointIndices

        for idx in l_indices:
            self.disjoint_process(idx, l_disjointIndices)

        return l_disjointIndices


    cpdef vect_int visitDFS(self, int idx=0):
        """Returns a visiting sequence that visits all nodes covered by a given node (default to global root), in a depth-first search order.

        Notes
        -----
        This function is obsolete when idx=0 because children ids are guaranteed to be greater than
        parent id for all nodes and when idx=0, all nodes are visited.
        """
        cdef int i, j
        cdef set_int curSet
        cdef vect_int stack
        cdef vect_int visit_seq

        # current root node
        i = idx
        curSet.insert(i)
        stack.push_back(i)
        visit_seq.push_back(i)

        # iterate
        while not stack.empty():
            i = stack.back()
            stack.pop_back()

            for j in self.c_idxChildren[i]:
                if curSet.count(j) == 0:
                    curSet.insert(j)
                    stack.push_back(j)
                    visit_seq.push_back(j)

        return visit_seq


def load_taxtree(df: pd.DataFrame, logger=None) -> Taxtree:
    """Loads the taxtree from a dataframe.

    Parameters
    ----------
    df : pandas.DataFrame
        The taxtree dataframe containing columns `['taxcode', 'parent_taxcode']`. There must be a
        single root taxcode whose parent taxcode is null. Every other row must have a valid
        parent taxcode.
    logger: logging.Logger or None
        logger for debugging

    Returns
    -------
    retval : Taxtree
        the generated taxtree
    """

    cdef deque[pair_str] v
    cdef pair_str p

    a = Taxtree()

    for index, row in df.iterrows():
        try:
            taxcode = row['taxcode'].encode()
        except:
            raise ValueError("Error turning query taxcode '{}' into bytes.".format(row['taxcode']))

        parentCode = row['parent_taxcode']
        if pd.isnull(parentCode):
            a.insert(taxcode, b'')
        else:
            try:
                parentCode = parentCode.encode()
            except:
                raise ValueError("Error turning parentCode '{}' of taxcode '{}' into bytes.".format(parentCode, row['taxcode']))
            if a.exists(parentCode):
                a.insert(taxcode, parentCode)
            else:
                v.push_back(pair_str(taxcode, parentCode))

    while not v.empty():
        p = v.front()
        v.pop_front()
        if a.exists(p.second):
            a.insert(p.first, p.second)
        else:
            v.push_back(p)
            if logger:
                logger.debug("Throwing ('{}','{}') back at the deque.".format(p.first.decode(), p.second.decode()))
    return a
