class Item:
    # Note
    # Class has magic methods, and magic attributes

    # Class attribute
    pay_rate = 0.8 # Price after discount
    all = []
    
    # Constructor, this is magic method
    def __init__(self, name: str, price: float, quantity=0):
        # Validation
        assert price >= 0, f"Price {price} can not be less than ZERO."
        assert quantity >= 0, f"Quantity {quantity} can not be less than ZERO."

        # Assignment
        self.name = name
        self.price = price
        self.quantity = quantity

        # Actions
        Item.all.append(self)
    

    def __repr__(self):
        return f"Item('{self.name}', '{self.price}', '{self.quantity}')"


    def calculate_total_price(self):
        return self.price * self.quantity
    

    def apply_discount(self):
        # Here accessing from Class Level, so value will not never update at instance level
        # self.price = self.price * Item.pay_rate
        # Here accessing from instance level, so value will be update at instance level
        self.price = self.price * self.pay_rate

    


item1 = Item(name="iPhone", price=150, quantity=5)
item2 = Item(name="MacBook", price=1000, quantity=3)
item3 = Item(name=1, price=100, quantity=5)

# print(item1.name)
# print(item2.name)
# print(item3.name)
# print(item1.calculate_total_price())
# print(item2.calculate_total_price())
# print(item3.calculate_total_price())

# print(Item.__dict__) # All attributes for Class Level
# print(item1.__dict__) # All attributes for Instance Level

# item2.pay_rate = 0.7
# item2.apply_discount()
# print(item2.price)

print(Item.all)