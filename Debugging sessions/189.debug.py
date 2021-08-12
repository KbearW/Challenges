def rotate(nums, k):
    """
    Do not return anything, modify nums in-place instead.
    """
    # method #1
    # in case k > nums and it goes in a loop
    k = k % len(nums)
    
    def rev(start,end):
        while start<end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
            
    nums.reverse()
    # k-1 due to zero base indexing
    rev(0, k-1)
    rev(k, len(nums)-1)

rotate([1,2,3,4,5],3)
        
# Steps:
# reverse the whole array
# reverse the k element
# reverse the len(nums)-k elements (remainder elements)
        
        # memory: O(1)