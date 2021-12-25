arr = [5,4,2,3,1]
def quick_sort(arr):
    if len(arr)<=1:
        return arr
    p = arr[0]
    t = arr[1:]
    left_side = [x for x in t if x<=p]
    right_side = [x for x in t if x>p]
    print(left_side)
    print(right_side)
    return quick_sort(left_side) + [p] + quick_sort(right_side)

print(quick_sort(arr))