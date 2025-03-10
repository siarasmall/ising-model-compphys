class Node():
    def __init__(self, row: int, col: int, idx: int, spin: int) -> None:
        """
        Initializes a Node object.

        Arguments:
            - row: int = Row index of node in two dimensional representation.
            - col: int = Column index of node in two dimensional representation.
            - idx: int = Index of node in one dimensional representation.
            - spin: int = Spin of node. Possible values = {1, -1}
        """
        self.row = row
        self.col = col
        self.idx = idx
        self.spin = spin

    def row(self):
        """
        Returns the row of a given node.
        """
        return self.row

    def col(self):
        """
        Returns the column of a given node.
        """
        return self.col

    def idx(self):
        """
        Returns the one dimensional index of a given node.
        """
        return self.idx

    def spin(self):
        """
        Returns the spin of a given node.
        """
        return self.spin

    def set_row(self, i):
        """
        Sets the row of a given node to provided value.
        """
        self.row = i

    def set_col(self, i):
        """
        Sets the column of a given node to provided value.
        """
        self.col = i

    def set_idx(self, i):
        """
        Sets the one dimensional index of a given node to provided value.
        """
        self.idx = i

    def set_spin(self, i):
        """
        Sets the spin of a given node to provided value.
        """
        self.spin = i

    def flip(self):
        """
        Flips the spin of a node; 1 flips to -1, -1 flips to 1.
        """
        self.spin *= -1
