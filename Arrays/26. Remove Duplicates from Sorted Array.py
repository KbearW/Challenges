# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

# Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

# Return k after placing the final result in the first k slots of nums.

# Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

# Custom Judge:

# The judge will test your solution with the following code:

# int[] nums = [...]; // Input array
# int[] expectedNums = [...]; // The expected answer with correct length

# int k = removeDuplicates(nums); // Calls your implementation

# assert k == expectedNums.length;
# for (int i = 0; i < k; i++) {
#     assert nums[i] == expectedNums[i];
# }

# If all assertions pass, then your solution will be accepted.

 

# Example 1:

# Input: nums = [1,1,2]
# Output: 2, nums = [1,2,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).

# Example 2:

# Input: nums = [0,0,1,1,1,2,2,3,3,4]
# Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
# Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        # for i in nums:
        #     for j in nums:
        #         if i == j:
        #             nums.pop(j)
        x = 1
        while x < len(nums):  # [1,1,2]--> len = 3
            if nums[x] == nums[x-1]:
                nums.pop(x)
            else:
                x += 1
        return len(nums)
        
# Note:
#     modify the array in place for O(1) memory--> cannot use a seperate list
#     delete/ pop the repeated
#     num array is sorted--> num[i] == num[i+1] 
    
# Pesudo Code:
#    iterate over the array-- len method:
#       if statement if curr == next:
#           pop(i) in place
#     return array

# Q: What's a two pointer approach? --> 
# 1.) nested loop with i and j 
# 2.) setup a fixed pointer--> think about linked list concept. can't look into the next num bc it doesn't have .next method, but can setup a seperate pointer to start looking at the next position--> x = 1

# How to get ride of the out of index range error msg:
# First, look at the # of element and range(), it's mostlikly due to 0 indexing count 
# By setting up a dummy fixed variable and iterate over the list.