class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for row in range(9):
            for col in range(9):

                num = board[row][col]

                # Ignore empty cells
                if num == ".":
                    continue

                # Calculate which 3x3 box the cell belongs to
                box_index = (row // 3) * 3 + (col // 3)

                # Check if number already exists
                if num in rows[row] or num in cols[col] or num in boxes[box_index]:
                    return False

                # Add number to row, column and box
                rows[row].add(num)
                cols[col].add(num)
                boxes[box_index].add(num)

        return True