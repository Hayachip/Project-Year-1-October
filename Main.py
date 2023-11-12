import tkinter as tk
from tkinter import messagebox

def calculate_pmt(rate, periods, present_value):
    rate = float(rate) / 100
    periods = int(periods)
    present_value = float(present_value)
    pmt = (rate * present_value) / (1 - (1 + rate) ** -periods)
    return pmt

def calculate_future_value(rate, periods, payment, present_value):
    rate = float(rate) / 100
    periods = int(periods)
    payment = float(payment)
    present_value = float(present_value)
    fv = present_value * (1 + rate) ** periods + payment * ((1 + rate) ** periods - 1) / rate
    return fv

def get_choice():
    selected_choice = variable.get()
    if selected_choice == "Loan payment (Payment)":
        # Function to perform the calculation
        def calculate():
            interest_rate = interest_entry.get()
            loan_periods = periods_entry.get()
            principal = principal_entry.get()
            # Calculating the PMT
            monthly_payment = calculate_pmt(interest_rate, loan_periods, principal)
            messagebox.showinfo("Calculation Result", f"The monthly payment (PMT) for the loan is: {round(monthly_payment, 2)}")

        # Create a new window for input
        input_window = tk.Toplevel(root)
        input_window.title("Loan Payment Details")

        # Labels and Entry fields for user input
        interest_label = tk.Label(input_window, text="Enter your interest rate in percent")
        interest_label.pack()
        interest_entry = tk.Entry(input_window)
        interest_entry.pack()

        periods_label = tk.Label(input_window, text="Enter your periods in month")
        periods_label.pack()
        periods_entry = tk.Entry(input_window)
        periods_entry.pack()

        principal_label = tk.Label(input_window, text="Enter your loan amount")
        principal_label.pack()
        principal_entry = tk.Entry(input_window)
        principal_entry.pack()

        calculate_button = tk.Button(input_window, text="Calculate", command=calculate)
        calculate_button.pack()

    elif selected_choice == "Bank Saving (Future Value)":
        def calculate_future():
            interest_rate = interest_entry.get()
            investment_periods = periods_entry.get()
            regular_payment = payment_entry.get()
            initial_investment = investment_entry.get()
            future_value = calculate_future_value(interest_rate, investment_periods, regular_payment, initial_investment)
            messagebox.showinfo("Calculation Result", f"The future value after {investment_periods} periods is: {round(future_value, 2)}")

        # Create a new window for future value input
        future_window = tk.Toplevel(root)
        future_window.title("Future Value Details")

        # Labels and Entry fields for future value user input
        interest_label = tk.Label(future_window, text="Enter your interest rate in percent")
        interest_label.pack()
        interest_entry = tk.Entry(future_window)
        interest_entry.pack()

        periods_label = tk.Label(future_window, text="Enter your periods in month")
        periods_label.pack()
        periods_entry = tk.Entry(future_window)
        periods_entry.pack()

        payment_label = tk.Label(future_window, text="Enter your monthly deposit amount")
        payment_label.pack()
        payment_entry = tk.Entry(future_window)
        payment_entry.pack()

        investment_label = tk.Label(future_window, text="Enter your initial saving amount")
        investment_label.pack()
        investment_entry = tk.Entry(future_window)
        investment_entry.pack()

        calculate_future_button = tk.Button(future_window, text="Calculate", command=calculate_future)
        calculate_future_button.pack()

    else:
        messagebox.showinfo("Selected Choice", f"You selected: {selected_choice}")

# Create the main window
root = tk.Tk()
root.title("Financial Calculator")
root.geometry("400x300")  # Width x Height

# Label for instruction
instruction_label = tk.Label(root, text="Select your financial calculation")
instruction_label.pack()

# Choices available
choices = ["Loan payment (Payment)", "Bank Saving (Future Value)"]

# Create a variable to hold the selected choice
variable = tk.StringVar(root)
variable.set(choices[0])  # Set default choice

# Create the dropdown menu
option_menu = tk.OptionMenu(root, variable, *choices)
option_menu.pack()

# Button to get the selected choice
select_button = tk.Button(root, text="Select", command=get_choice)
select_button.pack()

# Run the main loop
root.mainloop()