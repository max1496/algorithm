x, y = 1, 1
N = int(input())
plans = input().split()

dx = [0,0,-1,1]
dy = [-1,1,0,0]
D= ['L','R','U','D']

for plan in plans:
    for i in range(len(D)):
        if D[i] == plan:
            nx = x+dx[i]
            ny = y +dy[i]
    if nx<1 or ny<1 or nx>N or ny>N:
        continue
    x ,y= nx, ny

print(x,y)