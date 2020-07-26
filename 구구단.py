def multi(number):
    for i in range(1,10):
        print("{}*{} = {}".format(i,number, i*number))
while True:
    n= input("숫자를 입력하세요>")
    if n == "exit":
        break
    elif n.isdigit()!=True:
        break
    else:
        n=int(n)
        multi(n)
    