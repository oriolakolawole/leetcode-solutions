class Solution(object):
    def convert(self, s, numRows):
        
        
        if numRows == 1 or numRows >= len(s):
            return s
        
        thes = ""
        cycle = 2 * numRows - 2  # Length of one complete zigzag cycle
        
        for row in range(numRows):
            # For first and last rows, step is always cycle
            # For middle rows, alternate between two different steps
            i = row
            
            while i < len(s):
                thes += s[i]
                
                # For middle rows, add the diagonal character
                if row != 0 and row != numRows - 1:
                    # Diagonal character position
                    next_i = i + cycle - 2 * row
                    if next_i < len(s):
                        thes += s[next_i]
                
                # Move to next main character in this row
                i += cycle
        
        return thes