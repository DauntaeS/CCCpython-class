import math

# Assume each pizza has 8 slices. Assuming that there is a family of 4. Ask how many slices everyone in the family eats. Then calculate how many whole pizza are required for a family of 4 for one meal? How many are the leftover slices? So if everyone is eating 3 slices you need 2 pizzas with 4 leftover slices. Do not use loops or lists or functions. In this case write two programs one with everyone eating the same number of slices (only 1 input statement) and another with everone eating different number of slices (two input statements).

# The inputs
pizza = 8
family = 4
slices_Eaten = int(input("How many slices did everyone in the family eat? "))

# process
# 1. how many slices did everyone eat
# 2. covert to whole pizzas
# 3. find leftover slices

total_Eaten = slices_Eaten * family
whole_Pizzas = math.ceil(total_Eaten / pizza)

left_Over = total_Eaten % pizza

# output
# Whole pizzas needed to be ordered
# how many slices that are leftover

print("Whole pizzas needed to be ordered", whole_Pizzas)
print("Slices that are left over", left_Over)
