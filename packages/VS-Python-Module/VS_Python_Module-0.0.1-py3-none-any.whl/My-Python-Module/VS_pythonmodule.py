from sys import exit

def hello(name=None):
    if not name:
        print("Hello World")
    else:
        print("Hello", name)

def get_int(str="Enter an integer: "):
    while True:
        try:
            return(int(input(str)))
        except ValueError:
            pass