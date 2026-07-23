class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Cannot sort because it would break the index relationship.
        nums is not presorted
        
        * Solution 1: Keep track of which differences you've seen and their index. then if you've seen it before you can return both
        Time: O(n)
        Space: O(n)

        Solution 2: Brute force for each index. Given 2 <= nums.length <= 1000 it MIGHT be acceptable as a tradeoff if you want more space optimization.
        Time: O(n^2)
        Space: O(1) 
        """

        diffs = defaultdict(int)

        for i, num in enumerate(nums):
            diff = target - num

            if diff in diffs:
                return [diffs[diff], i]
            
            diffs[num] = i
        
        return [-1, -1]
