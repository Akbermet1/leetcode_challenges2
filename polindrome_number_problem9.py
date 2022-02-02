# class Solution:
def isPalindrome(x):
    string = str(x)
    string_reversed = string[::-1]
    return string == string_reversed

print(isPalindrome(1234))
print(isPalindrome(-1001))
print(isPalindrome(1001))
print(isPalindrome(1122522113))
print(isPalindrome(112252211))
print(isPalindrome(-112252211))
