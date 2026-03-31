class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        n = len(nums)
        res = float('inf')
        currSum = 0

        for r in range(n):
            currSum += nums[r]

            while currSum >= target:
                #currSum = r-l+1
                res = min(res,r-l+1)
                currSum -= nums[l]
                l += 1
            
        return 0 if res == float('inf') else res