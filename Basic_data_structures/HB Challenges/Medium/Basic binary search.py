# if num = 4, range(20), how many steps will it take to get there?
def search (arr, target):
    right = arr[-1]
    left = 0
    steps = 0

    while left <= right:
        mid = (right+left) // 2 
        # print(mid)

        if mid == target:
            steps += 1
            return steps

        if target < mid:
            # print('r')
            right = mid - 1
            steps += 1
        
        else:
            # print('l')
            left = mid + 1
            steps += 1
    
    return -1

arr = [x for x in range(41)]
# print(arr)
print(search(arr, 20))