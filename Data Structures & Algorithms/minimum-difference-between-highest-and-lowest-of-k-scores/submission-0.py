class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        l,r = 0,k-1
        minDiff = float('inf') #take the highest possible value because we need to return the smallest difference

        while r < len(nums):
            difference = nums[r] - nums[l]
            minDiff = min(minDiff,difference) 
            r += 1
            l += 1
        return minDiff





