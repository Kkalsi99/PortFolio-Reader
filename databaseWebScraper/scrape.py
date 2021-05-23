from selenium import webdriver
from selenium.webdriver.common.keys import Keys
PATH = "/media/kghost/study/Portfolio_Tracker/databaseWebScraper/chromedriver_linux64/chromedriver"
driver = webdriver.Chrome(PATH)
driver.get("https://www.google.com")
