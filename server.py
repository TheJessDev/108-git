from flask import Flask
import json
from about import me
from data import mock_data

app = Flask(__name__) # create an instance of Flask class

#### WEB SERVER #####
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







    



# start the server
app.run(debug=True)

# this is a change