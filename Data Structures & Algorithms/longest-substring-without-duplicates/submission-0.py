class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        alphSet = set()
        l = 0
        maxLength = 0

        for r in range(len(s)):
            while s[r] in alphSet:
                alphSet.remove(s[l])
                l += 1
            alphSet.add(s[r])
            maxLength = max(maxLength,len(alphSet))
        return maxLength
            
