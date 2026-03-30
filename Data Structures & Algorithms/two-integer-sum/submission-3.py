class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
  
        # seen = {}

        # for i,n in enumerate(nums):
        #     d = target - n
        #     if d in seen:
        #         return[seen[d],i]
        #     seen[n] = i 


