import tkinter as tk
from tkinter import messagebox
import mysql.connector

# Connect to MySQL Database
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",  # Your MySQL username
        password="password",  # Your MySQL password
        database="cafe"  # Database name
    )

# Create tables if not exist
def setup_database():
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS menu (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100),
            price FLOAT
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            id INT AUTO_INCREMENT PRIMARY KEY,
            customer_name VARCHAR(100),
            items TEXT,
            total_price FLOAT
        )
    """)
    db.commit()
    cursor.close()
    db.close()

# Insert sample menu items
def populate_menu():
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("SELECT COUNT(*) FROM menu")
    if cursor.fetchone()[0] == 0:
        sample_menu = [
            ("Coffee", 70),
            ("Tea", 30),
            ("Sandwich", 80),
            ("Steam Momos", 80),
            ("Spring Rolls", 60),
            ("Milk Shake", 100),
            ("Fried Momos", 90),
            ("Burger", 60)
        ]
        cursor.executemany("INSERT INTO menu (name, price) VALUES (%s, %s)", sample_menu)
        db.commit()
    cursor.close()
    db.close()

# Fetch menu items from database
def get_menu():
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM menu")
    menu_items = cursor.fetchall()
    cursor.close()
    db.close()
    return menu_items

# Main Application
class CafeManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Cafe Management System")
        self.root.configure(bg="#f8f1f1")
        self.cart = {}  # Store selected items with quantities

        self.menu_screen()

    def menu_screen(self):
        self.clear_screen()
        tk.Label(self.root, text="Cafe Menu", font=("Arial", 20, "bold"), bg="#ff7f50", fg="white").pack(pady=20)

        menu_items = get_menu()
        self.menu_vars = {}

        menu_frame = tk.Frame(self.root, bg="#f8f1f1")
        menu_frame.pack(pady=10)

        for item in menu_items:
            var = tk.IntVar()
            self.menu_vars[item[0]] = var
            tk.Checkbutton(
                menu_frame, 
                text=f"{item[1]} - Rs. {item[2]:.2f}",  # Changed to Rs.
                variable=var, 
                font=("Comic Sans MS", 14, "bold"), 
                bg="#ffe4b5", 
                fg="#000", 
                anchor="w"
            ).pack(anchor="w", padx=10, pady=5)

        tk.Button(self.root, text="Place Order", command=self.place_order, font=("Arial", 14, "bold"), bg="#ffa07a", fg="white").pack(pady=20)
        tk.Button(self.root, text="Exit", command=self.exit_app, font=("Arial", 14, "bold"), bg="#b22222", fg="white").pack(pady=10)

    def place_order(self):
        self.cart = {}
        menu_items = get_menu()

        for item in menu_items:
            if self.menu_vars[item[0]].get():
                self.cart[item[0]] = {"name": item[1], "price": item[2], "quantity": 1}

        if not self.cart:
            messagebox.showwarning("No Selection", "Please select at least one item.")
        else:
            self.order_screen()

    def order_screen(self):
        self.clear_screen()
        tk.Label(self.root, text="Order Summary", font=("Arial", 20, "bold"), bg="#20b2aa", fg="white").pack(pady=20)

        customer_name_label = tk.Label(self.root, text="Your Name:", font=("Arial", 14), bg="#f8f1f1")
        customer_name_label.pack()

        self.customer_name_entry = tk.Entry(self.root, font=("Arial", 14))
        self.customer_name_entry.pack(pady=10)

        order_frame = tk.Frame(self.root, bg="#fffacd")
        order_frame.pack(pady=10)

        total_price_var = tk.StringVar()

        def update_total():
            total_price = sum(item["price"] * item["quantity"] for item in self.cart.values())
            total_price_var.set(f"Total Price: Rs. {total_price:.2f}")  # Changed to Rs.

        def increase_quantity(item_id):
            self.cart[item_id]["quantity"] += 1
            render_order_list()

        def decrease_quantity(item_id):
            if self.cart[item_id]["quantity"] > 1:
                self.cart[item_id]["quantity"] -= 1
            else:
                del self.cart[item_id]
            render_order_list()

        order_list = tk.Frame(order_frame, bg="#fffacd")
        order_list.pack()

        def render_order_list():
            for widget in order_list.winfo_children():
                widget.destroy()

            for item_id, item in self.cart.items():
                row = tk.Frame(order_list, bg="#fffacd")
                row.pack(fill="x", pady=5)

                tk.Label(row, text=f"{item['name']} - Rs. {item['price']:.2f}", font=("Arial", 12), bg="#fafad2", fg="#000").pack(side="left", padx=10)
                tk.Label(row, text=f"Qty: {item['quantity']}", font=("Arial", 12), bg="#fafad2", fg="#000").pack(side="left", padx=10)
                tk.Button(row, text="+", command=lambda id=item_id: increase_quantity(id), font=("Arial", 12, "bold"), bg="#32cd32", fg="white").pack(side="left", padx=5)
                tk.Button(row, text="-", command=lambda id=item_id: decrease_quantity(id), font=("Arial", 12, "bold"), bg="#ff6347", fg="white").pack(side="left", padx=5)

            update_total()

        render_order_list()

        tk.Label(order_frame, textvariable=total_price_var, font=("Arial", 14, "bold"), bg="#fffacd", fg="#000").pack(pady=10)

        button_frame = tk.Frame(self.root, bg="#f8f1f1")
        button_frame.pack(pady=20)

        tk.Button(button_frame, text="Place Order", command=self.finalize_order, font=("Arial", 12, "bold"), bg="#32cd32", fg="white").pack(side="left", padx=10)
        tk.Button(button_frame, text="Remove Order", command=self.menu_screen, font=("Arial", 12, "bold"), bg="#ff6347", fg="white").pack(side="left", padx=10)
        tk.Button(button_frame, text="Exit", command=self.exit_app, font=("Arial", 12, "bold"), bg="#b22222", fg="white").pack(side="left", padx=10)

    def finalize_order(self):
        customer_name = self.customer_name_entry.get()
        if not customer_name.strip():
            messagebox.showwarning("Missing Information", "Please enter your name.")
            return

        total_price = sum(item["price"] * item["quantity"] for item in self.cart.values())
        items = ", ".join(f"{item['name']} x{item['quantity']}" for item in self.cart.values())

        db = connect_db()
        cursor = db.cursor()
        cursor.execute(
            "INSERT INTO orders (customer_name, items, total_price) VALUES (%s, %s, %s)",
            (customer_name, items, total_price)
        )
        db.commit()
        cursor.close()
        db.close()

        messagebox.showinfo("Order Placed", "Thank you for ordering! It will arrive soon.")
        self.menu_screen()

    def exit_app(self):
        messagebox.showinfo("Goodbye", "Thank you for visiting! Come again.")
        self.root.destroy()

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

# Setup database and run application
setup_database()
populate_menu()

root = tk.Tk()
app = CafeManagementSystem(root)
root.mainloop()
