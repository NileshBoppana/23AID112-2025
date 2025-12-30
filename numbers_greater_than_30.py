numbers = [12, 45, 3, 98, 7, 34, 21]

count = 0

for num in numbers:
    print(num)
    if num > 30:
        print("Greater than 30:", num)
        count += 1

print("Count of numbers greater than 30:", count)
