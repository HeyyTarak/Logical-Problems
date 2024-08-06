#Function of GCD
def GCD(a, b):
    while b != 0:
        a, b = b, a % b
    return a


a = int(input("enter a value: "))
b = int(input("enter b value: "))
print(f"The GCD of {a} and {b} is {GCD(a, b)}.")
