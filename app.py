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




















# from flask import Flask, render_template
# import pymongo
# import scrape_mars

# app = Flask(__name__)

# # setup mongo connection
# conn = "mongodb://localhost:27017"
# client = pymongo.MongoClient(conn)

# # connect to mongo db and collection
# db = #new mongo name client.store_inventory
# produce = db.produce



# @app.route("/scrape")
# def scrape():
#     import pandas as pd
#     from splinter import Browser
#     from bs4 import BeautifulSoup
#     from webdriver_manager.chrome import ChromeDriverManager

#     # Setup splinter
#     executable_path = {'executable_path': ChromeDriverManager().install()}
#     browser = Browser('chrome', **executable_path, headless=False)
#     html = browser.html

#     news_url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
#     browser.visit(news_url)
#     #soup = BeautifulSoup(html, 'html.parser')
#     html = browser.html
#     # Parse HTML with Beautiful Soup
#     soup = BeautifulSoup(html, 'html.parser')

       
#     # Retrieve all elements that contain book information
#     article_title = soup.find(class_='content_title')
#     article_text = soup.find(class_='article_teaser_body')


#     print(article_title)
#     print(article_text)

#     image_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
#     browser.visit(image_url)
#     html = browser.html
#     soup = BeautifulSoup(html, 'html.parser')

#     image = soup.find('img',class_='thumb')

#     print(image)

#     facts_url = 'https://space-facts.com/mars/'
#     browser.visit(facts_url)
#     html = browser.html
#     soup = BeautifulSoup(html, 'html.parser')

#     tables = pd.read_html(facts_url)
#     tables

#     hemisphere_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
#     browser.visit(hemisphere_url)
#     html = browser.html
#     soup = BeautifulSoup(html, 'html.parser')

#     h3_loop = soup.find_all('h3')

#     h3_list = []
#     for x in h3_loop:
#         h3_list.append(x.text)
        
#     print(h3_list)
#     hemisphere_image_urls = []

#     for x in h3_list:
        

        
#         mars_dict = {}
#         browser.click_link_by_partial_text(x)
#         html = browser.html
#         soup = BeautifulSoup(html, 'html.parser')
#         mars_title = soup.find('h2', class_="title")
#         sample_1 = soup.find('img',class_="wide-image")
                
#         print(sample_1['src'])           
#         mars_dict['title']=mars_title.text
#         mars_dict['image_url']=sample_1['src']
        
#         hemisphere_image_urls.append(mars_dict)
#         browser.back()
#     browser.quit()



#     # write a statement that finds all the items in the db and sets it to a variable
#     inventory = list(produce.find())
#     print(inventory)

#     # render an index.html template and pass it the data you retrieved from the database
#     return render_template("index.html", inventory=inventory)


# if __name__ == "__main__":
#     app.run(debug=True)