import pandas as pd

df = pd.read_csv('C:\\Users\\hp\\Desktop\\python\\csv files\\temp.csv')

# df stands for data frame

# print(df);

# print(df['Data.Temperature.Max Temp'].max())

# print(df['Date.Full'][df['Station.City'] == 'Cold Bay'])

# print(df['Date.Full'][df['Data.Precipitation'] == 0.6])

# print(df['Station.City'][df['Data.Temperature.Avg Temp'] == 45])

# print(df['Data.Temperature.Max Temp'].mean())  # For dinding out average

# print(df['Station.Code'][df['Station.Location'] == 'Birmingham, AL'])

print(df.shape)

# gives r and c's

# print(df.columns)

rows , columns = df.shape

print(columns)

print(rows)

print(df.head())

print(df.head(3))

print(df.tail(4))

print(df.columns[1])






