#This is the Main function logic
def Fact(n):
    if n == 0:
        return 1
    else:
        return n * Fact(n-1)
#Main program

n = int(input("Enter the number for which you want to find the factorial: "))
if n >= 0:
    print(f"The factorial of the given number {n} is {Fact(n)}")
else:
    print("Your input is a Negative value please enter a Positive value")