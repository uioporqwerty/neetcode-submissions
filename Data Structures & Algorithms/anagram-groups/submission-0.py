class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Solution 1: Create a dictionary and sort each word. Each sorted word will be an index into the dict and you append that unsorted word to the list.
        Time: O(nlogn)
        Space: O(n)
        """

        res = []
        sorted_words = defaultdict(list)

        for s in strs:
            key = ''.join(sorted(list(s)))
            sorted_words[key].append(s)
        
        for _, val in sorted_words.items():
            res.append(val)
            
        return res
