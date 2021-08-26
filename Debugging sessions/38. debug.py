
def countAndSay( n):
#         res = '1'
#         for i in range(n-1):
#             res = self.getnext(res)
#         return res
    
#     def getnext(self,res):
#         i, next_seq = 0, ''
#         while i<len(res):
#             count = 1
# # i< len(seq)-1--> limit the # of times this is being run..remember 0 indexing? 
#             while i< len(res)-1 and res[i] == res[i+1]:
#                 count += 1
#                 i += 1
# #Exit the while loop when two # ain't the same, nest the res once before moving back into the while loop
#             next_seq += str(count) + res[i]
#             i += 1
#         return next_seq

        s = '1'
        for i in range(n-1):
            count = 1
            temp = []
            for index in range(1, len(s)):
                if s[index] == s[index-1]:
                    count += 1
                else:
                    temp.append(str(count))
                    temp.append(s[index-1])
                    count = 1
            temp.append(str(count))
            temp.append(s[-1])
            s = ''.join(temp)
        return s