# class Solution:
def isPalindrome(x):
    if x < 0 or (x % 10 == 0 and x != 0): # excluding all numbers ending with 0, except 0
        return False

    second_half = 0

    while(second_half < x):
        second_half = (x % 10) + (second_half * 10)
        if isinstance(x / 10, int): # when the first half is in the range [0,9], division would return a floating point number 
            break
        x //= 10
    return x == second_half or x == second_half // 10  # when the number has an odd number of digits the middle one can be just thown out after calculating teh second

print(isPalindrome(11))
print(isPalindrome(121))
print(isPalindrome(1234))
print(isPalindrome(-1001))
print(isPalindrome(1001))
print(isPalindrome(1122522113))
print(isPalindrome(112252211))
print(isPalindrome(-112252211))
