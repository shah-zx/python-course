import pandas as pd;

df = pd.read_csv('C:\\Users\\hp\\Desktop\\python\\csv files\\temp.csv')

# print(df);

print(df['Data.Temperature.Max Temp'].max())

print(df['Date.Full'][df['Station.City'] == 'Cold Bay'])
