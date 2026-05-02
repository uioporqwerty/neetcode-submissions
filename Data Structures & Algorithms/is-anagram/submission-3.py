class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_arr = sorted(s)
        t_arr = sorted(t)

        for i in range(min(len(s), len(t))):
            if s_arr[i] != t_arr[i]:
                return False
        
        return len(s) == len(t)
