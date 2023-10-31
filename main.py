import csv
import logging

from models.sudoku import Sudoku

logging.basicConfig(filename="logs.log",
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.DEBUG)

def bkt_with_fc_mrv(sudoku: Sudoku):
    if sudoku.is_complete():
        return True
    
    print(sudoku.domain_matrix)

    i, j = sudoku.get_next_unassigned_variable()

    for value in sudoku.domain_matrix[i][j]:
        if sudoku.is_consistent(value=value, i=i, j=j):
            print(f"value {value} is consistent")


def main():
    examples = ["1"]

    for example in examples:
        sudoku = Sudoku()

        with open(f"in/{example}.csv",'r') as file:
            reader = csv.reader(file, delimiter=",")
            domain_matrix = []
            for reader_row in reader:
                row = []
                for value in reader_row:
                    value = int(value)
                    if value > 0:
                        row.append(set([value]))
                    elif value % 2 == 0: #it is -2 => empty grey cell 
                        row.append(set([2, 4, 6, 8]))
                    else: # it is -1 => normal empty cell
                        row.append(set([1, 2, 3, 4, 5, 6, 7, 8, 9]))
            

                domain_matrix.append(row)
            
            # Instantiate a puzzle to solve
            sudoku.domain_matrix = domain_matrix
            sudoku.clean_domains()

        bkt_with_fc_mrv(sudoku=sudoku)
        
        with open(f"out/{example}.csv",'w') as sud_out:
            writer = csv.writer(sud_out,lineterminator="\n")

            for row in sudoku.domain_matrix:
                writer.writerow(row)


if __name__ == "__main__":
    main()
