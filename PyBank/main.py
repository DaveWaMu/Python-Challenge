import os
import csv

#Import path
dir_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(dir_path)
pybank_path = os.path.join(dir_path, 'Resources')
os.chdir(pybank_path)

#Export path
output_path = os.path.join(dir_path, 'analysis')

#Variables
count=0
total_profit=0
pl_list1=[]
pl_list2=[0]
date=[]
change_pl=[]

#Read file
with open('budget_data.csv','r') as csv_file:
    csvreader = csv.reader(csv_file, delimiter=',')
    csv_header=next(csvreader)
    
#Lists
    for row in csvreader:
        count+=1
        profit_loss=int(row[1])
        total_profit+=profit_loss
        pl_list1.append(profit_loss)
        pl_list2.append(profit_loss)
        date.append(row[0])
    change_pl=[(pl_list1[index] - pl_list2[index]) for index in range(len(pl_list1))]

#Calculations
    change_pl.pop(0)
    average_change=sum(change_pl)/len(change_pl)
    average_change=round(average_change,2)
    increase= max(change_pl)
    decrease= min(change_pl)
    change_pl.insert(0,"N/A")

#Zip file
    zip_list=zip(date,pl_list1,change_pl)
    for i in zip_list:
        if i[2] == increase:
            increase_date=i[0]
        if i[2] == decrease:
            decrease_date=i[0]

#Display
print("Financial Report")
print("----------------------------")
print(f"Total Months: {count}")
print(f"Net Total in Profits/Loss: ${total_profit}")
print(f"Average Change in Profits/Loss: ${average_change}")
print(f"Greatest Increase in Profits/Loss: {increase_date} (${increase})")
print(f"Greatest Decrease in Profits/Loss: {decrease_date} (${decrease})")

#Write file
os.chdir(output_path)
with open("output_file_pybank.txt","w") as datafile:
    csvwriter = csv.writer(datafile, lineterminator='\n')
    
    csvwriter.writerow(["Financial Report"])
    csvwriter.writerow(["----------------------------"])
    csvwriter.writerow([f"Total Months: {count}"])
    csvwriter.writerow([f"Net Total in Profits/Loss: ${total_profit}"])
    csvwriter.writerow([f"Average Change in Profits/Loss: ${average_change}"])
    csvwriter.writerow([f"Greatest Increase in Profits/Loss: {increase_date} (${increase})"])
    csvwriter.writerow([f"Greatest Decrease in Profits/Loss: {decrease_date} (${decrease})"])