class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq = {}

        if len(s1) > len(s2):
            return False
        for char in s1:
            freq[char] = freq.get(char,0) + 1
            
        window = {}
        for i in range(len(s1)):
            char = s2[i]
            window[char] = window.get(char,0) + 1
        if window == freq:
            return True
        
        for i in range(len(s1),len(s2)):
            newChar = s2[i]
            window[newChar] = window.get(newChar,0) + 1

            oldChar = s2[i-len(s1)]
            window[oldChar] -= 1
            if window[oldChar] == 0:
                del window[oldChar]

            if window == freq:
                return True
        return False
            

            