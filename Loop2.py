num1 = int(input("Enter a number "))
num2 = int(input("Enter a second number "))

while True:
    print("Inside while Loop")
    choice = input("Do you want the loop to continue? Y/N ")
    if choice in ("Y", "y"):
        print("continuing...")
        num1 = int(input("Enter a number "))
        num2 = int(input("Enter a second number "))
    else:
        break