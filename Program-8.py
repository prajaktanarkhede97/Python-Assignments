#Write a program which accept number from user and print that number of “*” on screen.
# Output : * * * * *

def printstar(x):
    for i in range (x): 
     print(" * ", end= " ")
        
x=(int(input("Enter the number")))
printstar(x)
