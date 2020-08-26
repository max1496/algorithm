m=3
n=2
def uniquePaths(m,n):
    ROW =m
    COL=n
    path=[[0]*n for x in range(m)]
    for r in range(ROW):
        path[r][0]=1
    for c in range(COL):
        path[0][c]=1
    for r in range(1,ROW):
        for c in range(1,COL):
            path[r][c]=path[r-1][c]+path[r][c-1]
    return path[m-1][n-1]
