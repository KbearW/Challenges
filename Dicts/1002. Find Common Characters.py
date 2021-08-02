# https://leetcode.com/problems/find-common-characters/

# Given an array words of strings made only from lowercase letters, return a list of all characters that show up in all strings within the list (including duplicates).  For example, if a character occurs 3 times in all strings but not 4 times, you need to include that character three times in the final answer.

# You may return the answer in any order.

 

# Example 1:

# Input: ["bella","label","roller"]
# Output: ["e","l","l"]

# Example 2:

# Input: ["cool","lock","cook"]
# Output: ["c","o"]

 

# Note:

#     1 <= words.length <= 100
#     1 <= words[i].length <= 100
#     words[i] consists of lowercase English letters.

from collections import Counter 
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        # counts = set{}
#         Above method doesn't work bc of the collections method. Fastest and most efficient way is to 
        counts = Counter(words[0])
        
        for index in range(1,len(words)):
#             x &= y is the same as x = x & y aka 'union set'
            counts &= Counter(words[index])
      
    #  counts in here is the 'collection' function: Counter({'l': 2, 'e': 1})
    #  eventhoug it is the right answer, it's not displaying the right way... we need the following loop to change the display format
        print(counts)
        result = []
    #   .items() will return the result as tuples
        for char, count in counts.items():
            result += [char]* count
        return result
    
# Pesudo:
# iterate over the array,
# use the build-in function: counter
# put everything in the counter function
# make sure the final display is in the right format
# return the answer