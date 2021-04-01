n =[0]*7
for i in range(7):
    n[i] = int(input())
result =0
min_value =100
for i in range(7):
    if n[i]%2==1:
        result +=n[i]
    if n[i]<min_value:
        min_value=n[i]
if n:
    print(result)
    print(min_value)
else:
    print(-1)