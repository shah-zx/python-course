# # Here we will study about raise :
# a = input("What is your name")
# b = input("How much do you earn")

# if int(b)==0:
#     raise ZeroDivisionError("b is 0 so stoping the process")  # Here we are raising one error 

# if a.isnumeric():
#     raise Exception("Numbers are not allowed")  # Here we are raising one error 
# print(f"Hello {a}")

# # 1000 lines taking one hour 


# These are some of the built in errors which are in use :
 
# exception IndexError
# Raised when a sequence subscript is out of range. (Slice indices are silently truncated to fall in the allowed range; if an index is not an integer, TypeError is raised.)

# exception KeyError
# Raised when a mapping (dictionary) key is not found in the set of existing keys.

# exception KeyboardInterrupt
# Raised when the user hits the interrupt key (normally Control-C or Delete). During execution, a check for interrupts is made regularly. The exception inherits from BaseException so as to not be accidentally caught by code that catches Exception and thus prevent the interpreter from exiting.