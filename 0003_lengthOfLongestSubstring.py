class Solution:
    def lengthOfLongestSubstring(self, str):
        seen = ""
        lengths = []

        for char in str:
            if char in seen:
                
                #saving all length in an array (not optimal though)
                lengths.append(len(seen))
                index = seen.find(char)

                #removing duplicates in substring {acade -> ade}
                seen = seen[index + 1:]
            seen += char

        lengths.append(len(seen))
        return max(lengths)

                
