"""
Please write a function named row_correct(sudoku: list, row_no: int), which takes a two-dimensional
array representing a sudoku grid, and an integer referring to a single row, as its arguments. Rows are indexed from 0.
The function should return True or False, depending on whether the row is filled in correctly,
that is, whether it contains each of the numbers 1 to 9 at most once.
"""

def check_row(sudoku:list, row_no: int):
    target_row = sudoku[row_no] # that will return a list inside sudoku nested list
    seen = []

    for num in target_row:
        if num == 0:
            continue
        else:
            if num not in seen:
                seen.append(num)
            else:
                return False
    return True
    



def main():
    sudoku = [
  [9, 0, 0, 0, 8, 0, 3, 0, 0],
  [2, 0, 0, 2, 5, 0, 7, 0, 0],
  [0, 2, 0, 3, 0, 0, 0, 0, 4],
  [2, 9, 4, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 7, 3, 0, 5, 6, 0],
  [7, 0, 5, 0, 6, 0, 4, 0, 0],
  [0, 0, 7, 8, 0, 3, 9, 0, 0],
  [0, 0, 1, 0, 0, 0, 0, 0, 3],
  [3, 0, 0, 0, 0, 0, 0, 0, 2]
]
    print(check_row(sudoku, 0))
    print(check_row(sudoku, 1))
    pass


main()