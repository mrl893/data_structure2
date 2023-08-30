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

