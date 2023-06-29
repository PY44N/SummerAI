import random, math

result_1 = math.pow(2, 4)
print("Result_1 is", result_1)


result_2 = math.sqrt(16)
print("Result_2 is", result_2)

result_3 = random.randint(0, 100)
print("Result_3 is", result_3)

names = ["Amaryllis", "Godson", "Emily", "Reina", "Derin", "Elena", "Inacio"]
print("Original Names:", names)

random.shuffle(names)
print("Shuffled Names:", names)

result_4 = random.choice(names)
print("Result_4 is", result_4)