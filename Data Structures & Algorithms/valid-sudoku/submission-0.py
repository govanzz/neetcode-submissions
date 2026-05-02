class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows=[]
        cols=[]
        boxes=[]
        for i in range(9):
            rows.append(set())
            cols.append(set())
            boxes.append(set())
        for r in range(9):
            for c in range(9):
                val=board[r][c]
                if board[r][c]==".":
                    continue
                box_index = (r//3)*3+(c//3)

                if val in rows[r] or val in cols[c] or val in boxes[box_index]:
                    return False
                
                rows[r].add(val)
                cols[c].add(val)
                boxes[box_index].add(val)
        return True
        
                
        

        
        