from product import Product
from supplier import Supplier
from utils import Utils
from stock import Stock
from purchase_order import PurchaseOrder

# user login system

admin_username = ["admin", "ADMIN"]
admin_password = ["test", "TEST"]

time = Utils()
print("********** Login System **********")
while True:
    username_input = input(
        "Please enter your username: ")
    if username_input.lower() in admin_username:
        password_input = input(f"Please enter the password for *{username_input}* account: ")
        if password_input.lower() in admin_password:
            print("\nLogin successful\nTime : " + time.format_date())
            break
        else:
            print(f"Incorrect password for {username_input}, try the login system again")
    else:
        print("login error. Please try again")


# product manager system
def product_manager_system():
    product_manager = Product()

    while True:
        print("\n1. Add product")
        print("2. Update product")
        print("3. Delete product")
        print("4. Search product")
        print("5. Exit")

        product_choice = input("\nEnter your choice: ")

        if product_choice == '1':
            product_name = input("Enter product name: ")
            product_price = float(input("Enter product price: "))
            product_quantity = int(input("Enter product quantity: "))
            product = {'name': product_name, 'price': product_price, 'quantity': product_quantity}
            product_manager.add_product(product)
            product_manager.save_products()

        elif product_choice == '2':
            product_name = input("Enter product name to update: ")
            updated_product_name = input("Enter updated product name: ")
            updated_product_price = float(input("Enter updated product price: "))
            updated_product_quantity = int(input("Enter updated product quantity: "))
            updated_product = {'name': updated_product_name, 'price': updated_product_price,
                               'quantity': updated_product_quantity}
            product_manager.update_product(product_name, updated_product)
            product_manager.save_products()

        elif product_choice == '3':
            product_name = input("Enter product name to delete: ")
            product_manager.delete_product(product_name)
            product_manager.save_products()

        elif product_choice == '4':
            product_name = input("Enter product name to search: ")
            product = product_manager.search_product(product_name)
            if product:
                print(product)

        elif product_choice == '5':
            break

        else:
            print("Invalid choice. Please try again.")


# supplier manager system
def supplier_manager_system():
    supplier_manager = Supplier()

    while True:
        print("\n1. Add supplier")
        print("2. Update supplier")
        print("3. Delete supplier")
        print("4. Search supplier")
        print("5. Exit")

        supplier_choice = input("\nEnter your choice: ")

        if supplier_choice == '1':
            supplier_name = input("Enter supplier name: ")
            supplier_contact_information = input("Enter contact information: ")
            supplier_product_category = input("Enter product category: ")
            supplier = {'name': supplier_name, 'supplier_contact_information': supplier_contact_information,
                        'supplier_product_category': supplier_product_category}
            supplier_manager.add_supplier(supplier)
            supplier_manager.save_supplier()

        elif supplier_choice == '2':
            supplier_name = input("Enter product name to update: ")
            updated_supplier_name = input("Enter updated product name: ")
            updated_supplier_contact_information = input("Enter updated contact information: ")
            updated_supplier_product_category = input("Enter updated product category: ")
            updated_supplier = {'name': updated_supplier_name,
                                'supplier_contact_information': updated_supplier_contact_information,
                                'supplier_product_category': updated_supplier_product_category}
            supplier_manager.update_supplier(supplier_name, updated_supplier)
            supplier_manager.save_supplier()

        elif supplier_choice == '3':
            supplier_name = input("Enter supplier name to delete: ")
            supplier_manager.delete_supplier(supplier_name)
            supplier_manager.save_supplier()

        elif supplier_choice == '4':
            supplier_name = input("Enter supplier name to search: ")
            supplier = supplier_manager.search_product(supplier_name)
            if supplier:
                print(supplier)

        elif supplier_choice == '5':
            break

        else:
            print("Invalid choice. Please try again.")


# purchase order system


def purchase_order():
    # ask the user for the product name and the quantity to add
    product_name = input("Enter the product name: ")
    quantity = int(input("Enter the quantity to add: "))

    po = PurchaseOrder(product_name, quantity)
    po.generate_order()


# stocking system


def stock():
    while True:
        print("\n1. Receive stock")
        print("\n2. Record sale")
        print("3. Exit")

        stock_choice = input("\nEnter your choice: ")
        stock_manager = Stock('../datas/data.csv')

        # receive stock
        if stock_choice == '1':
            product_name = input("Enter the product name to receive stock: ")
            quantity = int(input("Enter the quantity to receive: "))
            stock_manager.receive_stock(product_name, quantity)
        elif stock_choice == '2':
            # record sale
            product_name = input("Enter the product name to record sale: ")
            quantity = int(input("Enter the quantity sold: "))
            stock_manager.record_sale(product_name, quantity)
        elif stock_choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")


# Main menu
if __name__ == '__main__':
    print("\n********** Menu **********")
    print("\n1. To see transactions related to products")
    print("2. To see transactions related to supplier")
    print("3. To generate purchase orders for low stock items")
    print("4. to stock tracking (receive stock, record sales, update stock levels).")
    choice = input("\nEnter your choice: ")
    if choice == '1':
        product_manager_system()
    elif choice == '2':
        supplier_manager_system()
    elif choice == '3':
        purchase_order()
    elif choice == '4':
        stock()
    else:
        print("Invalid choice. Please try again.")
