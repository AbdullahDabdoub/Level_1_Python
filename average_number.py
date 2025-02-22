import tkinter as tk
from tkinter import simpledialog, messagebox

def calculate_average():
    """Calculates the arithmetic mean of a set of numbers entered by the user."""

    numbers_str = simpledialog.askstring("Enter Numbers", "Enter numbers separated by commas:")

    if numbers_str is None:  # User clicked cancel
        return

    if not numbers_str:
        messagebox.showerror("Error", "No numbers entered.")
        return

    try:
        numbers = [float(x.strip()) for x in numbers_str.split(",")]  # Handle potential whitespace
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter numbers only, separated by commas.")
        return

    if not numbers:
         messagebox.showerror("Error", "No valid numbers were entered.")
         return

    average = sum(numbers) / len(numbers)

    # Display the result in a message box
    messagebox.showinfo("Result", f"The arithmetic mean is: {average}")



# Create the main Tkinter window (but don't show it)
root = tk.Tk()
root.withdraw()  # Hide the main window

# Call the function to start the process
calculate_average()

# Optional: Keep the script running to prevent immediate exit (if needed)
# root.mainloop() #Uncomment if you want to keep the script running.