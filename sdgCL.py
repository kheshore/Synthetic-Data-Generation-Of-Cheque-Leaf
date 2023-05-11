from tkinter import *
from tkinter import filedialog
import csv
from faker import Faker
import random

class App:
    def __init__(self, master):
        self.master = master
        self.master.title("Synthetic Cheque Leaf Data Generator")

        # Create the UI
        self.label1 = Label(master, text="Enter the number of cheque leaves to generate:")
        self.label1.grid(row=0, column=0, padx=10, pady=10)

        self.num_leaves_entry = Entry(master)
        self.num_leaves_entry.grid(row=0, column=1, padx=10, pady=10)

        self.generate_button = Button(master, text="Generate", command=self.generate_data)
        self.generate_button.grid(row=1, column=0, padx=10, pady=10)

        self.save_button = Button(master, text="Select Save Location", command=self.select_save_location)
        self.save_button.grid(row=1, column=1, padx=10, pady=10)

        self.label2 = Label(master, text="")
        self.label2.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        self.label3 = Label(master, text="SYNTHETIC DATA GENERATION OF CHEQUE LEAF")
        self.label3.grid(row=3, column=0 ,padx=10, pady=10)

        self.label4 = Label(master, text=" - A Machine Learning Project By SAHANA S (20BCS079)")
        self.label4.grid(row=3, column=1 ,padx=10, pady=10)

    def generate_data(self):
        # Get the number of cheque leaves to generate
        num_leaves = int(self.num_leaves_entry.get())

        # Generate the cheque leaf data using Faker
        bwords = ['SBI', 'HDFC', 'ICICI', 'KOTAK', 'HSBC', 'KVB']
        ctwords = ['bearer', 'order', 'crossed', 'open', 'self', 'traveller']
        faker = Faker()
        data = []
        for i in range(num_leaves):
            data.append([
                faker.random_int(min=1000000, max=9999999),
                faker.date_between(start_date='-2y', end_date='today').strftime('%m/%d/%Y'),
                faker.name(),
                faker.random_int(min=1000000, max=9999999),
                faker.random_int(min=1000000, max=9999999),
                random.choice(bwords),
                random.choice(ctwords)
            ])

        # Display the number of cheque leaves generated
        self.label2.config(text=f"{num_leaves} cheque leaves generated.")

        # Save the data to a CSV file
        if self.save_location:
            with open(self.save_location, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Cheque Number", "Date", "Payee Name", "Account Number", "Amount", "Bank Name","Cheque Type"])
                writer.writerows(data)

    def select_save_location(self):
        self.save_location = filedialog.asksaveasfilename(defaultextension=".csv")
        if self.save_location:
            self.save_button.config(text=f"Selected: {self.save_location}")

# Create the main window
root = Tk()
app = App(root)
root.mainloop()
