from flask import Flask, request, abort  # requests posts to db, abort is for errors
import json
from about import me
from data import mock_data
from config import db
from flask_cors import CORS

app = Flask(__name__) # create an instance of Flask class
CORS(app) # WARNING: disables CORS check


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





@app.get("/api/catalog")
def get_catalog():
    cursor = db.products.find({})
    results = []
    for prod in cursor:
        results.append(fix_id(prod))

    return json.dumps(results)


def fix_id(record):
    record["_id"] = str(record["_id"])  # removes the word 'Object'and returns the number value only (parse into string)

    return record
    

@app.post('/api/catalog')
def save_product():
    product = request.get_json()  # get the json payload from the request
    # product is a dictionary, saves product to DB

    db.products.insert_one(product)  # product is collection name, CASE SENSITIVE

    print("-------------------------")
    print(product)  # this part goes to Terminal, return goes to ThunderClient

    # always needs a return to confirm everthing is correct
    return json.dumps(fix_id(product))



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
def sum_prices():
    cursor = db.products.find({})
    total = 0
    for product in cursor:
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

@app.get("/api/categories") # DB 
def categories():
    cursor = db.products.find({})
    cats = []
    for prod in cursor:
        category = prod["category"]

        # if category does not exist inside the list
        if category not in cats:
            cats.append(category)

    return json.dumps(cats)


# @app.get("/api/catalog/...") ---required for every category

@app.get("/api/catalog/<category>")  # category is now a variable
def products_by_category(category):
    cursor = db.products.find({"category": category})
    results = []
    for prod in cursor:
        results.append(fix_id(prod))

    return json.dumps(results)



@app.get("/api/product/lower/<price>")  # price is now a variable -- need to enter a specific dollar amount at end point
def products_lower_price(price):
    cursor = db.products.find({})
    fixed_price = float(price)   # float changes string to number 

    filter_lower_price = []
    for product in cursor:
        
        if product["price"] <= fixed_price:
            filter_lower_price.append(fix_id(product))

    return json.dumps(filter_lower_price)


@app.get("/api/product/greater/<price>")
def products_greater_price(price):
    cursor = db.products.find({})
    fixed_price = float(price)

    filter_greater_price =[]
    for product in cursor:

        if product ["price"] >= fixed_price:
            filter_greater_price.append(fix_id(product))

    return json.dumps(filter_greater_price)   # make sure the return is outside of loop
    

# find how to check if a string contains another string in python
# if term in [product title in lowercase]

#@app.get('/api/product/search/<term>')
#def search_product(term):

    #search_product =[]
    #for product in mock_data:
       # if term.lower() in product['title'].lower():  # when searching, use in vs ==
            #search_product.append(product)

    #return json.dumps(search_product)


@app.get('/api/product/search/<term>')
def search_product(term):
    
    cursor = db.product.find({"title":{'$regex' : term, "$optiions": "i"}})
    search_product = []
    for prod in cursor:
        search_product.append(fix_id(prod))

    return json.dumps(search_product)

# mongo    https://www.mongodb.com

#################################
####### Coupon Codes ###########
#################################


@app.post("/api/coupons")
def save_coupon():
    coupon = request.get_json()
    db.coupons.insert_one(coupon)

    return json.dumps(fix_id(coupon))

@app.get("/api/coupons")
def get_coupons():
    cursor = db.coupons.find({})
    results = []
    for coupon in cursor:
        results.append(fix_id(coupon))
    
    return json.dumps(results)

@app.get("/api/coupons/<code>")
def coupon_code_filter(code):
    coupon = db.coupons.find_one({"code": code})    # find_one will grab a single item vs cursor that grabs many. 
    if coupon == None:
        return abort("Invalid code")
    
    return json.dumps(fix_id(coupon))
    






# def products_by_category(category):
   # cursor = db.products.find({"category": category})
    #results = []
    #for prod in cursor:
        #results.append(fix_id(prod))

    #return json.dumps(results)





# start the server
app.run(debug=True)

# this is a change