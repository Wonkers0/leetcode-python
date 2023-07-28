#
# @lc app=leetcode id=36 lang=python
#
# [36] Valid Sudoku
#

# @lc code=start
class Solution(object):
    def isValidSudoku(self, rows):
        for row in rows:
            if self.hasDuplicates(row):
                return False
            
        columns = self.getColumns(rows)
        for column in columns:
            if self.hasDuplicates(column):
                return False
            
        boxes = self.getBoxes(rows)
        for box in boxes:
            if self.hasDuplicates(box):
                return False
            
        return True
        

    def getColumns(self, rows):
        columns = []
        
        for i in range(9):
            columns.append([row[i] for row in rows])

        return columns

    def getBoxes(self, rows):
        boxes = []

        for row in range(3):
            for column in range(3):
                box = []
                for boxY in range(3):
                    boxRow = rows[row * 3 + boxY] 
                    for boxX in range(3):
                        box.append(boxRow[column * 3 + boxX])
                boxes.append(box)
        
        return boxes

    def concat(self, a, b):
        for i in b:
            a.append(i)
        return a

    def hasDuplicates(self, arr):
        return len([x for x in arr if x != "." and arr.count(x) > 1]) != 0

        
# @lc code=end

solution = Solution()
print(solution.isValidSudoku([[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."]]))