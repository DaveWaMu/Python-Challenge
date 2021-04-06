import os
import csv

#Import path
dir_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(dir_path)
pypoll_path = os.path.join(dir_path, 'Resources')
os.chdir(pypoll_path)

#Export path
output_path = os.path.join(dir_path, 'analysis')

#Variables
vote_total=0
voterid_list=[]
county_list=[]
choice_list=[]
candidate_list=[]
khan_vote=0
correy_vote=0
li_vote=0
otooley_vote=0

#Read file
with open('election_data.csv','r') as csv_file:
    csvreader = csv.reader(csv_file, delimiter=',')
    csv_header=next(csvreader)

#Lists
    for row in csvreader:
        vote_total+=1
        voterid=int(row[0])
        voterid_list.append(voterid)
        county=row[1]
        county_list.append(county)
        candidate=row[2]
        choice_list.append(candidate)
    for c in choice_list:
        if c not in candidate_list:
            candidate_list.append(c)
            
#Vote totals
    for v in choice_list:
        if v == candidate_list[0]:
            khan_vote+=1
        if v == candidate_list[1]:
            correy_vote+=1
        if v == candidate_list[2]:
            li_vote+=1
        if v == candidate_list[3]:
            otooley_vote+=1

#Percent vote
    khan=khan_vote/vote_total
    perc_khan="{:.0%}".format(khan)
    correy=correy_vote/vote_total
    perc_correy="{:.0%}".format(correy)
    li=li_vote/vote_total
    perc_li="{:.0%}".format(li)
    otooley=otooley_vote/vote_total
    perc_otooley="{:.0%}".format(otooley)

#Display
print('Election Results')
print('-------------------------')
print(f'Total Votes: {vote_total}')
print('-------------------------')
print(f'Khan: {perc_khan} ({khan_vote})')
print(f'Correy: {perc_correy} ({correy_vote})')
print(f'Li: {perc_li} ({li_vote})')
print(f"O'Tooley: {perc_otooley} ({otooley_vote})")
print('-------------------------')
print('Winner: Khan')
print('-------------------------')

#Write file
os.chdir(output_path)
with open("output_file_pypoll.txt","w") as datafile:
    csvwriter = csv.writer(datafile, lineterminator='\n')

    csvwriter.writerow(['Election Results'])
    csvwriter.writerow(['-------------------------'])
    csvwriter.writerow([f'Total Votes: {vote_total}'])
    csvwriter.writerow(['-------------------------'])
    csvwriter.writerow([f'Khan: {perc_khan} ({khan_vote})'])
    csvwriter.writerow([f'Correy: {perc_correy} ({correy_vote})'])
    csvwriter.writerow([f'Li: {perc_li} ({li_vote})'])
    csvwriter.writerow([f"O'Tooley: {perc_otooley} ({otooley_vote})"])
    csvwriter.writerow(['-------------------------'])
    csvwriter.writerow(['Winner: Khan'])
    csvwriter.writerow(['-------------------------'])