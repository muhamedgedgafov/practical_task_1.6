my_dict = {"Muhamed": 2001, "Max": 2003}
print("Dict:", my_dict)
print("Existing value:", my_dict.get('Muhamed'))
print("Not existing value:", my_dict.get('Anton'))
my_dict.update({"Alex": 1998,
                "Sasha": 1999})
print(my_dict)
deleted_value = my_dict.pop('Muhamed', None)
print("Deleted value:", deleted_value)
print("Modified dictionary:", my_dict)

# Множество

my_set = {1, 2, 3, 4, "World", True, 5, 1, 2, 3, "World", (1, 2, 3)}
print("Set:", my_set)
my_set.add(13)
my_set.add((5, 6, 1.6))
my_set.discard('World')
print("Modified set:", my_set)