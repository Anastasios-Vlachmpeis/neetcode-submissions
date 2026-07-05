class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        setB =[
        [[],[],[]],
        [[],[],[]],
        [[],[],[]]
        ]
        setR =[
        [],[],[],[],[],[],[],[],[]
        ]
        setC =[
        [],[],[],[],[],[],[],[],[]
        ]
        m = {
            0:0,1:0,2:0,
            3:1,4:1,5:1,
            6:2,7:2,8:2,
        }
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                k = m[i]
                z = m[j]
                if board[i][j] in setB[k][z]:
                    return False
                if board[i][j] in setC[j]:
                    return False
                if board[i][j] in setR[i]:
                    return False
                setR[i].append(board[i][j])
                setC[j].append(board[i][j])
                setB[k][z].append(board[i][j])
        return True