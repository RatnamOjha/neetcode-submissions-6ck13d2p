class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}

        max = len(nums) // 2
        for n in nums:
            count[n] = count.get(n,0) + 1
            if count[n] > max:
                return n
