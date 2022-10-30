#used constructors in class
#They are called the init methodor the magic method1 in class and object in python
#going to go over this again

class Item:
    def __init__(self, name: str, price = 0, quantity = 0):
        #running vaidation checks about for possible edge cases
        assert price >= 0, f"Price {price} can't be less than 0" #assert is used as a part if else/while inside constructors for validation checks and to find out errors
        assert quantity >= 0, f"Price {quantity} can't be less than 0"


        #Assigning to self objects
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate(self):
        return self.price * self.quantity

name = input("Enter your name: ")
price = int(input("Enter the price of your car: "))
quantity = int(input("How many cars do you own? "))

item1 = Item(name, price, quantity)
print(f"Hey, this is {item1.name}. I have {item1.quantity} cars, whose price is ${item1.price} each")
totalCost = item1.calculate()
print(f"The total amount is {totalCost}")