from flask import Flask
import json
from about import me

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


# start the server
app.run(debug=True)


app.run(debug=True)