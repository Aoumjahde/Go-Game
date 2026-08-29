def block_correct(sudoku:list, row_no:int, column_no:int):
    seen = []
    for i in range(row_no, row_no+3):
        for j in range(column_no, column_no+3):
            if sudoku[i][j] == 0:
                continue
            else:
                if sudoku[i][j]  not in seen:
                    seen.append(sudoku[i][j])
                else:
                    return False
    return True
    