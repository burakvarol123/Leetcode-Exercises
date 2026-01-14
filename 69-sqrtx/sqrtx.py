class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        guess = 0
        while guess *guess < x:
            guess += 1
        if guess *guess == x: 
            return guess
        else:
            return guess - 1
      