n,m,k = map(int, input().split())
data = list(map(int, input().split()))
data.sort()
first = data[n-1]
second = data[n-2]
result =(m//(k+1))*(k*first +second)+m%(k+1)*first
print(result)