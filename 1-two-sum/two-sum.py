class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        len_nums = len(nums)

        for i in range(len_nums):
            for j  in range(i+1 , len_nums):
                sum = nums[i] + nums[j]
                if sum == target:
                    return [i,j]
                    

        