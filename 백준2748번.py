n = int(input())
arr =[]
num=0
for i in range(n+1):
    if i==0:
        num=0
    elif i==1:
        num=1
    elif i>1:
        num=arr[-1]+arr[-2]
    arr.append(num)
print(arr[n])