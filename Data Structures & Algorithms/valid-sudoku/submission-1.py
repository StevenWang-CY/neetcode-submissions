from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        def has_duplicate_without_dot(row):
            seen = set()

            for x in row:
                if x == ".":
                    continue

                if x in seen:
                    return True

                seen.add(x)

            return False

        # 1. 检查每一行
        for row in board:
            if has_duplicate_without_dot(row):
                return False

        # 2. 检查每一列
        for i in range(len(board)):
            if has_duplicate_without_dot([row[i] for row in board]):
                return False

        # 3. 检查每个 3x3 box
        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                box = []

                for i in range(box_row, box_row + 3):
                    for j in range(box_col, box_col + 3):
                        box.append(board[i][j])

                if has_duplicate_without_dot(box):
                    return False

        return True
        