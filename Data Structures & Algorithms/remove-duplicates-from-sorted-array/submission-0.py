class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1  # First element is always unique
        
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:  # Found a new unique element
                nums[k] = nums[i]       # Place it at position k
                k += 1
        
        return k
