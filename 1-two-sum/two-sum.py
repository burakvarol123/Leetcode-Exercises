class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        len_nums = len(nums)
        d = {}
        for i in range(len_nums):
            number = nums[i]
            complement = target - number
            if complement in d:
                return [d[complement] , i]
            else:
                d[number] = i
                


                    

        