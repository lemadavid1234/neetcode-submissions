class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        

        #count = Counter(nums)
        
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        heap = []
        for num, freq in count.items():
            heapq.heappush(heap, (freq, num)) #sort by freq in tuples (freq,num)

            if len(heap) > k:
                heapq.heappop(heap)
            
        
        res = []
        #we want res to include actual num, not freq.
        for i in range(k):
            res.append(heapq.heappop(heap)[1])  

        return res