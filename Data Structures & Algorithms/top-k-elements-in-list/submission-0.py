class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # if key doesn't exist, defaultvalue to 0
        freq = defaultdict(int)

        for n in nums:
            freq[n] += 1

            

        # now we have freq hashmap
        sorted_list = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        # [("b", 3), ("c", 2), ("a", 1)]
        # now we have a list of tuples containing (key, value) --> (num, freq)

        res = []
        for key, value in sorted_list[:k]:
            res.append(key)

        return res
