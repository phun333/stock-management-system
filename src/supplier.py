import pandas as pd

class Supplier:
    def __init__(self):
        self.df = pd.read_csv('supplier.csv')

    def add_supplier(self, supplier):
        new_df = pd.DataFrame([supplier])
        self.df = pd.concat([self.df, new_df], ignore_index=True)
        print(f"supplier {supplier['name']} added successfully.")

    # Rest of your code...

    def update_supplier(self, supplier_name, updated_supplier):
        index = self.df[self.df['name'] == supplier_name].index
        if not index.empty:
            self.df.loc[index[0]] = updated_supplier
            print(f"supplier {supplier_name} updated successfully.")
        else:
            print(f"supplier {supplier_name} not found.")

    def delete_supplier(self, supplier_name):
        index = self.df[self.df['name'] == supplier_name].index
        if not index.empty:
            self.df = self.df.drop(index)
            print(f"supplier {supplier_name} deleted successfully.")
        else:
            print(f"supplier {supplier_name} not found.")

    def search_supplier(self, supplier_name):
        supplier = self.df[self.df['name'] == supplier_name]
        if not supplier.empty:
            return supplier.to_dict('records')[0]
        else:
            print(f"supplier {supplier_name} not found.")
            return None

    def save_supplier(self):
        self.df.to_csv('supplier.csv', index=False)

    def search_product(self, supplier_name):
        pass