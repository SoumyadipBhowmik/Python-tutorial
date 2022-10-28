def reverseNum(num):
    ans = 0
    while num:
        digit = num % 10
        ans = (ans * 10) + digit
        num //=10
    return ans

num = int(input("Enter a number: "))

ans = reverseNum(num)
print(ans)

#check palindrome
if reverseNum(num) == num:
    print("Palindrome!")
else:
    print("Not today buddy.")
