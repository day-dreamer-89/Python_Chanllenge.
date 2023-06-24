import csv

def financial_analysis(csv_file):
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)  

        
        total_months = 0
        total_profit_loss = 0
        previous_profit_loss = 0
        profit_changes = []
        months = []

        for row in reader:
            total_months += 1
            profit_loss = int(row[1])
            total_profit_loss += profit_loss

            if total_months > 1:
                profit_change = profit_loss - previous_profit_loss
                profit_changes.append(profit_change)
                months.append(row[0])

            previous_profit_loss = profit_loss

        average_change = sum(profit_changes) / len(profit_changes)

        max_increase = max(profit_changes)
        max_decrease = min(profit_changes)
        max_increase_month = months[profit_changes.index(max_increase)]
        max_decrease_month = months[profit_changes.index(max_decrease)]

        print("Financial Analysis")
        print("-----------------------------")
        print(f"Total Months: {total_months}")
        print(f"Total: ${total_profit_loss}")
        print(f"Average Change: ${average_change:.2f}")
        print(f"Greatest Increase in Profits: {max_increase_month} (${max_increase})")
        print(f"Greatest Decrease in Profits: {max_decrease_month} (${max_decrease})")

csv_file_path = 'Resources/budget_data.csv'

financial_analysis(csv_file_path)
