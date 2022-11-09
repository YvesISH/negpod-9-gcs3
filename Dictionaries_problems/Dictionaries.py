#!/usr/bin/python3
"""Python Program that converts RomanNumerals to Int"""

def Value(r):
    if (r == 'I'):
        return 1
    if (r == 'V'):
        return 5
    if (r == 'X'):
        return 10
    if (r == 'L'):
        return 50
    if (r == 'C'):
        return 100
    if (r == 'D'):
        return 500
    if (r == 'M'):
        return 1000
    return -1

def RomanToDecimal(str):
    res = 0
    i = 0

    while (i < len(str)):
        """Getting the value of s[i]"""
        s1 = value(str[i])
        if (i + 1 <len(str)):
            """Getting value of symbol s[i + 1]"""
            s2 = value(Str[i + 1])
            '''comparing both Values'''
            if (s1 >= s2):
                res += s1
                i += 1
            else:
                res += s2 - s1
                i = i + 2
        else:
            res += s1
            i += 1
    return res

print(RomanToDecimal("III"))
print(RomanToDecimal("LVIII"))
print(RomanToDecimal("MCMXCIV"))
print(RomanToDecimal("XCIX"))
print(RomanToDecimal("MMDCCCL"))
