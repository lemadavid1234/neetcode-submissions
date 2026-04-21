class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        #ex: [3, 2, 4, 5]
        #target = 8
        #return [0, 3]
        
        #key, value: value, index
        my_map = {}

        for i in range(len(nums)):
            x = target - nums[i]
            if x in my_map:
                return [my_map[x], i]

            my_map[nums[i]] = i

                     
        