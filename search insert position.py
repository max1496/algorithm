def searchinsert(nums, target):
    if not nums:
        return 0
    for i, num in enumerate(nums):
        if num>target or num==target:
            return i
    return len(nums)

print(searchinsert([1,3,5,6],4))