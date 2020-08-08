# Input: "III"
# Output: 3

# Input: "IV"
# Output: 4

# Input: "IX"
# Output: 9

# Input: "LVIII"
# Output: 58

# Input: "MCMXCIV"
# Output: 1994
def func(s):
    roman = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000 }    
    num = 0

    for i in range(len(s)):
        if i!=len(s)-1 and roman[s[i]] <roman[s[i+1]]:
            num += roman[s[i]]*(-1)
        else:
            num +=roman[s[i]]
    return num
s="XLVIII"
print(func(s))