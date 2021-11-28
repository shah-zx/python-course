# Here we will learn about utilites in python

import argparse  # This module helps us in creating the command line utilites
import sys    # This module helps in writing the work done by argparse in console


def calc(args):
    if args.o == 'add':
        return args.x + args.y
    
    elif args.o == 'mul':
        return args.x + args.y
    
    elif args.o == 'sub':
        return args.x + args.y
    
    elif args.o == 'div':
        return args.x + args.y
    
    else:
        return "something went wrong"


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('--x', type=float,
                        default=1.0, help="Enter first number . This is a utility. Please contact shahnawaz sayyed")
    parser.add_argument('--y', type=float,
                        default=3.0, help="Enter second number . This is a utility. Please contact shahnawaz sayyed")
    parser.add_argument('--o', type=str,
                        default="add", help="This is a utility for calculation . Please contact shahnawaz sayyed")

    args = parser.parse_args()
    sys.stdout.write(str(calc(args)))
