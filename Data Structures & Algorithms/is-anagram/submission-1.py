class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Use a array of length 26 because lowercase characters
        Count all characters in s
        Subtract all characters in t, if any character in the arr is < 0 then return False
        """
        cnt = [0] * 26

        for c in s:
            cnt[ord(c) - ord('a')] += 1

        for c in t:
            ltr = ord(c) - ord('a')
            cnt[ltr] -= 1

            if cnt[ltr] < 0:
                return False

        for i in range(26):
            if cnt[i] != 0:
                return False

        return True