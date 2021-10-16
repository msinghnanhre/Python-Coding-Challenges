import os
import csv

class Item:
    discounted_price = 0.8
    all = []
    def __init__(self,name: str,price: float, quantity = 0):
        #Run validations to the received arguments
        assert price >= 0 , f"Price {price} has to be positive"
        assert quantity >= 0, f"Quantity {quantity} has to be positive"

        #assign to self object
        self.name = name
        self.price = price 
        self.quantity = quantity

        #Actions to execute
        Item.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, {self.price},{self.quantity})"

    def calculate_total_price(self):
        return self.price*self.quantity

    def discounted_price_after_sale(self):
        return self.price*self.quantity*self.discounted_price

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, value):
        self.__name = value

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        for item in items:
            Item(
                name = item.get('name'),
                price = float(item.get('price')),
                quantity = int(item.get('quantity'))
            )

#print(Item.__dict__) #class level attributes
#print(item1.__dict__) #instance level attributes

Item.instantiate_from_csv()
print(Item.all)

#Start Inheritance
class Phone(Item):
    all=[]

    def __init__(self, name: str, price: float, broken_phones = 0, quantity=0):
        super().__init__(
            name, price, quantity
            )
        #Run validations to the received arguments
        assert broken_phones >= 0, f"Broken Phones {broken_phones} has to be positive"

        #assign to self object
        self.broken_phones = broken_phones

        #Actions to execute
        Phone.all.append(self)

phone1 = Phone("JscPhonev10", 500, 5, 1)
phone2 = Phone("JscPhonev20", 700, 5, 1)

print(phone1.calculate_total_price())
print(Phone.all)
# cwd = os.getcwd()  # Get the current working directory (cwd)
# files = os.listdir(cwd)  # Get all the files in that directory
# print("Files in %r: %s" % (cwd, files))


item19 = Item("Abc", 5, 10)
item19.name = "ABCD"

print(Item.all)
