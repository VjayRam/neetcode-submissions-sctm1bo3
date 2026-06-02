class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for i in nums:
            counts[i] = 1 + counts.get(i, 0)
        
        heap = []
        for num in counts.keys():
            heapq.heappush(heap, (counts[num], num))

            if len(heap) > k:
                heapq.heappop(heap)

        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res


        