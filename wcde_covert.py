import pandas as pd
import csv
data = pd.read_csv ("datasets/wcde_data.csv")   
df = pd.DataFrame(data)
cov_dic = {}
print(len(data))
for i in range(len(df)):
    if df.iloc[i]['Age'] in cov_dic:
        if df.iloc[i]['Area'] in cov_dic[df.iloc[i]['Age']] and df.iloc[i]['Year']<=2015:
            cov_dic[df.iloc[i]['Age']][df.iloc[i]['Area']][df.iloc[i]['Year']] = df.iloc[i]['Years']
        else:
            cov_dic[df.iloc[i]['Age']][df.iloc[i]['Area']] = {}
            cov_dic[df.iloc[i]['Age']][df.iloc[i]['Area']][df.iloc[i]['Year']] = df.iloc[i]['Years']
    else:
        cov_dic[df.iloc[i]['Age']] = {}
        cov_dic[df.iloc[i]['Age']][df.iloc[i]['Area']] = {}
        cov_dic[df.iloc[i]['Age']][df.iloc[i]['Area']][df.iloc[i]['Year']] = df.iloc[i]['Years']

header = ['country']
for i in range(1950,2016,5):
    header.append(str(i))


for k in cov_dic:
    with open('converted'+str(k)+'.csv', 'w', encoding='UTF8') as f:
        writer = csv.writer(f)

        # write the header
        writer.writerow(header)
        # write the data
        for row in cov_dic[k]:
            s = row
            for y in cov_dic[k][row]:
                s+=str(cov_dic[k][row][y])
            writer.writerow(s)

