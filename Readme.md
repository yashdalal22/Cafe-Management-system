# Cafe Management System 🏨

This is a simple and interactive Cafe Management System built using Python's Tkinter library for GUI and MySQL for database management. It allows customers to view a menu, place orders, adjust quantities, and complete their order with a name and total price. All data is stored in a MySQL database, which includes tables for the menu and orders.

## 🚀Features
### Menu Display: The menu is dynamically fetched from the MySQL database and displayed with items and prices.
### Order Handling: Customers can select items, adjust quantities, and view a detailed order summary.
### Order Confirmation: Once the order is placed, it is saved in the MySQL database with customer details, selected items, and the total price.
### Exit Functionality: The user can exit the application at any stage, with a farewell message.

## 🛠️Prerequisites
1. Python 3.x
2. Tkinter (pre-installed with Python)
3. MySQL Database
4. MySQL Connector (Install with pip install mysql-connector)

## 🔧Setup Instructions
1. Install MySQL and Set Up Database
Install MySQL if you haven't 

2. Install Required Python Packages
Run the following command to install MySQL connector:

pip install mysql-connector

3. Running the Application
Save the provided Python code to a file, e.g., cafe_management_system.py.

Open the terminal or command prompt and navigate to the folder where the script is saved.

The application will open a GUI where you can:

1. View the available menu items.
2. Select items and place an order.
3. Enter your name and finalize the order.
4. Exit the application.
  
4. Database Setup
The script will automatically create two tables if they do not already exist:

menu: Stores the menu items (name and price).
orders: Stores customer orders with the customer's name, ordered items, and total price.
Additionally, a set of sample menu items will be inserted into the menu table if it's empty.

## Code overview 👓

## Functions of CafeManagementSystem Class:

menu_screen(): Displays the main menu where customers can select items.
place_order(): Collects the selected items and proceeds to the order summary page.
order_screen(): Displays the order summary and allows customers to modify quantities or finalize the order.
finalize_order(): Saves the order to the database and confirms the order placement.
exit_app(): Exits the application with a farewell message.
clear_screen(): Clears the current screen to prepare for the next view.

## Important Note 📄
1. Ensure that MySQL is running before launching the application.
2. Modify the MySQL username, password, and database name in the connect_db() function if necessary.
3. Sample menu items will be inserted automatically into the database if the menu table is empty.
## Screenshots
### 💸Menu Screen: 
Displays a list of menu items with their prices.
![Screenshot 2025-01-09 153356](https://github.com/user-attachments/assets/7e06c5b2-2c60-4e82-9bc6-b09d2ed305d3)


### 🥘Order Summary:
Shows the selected items, their quantities, and the total price. Customers can adjust quantities or place the order.
![Screenshot 2025-01-09 153430](https://github.com/user-attachments/assets/74fcb676-c17a-41e6-81cc-5c46875f7cf9)


### 🚴‍♂️Order Confirmation:
After placing an order, the system confirms the order with a success message.
![Screenshot 2025-01-09 153800](https://github.com/user-attachments/assets/fea534a2-ec7a-4dec-914b-ad5fd5f80698)

### 🔚EXit:
After selected the exit, the system will close and shows a thank you message.
![Screenshot 2025-01-09 153554](https://github.com/user-attachments/assets/fd0c400c-f962-4799-aa80-64c5663fd423)


## Conclusion 👓

This README file explains the setup and usage of your Cafe Management System. You can add or modify the sections as needed based on further features or changes.

🥳Thank you for using the Cafe Management System!

