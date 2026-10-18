class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row,col=len(board),len(board[0])
        check=['1','2','3','4','5','6','7','8','9']
        for i in range(row):
            row_check=check.copy()
            for j in range(col):
                if board[i][j]==".":
                    continue
                elif board[i][j] in row_check:
                    row_check.remove(board[i][j])
                else:
                    return False
        
        for j in range(col):
            col_check=check.copy()
            for i in range(row):
                if board[i][j]==".":
                    continue
                elif board[i][j] in col_check:
                    col_check.remove(board[i][j])
                else:
                    return False
        step_row=0
        step_col=0
        while step_row<7:
            while step_col<7:
                box_check=check.copy()
                for i in range(step_row,step_row+3):
                    for j in range(step_col,step_col+3):
                        if board[i][j]==".":
                            continue
                        elif board[i][j] in box_check:
                            box_check.remove(board[i][j])
                        else:
                            return False
                step_col+=3
            step_row+=3
            step_col=0

        return True
        

            