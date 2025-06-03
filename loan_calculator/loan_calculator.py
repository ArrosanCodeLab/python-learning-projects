# Import the tkinter module for building GUI
import tkinter as tk

# Import messagebox from tkinter for showing popup error messages
from tkinter import messagebox

# Define the function that runs when the "Calculate" button is clicked
def calculate_payment():
    try:
        # Get loan amount entered by the user and convert it to float
        principal = float(entry_principal.get())

        # Get interest rate, convert annual % to monthly decimal
        rate = float(entry_rate.get()) / 100 / 12

        # Get loan term in years and calculate number of monthly payments
        years = int(entry_years.get())
        n_payments = years * 12

        # Check for invalid values like zero or negative amounts
        if principal <= 0 or years <= 0:
            raise ValueError("Loan amount and term must be greater than 0.")

        # Calculate the monthly payment
        if rate == 0:
            # If interest is 0%, use simple division
            monthly_payment = principal / n_payments
        else:
            # Use amortization formula for monthly payments
            monthly_payment = principal * (rate * (1 + rate) ** n_payments) / ((1 + rate) ** n_payments - 1)

        # Calculate total amount to be repaid and total interest paid
        total_payment = monthly_payment * n_payments
        total_interest = total_payment - principal

        # Update the GUI labels with the results
        label_monthly.config(text=f"Monthly Payment: ${monthly_payment:.2f}")
        label_total.config(text=f"Total Repayment: ${total_payment:.2f}")
        label_interest.config(text=f"Total Interest: ${total_interest:.2f}")

    except Exception:
        # Show an error if inputs are invalid or missing
        messagebox.showerror("Error", "Please enter valid numeric values.")

# ========================
# GUI SETUP STARTS HERE
# ========================

# Create the main application window
root = tk.Tk()
root.title("Loan Payment Calculator")  # Title for the window
root.minsize(width=300, height=200)   # Set a minimum size

# Set widths for consistent layout
label_width = 20
entry_width = 25

# Create label and entry for "Loan Amount"
tk.Label(root, text="Loan Amount ($):", width=label_width, anchor="w").grid(row=0, column=0, sticky="w")
entry_principal = tk.Entry(root, width=entry_width)
entry_principal.grid(row=0, column=1)

# Create label and entry for "Annual Interest Rate"
tk.Label(root, text="Annual Interest Rate (%):", width=label_width, anchor="w").grid(row=1, column=0, sticky="w")
entry_rate = tk.Entry(root, width=entry_width)
entry_rate.grid(row=1, column=1)

# Create label and entry for "Loan Term in Years"
tk.Label(root, text="Loan Term (Years):", width=label_width, anchor="w").grid(row=2, column=0, sticky="w")
entry_years = tk.Entry(root, width=entry_width)
entry_years.grid(row=2, column=1)

# Create the Calculate button and attach the function
tk.Button(root, text="Calculate", command=calculate_payment, width=25).grid(row=3, column=0, columnspan=2, pady=10)

# Labels to display results (initialized with $0.00)
label_monthly = tk.Label(root, text="Monthly Payment: $0.00", width=label_width + entry_width)
label_monthly.grid(row=4, column=0, columnspan=2)

label_total = tk.Label(root, text="Total Repayment: $0.00", width=label_width + entry_width)
label_total.grid(row=5, column=0, columnspan=2)

label_interest = tk.Label(root, text="Total Interest: $0.00", width=label_width + entry_width)
label_interest.grid(row=6, column=0, columnspan=2)

# Run the main event loop — keeps the window open
root.mainloop()