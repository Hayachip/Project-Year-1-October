import tkinter as tk
from tkinter import messagebox

def calculate_pmt(rate, periods, present_value):
    try:
        monthly_rate = float(rate) / (12 * 100)
        periods = int(periods)
        present_value = float(present_value)
        pmt = (monthly_rate * present_value) / (1 - (1 + monthly_rate) ** -periods)
        return pmt
    except ValueError:
        messagebox.showerror("Error, Please enter only number values.")
        return None

def calculate_future_value(rate, periods, payment, present_value):
    try:
        monthly_rate = float(rate) / (12 * 100)
        periods = int(periods)
        payment = float(payment)
        present_value = float(present_value)
        fv = present_value * (1 + monthly_rate) ** periods + payment * ((1 + monthly_rate) ** periods - 1) / monthly_rate
        return fv
    except ValueError:
        messagebox.showerror("Error, Please enter only number values.")
        return None

def calculate_cash_flow(income_list, expense_list):
    total_income = sum(income_list)
    total_expense = sum(expense_list)
    cash_flow = total_income - total_expense
    return cash_flow

def get_choice():
    selected_choice = variable.get()
    if selected_choice == "Loan payment (Payment)":
        def calculate():
            interest_rate = interest_entry.get()
            loan_periods = periods_entry.get()
            principal = principal_entry.get()
            # Calculating the PMT
            monthly_payment = calculate_pmt(interest_rate, loan_periods, principal)
            messagebox.showinfo("Calculation Result", f"The monthly payment (PMT) for the loan is: {round(monthly_payment, 2)}")

        input_window = tk.Toplevel(root)
        input_window.title("Loan Payment Details")

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

        future_window = tk.Toplevel(root)
        future_window.title("Future Value Details")

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

    elif selected_choice == "Free Cash Flow Calculator":
        def calculate_free_cash_flow():
            income = []
            expenses = []

            for entry in income_entries:
                value = entry.get()
                if value:
                    try:
                        income.append(float(value))
                    except ValueError:
                        messagebox.showerror("Error, Please enter only number values for income.")
                        return

            for entry in expense_entries:
                value = entry.get()
                if value:
                    try:
                        expenses.append(float(value))
                    except ValueError:
                        messagebox.showerror("Error, Please enter only number values for expenses.")
                        return

            free_cash_flow = calculate_cash_flow(income, expenses)
            if free_cash_flow > 0:
                messagebox.showinfo("Calculation Result", f"The Free Cash Flow is: {free_cash_flow}")
            else:
                messagebox.showinfo("Calculation Result", f"There is Negative Cash Flow, The Negative Cash Flow is: {abs(free_cash_flow)}")

        input_window = tk.Toplevel(root)
        input_window.title("Free Cash Flow Calculator")

        num_income_sources = tk.StringVar()
        num_expense_sources = tk.StringVar()

        def get_num_sources():
            num_income = int(num_income_sources.get())
            num_expense = int(num_expense_sources.get())

            income_label = tk.Label(input_window, text="Enter the number of maximum sources (Income/Expense)")
            income_label.pack()

            for i in range(num_income):
                income_entry = tk.Entry(input_window)
                income_entry.pack()
                income_entries.append(income_entry)

            expense_label = tk.Label(input_window, text="Enter the number of maximum sources (Income/Expense)")
            expense_label.pack()

            for i in range(num_expense):
                expense_entry = tk.Entry(input_window)
                expense_entry.pack()
                expense_entries.append(expense_entry)

            calculate_button = tk.Button(input_window, text="Calculate", command=calculate_free_cash_flow)
            calculate_button.pack()

        income_entries = []
        expense_entries = []

        num_sources_label = tk.Label(input_window, text="Enter the number of maximum sources (Income/Expense)")
        num_sources_label.pack()

        num_sources_entry = tk.Entry(input_window, textvariable=num_income_sources)
        num_sources_entry.pack()

        num_sources_label = tk.Label(input_window, text="Enter the number of maximum sources (Income/Expense)")
        num_sources_label.pack()

        num_sources_entry = tk.Entry(input_window, textvariable=num_expense_sources)
        num_sources_entry.pack()

        num_sources_button = tk.Button(input_window, text="Submit", command=get_num_sources)
        num_sources_button.pack()
        
    else:
        messagebox.showinfo("Selected Choice", f"You selected: {selected_choice}")

# main UI
root = tk.Tk()
root.title("Financial Calculator")
root.geometry("400x300")  # Width x Height

# instruction
instruction_label = tk.Label(root, text="Select your financial calculation")
instruction_label.pack()

# Choices
choices = ["Loan payment (Payment)", "Bank Saving (Future Value)","Free Cash Flow Calculator"]

# Variable to hold the selected choice
variable = tk.StringVar(root)
variable.set(choices[0])  # Set default choice

# dropdown menu
option_menu = tk.OptionMenu(root, variable, *choices)
option_menu.pack()

# Button to get the selected choice
select_button = tk.Button(root, text="Select", command=get_choice)
select_button.pack()

root.mainloop()