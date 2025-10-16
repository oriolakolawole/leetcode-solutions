class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers are not palindromes
        # Numbers ending with 0 are not palindromes (except 0 itself)
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        # Reverse the second half of the number
        # We only need to reverse half the number to check for palindrome
        reversed_half = 0
        while x > reversed_half:
            # Extract the last digit and append to reversed_half
            reversed_half = reversed_half * 10 + x % 10
            # Remove the last digit from x
            x //= 10
        
        # For even length numbers: x == reversed_half (e.g., 1221: x=12, reversed_half=12)
        # For odd length numbers: x == reversed_half // 10 (e.g., 12321: x=12, reversed_half=123)
        return x == reversed_half or x == reversed_half // 10

