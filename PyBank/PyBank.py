import os
import csv
import locale

BudgetData_csv = os.path.join("Resources", "budget_data.csv")

#Create lists to store our desired variables/data.
#Note that PL is an abbreviation for profits and losses. 

months = []
PL = []
net_change = []

#Reading the data

with open(BudgetData_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    #Obtaining the required output values.

    for row in csvreader:
        months.append(row[0])
        PL.append(row[1])

        #Changing the strings in the lists to float type for calculation purporses. Note that this method of conversion was obtained from stackoverflow.
        #Obtaining values of the net change list.

        for i in range(0, len(PL)): 
            PL[i] = float(PL[i])
        net_change = [PL[i + 1] - PL[i] for i in range(len(PL)-1)]
        for i in range(0, len(net_change)): 
            net_change[i] = float(net_change[i])

#Obtaining desired output values

number_of_months = int(len(months))
total_PL = sum(PL)
sum_change = sum(net_change)
avg_change = sum_change/(number_of_months - 1)
g_increase = max(net_change)
g_decrease = min(net_change)
p_increase = net_change.index(g_increase)
p_decrease = net_change.index(g_decrease)
d_increase = months[p_increase +1]
d_decrease = months[p_decrease +1]    

#Printing out the results in terminal

print("----------------------------------------------------------")
print("Financial Analysis")
print("----------------------------------------------------------")
print(f"Total Months: {number_of_months}")
print(f"Total Profits/Losses: ${total_PL:,.2f}")
print(f"Average Change: ${avg_change:,.2f}")
print(f"Greatest Increase in Profits: {d_increase} (${g_increase:,.2f})")
print(f"Greatest Increase in Profits: {d_decrease} (${g_decrease:,.2f})")
print("----------------------------------------------------------")

#Specifying the file to write to

output_path = os.path.join("Resources", "budget_data.txt")

#Opening the file using write mode and writing to a text.
#Writing text method obtained from stackoverflow.
#Link to stackoverflow: https://stackoverflow.com/questions/6159900/correct-way-to-write-line-to-file
with open(output_path, 'w') as text_file:
    text_file.write("----------------------------------------------------------\n")
    text_file.write("Financial Analysis\n")
    text_file.write("----------------------------------------------------------\n")
    text_file.write(f"Total Months: {number_of_months}\n")
    text_file.write(f"Total Profits/Losses: ${total_PL:,.2f}\n")
    text_file.write(f"Average Change: ${avg_change:,.2f}\n")
    text_file.write(f"Greatest Increase in Profits: {d_increase} (${g_increase:,.2f})\n")
    text_file.write(f"Greatest Increase in Profits: {d_decrease} (${g_decrease:,.2f})\n")
    text_file.write("----------------------------------------------------------\n")