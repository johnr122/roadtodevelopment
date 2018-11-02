hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]
total_price = 0
total_revenue = 0

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

for price in prices:
  total_price += price

average_price = total_price/len(prices)
print("Average Haircut Price: %.2f"%(average_price))

new_prices = [i-5 for i in prices]
print(new_prices)

for i in range(0,len(hairstyles)-1):
	total_revenue += prices[i] * last_week[i]

average_daily_revenue = total_revenue/7
print("Total Revenue: %i"%(total_revenue))
print("Average Daily Revenue: %i"%(average_daily_revenue))

cuts_under_30 = [hairstyles[i] for i in range(0,len(new_prices)-1) if new_prices[i] < 30]
print(cuts_under_30)


