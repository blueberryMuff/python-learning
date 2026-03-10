# Variables
stock = "AAPL"
buy_price = 150
current_price = 150

# Calculations
change_percent = (current_price - buy_price) / buy_price * 100
print(f"{change_percent:.2f} profit/loss on buy_price.")

if change_percent > 20:
    print("Strong gain - consider taking profits")
elif change_percent < -10:
    print("Significant loss - review position")
else:
    print("Hold steady")