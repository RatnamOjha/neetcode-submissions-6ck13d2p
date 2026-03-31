class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(arr) - k
        
        while l < r:
            if x - arr[l] > arr[r + k - 1] - x:
                l += 1
            else:
                r -= 1
        
        return arr[l:l + k]