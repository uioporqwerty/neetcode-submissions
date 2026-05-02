class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        """
        Time: O(n)
        Space: O(1)
        Pros: You can substitute the 2 to make it variable. Shorter code.
        """
        ans = []
        for i in range(2):
            for n in nums:
                ans.append(n)
        return ans