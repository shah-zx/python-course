import pandas

data = pandas.read_csv("squirrel.csv")
# print(data)

# Here we have to find out how many colors the squirrel os having  ,  how many squirrels are there.

c_squirrels = data[data.Primary == "Cinnamon"]
count_cinnamon = len(c_squirrels)
g_squirrels = data[data.Primary == "Gray"]
count_grey = len(g_squirrels)
b_squirrels = data[data.Primary == "Black"]
count_black = len(b_squirrels)

# print(count_grey)
# print(count_black)
# print(count_cinnamon)
# for color in color_list:
#     print(color)

# Now making the table for the count and the color of the squirrels

data_squirrels = {
    "color": ["Gray", "Black", "Cinnamon"],
    "count": [count_grey , count_black , count_cinnamon]
}

# Converting the dictionary to to_csv :

sq_data = pandas.DataFrame(data_squirrels)
sq_data.to_csv("squirrel-new.csv")
print(sq_data)

