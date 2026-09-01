class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        empty = []

        # Fill sets and find empty cells
        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    empty.append((row, col))
                else:
                    num = board[row][col]
                    box = (row // 3) * 3 + (col // 3)

                    rows[row].add(num)
                    cols[col].add(num)
                    boxes[box].add(num)


        def solve(index):

            # All empty cells are filled
            if index == len(empty):
                return True

            row, col = empty[index]
            box = (row // 3) * 3 + (col // 3)

            for num in "123456789":

                # Check validity in O(1)
                if (num not in rows[row] and
                    num not in cols[col] and
                    num not in boxes[box]):

                    # Place number
                    board[row][col] = num
                    rows[row].add(num)
                    cols[col].add(num)
                    boxes[box].add(num)

                    # Solve next empty cell
                    if solve(index + 1):
                        return True

                    # Backtrack
                    board[row][col] = "."
                    rows[row].remove(num)
                    cols[col].remove(num)
                    boxes[box].remove(num)

            return False


        solve(0)