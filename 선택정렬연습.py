arr = [2,3,1,5,4]

for i in range(len(arr)):
    min_index = i
    for j in range(i+1, len(arr)):
        if arr[min_index]>arr[j]:
            min_index=j
    arr[min_index], arr[i]= arr[i], arr[min_index]
print(arr)