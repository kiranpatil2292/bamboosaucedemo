import os
import time

from pageObjects.LoginPage import LoginPage
from utilities.CustomLoger import LogGen
from utilities.ReadProperties import ReadConfig


class Test_Invalid_Login():
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_invalid_Login(self, setup):
        self.logger.info("******* Starting test_invalid_login **********")
        self.driver = setup
        self.driver.implicitly_wait(10)
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUsername("locked_out_user")
        self.lp.setPassword(self.password)

        self.lp.clickLogin()
        time.sleep(4)

        self.targetPage = self.lp.displayErrorMsg()
        if self.targetPage == "Epic sadface: Sorry, this user has been locked out.":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir) + "\\screenshots\\" + "test_InvalidLogin.png")
            self.driver.close()
            self.logger.info("*** user should not be loged successfully ***")
            assert False
