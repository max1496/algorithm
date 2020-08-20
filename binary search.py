# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
def binarysearch(nums, target):
    start = 0 
    end = len(nums)-1
    result = -1
    while start<=end:
        mid =(start+end)//2
        if nums[mid]<target:
            start = mid+1
        elif nums[mid]>target:
            end = mid-1
        else:
            result = mid
            break
    return result
    print(result,nums[result])