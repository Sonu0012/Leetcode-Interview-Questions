#solution

def intersect(nums1,nums2):
    mylist = []
    if len(nums1)<len(nums2):
        for i in nums1:
            if i in nums2:
                nums2.pop(nums2.index(i))
                mylist.append(i)

    else:
        for i in nums2:
            if i in nums1:
                nums1.pop(nums1.index(i))
                mylist.append(i)

    return mylist


nums1 = [4,9,5]
nums2 = [9,4,9,8,4]

print(intersect(nums1,nums2))


