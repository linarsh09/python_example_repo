#7

class Product:
    def __init__(self, product_id, name, price, stock, reviews):
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__stock = stock
        self.__reviews = reviews

# геттер
    def get_product_id(self):
        return self.__product_id

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def get_stock(self):
        return self.__stock

    def get_reviews(self):
        return self.__reviews

# сеттер
    def set_name(self, name):
        self.__name = name

    def set_price(self, price):
        if price >= 0:
            self.__price = price

    def set_stock(self, stock):
        if stock >= 0:
            self.__stock = stock

# методы
    def restock(self, quantity):
        self.__stock += quantity

    def sell(self, quantity):
        if quantity <= self.__stock:
            self.__stock -= quantity
        else:
            print("Недостаточно товара на складе")

    def get_value(self):
        return self.__price * self.__stock

    def is_in_stock(self):
        return self.__stock > 0

    def calculate_average_review(self):
        if len(self.__reviews) == 0:
            return 0
        total = 0
        for review in self.__reviews:
            total += review
        return total / len(self.__reviews)

    def __eq__(self, other):
        return self.__product_id == other.__product_id

    def __ge__(self, other):
        return self.__price >= other.__price

    def __getitem__(self, index):
        return self.__reviews[index]

    def __str__(self):
        return f"Продукт: {self.__name}; Цена: {self.__price}"


##############################################


class DiscountedProduct(Product):
    def __init__(self, product_id, name, price, stock, discount_percent, reviews):
        super().__init__(product_id, name, price, stock, reviews)
        self.__discount_percent = discount_percent

    def apply_discount(self):
        discount = self.get_price() * (self.__discount_percent / 100)
        return self.get_price() - discount

# переопределение
    def get_value(self):
        discounted_price = self.apply_discount()
        return discounted_price * self.get_stock()

# переопределение среднего рейтинга (пример: учитываем скидку как бонус)
    def calculate_average_review(self):
        base = super().calculate_average_review()
        return base + (self.__discount_percent / 100)

##############################################

# Пример использования

p1 = Product(1, "Phone", 1000, 5, [4, 5, 5])
p2 = DiscountedProduct(2, "Laptop", 2000, 3, 10, [5, 4, 5])

print(p1)
print(p2)

print("Value p1:", p1.get_value())
print("Value p2:", p2.get_value())

print("Средний рейтинг p1:", p1.calculate_average_review())
print("Средний рейтинг p2:", p2.calculate_average_review())

print("Сравнение:", p1 >= p2)
print("Отзывы p1[1]:", p1[1])