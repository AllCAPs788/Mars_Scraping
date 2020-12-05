# import necessary libraries

import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager



# create route that renders index.html template

def scrape():
    

    # Setup splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    html = browser.html

    news_url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    browser.visit(news_url)
    #soup = BeautifulSoup(html, 'html.parser')
    html = browser.html
    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')

       
    # Retrieve all elements that contain book information
    article_title = soup.find(class_='content_title')
    article_text = soup.find(class_='article_teaser_body')


    print(article_title)
    print(article_text)

    image_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(image_url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    image = soup.find('img',class_='thumb')

    print(image)

    facts_url = 'https://space-facts.com/mars/'
    browser.visit(facts_url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    tables = pd.read_html(facts_url)
    tables

    hemisphere_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(hemisphere_url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    h3_loop = soup.find_all('h3')

    h3_list = []
    for x in h3_loop:
        h3_list.append(x.text)
        
    print(h3_list)
    hemisphere_image_urls = []

    for x in h3_list:
        

        
        mars_dict = {}
        browser.click_link_by_partial_text(x)
        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')
        mars_title = soup.find('h2', class_="title")
        sample_1 = soup.find('img',class_="wide-image")
                
        print(sample_1['src'])           
        mars_dict['title']=mars_title.text
        mars_dict['image_url']=sample_1['src']
        
        hemisphere_image_urls.append(mars_dict)
        browser.back()
    browser.quit()

    return mars_dict

    
if __name__ == "__main__":
    app.run(debug=True)