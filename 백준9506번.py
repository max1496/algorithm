a =[]

while True:
    
    n = int(input())
    if n==-1:
        break
    for i in range(1,n+1):
        if n%i==0:
            a.append(i)
    b= str(n) + " = 1" 
    if n==(sum(a)):
        for j in range(1,len(a)-1):
            b += " + " +str(a[j]) 
        print(b)
    else:
        print(n + " is NOT perfect.")