print("If you want to check your number is prime then choose 1: ")
print("If you want to see the prime numbers upto a given range then choose 2")
ch = int(input())
if ch == 1:
    n = int(input("Enter your number: "))
    if n > 1:
        is_prime = True
        for i in range(2, n):
            if n % i == 0:
                is_prime = False
                break
        if is_prime:
            print("Your number is a prime")
        else:
            print("Your number is not a prime")
    else:
        print("Please check your number again, it should be a natural number greater than 1")

elif ch==2:
    n=int(input("Enter your number up to which you want to print the prime numbers : "))
    print(f"prime numbers up to {n} are: ")
    for i in range(2,n):
        is_prime = True

        for j in range(2,i):

            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            print(i)
else:
    print("please choose 1 or 2 options")

