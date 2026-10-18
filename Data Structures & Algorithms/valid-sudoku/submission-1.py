class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row,col=len(board),len(board[0])
        for i in range(row):
            row_check=set()
            for j in range(col):
                if board[i][j]==".":
                    continue
                elif board[i][j] in row_check:
                    return False
                else:
                    row_check.add(board[i][j])
        
        for j in range(col):
            col_check=set()
            for i in range(row):
                if board[i][j]==".":
                    continue
                elif board[i][j] in col_check:
                    return False
                else:
                    col_check.add(board[i][j])
        step_row=0
        step_col=0
        while step_row<7:
            while step_col<7:
                box_check=set()
                for i in range(step_row,step_row+3):
                    for j in range(step_col,step_col+3):
                        if board[i][j]==".":
                            continue
                        elif board[i][j] in box_check:
                            return False
                        else:
                            box_check.add(board[i][j])
                step_col+=3
            step_row+=3
            step_col=0

        return True
        

            