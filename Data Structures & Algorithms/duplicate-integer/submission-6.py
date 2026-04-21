class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        #using hash set for constant time lookup

        seen = set()

        for num in nums:
            if num in seen:
                return True

            seen.add(num)
        
        return False




