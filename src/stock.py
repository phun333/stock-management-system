# stock.py
import csv

class Stock:
    def __init__(self, filename):
        self.filename = filename
        self.stock_data = self.load_stock_data()

    def load_stock_data(self):
        with open(self.filename, 'r') as file:
            reader = csv.DictReader(file)
            return list(reader)

    def update_stock_data(self):
        with open(self.filename, 'w') as file:
            fieldnames = ['name', 'price', 'quantity']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(self.stock_data)

    def receive_stock(self, product_name, quantity):
        for product in self.stock_data:
            if product['name'] == product_name:
                product['quantity'] = str(int(product['quantity']) + quantity)
        self.update_stock_data()

    def record_sale(self, product_name, quantity):
        for product in self.stock_data:
            if product['name'] == product_name:
                product['quantity'] = str(int(product['quantity']) - quantity)
        self.update_stock_data()