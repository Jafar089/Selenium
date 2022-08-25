from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
driver = webdriver.Chrome(ChromeDriverManager().install())



driver.get("https://www.hugedomains.com/")
time.sleep(2)
driver.get("https://google.com/")
time.sleep(2)
driver.back()
driver.forward()





# is_displayed
# driver.get("https://google.com/")
# var = driver.find_element_by_class_name('gNO89b')
# print(var.is_displayed())





# is_enabled
# driver.get("https://google.com/")
# var2 = driver.find_element_by_name('btnK')
# print(var2.is_enabled())





# is_selected
# driver.get("https://www.w3schools.com/html/html_forms.asp")
# var = driver.find_element_by_id('html')
# print(var.is_selected())

# driver.get("https://www.w3schools.com/html/html_forms.asp")
# var = driver.find_element_by_name('fav_language')
# print(var.is_selected())





# implicit wait and explicit wait
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# driver.get("https://masterprograming.com/")
# try:
#     element = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.ID, "site-navigation"))
#     )
#     print("Jab Website Ka Navigation Load Ho Gaya To Me Exit Ho Gaya Hu.... hahaha ")
# finally:
#     driver.quit()





# input button etc
# driver.get("https://google.com/")
# # go to google search bar and type this text
# name = driver.find_element_by_name('q')
# name.send_keys('Meaning of Jafar in islam')
# time.sleep(2)
# # press search button to search your text
# from selenium.webdriver.common.keys import Keys
# name.send_keys(Keys.ENTER)


# driver.get("https://myislam.org/surah-fatiha/")
# time.sleep(5)
# path = driver.find_element_by_xpath('//*[@id="post-4645"]/div/div/div/div[1]/div[2]/div/div/div/div[2]/div[1]/span[1]')
# path.click()


driver.quit()
