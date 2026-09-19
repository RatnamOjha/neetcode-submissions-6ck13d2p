class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)

        while l <= r:
            m = (l+r)//2
            
            curr_weight = 0
            days_needed = 1
            
            for w in weights:
                if curr_weight + w <= m:
                    curr_weight += w
                else:
                    days_needed += 1
                    curr_weight = w
            if days_needed <= days:
                r = m - 1
            else:
                l = m + 1
        return l