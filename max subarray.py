#solution(maximum sum of any subarray)

def maxsubarray(nums):
    csum = nums[0]
    maxsum = nums[0]

    for i in range(1,len(nums)):
        csum = max(nums[i],nums[i]+csum)
        maxsum = max(csum,maxsum)

    return maxsum

nums = [-2,1,-3,4,-1,2,1,-5,4]

print(maxsubarray(nums))