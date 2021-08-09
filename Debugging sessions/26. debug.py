def removeDuplicates(nums):
    if len(nums) == 0:
        return 0
    
    prev = 0

    for i in range(1,len(nums)):
        if nums[i] != nums[prev]:  #nums[1] != nums[0]
            prev += 1  #nums[1]
            nums[prev] = nums[i]  #reassign: nums[1] = nums[1]
    # print(len(nums))
    # print(nums)
    print(prev +1 )
    return prev+1

removeDuplicates([1,1,2,2,3,4,4])