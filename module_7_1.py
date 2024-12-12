class Product:
    def __init__(self, name, weight, category):
        self.name = str(name)
        self.weight = float(weight)
        self.category = str(category)

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name, 'r')
        product = file.read()
        file.close()
        return product

    def add(self, *products: Product):
        file = open(self.__file_name, 'a+')
        for product in products:
            products = self.get_products()
            if product.name in products:
                print(f'Продукт {product.name} уже есть в магазине')
            else:
                file.write(f'{product}\n')
        file.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Tomato', 5.5, 'Vegetables') # Мне показалось, что в задании ошибка! 2-ой раз Potato.
print(p2)
s1.add(p1, p2, p3)
print(s1.get_products())