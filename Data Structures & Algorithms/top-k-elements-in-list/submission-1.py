class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        #BUCKET SORT SOLUTION
        #T: O(n)
        #S: O(n)


        count = defaultdict(int)
        #bucket sort array
        freq = [[] for i in range(len(nums) + 1)]   #[ [],[],[],[],[],[] ]

        for n in nums:
            count[n] += 1
        
        # for n in nums:
        #     count[n] = 1 + count.get(n, 0)       

        #key, value pair
        for n, c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)

                if len(res) == k:
                    return res
    

