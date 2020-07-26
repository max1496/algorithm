def multi(number):
    for i in range(1,10):
        print("{}*{} = {}".format(i,number, i*number))
while True:
    n= input()
    if n == "exit":
        break
    elif n.isdigit()!=True:
        break
    else:
        n=int(n)
        multi(n)
    