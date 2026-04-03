class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        total = res = 0
        l = 0

        for r in range(n):
            total += nums[r]
            while nums[r] * (r-l+1) > total + k:
                total -= nums[l]
                l += 1
            res = max(res,r-l+1)
        return res