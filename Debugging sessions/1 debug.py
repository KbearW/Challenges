def twoSum(self, nums: List[int], target: int) -> List[int]:
    seen = {}
    
    for i, num in enumerate (nums):  #[2,7,11,15]  target = 9, i=0, num=2
        k = target - num  #k = 9-2--> 7, k = 2
    
        if k in seen: #--> O(1)
            # print(seen)
            return [seen[k],i]
        else:
            seen[num] = i  #seen{7:0, 2:1, 3:5, 4:6}

twoSum([2,7,11,15],7)