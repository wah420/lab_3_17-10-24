random_list = [94, 18.2, "Beans", 34 + 35, 92.9]
print(len(random_list))
random_list.append(420)
random_list.insert(0, "Why")
random_list.remove(420)
print(random_list)
print(len(random_list))
print(random_list[0])
random_list[1] = 734
print(type(random_list))
my_tuple = tuple(random_list)
print(type(my_tuple))
print(my_tuple[0])
print(len(my_tuple))
#my_tuple[0] = "Not" cannot add anything to a tuple

other_tuple = (83, 85, 12, 15, 62)
joined_tuple = my_tuple + other_tuple
print(joined_tuple)
another_list = list(joined_tuple)
print(type(another_list))
my_set = set(another_list)
my_set.add(2)
print(my_set)
another_set = {83, 151, 8}
new_set = my_set & another_set
print = new_set