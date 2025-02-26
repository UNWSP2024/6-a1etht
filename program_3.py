#Programmer: Alethea Lo
#Date: 2/25/25
#Title: Tax Rate

def calculate_taxes(total_sales):
    """Calculates county, state, and total sales tax based on given sales amount."""
    STATE_TAX_RATE = 0.05
    COUNTY_TAX_RATE = 0.025

    county_tax = total_sales * COUNTY_TAX_RATE
    state_tax = total_sales * STATE_TAX_RATE
    total_tax = county_tax + state_tax

    return county_tax, state_tax, total_tax

def main():
    total_sales = float(input("Enter the total sales for the month: "))
    county_tax, state_tax, total_tax = calculate_taxes(total_sales)

    print(f"County Sales Tax: ${county_tax:.2f}")
    print(f"State Sales Tax: ${state_tax:.2f}")
    print(f"Total Sales Tax: ${total_tax:.2f}")

if __name__ == "__main__":
    main()
