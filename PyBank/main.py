import csv
# Open CSV File
with open('./Resources/budget_data.csv', 'r') as csvfile:
    budget_data = csv.reader(csvfile, delimiter=',')
    next(budget_data)
    
    month = 0
    totalprofit = 0
    profit_changes = []
    previous_profit = 0
    greatest_increase = ['', 0]
    greatest_decrease = ['', 0]
    
    for row in budget_data:
        month += 1
        profit = int(row[1])
        totalprofit += profit
        
        if month > 1:
            change = profit - previous_profit
            profit_changes.append(change)
            if change > greatest_increase[1]:
                greatest_increase = [row[0], change]
            if change < greatest_decrease[1]:
                greatest_decrease = [row[0], change]
        previous_profit = profit
    
    avg_change = sum(profit_changes) / len(profit_changes)

with open("./Analysis/profitloss.txt", "a") as f:
    print("Financial Analysis", file=f)
    print("---------------------------", file=f)
    print(f"Total Months: {month}", file=f)
    print(f"Total: ${totalprofit}", file=f)
    print(f"Average Change: ${round(avg_change, 2)}", file=f)
    print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})", file=f)
    print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})", file=f)


