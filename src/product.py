import pandas as pd


class Product:
    def __init__(self):
        self.df = pd.read_csv('../datas/data.csv')

    # with the pd.concat function we add our value to our datasheet
    def add_product(self, product):
        new_df = pd.DataFrame([product])
        self.df = pd.concat([self.df, new_df], ignore_index=True)
        print(f"Product {product['name']} added successfully.")

    # with the loc function, we can change the information in any line
    def update_product(self, product_name, updated_product):
        index = self.df[self.df['name'] == product_name].index
        if not index.empty:
            self.df.loc[index[0]] = updated_product
            print(f"Product {product_name} updated successfully.")
        else:
            print(f"Product {product_name} not found.")

    def delete_product(self, product_name):
        index = self.df[self.df['name'] == product_name].index
        if not index.empty:
            self.df = self.df.drop(index)
            print(f"Product {product_name} deleted successfully.")
        else:
            print(f"Product {product_name} not found.")

    # if the DataFrame is not empty, converts the results to a list of
    # dictionaries and returns the first element of that list.
    def search_product(self, product_name):
        product = self.df[self.df['name'] == product_name]
        if not product.empty:
            return product.to_dict('records')[0]
        else:
            print(f"Product {product_name} not found.")
            return None

    def save_products(self):
        self.df.to_csv('../datas/data.csv', index=False)
