class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        major = []
        n = len(nums)

        for x in set(nums):
            if nums.count(x) > n//3:
                major.append(x)
        return major