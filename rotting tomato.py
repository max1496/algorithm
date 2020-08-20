grid = [[2,1,1],[1,1,0],[0,1,1]]
def dfs(grid):
    ROW = len(grid)
    COL = len(grid[0])
    queue = []

    for r in range(ROW):
        for c in range(COL):
            if grid[r][c] ==2:
                queue.append([r,c,0])
                
    #bfs
    visited = [[0]*COL for x in range(ROW)]
    dx=[0,0,1,-1]
    dy=[1,-1,0,0]

    while queue:
        r,c,level = queue.pop(0)
        print(r,c,level)
        for i in range(4):
            next_r,next_c=r+dx[i], c+dy[i]
            if next_r<0 or next_c<0 or next_r>=ROW or next_c>=COL or grid[next_r][next_c]==0:
                continue
            if grid[next_r][next_c] ==2:
                continue
            queue.append([next_r,next_c,level+1])
            grid[next_r][next_c] =2

    for r in range(ROW):
        for c in range(COL):
            if grid[r][c]==1:
                level=-1
    print(level)
    return level
print(dfs(grid))