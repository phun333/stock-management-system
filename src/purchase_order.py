from product import Product


# adds to that product by taking value from the user for stocks that are running out.
class PurchaseOrder:
    def __init__(self, product_name, quantity):
        self.product_name = product_name
        self.quantity = quantity
        self.product = Product()

    def generate_order(self):
        print(f"Purchase order generated for {self.quantity} units of {self.product_name}.")
        product = self.product.search_product(self.product_name)
        if product:
            product['quantity'] += self.quantity
            self.product.update_product(self.product_name, product)
            self.product.save_products()
