class Solution:
    def isPalindrome(self, x: int) -> bool:
        reverse = 0 
        original = x
        while original > 0:
            last_digit = original % 10
            reverse = reverse*10 + last_digit
            original = original // 10
        print(reverse)
        return reverse == x
        
