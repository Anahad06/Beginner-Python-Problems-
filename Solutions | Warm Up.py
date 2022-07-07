#1

# Factorial 
x = int(input("Factorial of: "))
val=1

for i in range(2, x + 1):
    val *= i
    
print("Solution:",val)
