n =[]
for i in range(7):
    a = int(input())
    if a%2==1:
        n.append(a)
if n:
    print(sum(n))
    print(min(n))
else:
    print("-1")