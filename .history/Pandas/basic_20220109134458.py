import pandas as pd

df = pd.read_csv('C:\\Users\\hp\\Desktop\\python\\csv files\\temp.csv')

# print(df);

print(df['Data.Temperature.Max Temp'].max())

print(df['Date.Full'][df['Station.City'] == 'Cold Bay'])

print(df['Date.Full'][df['Data.Precipitation'] == 0.6])

print(df['Station.City'][df['Data.Temperature.Avg Temp'] == 45])
