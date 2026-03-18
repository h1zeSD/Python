def roman_to_int(roman_num: str):
        values = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
        }

        reverse_str = roman_num[::-1]

        result = 0
        prev_value = -1
        
        for char in reverse_str:
            cur_value = values[char]

            if cur_value < prev_value:
                  result -= cur_value
            else:
                  result += cur_value
            prev_value = cur_value
        
        return result

print(roman_to_int("IV"))