class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        # 1, 2, 3, 4, 1
        # return True

        arr = []

        for num in nums:
            if num in arr:
                return True
            
            arr.append(num)

        
        return False




