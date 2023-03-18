from about import me

print(me)

print(me["name"])

name = me["name"]
last = me["last_name"]
print(name + " " + last)

#modify
me["age"] = me["age"] +1
print(me)

#add
me["preferred_color"] = "blue/gray"
print(me)

age = me["age"]
print(name + ":" + str(age))  # cannot add string + integer; use str()
# this line is not clean, needs string formatting

# string format
print(f"Wake up") 

# or
#print(f"{name}": {age})
print(f"{name}": {age})

# also
print(f"   {age} - ., {name}") # three spaces, - ., ,

# delete a key from dict
del me["age"]

# or
z = me["age"].pop()




# HW
# 1 print the same but using python string formatting
# 2 delete the age key from the dictionary and print the dictionary to confirm  # dictionary uses []