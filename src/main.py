# import os
# import datetime
# import csv
# import pandas
from product import Product
from supplier import Supplier

# user login system

admin_username = ["admin", "ADMIN"]
admin_password = ["test", "TEST"]

print("********** Login System **********")
while True:
    username_input = input(
        "Please enter your username: ")
    if username_input.lower() in admin_username:
        password_input = input(f"Please enter the password for *{username_input}* account: ")
        if password_input.lower() in admin_password:
            print("Login successful")
            break
        else:
            print(f"Incorrect password for {username_input}, try the login system again")
    else:
        print("login error. Please try again")


def product_manager_system():
    product_manager = Product()

    while True:
        print("\n1. Add product")
        print("2. Update product")
        print("3. Delete product")
        print("4. Search product")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        if choice == '1':
            product_name = input("Enter product name: ")
            product_price = float(input("Enter product price: "))
            product_quantity = int(input("Enter product quantity: "))
            product = {'name': product_name, 'price': product_price, 'quantity': product_quantity}
            product_manager.add_product(product)
            product_manager.save_products()

        elif choice == '2':
            product_name = input("Enter product name to update: ")
            updated_product_name = input("Enter updated product name: ")
            updated_product_price = float(input("Enter updated product price: "))
            updated_product_quantity = int(input("Enter updated product quantity: "))
            updated_product = {'name': updated_product_name, 'price': updated_product_price,
                               'quantity': updated_product_quantity}
            product_manager.update_product(product_name, updated_product)
            product_manager.save_products()

        elif choice == '3':
            product_name = input("Enter product name to delete: ")
            product_manager.delete_product(product_name)
            product_manager.save_products()

        elif choice == '4':
            product_name = input("Enter product name to search: ")
            product = product_manager.search_product(product_name)
            if product:
                print(product)

        elif choice == '5':
            break

        else:
            print("Invalid choice. Please try again.")


def supplier_manager_system():
    supplier_manager = Supplier()

    while True:
        print("\n1. Add supplier")
        print("2. Update supplier")
        print("3. Delete supplier")
        print("4. Search supplier")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        if choice == '1':
            supplier_name = input("Enter supplier name: ")
            supplier_contact_information = input("Enter contact information: ")
            supplier_product_category = input("Enter product category: ")
            supplier = {'name': supplier_name, 'supplier_contact_information': supplier_contact_information,
                        'supplier_product_category': supplier_product_category}
            supplier_manager.add_supplier(supplier)
            supplier_manager.save_supplier()

        elif choice == '2':
            supplier_name = input("Enter product name to update: ")
            updated_supplier_name = input("Enter updated product name: ")
            updated_supplier_contact_information = input("Enter updated contact information: ")
            updated_supplier_product_category = input("Enter updated product category: ")
            updated_supplier = {'name': updated_supplier_name,
                                'supplier_contact_information': updated_supplier_contact_information,
                                'supplier_product_category': updated_supplier_product_category}
            supplier_manager.update_supplier(supplier_name, updated_supplier)
            supplier_manager.save_supplier()

        elif choice == '3':
            supplier_name = input("Enter supplier name to delete: ")
            supplier_manager.delete_supplier(supplier_name)
            supplier_manager.save_supplier()

        elif choice == '4':
            supplier_name = input("Enter supplier name to search: ")
            supplier = supplier_manager.search_product(supplier_name)
            if supplier:
                print(supplier)

        elif choice == '5':
            break

        else:
            print("Invalid choice. Please try again.")


# Main menu
if __name__ == '__main__':
    test = input("type 1 to see transactions related to products, type 2 to see transactions related to supplier: ")
    if test == '1':
        product_manager_system()
    elif test == '2':
        supplier_manager_system()
    else:
        print("Invalid choice. Please try again.")

