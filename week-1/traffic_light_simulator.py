signal = input("Enter traffic light color (red/yellow/green): ").lower()

if signal == "red":
    print("STOP!")
elif signal == "yellow":
    print("Prepare to stop")
elif signal == "green":
    print("You can go")
else:
    print("Wrong input!")