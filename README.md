# Go-Game

This project is a small Python-based Sudoku validation exercise. The goal is to check whether a 9x9 Sudoku grid follows the essential Sudoku rules:

- Each row contains digits 1 to 9 without repetition.
- Each column contains digits 1 to 9 without repetition.
- Each 3x3 sub-grid contains digits 1 to 9 without repetition.
- Empty cells are represented as 0 and are ignored during validation.

The implementation was built in stages, with separate functions for row, column, block, and full-grid validation.

## Project structure

- `check_row.py` – validates a single row
- `check_colum.py` – validates a single column
- `check_block.py` – validates a single 3x3 block
- `check_grid.py` – validates the complete Sudoku board
- `main.py` – example execution and manual checks
- `*_test.py` files – test scripts for each validation layer

## Approach 1: row validation

The first approach checks one row at a time using a `seen` list.

```python
def check_row(sudoku: list, row_no: int):
    target_row = sudoku[row_no]
    seen = []

    for num in target_row:
        if num == 0:
            continue
        if num not in seen:
            seen.append(num)
        else:
            return False
    return True
```

### How it works

- Reads the chosen row from the 2D list.
- Ignores zeros, because empty cells are allowed.
- Tracks each non-zero value in a list.
- If the same number appears twice, the function returns `False`.

This approach is simple and matches the basic Sudoku rule for rows.

## Approach 2: column validation

The second approach validates a column by constructing a temporary list of all values in that column.

```python
def column_correct(soduku: list, column_no: int):
    new_list = []
    for row in soduku:
        new_list.append(row[column_no])

    seen = []
    for num in new_list:
        if num == 0:
            continue
        if num not in seen:
            seen.append(num)
        else:
            return False

    return True
```

### How it works

- Extracts every value from the requested column.
- Uses the same duplicate-detection logic as row validation.
- Repeats are rejected immediately.

This keeps the logic consistent across rows and columns.

## Approach 3: 3x3 block validation

The project also checks each 3x3 block independently.

```python
def block_correct(sudoku: list, row_no: int, column_no: int):
    seen = []
    for i in range(row_no, row_no + 3):
        for j in range(column_no, column_no + 3):
            if sudoku[i][j] == 0:
                continue
            if sudoku[i][j] not in seen:
                seen.append(sudoku[i][j])
            else:
                return False
    return True
```

### How it works

- Iterates a 3x3 region starting from the provided top-left position.
- Checks the nine cells in that block for duplicates.
- Again, zeros are ignored.

This mirrors the Sudoku rule for sub-grids.

## Approach 4: full-board validation

The grid-level function combines all three checks.

```python
def sudoku_grid_correct(soduku: list):
    for row_no in range(0, 9, 3):
        if not check_row(soduku, row_no):
            return False

    for colomn_no in range(0, 9, 3):
        if not column_correct(soduku, colomn_no):
            return False

    for row_no in range(0, 9, 3):
        for colomn_no in range(0, 9, 3):
            if not block_correct(soduku, row_no, colomn_no):
                return False

    return True
```

### Important note

This function is intended to validate the whole board, but it currently checks only the first row and first column groupings in a way that is not a full Sudoku validation across all 9 row/column positions. In other words, the project uses a staged validation approach, but the logic is intentionally minimal and built as a learning exercise rather than a production-grade Sudoku engine.

## Test cases in the project

The repository includes test scripts for each validation stage.

### 1. Row tests: `check_row_test.py`

This script tests two conditions:

```python
sudoku = [
  [9, 0, 0, 0, 8, 0, 3, 0, 0],
  [2, 0, 0, 2, 5, 0, 7, 0, 0],
  ...
]

tests = [
    (0, True),
    (1, False),
]
```

Expected result:

- Row 0 is valid → `True`
- Row 1 is invalid because 2 appears twice → `False`

Actual verification result:

- `2/2 tests passed`

### 2. Column tests: `check_colum_test.py`

This script checks column validity for several columns.

```python
tests = [
    (0, False),
    (1, True),
    (3, True),
]
```

Expected result:

- Column 0 is invalid → `False`
- Column 1 is valid → `True`
- Column 3 is valid → `True`

Actual verification result:

- `3/3 tests passed`

### 3. Block tests: `check_block_test.py`

This script validates 3x3 sub-grids.

```python
tests = [
    (0, 0, False),
    (1, 2, True),
    (3, 1, True),
]
```

Expected result:

- Block (0,0) is invalid → `False`
- Block (1,2) is valid → `True`
- Block (3,1) is valid → `True`

Actual verification result:

- `3/3 tests passed`

### 4. Full grid tests: `check_grid_test.py`

This script attempts to test the final grid-validation function using two boards:

```python
sudoku1 = [...]
sudoku2 = [...]
```

The intended idea was:

- `sudoku1` should fail validation → `False`
- `sudoku2` should pass validation → `True`

However, the test script currently has a bug in its loop:

```python
for sudoku in tests:
    result = sudoku_grid_correct(sudoku)
```

Here, `sudoku` is a boolean value (`True` or `False`), so the function receives a bool instead of a 9x9 board. That leads to a `TypeError` when the code tries to index it as a list.

This is a useful example of a test-case mistake: the test is checking the expected result value instead of passing the actual Sudoku board to the function.

## Execution examples

The project was designed to run as simple Python scripts.

Example commands:

```bash
python check_row_test.py
python check_colum_test.py
python check_block_test.py
python check_grid_test.py
```

## Verified results

The project was run in the terminal and the following results were observed:

- Row checks: `2/2 tests passed`
- Column checks: `3/3 tests passed`
- Block checks: `3/3 tests passed`
- Full-grid test script: currently fails due to the incorrect test loop in `check_grid_test.py`

## Summary

This project demonstrates a step-by-step approach to understanding Sudoku validation:

1. Validate each row separately.
2. Validate each column separately.
3. Validate each 3x3 block separately.
4. Combine all checks into a full-board version.

The code is a good learning example for Python list handling, duplicate detection, and modular validation logic, even though the final grid test still needs correction to fully reflect the intended project behavior.
