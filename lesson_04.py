stocks = ["AAPL", "TSLA", "NVDA", "BRK"]
buy_prices = [182.50, 245.00, 480.00, 500.00]
current_prices = [100, 245, 480, 1000]

def calculate_change(buy_price, current_price):
    change_percentage = (current_price - buy_price) / buy_price * 100
    return change_percentage

def get_recommendation(change_percentage):
    if change_percentage > 20:
        recommendation = "Strong gain - consider taking profits"
    elif change_percentage < -10:
        recommendation = "Significant loss - review position"
    else:
        recommendation = "Hold steady"
    return recommendation

for i in range(len(stocks)):
    change_percentage = calculate_change(buy_prices[i], current_prices[i])
    recommendation = get_recommendation(change_percentage)
    print(f"{stocks[i]} has change of {change_percentage:.2f}, {recommendation}")
    print()