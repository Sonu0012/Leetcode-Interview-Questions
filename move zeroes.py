nums = [0,1,0,3,12]

#brute force
def movezero(nums):
    for i in range(len(nums)-1,-1,-1):
        if nums[i]==0:
            nums.pop(i)
            nums.append(0)
    return nums


#bestsol
def movezero1(nums):
    last=0
    for i in range(0,len(nums)):
        if nums[i]!=0:
            nums[last] = nums[i]
            last+=1

    for i in range(last,len(nums)):
        nums[i]=0

    return nums


print(movezero(nums))
print(movezero1(nums))    




