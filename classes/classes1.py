# Define shopping cart class
# Initialise with empty contents
# Method to add
# Method to see what's in it

class Product:
    def __init__(self, name, price, brand):
        self.name = name
        self.price = price
        self.brand = brand

    def __repr__(self):
        return f"{self.name} ({self.brand}) £{self.price}"


class Cart:
    def __init__(self):
        self.contents = []



    def add(self, item: Product):
        self.contents.append(item)

    def check(self):
        for Product in self.contents:
            print(f"{Product.name} from {Product.brand}: {Product.price}")

    def total(self):
        total = 0
        for p in self.contents:
            total += p.price
        return total



shopping = Cart()
# print(shopping.check())
# shopping.add("cheese")
shopping.check()

shopping.add(Product("Chicken", 2.50, "Morrisons"))
shopping.add(Product("Coffee", 3.50, "Tesco"))
shopping.add(Product("Gold bar", 0.75, "Aldi"))
shopping.check()
print(shopping.total())

print(shopping.contents)