#brute force
def rotate1(nums,k):
    for i in range(0,k):
        a= nums.pop()
        nums = [a] + nums
    return nums


#best solution 
def rotate2(nums,k):
    k = k%len(nums)
    nums = nums[len(nums)-k:len(nums)]+nums[0:len(nums)-k]
    return nums


nums = [1,2,3,4,5,6,7]
k=3

print(rotate1(nums,k))
nums = [1,2,3,4,5,6,7]
print(rotate2(nums,k))