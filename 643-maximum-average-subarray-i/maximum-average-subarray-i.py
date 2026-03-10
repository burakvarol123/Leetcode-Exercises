class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window = nums[0:k]
        window_sum = sum(window)
        largest = window_sum
        for right in range(k,len(nums)):
            left = right - k
            window_sum -= nums[left] 
            window_sum += nums[right] 
            largest = max(largest, window_sum)
        return largest / k
        