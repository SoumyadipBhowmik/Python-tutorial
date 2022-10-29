#used constructors in class
#They are called the init methodor the magic method1 in class and object in python
#going to go over this again

class Item:
    def __init__(self, name, price = 0, quantity = 0):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate(self):
        return self.price * self.quantity


item1 = Item("Soumyadip", 14000, 2)
print(f"Hey, this is {item1.name}. I have {item1.quantity} cars, whose price is ${item1.price} each")
totalCost = item1.calculate()
print(f"The total amount is {totalCost}")