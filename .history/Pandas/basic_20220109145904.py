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

print(df['Data.Precipitation'])

print(type(df['Data.Precipitation']))

print(df[['Data.Precipitation' , 'Date.Full']])

print(df['Data.Precipitation'].std())

# The above is the standard deviation

print(df.describe)

# The above method prints the statistics of our data


# Cnditional statements 


# print(df[df['Data.Precipitation']>=0.40])

print(df[df['Data.Precipitation'] == df['Data.Precipitation'].max()])

print(df[df['Data.Temperature.Min Temp'] <= 20])









