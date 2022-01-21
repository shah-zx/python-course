from email import header
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

# print(df.shape)

# # gives r and c's

# # print(df.columns)

# rows , columns = df.shape

# print(columns)

# print(rows)

# print(df.head())

# print(df.head(3))

# print(df.tail(4))

# print(df['Data.Precipitation'])

# print(type(df['Data.Precipitation']))

# print(df[['Data.Precipitation' , 'Date.Full']])

# print(df['Data.Precipitation'].std())

# # The above is the standard deviation

# print(df.describe)

# The above method prints the statistics of our data


# Cnditional statements 


# print(df[df['Data.Precipitation']>=0.40])

# print(df[df['Data.Precipitation'] == df['Data.Precipitation'].max()])

# print(df[df['Data.Temperature.Min Temp'] <= 20])

# print(df['Data.Temperature.Min Temp'])

# print(df['Date.Full'][df['Data.Precipitation'] == df['Data.Precipitation'].max()])  # Finding the date 

# print(df['Station.City'][df['Data.Precipitation'] == df['Data.Precipitation'].max()])

# print(df.index)

# print(df.set_index('Date.Full' , inplace=True))  # This will convert the given attribute to index
                        
# print(df.loc['2016-01-03'])

# print(df)

# print(df.reset_index(inplace = True))   # This will undo the indexing

# print(df)

# print(df.set_index('Data.Temperature.Max Temp' , inplace=True))  # This will convert the given attribute to index

# print(df)

# df = pd.read_csv('C:\\Users\\hp\\Desktop\\python\\csv files\\temp.csv' , header = 1)  # This will skip first row and print other rows 



# df = pd.read_csv('C:\\Users\\hp\\Desktop\\python\\csv files\\temp.csv' , header = None)  # This will skip first row and print other rows 

# print(df)

# df = pd.read_csv('C:\\Users\\hp\\Desktop\\python\\csv files\\temp.csv' , header = None) // This will print numbers in place of first column , if any header is not present 

# df = pd.read_csv('C:\\Users\\hp\\Desktop\\python\\csv files\\temp.csv' , nrows = 5)  # This will print the number of rows given

# print(df)

# df = pd.read_csv('C:\\Users\\hp\\Desktop\\python\\csv files\\temp.csv' , na_values = ["Not avaialable" , "n.a."])  # This will make the not availabke values as NaN.

# df = pd.read_csv('C:\\Users\\hp\\Desktop\\python\\csv files\\temp.csv' , na_values = {'Data.Precipitation' : ["0.0" , "n.a."]})  # This will change the 0.0 values to NaN in Data.Precipitation column 

# print(df)

# making our own csv 👍

# df.to_csv('Hello.csv')  # By doing this we had copied our data frame into Hello.csv

# df.to_csv('Hello.csv' , index = False)  # By doing this we had copied our data frame into Hello.csv

# The above will remove the row nos.

# I we want to eport specific columns in the Hello.csv 

# df.to_csv('Hello.csv' , columns = ['Data.Precipitation' , 'Station.City'])

df.to_csv('Hello.csv' , header = False)  # Removing the header 


