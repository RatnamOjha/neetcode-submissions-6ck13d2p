class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0 
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k

        # temp = []

        # for n in nums:
        #     if n == val:
        #         continue
        #     temp.append(n)
        # for i in range (len(temp)):
        #     nums[i] = temp[i]
        # return len(temp)
