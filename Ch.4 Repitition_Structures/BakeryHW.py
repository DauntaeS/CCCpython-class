# You work for a bakery that sells two items: muffins and cupcakes. The number of muffins and cupcakes in your shop at any given time is stored in the variables muffins and cupcakes which you will define, and the store has 10 muffins and 10 cupcakes.  Write a program that takes strings from standard input indicating what your customers are buying ("muffin" for a muffin, "cupcake" for a cupcake). If they buy a muffin, decrease muffins by one, and if they buy a cupcake, decrease cupcakes by 1. If there is no more of that baked good left, print ("Out of stock").  Once you are done selling, input "0", and have the program print out the number of muffins and cupcakes remaining, in the form "muffins: 9 cupcakes: 3" (if there were 9 muffins and 3 cupcakes left, for example).

# Input
# muffins = 10
# cupcakes = 10
# store_qty = 10

# Process
# ask user Cupcake or Muffin?
# How to get code to repeat until out of stock

# Output
# Store inventory
# muffin count
# cupcake count


muffins = 10
cupcakes = 10
store_qty = 10

for i in range(store_qty):

    order = input("What will you be having, cupcake or muffin? ")

    if store_qty <= 0:
        print("Sorry we are out of stock of everything, See you tomorrow ")

    elif order == "cupcake":
        if cupcakes <= 0:
            print("Out of stock")
        else:
            cupcakes -= 1
            store_qty -= 1

    elif order == "muffin":
        if muffins <= 0:
            print("Out of stock")
        else:
            muffins -= 1
            store_qty -= 1

    elif order == "0":
        print(f"Store inventory muffins: {muffins}, cupcakes {cupcakes}.")

    else:
        print("Not sure?")

    # print(f"Store inventory muffins: {muffins}, cupcakes {cupcakes}.")
