class Sudoku:
    def __init__(self):
        self._matrix = list()
        
    @property
    def matrix(self):
        return self._matrix

    @matrix.setter
    def matrix(self, matrix):
        self._matrix = matrix