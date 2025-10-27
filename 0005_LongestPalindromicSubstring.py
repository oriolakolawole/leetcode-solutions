class Solution:
    def longestPalindrome(self, s):
        if not s:
            return ""
        
        #expanding from the center of the string to check for palindrome
        def expansion (a , b):
            while a >= 0 and b < len(s) and s[a] == s[b]:
                a -= 1
                b += 1
            return s[a+1:b]
        
        longest = "" #keep track of longest palindrome
        for i in range(len(s)):
            
            #check for odd palindrome
            oddPal = expansion(i, i)
            if len(oddPal) > len(longest):
                longest = oddPal
            
            #incase there are even palindrome   
            evenPal = expansion(i, i+1)
            if len(evenPal) > len(longest):
                longest = evenPal
        return longest
        

sol = Solution()
print(sol.longestPalindrome("dabage"))
        
