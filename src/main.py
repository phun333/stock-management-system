#import os
#import datetime
#import csv
#import pandas

# user login system

admin_username = ["admin", "ADMIN"]
admin_password = ["test", "TEST"]

print("********** Login System **********")
while True:
    username_input = input(
        "Please enter your username: ")
    if username_input.lower() in admin_username:
        password_input = input(f"Please enter the password for *{username_input}* account.")
        if password_input.lower() in admin_password:
            print("Login successful")
            break
        else:
            print(f"Incorrect password for {username_input}, try the login system again")
    else:
        print("login error. Please try again")

print("passed the login system")

