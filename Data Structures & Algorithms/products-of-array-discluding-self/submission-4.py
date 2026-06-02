class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        out = [1] * n

        pre = 1
        for i in range(n):
            out[i] = pre
            pre *= nums[i]
        
        suf = 1
        for j in range(n-1, -1, -1):
            out[j] *= suf
            suf *= nums[j]

        return out



        