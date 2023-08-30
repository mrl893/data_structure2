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

