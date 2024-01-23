name = input("Enter your name:")
valid="n"
num=0
end= "y"
while end.lower() =="y":
    num = int(input(name + " Enter a number between 1 and 100: "))
    while valid != "y":
            if num < 1 or num > 100:
                print("Invalid Input please try again")
                num = int(input(name + " Enter a number between 1 and 100: "))
            else:
                valid = "y"
    if num%2 != 0 and num<60: #a
            print(str(num) +" Odd and less than 60")
    elif num % 2 == 0 and num >= 2 and num <= 24: #b
            print(str(num)+ " Even and less than 25")
    elif num % 2 == 0 and num>=26 and num <=60: #c
            print(str(num)+ " Even and between 26 and 60 inclusive.")
    elif num % 2 == 0 and num >60:#d
            print(str(num) + " Even and greater than 60")
    elif num % 2 != 0 and num >60:#e
            print(str(num) + " Odd and greater than 60")
    else:
            print("Invalid input")
    end = input("Would you like to continue (y/n): ")
