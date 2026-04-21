class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:


        my_set = set()
        my_set.update(nums)

        if len(nums) > len(my_set):
            return True

        return False



        