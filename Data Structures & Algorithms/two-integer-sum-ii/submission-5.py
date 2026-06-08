class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        num_map = defaultdict(int)
        for i in range(len(numbers)):
            temp = target - numbers[i]
            if num_map[temp]:
                return [num_map[temp], i + 1]
            num_map[numbers[i]] = i + 1
        return []
                 
        