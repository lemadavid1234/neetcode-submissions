class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        

        #BRUTE FORCE APPROACH
        # T: O(n^2)
        # S: O(1)
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):

                if nums[i] + nums[j] == target:
                    return [i, j]