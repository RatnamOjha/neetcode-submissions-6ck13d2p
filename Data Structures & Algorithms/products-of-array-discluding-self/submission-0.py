class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefx = [0] * n
        suffx = [0] * n
        res = [0] * n

        prefx[0] = suffx[n-1] = 1

        for i in range(1,n):
            prefx[i] = nums[i-1] * prefx[i-1]
        for i in range(n-2,-1,-1):
            suffx[i] = nums[i+1] * suffx[i+1]
        for i in range(n):
            res[i] = prefx[i] * suffx[i]
        return res