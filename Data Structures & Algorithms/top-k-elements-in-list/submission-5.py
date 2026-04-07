from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        sorted_items = sorted(counts.items(), key=lambda x:x[1], reverse=True)
        return [item for item, count in sorted_items[:k]]

        