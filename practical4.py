#No of queens
n = 4
#Matrix chessborad
matrix = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
#bactrack
path = {}

def isColumnSafe(r,c):
    while (r>=0):
        if(matrix[r][c]==1):
            return 0
        r = r -1
    return 1

def ifLeftDigonalSafe(r,c):
    while ( r>=0 and c>=n):
        if(matrix[r][c]==1):
            return 0
        r = r - l̥1
        c = c + 1
    return 1

def ifRightDigonalSafe(r,c):
    while ( r>=0 and c<n):
        if(matrix[r][c]==1):
            return 0
        r = r - 1
        c = c + 1
    return 1

def isSafe(r,c):
    if(isColumnSafe(r,c) and ifLeftDigonalSafe(r,c) and ifRightDigonalSafe(r,c)):
        return True
    return False

def chessborad(r,c):
    if(r>=n):
        return
    p = 0
    while c < n:
        p = isSafe(r,c)
        if p == 1:
            matrix[r][c] = 1
            path.update({r:c})
            break
        c = c + 1
    
    if p == 1:
        chessborad(r+1,0)
    else:
        matrix[r-1][path.get(r-1)] = 0
        chessborad(r - 1,int(path.get(r - 1)) + 1)

chessborad(0,0)
print('Matrix:',matrix)
print('Path:',path)
