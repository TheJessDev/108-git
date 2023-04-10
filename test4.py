
def print_total():
    print ("your total is: 123")


def can_drink(age):
    if age < 21:
        print ("no") 
    else: 
        print("yes")


def users():
    people = [  
        {'name': 'Alice', 'age': 25},
        {'name': 'Bob', 'age': 30},
        {'name': 'Charlie', 'age': 35},
        {'name': 'Dave', 'age': 40},
        {'name': 'Emily', 'age': 45},
    ]
# ** array **

    for user in people:
        print(user)
        
    print("2-only names")
    for user in people:
        print(user["name"])
    
# Don't forget to call funtion at bottom

    print("3-users over30")
    for user in people:
        if user["age"] > 30:
            print(user["name"] + "-" + str(user["age"]))


    print("4- total ages")
    total = 0
    for user in people:
        total += user["age"]
    print(f"Total is: {total}")
    # or
    print("Total is: " + str(total))



    print("5- find by name")
    name = input("Type the user name: ")
    found= False
    for user in people:
        if user ["name"].lower() == name.lower():
            found = True
            print(f"{user['name']} => {user['age']}") # f means string format vs str() interpolates integer into string...

    if not found: 
        print("Error: User not found")



















print_total()

can_drink(19)
can_drink(23)

users()