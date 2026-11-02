# Stock Portfolio Tracker

# Dictionary containing stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 400,
    "AMZN": 190
}

portfolio = []
total_investment = 0

print("===================================")
print("     STOCK PORTFOLIO TRACKER")
print("===================================")

print("\nAvailable Stocks:")

for stock, price in stock_prices.items():
    print(stock, "- $", price)

# Get number of stocks
n = int(input("\nHow many different stocks do you own? "))

# Get stock details
for i in range(n):

    stock_name = input("\nEnter stock name: ").upper()

    if stock_name in stock_prices:

        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than zero.")
            continue

        price = stock_prices[stock_name]

        investment = price * quantity

        total_investment += investment

        portfolio.append(
            (stock_name, quantity, price, investment)
        )

        print("Investment added successfully!")

    else:
        print("Stock not available!")

# Display portfolio
print("\n========== YOUR PORTFOLIO ==========")

print("Stock\tQuantity\tPrice\tValue")

for stock, quantity, price, value in portfolio:
    print(stock, "\t", quantity, "\t\t", price, "\t", value)

print("\nTotal Investment: $", total_investment)

# Save results to a text file
with open("portfolio.txt", "w") as file:

    file.write("STOCK PORTFOLIO REPORT\n")
    file.write("======================\n")

    for stock, quantity, price, value in portfolio:
        file.write(
            f"{stock} | Quantity: {quantity} | "
            f"Price: ${price} | Value: ${value}\n"
        )

    file.write(f"\nTotal Investment: ${total_investment}")

print("\nPortfolio saved successfully to portfolio.txt")
print("Thank you for using Stock Portfolio Tracker!")