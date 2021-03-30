N, M = map(int, input().split())
L=[]
for _ in range(N):
    L.append(input().rstrip())

res = ''
cnt=0
for j in range(M):
    D= {'A':0,  'G':0, 'C':0, 'T':0}
    for i in range(N):
        D[L[i][j]] +=1

    m=0
    c = ''
    for k in 'ACGT':
        if m < D[k]:
            m=D[k]
            c = k

    res +=c
    cnt +=(N-m)
print(res)
print(cnt)