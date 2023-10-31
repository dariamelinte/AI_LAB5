class Sudoku:
    def __init__(self):
        self._domain_matrix = list()

    @property
    def domain_matrix(self):
        return self._domain_matrix

    @domain_matrix.setter
    def domain_matrix(self, domain_matrix):
        self._domain_matrix = domain_matrix

    def is_complete(self):
        for row in self.domain_matrix:
            for domain in row:
                if len(domain) != 1:
                    return False

        return True

    def get_next_unassigned_variable(self):
        next_i, next_j = -1, -1
        min_cardinality = 9

        for i in range(len(self.domain_matrix)):
            for j in range(len(self.domain_matrix[i])):
                domain = self.domain_matrix[i][j]
                if len(domain) == 1:  # the variable with this domain is already found
                    continue

                if len(domain) < min_cardinality:
                    next_i, next_j = i, j
                    min_cardinality = len(domain)

        return next_i, next_j

    # we are clearing the domains based on the initial values of the sudoku puzzle, for optimization
    def clean_domains(self):
        # clean domain based on rows
        for i in range(9):
            for j in range(9):
                domain = self.domain_matrix[i][j]
                if len(domain) != 1:
                    continue

                value = list(domain)[0]

                for k in range(9):
                    if k == j:
                        continue

                    self.domain_matrix[i][k].discard(value)

        # clean domain based on columns
        for i in range(9):
            for j in range(9):
                domain = self.domain_matrix[j][i]
                if len(domain) != 1:
                    continue

                value = list(domain)[0]

                for k in range(9):
                    if k == j:
                        continue

                    self.domain_matrix[k][i].discard(value)

        # clean domain in the small squares
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                for k in range(i, i + 3):
                    for l in range(j, j + 3):
                        domain = self.domain_matrix[k][l]
                        if len(domain) != 1:
                            continue

                        value = list(domain)[0]

                        for m in range(i, i + 3):
                            for n in range(j, j + 3):
                                if m == k and n == l:
                                    continue

                                self.domain_matrix[m][n].discard(value)

    def pinpoint_square(self, i, j):
        x1, y1, x2, y2 = -1, -1, -1, -1

        if 0 <= i <= 2:
            x1 = 0
            x2 = 2

        if 3 <= i <= 5:
            x1 = 3
            x2 = 5

        if 6 <= i <= 8:
            x1 = 6
            x2 = 8

        if 0 <= j <= 2:
            y1 = 0
            y2 = 2

        if 3 <= j <= 5:
            y1 = 3
            y2 = 5

        if 6 <= j <= 8:
            y1 = 6
            y2 = 8

        return (x1, y1), (x2, y2)

    def check_row(self, value, i, j):
        for k in range(9):
            if k == j:
                continue

            domain = self.domain_matrix[i][k]
            if len(domain) == 1 and value in domain:
                return False

        return True

    def check_column(self, value, i, j):
        for k in range(9):
            if k == i:
                continue

            domain = self.domain_matrix[k][j]
            if len(domain) == 1 and value in domain:
                return False

        return True

    def check_square(self, value, i, j):
        (x1, y1), (x2, y2) = self.pinpoint_square(i, j)

        for l in range(x1, x2 + 1):
            for m in range(y1, y2 + 1):
                if l == i and m == j:
                    continue
                domain = self.domain_matrix[l][m]
                print(f"DOMAIN ({l}, {m}): {domain}")
                if len(domain) == 1 and value in domain:
                    return False

        return True

    def is_consistent(self, value, i, j):
        return self.check_row(value, i, j) and self.check_column(value, i, j) and self.check_square(value, i, j)

    def is_empty_set(self):
        for i in range(9):
            for j in range(9):
                if len(self.domain_matrix[i][j]) == 0:
                    return True
        
        return False