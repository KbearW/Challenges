def chunks(list1):
    res = {}
    for i in range(len(list1)):
        if res.get(len(list1[i])) is None:
            res[len(list1[i])] = [list1[i]]
        else:
            res[len(list1[i])].append(list1[i])
    return res
print(chunks(['asfd','avx','wdge']))
#{4: ['asfd', 'wdge'], 3: ['avx']}

# def find_k_largest(list, k):
#     # A = sorted(list)[::-1]
#     list.sort() #sort can't use [::-1]
#     print(list)
#     print(list[k-1])
#     return list[k-1]
    
# find_k_largest([2,4,6,2,9,-19,-2],2)
# find the 2nd largest and 2nd smallest

# def even(list):
#     res = []
#     for num in list:
#         if num %2 == 0:
#             res.append(num)
#     print(res)

# even([3,4,5,6,7,4])

# def count_odd_even(list):
#     odd_count = 0
#     even_count = 0
#     for num in list:
#         if num % 2 == 0:
#             even_count += 1
#         else:
#             odd_count += 1
#     print(f'odd_count: {odd_count}, even_count: {even_count}')
# count_odd_even([3,4,35,6,3,7,8])

# def remove_item(list, k):
#     res = []
#     for num in list:
#         if num < k:
#             res.append(num)
    
#     print(sorted(res))
# remove_item([4,5,7,8,2,96],10)
# def find_dups(list):
#     # sort then comp each
#     res = []
#     A = sorted(list)
#     print(A)
#     for idx in range(len(A)-1):
#         if A[idx] == A[idx+1]:
#             res.append(A[idx])
#     return res
# print(find_dups([3,4,4,3,2,5,7,8,5,5,5,3]))

