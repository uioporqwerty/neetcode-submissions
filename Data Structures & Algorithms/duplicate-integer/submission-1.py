class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
        Solution 1: Use a set. O(n) time and O(1) space
        Solution 2: Sort and then check if previous == current. O(nlogn) time O(1) space
        """

        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        
        return False