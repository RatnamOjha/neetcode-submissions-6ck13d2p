class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        while l <= r:
            k = (l + r) // 2
            
            hours_needed = 0
            for pile in piles:
                hours_needed += math.ceil(pile/k)
            
            if hours_needed <= h:
                r = k - 1
            else:
                l = k + 1

        return l