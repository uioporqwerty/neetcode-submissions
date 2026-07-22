class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Solution 1: Use a dict to get counts of each string then compare counts.
        Since all lowercase characters we can use arr or default dict.
        Time: O(s + t)
        Space: O(1) since all small characters

        Solution 2: Sort s and t and compare characters. Compare each
        Time: O(slogs + tlogt)
        Space: O(1)
        """
        if len(s) != len(t):
            return False

        chars = [0] * 26

        for c in s:
            chars[ord(c) - ord('a')] += 1
        
        for c in t:
            chars[ord(c) - ord('a')] -= 1
        
        for i in range(26):
            if chars[i] != 0:
                return False 
        
        return True