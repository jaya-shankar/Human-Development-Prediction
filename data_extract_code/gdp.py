import csv

file  = open("../datasets/gdppercapita_us_inflation_adjusted.csv")

csvreader = csv.reader(file)

header = next(csvreader)
l = len(header)

with open('gdppercapita_us_inflation_adjusted_b.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)
    # write the data
    for row in csvreader:
        s=[row[0]]

        for e in range(1,l):
            m=1
            if(row[e]==""):
                s.append(row[e])
            elif(row[e][-1]=='k'):
                m=1000
                s.append(str(int(float(row[e][:-1])*m)))
                # print(int(float(row[e][:-1])*m))
            elif(row[e][-1]=='M'):
                m=1000000
                s.append(str(int(float(row[e][:-1])*m)))
                # print(int(float(row[e][:-1])*m))
            elif(row[e][-1]=='B'):
                m=1000000000
                s.append(str(int(float(row[e][:-1])*m)))
                # print(int(float(row[e][:-1])*m))
            else:
                s.append(row[e])
            
        writer.writerow(s)
    
