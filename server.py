from flask import Flask
import json
from about import me
from data import mock_data

app = Flask(__name__) # create an instance of Flask class


#####################
#### WEB SERVER #####
#####################
@app.get("/") # calls the root page 
def home():
    return "Hello World from a flask server"

@app.get("/test")  # remember to type ("") variable in url
def test():
    return "This is a test"



################################
########### API SERVER #########
################################

@app.get("/api/version")
def version():
    return json.dumps("1.0")

@app.get("/api/about")
def about():
    return json.dumps(me)

############

@app.get("/api/catalog") # <---new url for display**
def get_data():
    return json.dumps(mock_data)
# product = dictionary (object)

@app.get("/api/product/count")
def product_count():
    count = len(mock_data)
    return json.dumps(count) 


@app.get("/api/about/dev_info")
def dev_info():
    name = me["name"]
    last_name = me["last_name"]
    email = me["email"]
    response = f"{name} {last_name} -- {email}"
    return json.dumps(response)
# or
#  # return json.dumps(f"{me["name"]} {me["last_name"]} -- {me["email"]}")


@app.get("/api/products/total")
def sum_practice():
    total = 0
    for product in mock_data:
        price = product["price"]
        total =  total + price

    return json.dumps(price) 



# get /api/categories
# return a list of categories
# 1 - create a list
# 2 - for to travel the catalog
# 3 - get the category from the product
# 4 - add the category to the list
# 5 - return the list as json

@app.get("/api/categories")
def cat_list():
    cats = []
    for product in mock_data:
        category = product["category"]

        # if category does not exist inside the list
        if category not in cats:
            

        
            cats.append(category)
    return  json.dumps(cats)


# @app.get("/api/catalog/...") ---required for every category

@app.get("/api/catalog/<category>")  # category is now a variable
def products_by_category(category):

    filter_category = []
    for product in mock_data:
        
        if product["category"].lower() == category.lower():
            filter_category.append(product)

    return json.dumps(filter_category)


# create a list
# travel mock_data with a for loop
# from the product, get the category
# if category is equal to the category we recieved
#   if so, append product to the list
# at the end of the for loop, return the list
    



    




    



# start the server
app.run(debug=True)

# this is a change