# https://leetcode.com/problems/intersection-of-two-arrays-ii/

# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

 

# Example 1:

# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]

# Example 2:

# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [4,9]
# Explanation: [9,4] is also accepted.

 

# Constraints:

#     1 <= nums1.length, nums2.length <= 1000
#     0 <= nums1[i], nums2[i] <= 1000

 

# Follow up:

#     What if the given array is already sorted? How would you optimize your algorithm?
#     What if nums1's size is small compared to nums2's size? Which algorithm is better?
#     What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Method #1
        # lst1 = collections.Counter(nums1)
        # lst2 = collections.Counter(nums2)
        # result = []
        # for k,v in lst1.items():
        #     for k2,v2 in lst2.items():
        #         if k == k2:
        #             mintimes = min(v, v2)
        #             result = result + [k] * mintimes
        # return result
        
        # Method #2
        nums1, nums2 = sorted(nums1), sorted(nums2)
        pt1 = pt2 = 0
        res = []

        while True:
            try:
                if nums1[pt1] > nums2[pt2]:
                    pt2 += 1
                elif nums1[pt1] < nums2[pt2]:
                    pt1 += 1
                else:
                    res.append(nums1[pt1])
                    pt1 += 1
                    pt2 += 1
            except IndexError:
                break

        return res
# Notes:           
# Set, Hashmap method: dicts, counter
# iterate over the list --> slow method

