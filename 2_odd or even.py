# WAP to check if a number entered by the useris odd or even
num = int(input("enter number:"))
rem = num % 2
if(rem == 0):
    print("Even")
else:
    print("Odd")