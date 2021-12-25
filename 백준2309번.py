data = list(map(int, input().split()))
total = sum(data)

for i in range(9):
    for j in range(i+1, 9):
        if 100 == total - (data[i]+data[j]):
            num1 = data[i]
            num2 = data[j]
            data.remove(num1)
            data.remove(num2)
            data.sort()
        
            for i in range(len(data)):
                print(data[i])
            break
    if len(data)<9:
        break