from math import pow, sqrt
from random import randint, choice, shuffle

result_1 = pow(2, 4)
print("Result_1 is", result_1)


result_2 = sqrt(16)
print("Result_2 is", result_2)

result_3 = randint(0, 100)
print("Result_3 is", result_3)

names = ["Amaryllis", "Godson", "Emily", "Reina", "Derin", "Elena", "Inacio"]
print("Original Names:", ", ".join(names))

shuffle(names)
print("Shuffled Names:", ", ".join(names))

result_4 = choice(names)
print("Result_4 is", result_4)