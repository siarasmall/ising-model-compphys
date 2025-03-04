class Node():
    def __init__(self, row, col, idx, spin) -> None:
        self.row = row
        self.col = col
        self.idx = idx
        self.spin = spin

    def get_row(self):
        return self.row

    def get_col(self):
        return self.col

    def get_idx(self):
        return self.idx

    def get_spin(self):
        return self.spin

    def set_row(self, i):
        self.row = i

    def set_col(self, i):
        self.col = i

    def set_idx(self, i):
        self.idx = i

    def set_spin(self, i):
        self.spin = i
