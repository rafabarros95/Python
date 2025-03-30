# Functions called by functions - Helper Functions

def main():
    number = get_number()
    meow(number)


def get_number():
    n = int(input("Enter a number: "))
    while True:
       if n > 0:
          break
    return n

def meow(n):
    print("Meow\n" * n)

main()

    