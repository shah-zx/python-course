# Here we will study about pickle module :
import pickle

cars = ["Audi" ,"BMW" , "Aston martin" , "Nissan" , "Rolls Royce"]
 
 # Now we will store the cars object in a file 
 
file = "mycar.pkl"
fileobj = open(file , 'wb')
pickle.dump(cars , fileobj)
