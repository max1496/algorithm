n = int(input())
# students = list(map(int, input().split()))
students = input().split()
students = list(map(int, students))
# students = int(input().split)
b,c = map(int, input().split())

cnt =0

for student in students:
    if student > b:
        cnt +=1
        if (student -b)%c ==0:
            cnt+=(student -b)//c
        else:
            cnt+=(student -b)//c+1
print(cnt)