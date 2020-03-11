# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 19:50:25 2020

@author: p_pat
"""

# Dependencies
import pandas as pd
import time as time
import numpy as np
import requests
from flask import Flask, jsonify
import flask
import scrape_mars


#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################
# Display routes
@app.route('/routes')
def routes():
    """List of all available api routes."""
    return (
        f"Available Routes:<br>"
        f"/routes<br>"
        f"/scrape"
    )
# end def routes()

@app.route("/scrape")
def scrape():
    try:
        if scrape_mars.populate_mars_db() == 200:
            mars_data = scrape_mars.get_mars_data_from_db()

            # Return the template with the teams list passed in
            return render_template("index.html", 
                    news_title=mars_data[0]["news_title"],
                    news_p=mars_data[0]["news_p"],
                    featured_image_url=mars_data[0]["featured_image_url"],
                    mars_weather=mars_data[0]["mars_weather"],
                    mars_table=mars_data[0]["mars_table"],
                    hem1_name=mars_data[0]["hemisphere_image_urls"][0]["title"],
                    hem1_image=mars_data[0]["hemisphere_image_urls"][0]["img_url"],
                    hem2_name=mars_data[0]["hemisphere_image_urls"][1]["title"],
                    hem2_image=mars_data[0]["hemisphere_image_urls"][1]["img_url"],
                    hem3_name=mars_data[0]["hemisphere_image_urls"][2]["title"],
                    hem3_image=mars_data[0]["hemisphere_image_urls"][2]["img_url"],
                    hem4_name=mars_data[0]["hemisphere_image_urls"][3]["title"],
                    hem4_image=mars_data[0]["hemisphere_image_urls"][3]["img_url"])
        else:
            print("There was a problem scraping data from NASA. Please try again later.")
        # end if

    except Exception as e:
        print(e)
# end def scrape()
        
@app.route('/')
def index():
    return scrape()
# end def index()



if __name__ == '__main__':
    app.run(debug=False)