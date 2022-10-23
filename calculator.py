import math
import time 

def add(x,y):
    return x + y
def subtract(x,y):
    return x - y
def multiply(x,y):
    return x * y
def divide(x,y):
    return x / y
def pythagtheo(x,y):
    return (x*x+y*y)**(1/2)
def root(x,y):
    return (math.pow(x, (1/y)))
def expn(x,y):
    return (x**y)
def pct(x,y):
    return ((x/y)*100)

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("if you want to do a more complicated calculation, type a number not listed")

while True:
    choice = input("Enter your choice(1/2/3/4): ")
    if choice in ('1', '2', '3', '4'):
        number1 = float(input("Enter first number: "))
        number2 = float(input("Enter second number: "))
        
        if choice == '1':
           print(number1, "+", number2, "=", add(number1, number2))
           
        elif choice == '2':
           print(number1, "-", number2, "=", subtract(number1, number2))
           
        elif choice == '3':
           print(number1, "*", number2, "=", multiply(number1, number2))
           
        elif choice == '4':
           print(number1, "/", number2, "=", divide(number1, number2))
           
        break
    
    else:
        
         print("Entered input is invalid. Do you want to do a more complex calculation?")
         print("5.Terminate Program")
         print("6.Pythagorean Theorem")
         print("7.Root of a number")
         print("8.Exponential notation")
         print("9.Percent calculation")
         Elsechoise = input("Enter your decision (5/6/7/8/9)")
         if Elsechoise in ('5', '6', '7', '8', '9'):
             cpxnum1 = float(input("Enter first number:"))
             cpxnum2 = float(input("Enter second number:"))
             if Elsechoise == '5':
                quit()
             elif Elsechoise == '6':
                print("a:", cpxnum1, "b:", cpxnum2, "c is equal to", pythagtheo(cpxnum1, cpxnum2))
                quit()
             elif Elsechoise == '7':
                print(cpxnum1, "to the root of", cpxnum2, "is", root(cpxnum1, cpxnum2))
                quit()
             elif Elsechoise == '8':
                 print(cpxnum1, "to the power of", cpxnum2, "is", expn(cpxnum1, cpxnum2))
                 quit()
             elif Elsechoise == '9':
                 print(cpxnum1, "is", pct(cpxnum1, cpxnum2),"%", "of", cpxnum2)
                 quit()
             else: quit()
                 
         break