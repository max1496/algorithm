grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

def numIslands(grid):
    if not grid:
        return 0
    ROW = len(grid)
    COL = len(grid[0])
    queue=[]
    numofIsland=0
    visited = [[0]*COL for x in range(ROW)]
    for r in ROW:
        for c in COL:
            if grid[r][c]==1 and visited[r][c]==0:
                bfs(r,c)
    
    def bfs(r,c):
        dx=[-1,1,0,0]
        dy=[0,0,-1,1]
        queue.append([r,c])
        visited[r][c]==1
        numofIsland+=1

        while(queue):
            r,c=queue.pop(0)
            for i in range(4):
                next_r=r+dx[i]
                next_c=c+dy[i]
                if next_r<0 or next_r>=ROW or next_c<0 or next_c>=COL or grid[next_r][next_c]==0 or visited[next_r][next_c]==1:
                    continue
                if grid[next_r][next_c]==1:
                    visited[next_r][next_c]==1
                    queue.append([next_r,next_c])
    return numofIsland
print(numIslands(grid))