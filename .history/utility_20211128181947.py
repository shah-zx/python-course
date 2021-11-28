# Here we will learn about utilites in python 

import argparse  # This module helps us in creating the command line utilites
import sys    # This moduke helps in writing the work done by argparse in console

if __name__ == '__name__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--x' , type = float ,
                        default = 1.0 , help = "Enter first number . This is a utility. Please contact shahnawaz sayyed")
    parser.add_argument('--y' , type = float ,
                        default = 3.0 , help = "Enter second number . This is a utility. Please contact shahnawaz sayyed")
    parser.add_argument('--o' , type = str ,
                        default = "add" , help = "This is a utility. Please contact shahnawaz sayyed")
    
    