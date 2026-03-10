stocks = ["AAPL", "TSLA", "NVDA", "BRK"]
buy_prices = [182.50, 245.00, 480.00, 500.00]
current_prices = [100, 245, 480, 1000]

for i in range(len(stocks)):
    print(f"stock = {stocks[i]}")
    print(f"buy_prices = {buy_prices[i]}")
    print(f"current_price = {current_prices[i]}")
   

    # calculate change_percentage
    change_percentage = (current_prices[i] - buy_prices[i]) / buy_prices[i] * 100
    print(f"change_percentage = {change_percentage:.2f}")
    
    if change_percentage > 20:
        print("Strong gain - consider taking profits")
    elif change_percentage < -10:
        print("Significant loss - review position")
    else:
        print("Hold steady")

    print()