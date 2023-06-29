hours = input("Convert to hours or minutes? ")
num = eval(input("How many? "))
if hours.lower() == "hours":
    print(f"{num / 60} hours")
elif hours.lower() == "minutes":
    print(f"{num * 60}mins")
else:
    print("Invalid option")