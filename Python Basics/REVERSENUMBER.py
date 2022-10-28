n = int(input("Enter a number: "))
ans = 0

while n:
    ans = ans * 10 + n % 10
    n = n//10 #double divide returns an integer number. sngle / returns a floating point number

print(ans)
