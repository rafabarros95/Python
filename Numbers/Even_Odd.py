import sys

# Even or odd based on user input

#----------------------------------------------------------------------------------------------

 # First solution
""" number = int(input("Enter a number: "))
if number%2 == 0:
    print("The number is even")
else:
    print("The number is odd") """

# another way of solving the problem
# def main():
#     number = int(input("Enter a number: "))
#     # num = even_odd(number)
#     print(f"The number {number} is even" if number%2 == 0 else f"The number {number} is odd")

#------------------------------------------------------------------------------------------------

# Second way
def main():
    # number = int(input("Enter a number: "))
    if len(sys.argv) == 2:
        even_odd(int(sys.argv[1]))
   
# By Default, if function does not return anything, it returns None
def even_odd(num):
    if num%2 == 0:        
        return "The number is even"
    else:
        return "The number is odd"

   
if __name__ == "__main__":
    main()

