try:
    number = int(input("Enter a number: "))
    print("The number is:", number)
except ValueError:
    print("That wasn't a valid number")
except Exception as ex:
    print("Exception: ", ex)