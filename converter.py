import csv
import json

print("enter file path of the extracted json contacts from telegram")
file = str(input())
print("enter your output file name, without '.csv'")
name = str(input())

header = ['Name', 'Given Name', 'Additional Name', 'Family Name', 'Yomi Name',
           'Given Name Yomi', 'Additional Name Yomi', 'Family Name Yomi', 'Name Prefix',
           'Name Suffix', 'Initials', 'Nickname', 'Short Name', 'Maiden Name', 'Birthday',
           'Gender', 'Location', 'Billing Information', 'Directory Server', 'Mileage', 'Occupation',
           'Hobby', 'Sensitivity', 'Priority', 'Subject', 'Notes', 'Language', 'Photo', 'Group Membership',
           'E-mail 1 - Type', 'E-mail 1 - Value', 'Phone 1 - Type', 'Phone 1 - Value', 'Phone 2 - Type',
           'Phone 2 - Value', 'Website 1 - Type', 'Website 1 - Value']

with open(name+'.csv', 'w') as csvfile:
    fields = header
    writer = csv.DictWriter(csvfile, fieldnames=fields)
    writer.writeheader()

    f = open(file, encoding='UTF-8')
    data = json.load(f)
    i = 0

    while i < len(data['contacts']['list']):
        c = 1
        person = data['contacts']['list'][i]
        phone = person["phone_number"]
        while (i + c < len(data['contacts']['list']) and
               person["first_name"] == data['contacts']['list'][i+c]["first_name"] and
               person["last_name"] == data['contacts']['list'][i+c]["last_name"]):
            phone += ' ::: ' + data['contacts']['list'][i+c]["phone_number"]
            c += 1
        if c > 1:
            i += c-1
        writer.writerow({'Name': person["first_name"] + ' ' + person["last_name"],
                     'Given Name': person["first_name"], 'Family Name': person["last_name"],
                     'Phone 1 - Value': phone})
        i+=1
    csvfile.close()

print("your contact file was generated in the code file directory")