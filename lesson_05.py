portfolio = [
    {"name": "AAPL", "buy_price" : 100, "current_price" : 100},
    {"name": "TSLA", "buy_price" : 150, "current_price" : 100},
    {"name": "NVDA", "buy_price" : 50, "current_price" : 100},
    {"name": "BRK", "buy_price" : 120, "current_price" : 100}
]

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

for stock in portfolio:
    change_percentage = calculate_change(stock["buy_price"], stock["current_price"])
    recommendation = get_recommendation(change_percentage)
    print(f'{stock["name"]} has change of {change_percentage:.2f}, {recommendation}')
    print()