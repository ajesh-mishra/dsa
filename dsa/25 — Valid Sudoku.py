"""
Time complexity: O(1)
Space complexity: O(n^2)
"""

from collections import defaultdict
from typing import DefaultDict


def valid_sudoku(board: list[list[str]]) -> bool:
    rows: DefaultDict[int, set[str]] = defaultdict(set)
    cols: DefaultDict[int, set[str]] = defaultdict(set)
    boxes: DefaultDict[tuple[int, int], set[str]] = defaultdict(set)

    for i in range(9):
        for j in range(9):
            num = board[i][j]

            if num == ".":
                continue

            if num in rows[i]:
                return False

            if num in cols[j]:
                return False

            box_row = i // 3
            box_col = j // 3

            if num in boxes[(box_row, box_col)]:
                return False

            rows[i].add(num)
            cols[j].add(num)
            boxes[(box_row, box_col)].add(num)

    return True


if __name__ == "__main__":
    assert (
        valid_sudoku(
            board=[
                ["5", "3", ".", ".", "7", ".", ".", ".", "."],
                ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                [".", "9", "8", ".", ".", ".", ".", "6", "."],
                ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                [".", "6", ".", ".", ".", ".", "2", "8", "."],
                [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                [".", ".", ".", ".", "8", ".", ".", "7", "9"],
            ]
        )
        == True
    )
    assert (
        valid_sudoku(
            board=[
                ["5", "3", ".", ".", "7", ".", ".", ".", "."],
                ["6", ".", "8", "1", "9", "5", ".", ".", "."],
                [".", "9", "8", ".", ".", ".", ".", "6", "."],
                ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                [".", "6", ".", ".", ".", ".", "2", "8", "."],
                [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                [".", ".", ".", ".", "8", ".", ".", "7", "9"],
            ]
        )
        == False
    )
