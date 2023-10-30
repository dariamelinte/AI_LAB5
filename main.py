import csv
import logging

from models.sudoku import Sudoku

logging.basicConfig(filename="logs.log",
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.DEBUG)

def main():
    examples = ["1"]

    for example in examples:
        sudoku = Sudoku()

        with open(f"in/{example}.csv",'r') as file:
            reader = csv.reader(file, delimiter=",")
            matrix = []
            for row in reader:
                matrix.append(row)
            
            # Instantiate a puzzle to solve
            sudoku.matrix = matrix
        
        with open(f"out/{example}.csv",'w') as sud_out:
            writer = csv.writer(sud_out,lineterminator="\n")

            for row in sudoku.matrix:
                print(row)
                writer.writerow(row)


if __name__ == "__main__":
    main()
