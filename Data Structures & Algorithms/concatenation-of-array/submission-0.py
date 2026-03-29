class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * (2 * n)         # Pre-allocate space
        
        for i in range(n):
            ans[i] = nums[i]        # First half
            ans[i + n] = nums[i]    # Second half
            
        return ans