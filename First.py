# print("Hello world")
# print(2 + 3 - 2)

# with open("weather.csv") as data_file:
#   data = data_file.readlines()
#   print(data)
import pandas
import csv

# We are having a library for reading csv files
# Here we are reading the values from the csv file

# with open("weather.csv") as data_file:
#   data = data_file.readlines()
#   temperatures = []
#   for row in data:
#       if row[1] != "temp":     
#           temperatures.append(row[1])   # This is done for temperature values 
#   print(temperatures)


# This is the pandas library for reading the csv file
  


data = pandas.read_csv("weather.csv")
# print(type(data))
# print(data["temp"])
# data_dict = data.to_dict()
# print(data_dict)
# temp_list = data["temp"].to_list()
# print(len(temp_list))


# This is used to fimd the average of the values in temperature 

# avg_temp = data["temp"].to_list()
# avg = sum(avg_temp) / len(avg_temp)
# print(avg)


# We can also do this by doing

# print(data["temp"].mean())
# print(data["temp"].median())
# print(data["temp"].mode())
# print(data["temp"].max())

 # This is for taking the condition column 

# print(data["condition"])

 # For getting hold of a row from the csv file
 
# print(data[data.day == "Monday"])  # Selecting the row with the value monday 

# print(data[data.temp == data.temp.max()]) # Selecting the row with the value having max temperature

# monday = data[data.day == "Monday"]
# # print(monday.condition)

# monday_temp = int(monday.temp)

# farenhiet = (monday_temp * 9/5) + 32

# print(farenhiet)

# How to create a dataframe from scratch :

# data_dict = {
#   "students" : ["jimmy" , "jones" , "khali"],
#   "scores" : [78 , 89, 90]
# }

# # Now how to convert this dictionary into a dataframe

# data = pandas.DataFrame(data_dict)
# data.to_csv("students.csv")   # Here we converted the dictonary into an actual csv file 
# # print(data)


# some coding 

# Find out the minimum temperture in the data

# print(data["temp"].min()) 

# Get hold of the condition rows with weather data : rainy

# con = data[data.condition == "rainy"]
# print(con)

# wed_day = data[data.day == "Wednesday"]
# print(wed_day)














  
  
        
