from math import pow as power, sqrt as square_root
from random import randint as random_int, shuffle as shuffle_array, choice as random_element

result_1 = power(2, 4)
print("Result_1 is", result_1)


result_2 = square_root(16)
print("Result_2 is", result_2)

result_3 = random_int(0, 100)
print("Result_3 is", result_3)

names = ["Amaryllis", "Godson", "Emily", "Reina", "Derin", "Elena", "Inacio"]
print("Original Names:", ", ".join(names))

shuffle_array(names)
print("Shuffled Names:", ", ".join(names))

result_4 = random_element(names)
print("Result_4 is", result_4)