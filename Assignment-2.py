my_set_1 = {20, 21, 22, 23, 24}
my_set_2 = {23, 24, 25, 26, 27}

print(f"Set 1: {my_set_1}")
print(f"Set 2: {my_set_2}")

element_to_check = 22
if element_to_check in my_set_1:
    print(f"Element {element_to_check} is in Set 1.")
else:
    print(f"Element {element_to_check} is not in Set 1.")

    # .union Method
# combine all from both : ignore duplicate

print(my_set_1.union(my_set_2)) 
 
# .intersection
# combine all values from both : Only Same values

print(my_set_1.intersection(my_set_2))

