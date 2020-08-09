nums=[2,2,1,1,1,2,2]
count = {}
for i in range(len(nums)):
    if nums[i] in count:
        count[nums[i]]+=1
    else:
        count[nums[i]]=1
for num_key, value in count.items():
    if value>len(nums)//2:
        return num_key

#counter version :
# count = Counter(nums)
# for x in count:
#     if count[x]>len(nums)//2:
#         return x