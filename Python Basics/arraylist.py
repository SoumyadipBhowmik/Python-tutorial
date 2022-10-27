# lists are basically how array works in java or most commonly how vector works in C++
# this is a demonstration on how to take user input for a list in python

list = []
n = int(input("Enter the size of the array: "))
for i in range(n):
    element = int(input("Enter element no. %d: " %(i+1)))
    list.append(element)

print(list)