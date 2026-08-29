from check_block import block_correct


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

print(block_correct(sudoku, 0, 0))
print(block_correct(sudoku, 1, 2))


tests = [
    (0,0, False),
    (1,2, True),
    (3, 1, True),
]

passed = 0
total = len(tests)

for row_no, column_no,expected in tests:
    result = block_correct(sudoku, row_no, column_no)
    if result == expected:
        passed += 1
        print(f"Test row {row_no}: PASS (got {result})")
    else:
        print(f"Test row {row_no}: FAIL (expected {expected}, got {result})")

print(f"{passed}/{total} tests passed")