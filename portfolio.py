stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "MSFT": 330,
    "GOOGL": 140,
    "AMZN": 145
}

portfolio = {}
total_investment = 0

print("📈 Stock Portfolio Tracker")
print("Available stocks & prices:")
for stock, price in stock_prices.items():
    print(f"{stock}: ${price}")

while True:
    stock_name = input("\nEnter stock symbol (or 'done' to finish): ").upper()
    if stock_name == "DONE":
        break

    if stock_name not in stock_prices:
        print("❌ Stock not found in price list.")
        continue

    try:
        quantity = int(input(f"Enter quantity for {stock_name}: "))
    except ValueError:
        print("❌ Please enter a valid number.")
        continue

    portfolio[stock_name] = portfolio.get(stock_name, 0) + quantity


for stock, qty in portfolio.items():
    total_investment += stock_prices[stock] * qty

print("\n📊 Portfolio Summary:")
for stock, qty in portfolio.items():
    print(f"{stock}: {qty} shares → ${stock_prices[stock] * qty}")

print(f"\n💰 Total Investment: ${total_investment}")

save_option = input("\nDo you want to save the result to a file? (y/n): ").lower()
if save_option == "y":
    with open("portfolio.txt", "w") as file:
        file.write("Stock Portfolio Summary\n")
        file.write("-----------------------\n")
        for stock, qty in portfolio.items():
            file.write(f"{stock}: {qty} shares → ${stock_prices[stock] * qty}\n")
        file.write(f"\nTotal Investment: ${total_investment}\n")
    print("✅ Portfolio saved to 'portfolio.txt'")
