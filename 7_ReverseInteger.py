class Solution:
    def reverse(self, x):
        sign = -1 if x < 0 else 1
        x = abs(x)
        # convert to str, reverse the convert to int
        rev = int(str(x)[::-1]) * sign
        
        # Check 32-bit overflow
        if rev < -2**31 or rev > 2**31 - 1:
            return 0
        return rev
