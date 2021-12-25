arr = [1,4,3,2,0]
cnt=[0]*(max(arr)+1)
for i in range(len(arr)):
    cnt[arr[i]]+=1
for i in range(len(arr)):
    for j in range(cnt[i]):
        print(i, end=' ')