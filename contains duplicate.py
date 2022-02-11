#brute force
def dup1(nums):
    for i in range(0,len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] == nums[j]:
                return True
    return False

#o(n) solution
def dup2(nums):
    a=[]
    for i in nums:
        if i not in a:
            a.append(i)
        else:
            return True
    return False

#best solution
def dup3(nums):
    return len(set(nums))!=len(nums)    


nums = [1,2,2,3,4]
print(dup1(nums))    
print(dup2(nums))   
print(dup3(nums))   
