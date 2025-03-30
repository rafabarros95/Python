

def main():
    # number = int(input("Enter a number: "))
    number = input("Enter a number: ")
    result = square(number)
    print(f"The square of {number} is: {result}")

def square(number):
    return number * number

if __name__ == "__main__":
    main()