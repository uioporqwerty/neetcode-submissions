from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = defaultdict(int)
        t_map = defaultdict(int)

        for c in s:
            s_map[c] += 1
        
        for c in t:
            if c not in s_map:
                return False
            t_map[c] += 1
        
        for key in s_map:
            if s_map[key] != t_map[key]:
                return False
        
        return True