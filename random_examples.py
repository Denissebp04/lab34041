import random


print("Random float between 0 and 1:")
print(random.random())
print()

print("Two random integers between 1 and 100:")
print(random.randint(1, 100))
print(random.randint(1, 100))
print()


print("Random numbers using randrange():")

print("randrange(1, 10):", random.randrange(1, 10))

print("randrange(1, 10, 2):", random.randrange(1, 10, 2))

print("randrange(0, 101, 10):", random.randrange(0, 101, 10))
print()


print("Random sampling from a predefined list:")
aList = [20, 40, 80, 100, 120]
sampled_list = random.sample(aList, 3)
print("Original list:", aList)
print("Randomly sampled 3 items:", sampled_list)
print()


print("Random sampling from range:")
num_list = random.sample(range(100), 5)
print("5 random numbers between 0 and 99:", num_list) 