import sys  #it's a Library that gets user inputs in command line

# print("Hello: " , sys.argv[1], sys.argv[2]) -->  sys.argv[0] is the name of the script

""" if len(sys.argv) < 2:
    # print(" Few Arguments passed")
     sys.exit(print("Few Arguments passed"))  #quit the program
elif len(sys.argv) > 2:
    # print("Too many arguments passed")
    sys.exit(print("Too many arguments passed"))  #quit the program 
else:
    print("Hello: ", sys.argv[1]) """


# Another way of interacting with loops

if len(sys.argv) < 2:
    sys.exit(print("Few Arguments passed"))

for arg in sys.argv[1:]:  # 1: is the slice starting from 1 and goes to the end
    print("Hello: my name is: " , arg)
    
