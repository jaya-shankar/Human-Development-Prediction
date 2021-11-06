import csv

file  = open("sex-ratio.csv")

csvreader = csv.reader(file)

header = next(csvreader)

mapped = {}
for row in csvreader:
    if(row[0] not in mapped):
        mapped[row[0]]={}
    mapped[row[0]][row[2]] = row[3]

# f = open("converted.csv",'w')
rows=[]
for c in mapped:
    row = [c]
    for y in mapped[c]:
        row.append(mapped[c][y])
    rows.append(row)
header =['country']
for i in range(1950,2018):
    header.append(str(i))

with open('converted.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)
    # write the data
    for row in rows:
        writer.writerow(row)


