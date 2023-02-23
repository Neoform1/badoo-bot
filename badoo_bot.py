from selenium import webdriver
from time import sleep

from secrets import username, pw


class BadooBot():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get('https://badoo.com')
        sleep(2)

        # fb_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/div[2]/button')
        # fb_btn.click()

        # switch to login popup
        # base_window = self.driver.window_handles[0]
        # self.driver.switch_to_window(self.driver.window_handles[1])

        login_btn = self.driver.find_element_by_xpath(
            "/html/body/div[2]/div[1]/div[3]/div/div[2]/header/div/div[2]/div/div/a")
        login_btn.click()  # login botton
        sleep(2)

        log_in = self.driver.find_element_by_xpath(
            '/html/body/div[2]/div[1]/div[3]/section/div/div/div[1]/form/div[1]/div[2]/div/input')
        log_in.send_keys(username)

        pw_in = self.driver.find_element_by_xpath(
            '/html/body/div[2]/div[1]/div[3]/section/div/div/div[1]/form/div[2]/div[2]/div/input')
        pw_in.send_keys(pw)

        login_btn = self.driver.find_element_by_xpath(
            '/html/body/div[2]/div[1]/div[3]/section/div/div/div[1]/form/div[5]/div/div[1]/button')
        login_btn.click()

        # self.driver.switch_to_window(base_window)

    #     popup_1 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
    #     popup_1.click()
    #
    #     popup_2 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
    #     popup_2.click()
    #
    def like(self):
        like_btn = self.driver.find_element_by_xpath(
            '/html/body/div[2]/div[1]/main/div[1]/div/div[1]/section/div/div[2]/div/div[2]/div[1]/div[1]')
        like_btn.click()

    # def super_like(selfself):
    #     super_like = self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/main/div[1]/div/div[1]/section/div/div[2]/div/div[3]/div[1]')
    #     super_like.click()
    # function for some money

    def dislike(self):
        dislike_btn = self.driver.find_element_by_xpath(
            '/html/body/div[2]/div[1]/main/div[1]/div/div[1]/section/div/div[2]/div/div[2]/div[2]/div[1]')
        dislike_btn.click()

    def auto_swipe(self):
        while True:
            sleep(0.5)
            try:
                self.like()
            except Exception:
                try:
                    self.close_popup()
                except Exception:
                    self.close_match()

    def close_popup(self):
        popup = self.driver.find_element_by_xpath('/html/body/aside/section/div[1]/div/div/section/div/div/div/div[1]/div')
        popup.click()

    # def close_popup_2(self):
    #     popup_2 = self.driver.find_element_by_xpath('/html/body/aside/section/div[1]/div/div[3]/div[2]/span')
    #     popup_2.click()

    def close_match(self):
        match_popup = self.driver.find_element_by_xpath('/html/body/aside/section/div[1]/div/div[2]/i')
        match_popup.click()


bot = BadooBot()
bot.login()
