# Work this Slovar'
print("Работа со словарем")
my_dict = {"Nikita" : 1997 , "Marysia" : 2001 , "Misha" : 1998 , "Sasha" : 1995}
print(my_dict)
print(my_dict.get("Nikita"))
print(my_dict.get("Alex", "Такого заначения нет"))
my_dict.update({"Grisha":2000, "Max":2005})
print(my_dict)
a = my_dict.pop("Misha")
print(a)
print(my_dict)
# Work this Mnojestva
print("Работа с множествами")
my_set = {1, 2, 3, 4, 5, 1, 2, 3, 4, "Egg"}
print(my_set)
my_set.add((10, 12))
print(my_set)
my_set.remove(4)
my_set.discard(2)
print(my_set)
