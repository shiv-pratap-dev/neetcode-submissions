class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for i in board:
            row = []
            for j in i:
                if j == ".":
                    continue
                if j not in row:
                    row.append(j)
                else:
                    return False



        for i in range(9):
            col = []
            
            for j in range(9):
                
                if board[j][i] == ".":
                    continue
                
                if board[j][i] not in col:
                    col.append(board[j][i])

                else:
                    return False

        
        boxes = {}


        for i in range(9):
            
            for j in range(9):

                keys = (i//3 , j//3)
                
                if board[i][j] == ".":
                    continue    
                if keys not in boxes:
                    boxes[keys] = []
                    
                if board[i][j] in boxes[keys]:
                    return False
                else:
                    boxes[keys].append(board[i][j])

        return True
        