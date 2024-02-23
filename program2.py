def romanToInt(s):
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    
    total = 0
    prev_value = 0
    
    for symbol in reversed(s):
        current_value = roman_dict[symbol]
        
        if current_value < prev_value:
            total -= current_value
        else:
            total += current_value
        
        prev_value = current_value
    
    return total


print(romanToInt("III"))      
print(romanToInt("LVIII"))    
print(romanToInt("MCMXCIV"))