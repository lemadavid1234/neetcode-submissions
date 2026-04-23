class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        #create a tuple signature using 26 idx
        my_groups = {}
        for word in strs:
            count = [0] * 26 # [0, 0, 0, ..., 0]
            for char in word:
                count[ord(char) - ord('a')] += 1
            
            #converting array into tuple, so it's no longer mutable 
            # ex: abc --> (1, 1, 1, 0, 0 ...)
            key = tuple(count)
            if key in my_groups:
                my_groups[key].append(word)
            else:
                my_groups[key] = [word]
                

        return list(my_groups.values())

