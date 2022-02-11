nums = [2,7,11,15]
target = 9
#brute force
def twosum1(nums,target):
    a=[]
    for i in range(0,len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] + nums[j] == target:
                a.append(i)
                a.append(j)
                return a
print(twosum1(nums,target))

#best solution
def twosum2(nums,target):
    seen = {}
    for i,value in enumerate(nums):
        remain = target - nums[i]

        if remain in seen:
            return[i,seen[remain]]
        else:
            seen[value] = i

print(twosum2(nums,target))            


