celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = celsius * 9/5 + 32
print(f"Temperature in Fahrenheit: {fahrenheit:.2f}°F")

if celsius < 0:
    print("Very cold! Wear thick jacket")
elif celsius <= 15:
    print("Cold. Wear jacket")
elif celsius <= 25:
    print("Nice weather")
else:
    print("Hot! Stay hydrated")