
import time
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
binary = FirefoxBinary('/Applications/Firefox.app/Contents/MacOS/firefox-bin')

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox(firefox_binary=binary)




# class Ayu:
#     def __init__(self):
#         self.age = 10
#         self.hair_color = "brown"
#         self.name = "Ayu Tskukimia"
#
#     def reverse_tanjoubi(self, number_of_years):
#         self.age -= number_of_years
#         print("Happy Birthday! You are " + str(self.age) + " years old!")
#
# def test():
#     ayu = Ayu()
#
#     while ayu.age > 0:
#         ayu.reverse_tanjoubi(2)
#         if 5.0 == 5:
#             print("AAAH")
#
#     def fuck_the_loli(name="Ayu", enjoying_it=True):
#         print(name + ": ONII CHAN!!!")
#         if enjoying_it:
#             print("DON'T STOP!")
#         else:
#             print("YAMETE!!!!")
#
#     ayu.reverse_tanjoubi(2)
#
#     fuck_the_loli("Kobato", False)
#     fuck_the_loli("Ayu", True)
#     fuck_the_loli(enjoying_it=False)
#
driver.get("https://google.com")

driver.find_element_by_id("lst-ib").send_keys("hello")



browser = webdriver.Firefox()
browser.get('http://www.google.com')

search = browser.find_element_by_name('q')
search.send_keys("ayu")
search.send_keys(Keys.RETURN) # hit return after you enter search text
time.sleep(10) # sleep for 5 seconds so you can see the results
browser.quit()

# time.sleep(10)

driver.quit()
