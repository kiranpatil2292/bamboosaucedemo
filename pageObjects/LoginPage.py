import os.path

from selenium.webdriver.common.by import By


class LoginPage():
    txt_username_xpath = "//input[@id='user-name']"
    txt_password_xpath = "//input[@id='password']"
    btn_login_xpath = "//input[@id='login-button']"
    msg_ProductPage_xpath = "//span[@class='title']"

    errorMsg_LoginFail_xpath = "//h3[@data-test='error']"

    def __init__(self, driver):
        self.driver = driver

    def setUsername(self, username):
        self.driver.find_element(By.XPATH, self.txt_username_xpath).send_keys(username)

    def setPassword(self, pwd):
        self.driver.find_element(By.XPATH, self.txt_password_xpath).send_keys(pwd)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.btn_login_xpath).click()

    def productPageExists(self):
        try:
            return self.driver.find_element(By.XPATH, self.msg_ProductPage_xpath).text
        except:
            return False

    def displayErrorMsg(self):
        try:
            return self.driver.find_element(By.XPATH, self.errorMsg_LoginFail_xpath).text
        except:
            return None
