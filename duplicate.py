nums=[1,2,3,4]
nums_diff=[]
for i in range(len(nums)-1):
    print nums
    nums_diff=nums
    print nums
    nums_diff.pop(i)
    print nums
    print nums_diff
    if nums[i] in nums_diff:
        print True
print False
        