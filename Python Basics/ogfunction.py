#Little changes have been made to the functions as I have added another function which checks if thenumbe is a palindrome or not.
#Strange thig is this exact copy of logic doesn't apply on leetcode

def reverseNum(num):
    ans = 0
    while num:
        digit = num % 10
        ans = (ans * 10) + digit
        num //=10
    return ans

def isPalindrome(num: int) -> bool:
    return num == reverseNum(num)

num = int(input("Enter a number: "))

ans = reverseNum(num)
print(ans)

#check palindrome
if isPalindrome(num) == True:
    print("Palindrome")
else:
    print("What?")
