class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        freq = {}
        
        # Build frequency map for s1
        for char in s1:
            freq[char] = freq.get(char, 0) + 1
        
        # Initialize window with first len(s1) characters of s2
        window = {}
        for i in range(len(s1)):
            char = s2[i]
            window[char] = window.get(char, 0) + 1
        
        # Check if first window matches
        if window == freq:
            return True
        
        # Slide the window across s2
        for i in range(len(s1), len(s2)):
            # Add new character to the right
            new_char = s2[i]
            window[new_char] = window.get(new_char, 0) + 1
            
            # Remove character from the left
            old_char = s2[i - len(s1)]
            window[old_char] -= 1
            if window[old_char] == 0:
                del window[old_char]
            
            # Check if current window matches
            if window == freq:
                return True
        
        return False
        