def twoSum(nums, target):
    seen = {}
    
    for i, num in enumerate(nums):  #[2,7,11,15]  target = 9, i=0, num=2
        k = target - num
    
        if k in seen: #--> O(1)
            return [seen[k],i]
        else:
            seen[num] = i

        # print(i,num)

print(twoSum([2,7,11,15],9))

