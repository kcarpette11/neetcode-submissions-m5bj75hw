class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0: # 0 raised to any power is 0 itself
            return 0
        if x == 1: # 1 raised to any power is one itself
            return 1

        if n < 0:
           x = 1 /x # if n is a negative integer 
           n = -n
        if n == 0: # if the exponent is 0, answer is 1
            return 1 
        if n == 1: # any number with 1 as exponent, it will be the base itself
            return x
        res = 1 # initialize result 
         
        power = abs(n) 
        for i in range(power):
            res *= x 

        return res # return result 

        























































            