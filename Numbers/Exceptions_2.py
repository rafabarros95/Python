def main():
    number_returned = get_int()
    print(f"The number is: {number_returned} ")

def get_int():
    try:
        number = int(input("Enter a number: "))
        return number
    except ValueError:
        print("You must enter a number (int):")
        
main()
