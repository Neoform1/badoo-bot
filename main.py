from selenium import webdriver
from time import sleep
from secrets import pw


class BadooBot:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        # self.username = username
        self.driver.get("https://badoo.com")
        sleep(2)

        self.driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[3]/div/div[2]/header/div/div[2]/div/div/a")\
            .click()  # login bottom
        sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[3]/section/div/div/div[1]/form/div[1]/div[2]/div/input")\
            .send_keys(username)
        self.driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[3]/section/div/div/div[1]/form/div[2]/div[2]/div/input")\
            .send_keys(pw)
        self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[3]/section/div/div/div[1]/form/div[5]/div/div[1]/button')\
            .click()  # we are logged in
        sleep(6)
        self.driver.find_element_by_xpath("/html/body/div[2]/div[2]/main/div[1]/div/div[1]/section/div/div[2]/div/div[2]/div[1]/div[1]")\
            .click()  # entering like
        sleep(2)
        self.driver.find_element_by_xpath("/html/body/aside/section/div[1]/div/div[2]/div/div[1]")\
            .click()  # enabling showing notification



my_bot = BadooBot('89274448357', pw)