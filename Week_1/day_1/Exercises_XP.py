# Exercise 1
print(*["Hello world"] * 4, sep="\n")

# Exercise 2
x = (99**3)*8
print(x)

 # Exercise 3
name = input('What is your name? ')
if name == 'Olga':
   print(f'Cool! My name is {name} too!')
else:
   print(f'Nice to meet you {name}!')

# Exercise 4
height = int(input('Enter your height: '))
if height > 145:
    print('Super! You are tall enough to ride!')
else:
    print('Oups... You need to grow some more to ride.')

# Exercise 5
my_fav_numbers = {3, 7, 9, 5}
my_fav_numbers.add(1)
my_fav_numbers.add(17)
my_fav_numbers.remove(17)
friend_fav_numbers = {5, 12, 15} 
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
print(our_fav_numbers)

# Exercise 6
# No, tuples are immutable, their contents cannot be changed after creation. 

# Exercise 7
basket = ["Banana", "Apples", "Oranges", "Blueberries"];
basket.remove("Banana")
basket.remove("Blueberries")
basket.append("Kiwi")
basket.insert(0, "Apples")
apple_count = basket.count("Apples")
basket.clear()
print(basket) 

# Exercise 8
sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]

while "Pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove("Pastrami sandwich")
print(sandwich_orders)

finished_sandwiches = []
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    finished_sandwiches.append(current_sandwich)
    print(f"I made your tuna sandwich {current_sandwich}.")
print(finished_sandwiches) 
