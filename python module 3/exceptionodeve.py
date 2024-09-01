"""Write python program that user to enter only odd numbers,
else will raise an exception."""

try:
    number = int(input("Enter an odd number: "))
    if number % 2 == 0:
        raise ValueError
    else:
        print("The number is odd.")
except ValueError:
    print("You have not entered an odd number.")
    