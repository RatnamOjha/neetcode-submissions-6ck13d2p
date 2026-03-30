class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        s = []
        l,r = 0,len(numbers)-1
        while l < r:
            f = numbers[l] + numbers[r]
            if f > target:
                r -= 1
            elif f < target:
                l += 1
            else:
                return[l+1,r+1]
        return s
        