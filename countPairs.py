def countPairs(nums,k):
    count = 0
    nums.sort()
    for i in range(len(nums)-1):
        if nums[i] == nums[i+1] and i*(i+1)%k == 0:
            count+=1
    return count
nums = [3,1,2,2,2,1,3]
k = 2

print(countPairs(nums,k))
