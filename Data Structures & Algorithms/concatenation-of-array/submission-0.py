class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        """
        n = 4
        n * 2 = 8
        nums = 
        [1,4,1,2]
                 i
        ans = 
        [1,4,1,2,1,4,1,2]
                 i
                         j      
        """
        n = len(nums)
        ans = [0] * (n * 2)

        i = 0
        j = n

        while i < n:
            ans[i] = nums[i]
            ans[j] = nums[i]
            i += 1
            j += 1
        
        return ans
    