class Solution:
    def romanToInt(self, s):
        # Map each Roman numeral to its integer value
        roman_map = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
        
        total = 0        # Initialize total sum
        prev_value = 0   # Keep track of the previous numeral's value
        
        # Process the string from right to left
        for char in reversed(s):
            value = roman_map[char]  # Get integer value of current numeral
            
            if value < prev_value:
                # Subtract if current numeral is smaller than previous
                # Example: in "IV", I(1) < V(5) → subtract 1
                total -= value
            else:
                # Otherwise, add the value
                total += value
            
            # Update previous value for next iteration
            prev_value = value
            
        return total

        