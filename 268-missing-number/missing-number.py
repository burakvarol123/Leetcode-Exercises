class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sums = sum(nums)
        n = len(nums)
        missing = n*(n+1)//2 - sums
        return missing 
        