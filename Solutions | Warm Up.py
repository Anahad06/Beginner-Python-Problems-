#1: Factorial Solution 
x = int(input("Factorial of: "))
val=1

for i in range(2, x + 1):
    val *= i
    
print("Solution:",val)


#2: Multiplication Table 

x = int(input("Multiplication Table Of: "))

for i in range(1, 11):
    print(i, "x", x, "=", x * i)

 
#3: Cube 

x = int(input("Find The Cubes Until: "))

for i in range(1, x + 1):
    print("Cube of", i, "=", i ** 3)

# MOVE ON TO NEXT WORKSHEET ONCE FINISHED. BE SURE TO REDO PROBLEMS THAT YOU HAVE DOUBT WITH!

