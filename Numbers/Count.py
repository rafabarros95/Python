# Testing functions call

def count():
    print("Let's count :) ")
    end = int(input("Until when?")) 
    print("Starting----------")
    n = 1
    while n<=end:
        print(n, " ")
        n+=1
   
    print("End----------")
    print("Counting completed")
    

count()