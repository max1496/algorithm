n=1260
cnt =0
cointypes = [500, 100, 50, 10]
for coin in cointypes:
    print(coin)
    cnt += n//coin
    n %= coin
print(coin)