def calculateTime():
    monkey_one = input("Is the first monkey smiling?: ")
    monkey_two = input("Is the second monkey smiling?: ")

    if monkey_one.lower() == "y" and monkey_two.lower() == "n":
        print("Yay! We're going to have a good day!")
    
    elif monkey_one.lower() =="n" and monkey_two.lower() =="y":
        print("Yay! We're going to have a good day!")
    else:
        print("Uh Oh! We're in trouble!")

## If you want to test locally run > python monkeyCalculator.py

if __name__ == "__main__":
    calculateTime()
    
