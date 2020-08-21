# Web Checker allows you to monitor websites and notify you when a change has been made.
# This is done by checking only the HTML that you want to check, for example:

# <body>
#        <div>
#            <h1>Some Title</h1>
#            <h2>Price: $99.99</h2>
#        </div>
#    </body>


# If you only wanted to check the H2 for the price, web checker would allow you to do so.

import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

page = 'https://trjones.dev'

c_options = Options()
c_options.add_argument('--headless')
c_options.add_argument('--window-size=1920x1080')

c_driver = webdriver.Chrome(options=c_options, executable_path="chromedriver.exe")

c_driver.get(page)
elem = c_driver.find_element_by_id('banner')

# Check for change on the following
## Text content
## Attribute(s)
## Placement

print(elem.text)