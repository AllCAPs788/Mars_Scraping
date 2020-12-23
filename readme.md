# Mars Scraping #

Using Splinter and Chrome Development Manager tools, this project goes through various NASA websites and pulls specific information via web scraping techniques. That information is then compiled into a web API. 

### NASA Mars News

Found the most recent article title and text using splinter for the following url: 
### Mars Images
Found the featured full-scale image for this url. 
### Mars Facts
From the Mars hemispheres page, I pulled each hemisphere page. 
## Flask Application
All of the aboved information is then compiled into a Python dictionary into a document called scrape_mars.py, which also contains a function to run that dictionary. 

Then, in app.py, that scrape function is initialized to display the compiled information onto a web application. 