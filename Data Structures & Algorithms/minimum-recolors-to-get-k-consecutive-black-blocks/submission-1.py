class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        whiteCount = 0
        l = 0
        for r in range(k):
            if blocks[r] == 'W':
                whiteCount += 1
        
        res = whiteCount
        for r in range(k,len(blocks)):
            if blocks[r-k] == 'W':
                whiteCount -= 1
            if blocks[r] == 'W':
                whiteCount += 1
            res = min(res,whiteCount)
        return res
            