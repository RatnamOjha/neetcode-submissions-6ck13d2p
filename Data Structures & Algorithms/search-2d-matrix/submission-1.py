class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r = len(matrix)
        c = len(matrix[0])
        l,r = 0, r*c-1
        while l <= r:
            m = (l+r)//2
            val = matrix[m//c][m%c]
            if val < target:
                l = m + 1
            elif val > target:
                r = m - 1
            else:
                return True
        return False