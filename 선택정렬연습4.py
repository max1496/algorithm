arr = [3,4,1,5,2]
for i in range(len(arr)):
    min_index = i
    for j in range(i+1,len(arr)):
        if arr[min_index]>arr[j]:
            min_index = j
    arr[min_index],arr[j]=arr[j],arr[min_index]
print(arr)