# working with List

#create a list
ages = []



# add elements to a list
ages.append(38)
ages.append(39)
ages.append(44)
ages.append(48)
ages.append(50)
print(ages)

# for loop
for age in ages:
    print(age)



# in for loop, variable needs to be outside
# print sum of all ages
total = 0
for age in ages:
    total = total + age
    print(total)