# Variables
stock = "AAPL"
buy_price = 150.00
current_price = 250.00

# Calculate
profit_loss = current_price - buy_price
change_percent = (current_price - buy_price) / buy_price * 100

# Output
print(f"Stock: {stock}")
print(f"Buy price: {buy_price}")
print(f"Current price: {current_price}")
print(f"Profit/Loss: {profit_loss}")
print(f"Change: {change_percent:.2f}%")