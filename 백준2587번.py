num = [int(input()) for i in range(5)]
# num = []
# for i in range(5):
#   num.append(int(input()))

num.sort()
ave = sum(num)/5
mid = num[2]
print(int(ave))
print(mid)