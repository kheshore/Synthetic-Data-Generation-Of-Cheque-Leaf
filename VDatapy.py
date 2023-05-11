import tkinter as tk
from tkinter import filedialog
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create a function to generate and select the CSV file
def select_file():
    global file_path
    file_path = filedialog.askopenfilename()

    # Read the CSV file using Pandas
    df = pd.read_csv(file_path)

    # Display statistical data visualization using Seaborn
    sns.set(style="darkgrid")

    # Calculate the average amount per bank
    avg_amounts = df.groupby('Bank Name')['Amount'].mean().reset_index()

    # Display the bar chart of average amounts per bank
    sns.barplot(x="Bank Name", y="Amount", data=avg_amounts)
    plt.title("Average Amount per Bank")
    plt.show()

    # Display the heatmap of the cheque leaf data
    heatmap_data = df.pivot_table(index='Bank Name', columns='Cheque Type', values='Amount', aggfunc='mean')
    sns.heatmap(heatmap_data, cmap="YlGnBu")
    plt.title("Cheque Leaf Data Heatmap")
    plt.show()

# Create a Tkinter window
root = tk.Tk()

# Add a button to select the CSV file
file_button = tk.Button(root, text="Select CSV file", command=select_file)
file_button.pack()

# Run the Tkinter window
root.mainloop()
