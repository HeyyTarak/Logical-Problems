print("If you want to print the series upto your required range enter 1 ")
print("If you want to print the series upto your required number in the series enter 2 ")
ch=int(input())
if (ch==1):
    n=int(input("Enter the number of series you want to see: "))
    if n>=2:
        print("Your fibonacci series: ")
        n1=0
        n2=1
        print(n1)
        print(n2)
        for i in range(2,n):
            n3=n1+n2
            print(n3)
            n1,n2=n2,n3
    else:
        print("your Value is Negative enter the Positive value")
elif ch==2:
    num = int(input("Upto which number the series should be printed? "))
    print("Your fibonacci series: ")
    n1 = 0
    n2 = 1
    print(n1)
    print(n2)
    for i in range(2,1000):
        n3 = n1 + n2
        if n3==num:
            break
        print(n3)
        n1,n2=n2,n3
else:
    print("Your input is invalid ")
