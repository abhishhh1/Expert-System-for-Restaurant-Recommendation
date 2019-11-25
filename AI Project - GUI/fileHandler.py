import csv
import pandas as pd

def readDataFromCSVFile(filename):
  lst=[]
  try:
    with open(filename, 'r', newline='', encoding="utf-8") as file:
      reader = csv.reader(file,delimiter=',')
      headRow = next(reader)
      for line in reader:
        d = {} 
        for i in range(len(headRow)):
          d[headRow[i]]=line[i]
        lst.append(d)
  except OSError as e:
    print("\nSorry, "+filename+" could not be found.\n")
  return lst

def createDataframe(dataset):
  df={'Name':[],'Rating':[],'Budget':[],'Distance':[]}
  cnt=0
  for data in dataset:
    df['Name'].append(data['name'])
    df['Rating'].append(data['rating'])
    df['Budget'].append(data['price'])
    df['Distance'].append(data['distance'])
    cnt+=1
    if cnt==5:
      break
  dataframe=pd.DataFrame(df)
  dfStyler = dataframe.style.set_properties(**{'text-align': 'left'})
  dfStyler.set_table_styles([dict(selector='th', props=[('text-align', 'left')])])
  return dataframe

