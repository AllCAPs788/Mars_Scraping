from flask import Flask, render_template, redirect
import pymongo
import scrape_mars
from flask_pymongo import PyMongo 
app = Flask(__name__)
conn = "mongodb://localhost:27017/mars_db"
mongo = PyMongo(app,uri=conn)

@app.route("/")
def index():
    full_data = mongo.db.mars_collection.find_one()
    return render_template("index.html",full_data=full_data)

@app.route("/scrape")
def mongo_scrape():
    final_mars_data= scrape_mars.scrape()
    mongo.db.mars_collection.update({},final_mars_data,upsert=True)

    return redirect("/")
    


if __name__ == "__main__":
    app.run(debug=True)




















