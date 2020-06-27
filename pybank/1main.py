import csv
net_amount = 0
month = []
monthly_profit = []
max_change = 0
min_change = 0
path = "budget_data.csv"
analysis_path = "analysis1.txt"
with open(path) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    csv_header = next(csvfile)

    for row in csvreader:
        net_amount = net_amount + int(row[1])
        month.append(row[0])
        monthly_profit.append(int(row[1]))
    for i in range(len(monthly_profit)-1):
        if (monthly_profit[i+1]-monthly_profit[i]) > max_change: 
            max_change = (monthly_profit[i+1]-monthly_profit[i])
            max_month = month[i+1]
        if (monthly_profit[i+1]-monthly_profit[i]) < min_change:
            min_change = (monthly_profit[i+1]-monthly_profit[i])
            min_month = month[i+1]
    change = monthly_profit[len(month)-1]-monthly_profit[0]
    average_change = change/(len(month)-1)
    average_change = "{:.2f}".format(average_change)

output = (f"Financial Analysis\n"
            "------------------------------\n"
            f"Total Months: {len(month)}\n"
            f"Total: ${net_amount}\n"
            f"Average change: ${average_change}\n"
            f"Greatest Increase in Profits: {max_month} (${max_change})\n"
            f"Greatest Decrease in Profits: {min_month} (${min_change})\n"
)
print(output)
    # print("Financial Analysis",file = open("analysis1.txt","a"))
    # print("------------------------------",file = open("analysis1.txt","a"))
    # print(f"Total Months: {len(month)}",file = open("analysis1.txt","a"))
    # print(f"Total: ${net_amount}",file = open("analysis1.txt","a"))
    # print(f"Average change: ${average_change}",file = open("analysis1.txt","a"))
    # print(f"Greatest Increase in Profits: {max_month} (${max_change})",file = open("analysis1.txt","a"))
    # print(f"Greatest Decrease in Profits: {min_month} (${min_change})",file = open("analysis1.txt","a"))
with open(analysis_path,"a") as txt_file:
    txt_file.write(output)