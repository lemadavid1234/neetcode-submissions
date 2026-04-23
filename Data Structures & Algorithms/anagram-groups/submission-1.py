class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        #USING defaultdict(list)

        #create a tuple signature using 26 idx
        my_groups = defaultdict(list)
        for word in strs:
            count = [0] * 26 # [0, 0, 0, ..., 0]
            for char in word:
                count[ord(char) - ord('a')] += 1
            
            #converting array into tuple, so it's no longer mutable 
            # ex: abc --> (1, 1, 1, 0, 0 ...)
            key = tuple(count)


            my_groups[key].append(word)
                

        return list(my_groups.values())