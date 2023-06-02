from abc import ABC, abstractmethod


class Promotion(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def apply_promotion(self, product, quantity):
        pass


class PercentDiscount(Promotion):
    def __init__(self, name, percent):
        super().__init__(name)
        self.percent = percent

    def apply_promotion(self, product, quantity):
        discount_amount = product.price * self.percent / 100
        total_price = product.price * quantity
        discounted_price = total_price - discount_amount
        return discounted_price


class SecondHalfPrice(Promotion):
    def __init__(self, name):
        super().__init__(name)

    def apply_promotion(self, product, quantity):
        full_price_items = quantity // 2
        half_price_items = quantity - full_price_items
        total_price = (full_price_items * product.price) + (half_price_items * (product.price / 2))
        return total_price


class ThirdOneFree(Promotion):
    def __init__(self, name):
        super().__init__(name)

    def apply_promotion(self, product, quantity):
        full_price_items = (quantity // 3) * 2
        free_items = quantity - full_price_items
        total_price = full_price_items * product.price
        return total_price


class Product:
    def __init__(self, name, price, quantity):
        if not name or price < 0 or quantity < 0:
            raise ValueError("Invalid input. Please provide a valid name, positive price, and quantity.")
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True
        self.promotion = None

    def __str__(self):
        return f"Product: {self.name}, Price: ${self.price}, Quantity: {self.quantity}"

    def purchase(self, quantity):
        if self.quantity < quantity:
            raise ValueError("Insufficient quantity available")
        self.quantity -= quantity
        return self.price * quantity

    def get_quantity(self):
        return self.quantity

    def set_quantity(self, quantity):
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def is_active(self):
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def set_promotion(self, promotion):
        self.promotion = promotion

    def remove_promotion(self):
        self.promotion = None

    def show(self):
        print(f"{self.name} - ${self.price} ({self.quantity} available)")
        if self.promotion:
            print(f"Promotion: {self.promotion.name}")

    def buy(self, quantity):
        if self.quantity >= quantity:
            self.quantity -= quantity
            if self.promotion:
                return self.promotion.apply_promotion(self, quantity)
            else:
                return self.price * quantity
        else:
            print("Insufficient quantity!")
            return 0


class NonStockedProduct(Product):
    def __init__(self, name, price):
        super().__init__(name, price, 0)

    def show(self):
        print(f"{self.name} - ${self.price} (Not stocked)")


class LimitedProduct(Product):
    def __init__(self, name, price, quantity, maximum):
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def show(self):
        print(f"{self.name} - ${self.price} ({self.quantity}/{self.maximum} available)")


product_list = [
    Product("MacBook Air M2", price=1450, quantity=100),
    Product("Bose QuietComfort Earbuds", price=250, quantity=500),
    Product("Google Pixel 7", price=500, quantity=250),
    Product("Windows License", price=125, quantity=0),
    Product("Shipping", price=10, quantity=250)
]

# Create promotion catalog
second_half_price = SecondHalfPrice("Second Half price!")
third_one_free = ThirdOneFree("Third One Free!")
thirty_percent = PercentDiscount("30% off!", percent=30)

# Add promotions to products
product_list[0].set_promotion(second_half_price)
product_list[1].set_promotion(third_one_free)
product_list[3].set_promotion(thirty_percent)

# Test the code
for product in product_list:
    product.show()

print("-------------------------")
total_price = product_list[0].buy(3)
print(f"Total price: ${total_price}")

print("-------------------------")
total_price = product_list[1].buy(4)
print(f"Total price: ${total_price}")

print("-------------------------")
total_price = product_list[3].buy(2)
print(f"Total price: ${total_price}")
