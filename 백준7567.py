n= list(st(input()))
result = 10
for i in range(1,len(n)):
    if n[i] =='(':
        result+=5
    elif n[i] ==')':
        result+=10
print(result)