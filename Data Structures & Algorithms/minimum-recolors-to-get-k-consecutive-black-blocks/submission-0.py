class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        colorBlock = blocks[:k].count('W') #count number of W elements in the first 'k' window 
        minOps = colorBlock

        for r in range(k,len(blocks)):
            if blocks[r] == 'W':
                colorBlock += 1
            if blocks[r-k] == 'W':
                colorBlock -= 1
            minOps = min(minOps,colorBlock)
        return minOps

        # TC = O(n)