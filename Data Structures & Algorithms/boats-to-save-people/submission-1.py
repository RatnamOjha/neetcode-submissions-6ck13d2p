class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        n = len(people)
        res = 0

        l,r = 0,n-1
        while l <= r:
            if people[l] + people[r] == limit:
                res += 1
                l += 1
                r -= 1
            elif people[l] + people[r] < limit:
                res += 1
                l += 1
                r -= 1
            else:
                res += 1
                r -= 1
        return res

