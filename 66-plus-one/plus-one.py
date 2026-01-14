class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        counter = 1

        for digit in digits:
            last_digit = digits[-counter]
            remainder = (last_digit + 1) // 10
            if remainder == 0:
                digits[-counter] = digits[-counter] + 1  
                break 
            else:
                digits[-counter] = 0
                counter += 1
        if remainder == 1:
            digits = [1] + digits  
        return digits
            


            
            


        