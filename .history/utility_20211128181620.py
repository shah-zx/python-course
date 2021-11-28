# Here we will learn about utilites in python 

import argparse  # This module helps us in creating the command line utilites
import sys    # This moduke helps in writing the work done by argparse in console

if __name__ == '__name__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--x' , type = float ,default = 1.0)
    