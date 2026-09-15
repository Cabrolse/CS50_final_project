import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def main():
    driver = webdriver.Chrome()
    
    driver.get("https://www.vinted.com")
    
    search_box = driver.find_element(By.ID, "search_text")
    
    search_box.send_keys("blue shirt" + Keys.RETURN)
    input("Press Enter in your terminal to close browser...")
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