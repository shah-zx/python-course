# Here we will learn about name = main
# import sklearn

def printhar(s):
    return f"Ye string shahnawaz ko dede thakur {s}"


def add(num1, num2):
    return num1 + num2 + 4


print("And the name is :", __name__)  # This will give the value : And the name is : main , as we are in the program where it is defined 

if __name__ == "__main__":
    print(printhar("strings"))
