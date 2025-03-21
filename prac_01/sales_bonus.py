"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

def main():
    sales = float(input("Enter sales: $"))
    while sales >= 0:
        bonus = calculate_bonus(sales)
        print(f"Bonus: ${bonus:.2f}")
        try:
            sales = float(input("Enter sales: $"))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            sales = 0
    print("Program ended.")

def calculate_bonus(sales):
    if sales < 1000:
        return sales * 0.10
    return sales * 0.15

if __name__ == "__main__":
    main()