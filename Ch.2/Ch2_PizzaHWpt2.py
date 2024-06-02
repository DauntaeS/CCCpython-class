import math

# Input
# pizza = 8
# person 1-4 and the slices each digest

# Process
# 1. how many slices did everyone eat?
# 2. covert to whole pizzas
# 3. find leftover slices

# Output
# How many whole pizzas are needed to be ordered
# How many pizza slices are left over

pizza = 8
person1 = int(input("How many slices did person1 eat? "))
person2 = int(input("How many slices did person2 eat? "))
person3 = int(input("How many slices did person3 eat? "))
person4 = int(input("How many slices did person4 eat? "))

total_eaten = person1 + person2 + person3 + person4

whole_pizzas = math.ceil(total_eaten / pizza)

leftovers = whole_pizzas * pizza - total_eaten

if total_eaten <= pizza and total_eaten >= 1:
    print("You only need to order 1 pizza")
    print(f"There will be {leftovers} slices leftover")

elif total_eaten <= 0:
    print("I guess no one is hungry for pizza")

elif total_eaten >= pizza:
    print(f"You need to order {whole_pizzas} pizzas")
    print(f"There will be {leftovers} slices leftover")

else:
    print("Error")
