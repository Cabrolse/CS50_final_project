import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def main():
    options = Options()
    options.add_argument("user-data-dir=./vinted_profile")
    
    driver = webdriver.Chrome(options=options)
    
    driver.get("https://www.vinted.com")
    
    print("Bringing you to Vinted......")
    
    search_box = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "search_text")))
    
    search_box.clear()
    
    search_box.send_keys("blue shirt" + Keys.RETURN)
    print("I searched for Blue tshirt")
    
    
    input("\nIf not logged in, log in manually now. Press ENTER when done to exit...")
    driver.quit()
    
    
    """ if len(sys.argv) > 1 and sys.argv[1] == "listing":
    listing()



def listing():
    print("Please enter the following details of your new listing")
    
    #user enters details of items which are then saved in unique variables
    img()
    name()
    price()
    
def img():
    img = input("Images of item: ")

def name():
    name = input("Name of your Item here: ")
    if name == "":
        name()
    
def price():
    price = input("Price: ")
    if price.isAlpha():
        price()
            
         """   
    
    
    
    
    
    


main()

"""
program will auto list items for users through a few simplie prompts
will tell user the number of items that have sold and how much money they have made
"""