class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        num_list = set(nums)
        max_len = 0

        for num in num_list:
            if num-1 not in num_list:
                curr_num = num
                curr_len = 1

                while curr_num+1 in num_list:
                    curr_len += 1
                    curr_num += 1
            
                max_len = max(max_len, curr_len)
        
        return max_len