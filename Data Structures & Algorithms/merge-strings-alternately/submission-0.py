class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l,r = 0,0
        word = ""
        while l < len(word1) and r < len(word2):
            word += word1[l]+word2[r]
            l+=1
            r+=1
        word += word1[l:]
        word += word2[r:]
        return word