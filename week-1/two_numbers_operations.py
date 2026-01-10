num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

num1 = int(num1)
num2 = int(num2)

print("Sum:", num1 + num2)
print("Difference:", num1 - num2)
print("Product:", num1 * num2)

if num1 > num2:
    print("First number is bigger")
elif num2 > num1:
    print("Second number is bigger")
else:
    print("Both numbers are equal")