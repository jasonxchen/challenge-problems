# https://leetcode.com/problems/roman-to-integer/
# https://leetcode.com/submissions/detail/825747096/

def romanToInt(s):
    symbol_dict = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    total = 0
    for i, symbol in enumerate(s):
        if symbol == "I" and i < len(s) - 1 and (s[i + 1] == "V" or s[i + 1] == "X"):
            total -= 1
        elif symbol == "X" and i < len(s) - 1 and (s[i + 1] == "L" or s[i + 1] == "C"):
            total -= 10
        elif symbol == "C" and i < len(s) - 1 and (s[i + 1] == "D" or s[i + 1] == "M"):
            total -= 100
        else:
            total += symbol_dict[symbol]
    return total

print(romanToInt("III"))        # expect 3
print(romanToInt("LVIII"))      # expect 58
print(romanToInt("MCMXCIV"))    # expect 1994
