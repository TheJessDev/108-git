
colors = ['teal', 'PINK', 'PURPLE', 'ORANGE', 'green', 'BLUE', 'YELLOW', 'red', 'pink', 'TEaL', 'PurPLE', 'greEn', 'YELLOW', 'ORAnGE', 'blue', 'RED', 'teal', 'PINk', 'purPle', 'orange', 'GREEN', 'BluE', 'YelLow', 'ReD']

# 1 - print how many colors (in lowercase), case insesitive
print(len(colors))


# 2 - get the list of unique colors (in lowercase), case insestive
# create a list
# travel the list of colors
# get the color, parse it to lower, if the color is not in the list, append it
results = []
for color in colors:
    color_lower = color.lower()
    if color_lower not in results:
        results.append(color_lower)

print(results)



# 3 - given a color, count how many times it exist on the list
color = "red"
count = 0
for c in colors:
    if color == c.lower():
        count = count + 1

print(count)
# create a count equal to zero
# travel the list of colors
# if the color you are looking for, is equal to the color fro the list (in lowercase)
#increase count by 1  (count = count + 1
# print the result)