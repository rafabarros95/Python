def main():
    print_size(4)

def print_size(size):
    for i in range(size):
        for j in range(size):
            for k in range(size):
                print(f"({i}, {j}, {k})  " , end="")
            print()
        print()


main()