# import necessary libraries
from flask import Flask, render_template

# create instance of Flask app
app = Flask(__name__)


# create route that renders index.html template
@app.route("/scrape")
def scrape():
    import pandas as pd
    from splinter import Browser
    from bs4 import BeautifulSoup
    from webdriver_manager.chrome import ChromeDriverManager

    # Setup splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    html = browser.html

    news_url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    browser.visit(news_url)
    #soup = BeautifulSoup(html, 'html.parser')

        # HTML object

    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')
    # Retrieve all elements that contain book information
    article_title = soup.find(class_='content_title')
    article_text = soup.find(class_='article_teaser_body')


    print(article_title)
    print(article_text)

    image_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(image_url)
    soup = BeautifulSoup(html, 'html.parser')

    image = soup.find('li',class_='slide')

    print(image)

    facts_url = 'https://space-facts.com/mars/'
    browser.visit(facts_url)
    soup = BeautifulSoup(html, 'html.parser')

    table = soup.find(id='tablepress-p-mars-no-2')
    print(table)

    hemisphere_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(hemisphere_url)
    soup = BeautifulSoup(html, 'html.parser')

    hemisphere_image_urls = [
        {"Valles": "Valles Marineris Hemisphere", src="/cache/images/4e59980c1c57f89c680c0e1ccabbeff1_valles_marineris_enhanced.tif_thumb.png"},
        {"title": "Cerberus Hemisphere", src="/cache/images/39d3266553462198bd2fbc4d18fbed17_cerberus_enhanced.tif_thumb.png"},
        {"title": "Schiaparelli Hemisphere", src="/cache/images/08eac6e22c07fb1fe72223a79252de20_schiaparelli_enhanced.tif_thumb.png"},
        {"title": "Syrtis Major Hemisphere", src="/cache/images/55a0a1e2796313fdeafb17c35925e8ac_syrtis_major_enhanced.tif_thumb.png"}]


    browser.quit()


if __name__ == "__main__":
    app.run(debug=True)