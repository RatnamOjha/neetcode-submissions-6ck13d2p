class Solution:
    def validPalindrome(self, s: str) -> bool:
        l,r = 0,len(s) - 1
        while l < r:
            if s[l] != s[r]:
                sL , sR = s[l+1:r+1] , s[l:r]
                return sL == sL[::-1] or sR == sR[::-1]
            l += 1
            r -= 1
        return True