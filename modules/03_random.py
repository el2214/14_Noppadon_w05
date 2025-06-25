import random

# print(f"{random.random()}")
# print(f"{random.randint(1,99)}")
# print(f"{random.randrange(1,102)}")
# print(f"{random.uniform(1,100):.4f}")

colors = ["red" , "green" , "blue" , "black" , "white", "purple", "pink"]

numbers = list(range(1,101))

random_list = random.choice(colors) # สุ่มใน list
random_3 = random.choices(colors, k=3) # สุ่มใน list ออกมา 3 ค่า
random_uniq = random.sample(colors, 3) # สุ่มใน list ออกมา 3 ค่า (ไม่ซ้ำ)

num_shuf = random.shuffle(numbers)

print(numbers)
random.shuffle(numbers)
print("=================================================================")
print(numbers)