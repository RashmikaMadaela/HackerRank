#Python — Missing Characters

""" Summary: Implement a function missingCharacters that takes a string consisting of lowercase letters and digits. 
The function should return a new string containing all digits and lowercase English letters that are not present 
in the input string. The digits should come first in ascending order, followed by characters, also in ascending order."""

def missingcharactersfinder(s):
    main = '0123456789abcdefghijklmnopqrstuvwxyz'
    result=[]
    for i in main:
        if i not in s:
            result.append(i)
    return ''.join(result)

print(missingcharactersfinder('abc123')) # 0456789defghijklmnopqrstuvwxyz