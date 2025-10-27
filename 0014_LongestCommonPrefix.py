class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        
        for i in range(len(strs[0])):  # for each character in first string
            char = strs[0][i]
            for s in strs[1:]:
                # If index i exceeds string length or char mismatches
                if i >= len(s) or s[i] != char:
                    return strs[0][:i]
        
        return strs[0]  # All characters matched

        
