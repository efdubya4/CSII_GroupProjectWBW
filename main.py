from flask import Flask, render_template, request, jsonify
from replit import db
import json

#keeps track of homes submitted to database 

def get_entries():
  global entries
  entries = 0
  num_key = 0
  for key in db:
    num_key+=1

  if key == 0:
    db["house_listings"] = {}

    
  for entry in db["house_listings"]:
    entries += 1


app = Flask(__name__)
get_entries()


@app.route("/", methods=["GET"])
@app.route("/home", methods=["GET"])
def home_page():
    return render_template('home.html')

@app.route("/list", methods=["POST", "GET"])
def list_homes():
    # data = request.data
    # data = json.loads(data)
    if request.method == "POST":
      seller_name = request.form.get("seller_name")
      location = request.form.get("location")
      area = request.form.get("areas")
      price = request.form.get("price")
      bedrooms = request.form.get("bedrooms")
      bathrooms = request.form.get("bathrooms")
      image = request.form.get("image")
  
      # adding data to database
      entry_name = "entry" + str(entries + 1)
      db["house_listings"][entry_name] = {'name': seller_name, 
        'location': location,
        'area': area, 
        'price': price,
        'num_bedrooms': bedrooms,
        'num_bathrooms': bathrooms,
        'image': image
        }
      
      return "Thank you " + seller_name + ", your house has been listed!"
    return render_template('list.html')
  
@app.route("/find", methods=["GET"])
def display_homes():
  listed_homes = db["house_listings"]

  return render_template('display_homes.html', len=len(listed_homes), listed_homes = listed_homes)


app.run(host='0.0.0.0')