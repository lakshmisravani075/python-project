import tkinter as tk
from tkinter import messagebox



class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price




class Menu:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)


class Order:
    def __init__(self):
        self.order_items = []

    def add_to_order(self, item, quantity):
        self.order_items.append((item, quantity))

    def calculate_bill(self):
        return sum(item.price * qty for item, qty in self.order_items)


class BillingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Restaurant Billing System")
        self.root.geometry("400x500")

        # Create Menu
        self.menu = Menu()
        self.menu.add_item(MenuItem("Pizza", 199))
        self.menu.add_item(MenuItem("Burger", 99))
        self.menu.add_item(MenuItem("Pasta", 149))
        self.menu.add_item(MenuItem("Coke", 49))

        self.entries = []

        tk.Label(root, text="Restaurant Menu", font=("Arial", 16, "bold")).pack(pady=10)

        
        for item in self.menu.items:
            frame = tk.Frame(root)
            frame.pack(pady=5)

            label = tk.Label(frame, text=f"{item.name} - ₹{item.price}", width=20, anchor="w")
            label.pack(side="left")

            entry = tk.Entry(frame, width=5)
            entry.insert(0, "0")
            entry.pack(side="left")

            self.entries.append((item, entry))

        # Bill button
        tk.Button(root, text="Generate Bill", font=("Arial", 14), bg="green", fg="white",
                  command=self.generate_bill).pack(pady=20)

        # Output area
        self.output = tk.Text(root, height=10, width=40)
        self.output.pack()

    def generate_bill(self):
        order = Order()

        for item, entry in self.entries:
            qty_text = entry.get()
            try:
                qty = int(qty_text)
                if qty > 0:
                    order.add_to_order(item, qty)
            except ValueError:
                messagebox.showerror("Invalid Input", "Please enter a valid quantity!")
                return

        total = order.calculate_bill()

        # Display bill
        self.output.delete(1.0, tk.END)
        self.output.insert(tk.END, "------ BILL SUMMARY ------\n")
        for item, qty in order.order_items:
            self.output.insert(tk.END, f"{item.name} x {qty} = ₹{item.price * qty}\n")

        self.output.insert(tk.END, "\n----------------------------\n")
        self.output.insert(tk.END, f"TOTAL BILL: ₹{total}\n")
        self.output.insert(tk.END, "Thank You! Visit Again 😊")



root = tk.Tk()
app = BillingApp(root)
root.mainloop()         

