n=int(input())
cntA=0
m=input()
for i in m:
    if i == 'A':
        n-=1
        cntA+=1
if n>cntA:
    print("B")
elif n<cntA:
    print('A')
else:
    print("Tie")