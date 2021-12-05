

import pandas as pd

years = [(y,y+5) for y in range(1960,2011,5)]
datasets = ['Primary_OL', 'Lower_Secondary_OL']

file_prefix = "wcde-female_"

for name in datasets:
  data = pd.read_csv("../datasets/"+file_prefix+name+".csv")   
  df = pd.DataFrame(data)
  for r in range(len(df)):
    for s,e in years:
      df.at[r,str(s)] = round(df.iloc[r][str(s)],2)
      df.at[r,str(e)] = round(df.iloc[r][str(e)],2)
      d   = df.iloc[r][str(e)] - df.iloc[r][str(s)]
      inc = d/5
      i=1
      for y in range(s+1,e):
        df.at[r,str(y)] = round(df.iloc[r][str(s)] + inc*i,2)
        i+=1
  df.to_csv("../datasets/"+file_prefix+name+".csv", encoding='utf-8', index=False)