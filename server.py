from flask import Flask, abort, render_template, request
from mock_data import mock_data
from flask_cors import CORS
from config import db, json_parse
import json
from bson import ObjectId

app = Flask(__name__)
CORS(app) # allow anyone to call the server(**DANGER**)




coupon_codes=[
    {
        "code": "october21",
        "discount": 10  
    }
]

me = {
    "name": "Krystle",
    "last": "Berry",
    "email": "krystle.monet@gmail.com",
    "age": 35,
    "hobbies": [],
    "address": {
        "street": "Old Cropps",
        "City": "Fredericksburg"
    }
}

@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/test")
def test():
    return "Hello there!"

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/about/email")
def email():
    return me["email"]

@app.route("/about/address")
def address():
    return me["address"]

##################################################
################## API Methods
##################################################

@app.route("/api/catalog", methods=["get"])
def get_catalog():
    #returns the catalog as JSON string
    cursor = db.products.find({}) #find with no filter = get all data in the collection
    catalog = []
    for prod in cursor:
        catalog.append(prod)
    
    print( len(catalog), "Record obtained from db")

    return json_parse(catalog) #error

@app.route("/api/catalog", methods=["post"])
def save_product():
    #get request payload(body)
    product = request.get_json()

    ##data validation
    #1 title exist and is longer than 5 chars
    
    ##validate that title exist in the dict, if not abort(400)
    if not 'title' in product or len(product["title"]) < 5: #comparing length so needed len
        return abort(400, "Title is required, and should contain at least 5 char") #400 = bad request

    ##validate that the price exist and is greater than 0 
    if not 'price' in product:
        return abort(400, "Price is required")

    if not isinstance(product["price"], float) and not isinstance(product["price"], int):
        return abort(400, "Price should a valid number")

    if product['price'] <= 0:
        return abort(400,"Price should be greater than 0")

    #save the product
    #mock_data.append(product)
    #product["_id"] = len(product["title"])
    db.products.insert_one(product)

    #return the saved object
    return json_parse(product)


@app.route("/api/categories")
def get_categories():
    #return the list (string) of Unique categories
    categories = []
    #get all prods from the db into a cursor

    cursor = db.products.find({})
    #get iterate over the cusor instead of mock_data
    for prod in cursor:
        if not prod["category"] in categories:
            categories.append(prod["category"])
            
    #logic
    return json_parse(categories)

@app.route("/api/product/<id>")
def get_product(id):
    product = db.products.find_one({"_id": ObjectId(id)})
    if not product:
        return abort(404) # 404 = Not Found
    
    return json_parse(product)

#/api/catalog/<category>
@app.route("/api/catalog/<category>")
def get_by_catalog(category):
    #mongo to search case insensitive we use Regular Expressions
    cursor = db.products.find({"category": category})
    list = []
    for prod in cursor:
        list.append(prod)

    return json_parse(list)

#/api/cheapest
@app.route("/api/cheapest")
def get_cheapest():
    cursor = db.products.find({})
    pivot = cursor[0]
    if prod in cursor:
        if prod["price"] < pivot["price"]:
            pivot = prod

    return json_parse(pivot)

###########################################
############# Coupon Codes ################
###########################################

#Post to /api/couponCodes
@app.route("/api/couponCodes", methods = ["POST"])
def save_coupon():
    coupon = request.get_json()

    #validations
    if not 'couponCode' in product or len(product["couponCode"]) < 5: #comparing length so needed len
        return abort(400, "Coupon is required, and should contain at least 5 char") #400 = bad request

    #save
    db.couponCode.insert_one(coupon)
    return json_parse(cp)


#Get to /Api/couponCodes
@app.route("/api/couponCodes", methods=["GET"])
def get_coupons():
    cursor = db.coupon_codes.find({})
    all_coupons= []
    for cp in cursor:
        all_coupons.append(cp)

    return json_parse(coupon_codes)

#get coupon by its code or 404
@app.route("/api/couponCodes/<code>")
def get_coupon_by_code(code):
    coupon = db.couponCodes.find_one({"code": code})
    if coupon is None:
        return abort(404, "Invalid coupon code")

    return json_parse(coupon)

@app.route("/test/onetime/filldb")
def fill_db():
    #iterate the mock_data list
    for prod in mock_data:
    #save every object to db.product
        prod.pop("_id") #remove the _id from the dict/product
        db.products.insert_one(prod)

    return "Done!"


#start the server
#debut true will restart the server automatically 
app.run(debug = True)

