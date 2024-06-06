import pandas as pd


# Since there is also data addition and subtraction in each separate class,
# I only used it to add something separate here in the future,
# there is no active use of this function anywhere.
class Data:
    def __init__(self, data_file_path, supplier_file_path):
        self.data_file_path = data_file_path
        self.supplier_file_path = supplier_file_path

    def read_product_data(self):
        return pd.read_csv(self.data_file_path)

    def read_stock_data(self):
        return pd.read_csv(self.data_file_path)

    def read_supplier_data(self):
        return pd.read_csv(self.supplier_file_path)

    def read_purchase_order_data(self):
        return pd.read_csv(self.data_file_path)

    def write_product_data(self, data):
        data.to_csv(self.data_file_path, index=False)

    def write_stock_data(self, data):
        data.to_csv(self.data_file_path, index=False)

    def write_supplier_data(self, data):
        data.to_csv(self.supplier_file_path, index=False)

    def write_purchase_order_data(self, data):
        data.to_csv(self.data_file_path, index=False)
