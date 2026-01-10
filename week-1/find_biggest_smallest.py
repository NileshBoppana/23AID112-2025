numbers = [23, 87, 45, 12, 66, 91, 34, 58]

biggest = numbers[0]
smallest = numbers[0]

for num in numbers:
    if num > biggest:
        biggest = num
    if num < smallest:
        smallest = num

print("Biggest number:", biggest)
print("Smallest number:", smallest)
