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





