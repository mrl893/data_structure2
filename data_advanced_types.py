empty_list = []
type(empty_list)

empty_list = list() # constructor


a_xpress = [2,3,5,7,11,13,17,19]
fruits = ["Apple", "Mango", "Orange", "Kiwi", "Blueberry"]

# class list:
print(type(fruits)) 

# access elements 
# [1]
# [-2]
# [2:4]
# [0::2]
print(fruits[1])  == "mango" # mango True

# Iterate over list
for i in fruits:
    print(i)

for item in (range(len(fruits)-1,-1,1)):
    print(fruits[item])

for item in reversed(fruits):
    print(item
          )
# enumerate
for i, name in enumerate(fruits, start=1):
    print(f"{i}: {name}")

 
colors = ["red", "yewllow", "orange","green","blue"]
for i in range(len(fruits)):
    print(f"{fruits[i]} ---> {colors[i]}")
 
# zip()   
for item, color in zip(fruits, colors):
    print(f"{item} --> {color}")

print(fruits.index('Mango'))

for item in fruits:
    print(f"{fruits.index(item)} ---> {item}")


print(f"I have {len(fruits)} fruits")
print(f"     --> the list ID is: {id(fruits)}")

print("I also have to buy a banana.")
fruits.append("banana") 
print(f"My list of fruits is now: {fruits}")
print(f"     --> the list ID is: {id(fruits)}")

print("I will sort my list now")
fruits.sort()

print(f"Sorted list of fruits is: {fruits}")
print(f"     --> the list ID is: {id(fruits)}")

# Editing List 
# append()

fruits.append("Apple")
print(fruits)


morefruits = ["guava", "peach"]
fruits.extend(morefruits)
print(fruits)

# insert(index, item)
fruits.insert(2, "pineapple")
print(fruits)

# pop()
fruits.pop()
print(fruits)

# clear()
fruits.clear()
print(fruits)

# Mixed types
# mixed_list = [10,"Hello","World",[34]] # mixed type list
P = ["Wednesday", "April", 5, 2017, ("A","B","C")]
print((P[0:4]), "")
# print(("Wednesday"), P[-6])
print(P[4])

# Tuple
# Tupple = (8,'a',True,[1,2,3],"hello")   #(immutable)

empty_tuple = tuple()
type(empty_tuple)

primes = (2,3,5,7,11,13)
print(type(primes))


planets = ("mercury","venus","earth","mars","jupiter"
           "saturn","uranus","neptune")
# print(len(planets), planets[:3] , planets[:-1])
print(type(planets))
print(f"Number of planets in our solar system is: {len(planets)}")

# count
print(planets.count('earth'))

# index
print(planets.index("mars"))


solar_system_list = ["mercury", "venes", "earth", "mars",
                     "jupiter", "saturn", "uranus", "neptune"]

a_mutable_tuple = (solar_system_list, "pluto")
# print(a_mutable_tuple)


print(f"Original tuple: {a_mutable_tuple}")
print(f"ID id tuple: {id(a_mutable_tuple)}")

a_mutable_tuple[0][2] = "EARTH"

print(f"Modified tuple: {a_mutable_tuple}")
print(f'ID of tuple: {id(a_mutable_tuple)}')


(x,y,z) = ["a","b","c"]
x,y,z
(x,*y)=["a","b","c","d","e","f"] # * unpacking

data = (1,2,3,4,5,6,7,8,9)
data

# Dictionary
# dict = {"key":"value"}  {} or dictionary
# key must be immutable and value can be mutable as well

empty_dict = dict()
type(empty_dict)

daily_temps = dict()
daily_temps["mon"] = 70.2
daily_temps["tue"] = 67.2
daily_temps["web"] = 71.8
daily_temps["thu"] = 73.2
daily_temps["fri"] = 75.6

daily_temps1 = {"mon":70.2, "tue":67.2, "wed":71.8, "thu":73.2, "fri":75.6}
# print(daily_temps == daily_temps1 )

daily_temps2 = dict([("mon",70.2),("tue",67.2),
                     ("wed",71.8),("thu",73.2),
                     ("fri",75.6)])

daily_temps3 = dict(mon=70.2, tue=67.2, wed=71.8, thu=73.2, fri=75.6)
days  = ["mon", "tue", "wed", "thu", "fri"]
temps = [70.2, 67.2, 71.8, 73.2, 75.6]
daily_temps4 = dict(zip(days, temps))
print("\nDaily temperatures in Celsius:")


# access elements
print(daily_temps["web"])
daily_temps.keys()
daily_temps.values()
daily_temps.items()

"fri" in daily_temps
len(daily_temps)

# key must be Inmutable
temps   = {("June",10,2019): 75.2, "June-11-2019": 77.2, 3:88.9}
print(temps[3])

# loop over keys
for day in daily_temps:
    print(day)

for day in daily_temps:
    print(f"Key: {day} and Value: {daily_temps[day]}")


# Loop over keys and values
for day , temp in daily_temps.items():
    print(day, temp)


colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"] 
d = dict()

for color in colors:
    key = len(color)
    if key not in d:
        d[key] = []
    d[key].append(color)
print(f"d: {d}")
print(daily_temps2)

# Edit a Dictionary(add, delete items)
daily_temps2.update({"sat":32.3, "sun":76.8})
print(daily_temps2)


del daily_temps2["wed"]
print(daily_temps2)

removed_value = daily_temps2.pop("fri")
print("Romoved value: {}.format(removed_value)")
print("Updated dictionary: {}".format(daily_temps2))

# Useful Funct ass with Dictionaries

# Set

empty_set = set()
type(empty_set)

fibo = {1,1,2,3,5}
print(type(fibo))
print("Set fibo: ", fibo)

# fibo[0]

some_primes = [1,1,2,2,3,3,5,5]
primes = set(some_primes)
print("set primes:" , primes)


# Mathematical set operations
a = set({1,2,3,4})
b = set([3,4,5,6])

# a.union(b)
a|b
a&b
a.issubset(b)
a.difference(b)
a-b

a  = [[90,85,82], [72, 88, 90]]
print(id(a))

b = a
print(id(b))


b.append(23)
print("\na: ", a)
print("\nb:", b)

print("EQL?:", (a == b))
print("SOME ?:", (a is b))

b[0][0] = 30
print("b: ", b)
b = list(a)
print("a: ", a)


import copy

print(id(a))
print(a)
b = copy.copy(a)
print(id(b))

# Chage first year and firts subject's marks to 30
b[0][0] = 30

print("\nOringal List: ", a)
print("Shallow Copy: ", b)

print("\nEQl?:", (a == b))
print("\nSAME ?:", (a is b))

# Change first year and first subject's marks to 30
b = copy.deepcopy(a)
b[0][0] = 30

print("\nOriginal List: ", a)
print("Deep Copy: ", b)

print("EQL?:", (a == b))
print("SAME ?:", (a is b))


