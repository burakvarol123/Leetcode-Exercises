class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        caindex = 0
        left = 0 
        right = len(nums) -1
        if target > nums[-1]:
            return len(nums)
        while left <= right:
            mid = (left + right) // 2
            if target > nums[mid]:
                left = mid + 1
            else:
                right = mid -1
    
        return left 
            
       
        
            

                

        