n,m = map(int, input().split())
max_value=0
for _ in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)
    if max_value < min_value:
        max_value = min_value