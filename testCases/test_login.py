import os

from pageObjects.LoginPage import LoginPage
from utilities.CustomLoger import  LogGen
from utilities.ReadProperties import ReadConfig


class Test_Login():
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test001_Login(self, setup):
        self.logger.info("******* Starting test_001_login **********")
        self.driver = setup
        self.driver.implicitly_wait(10)
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)

        self.lp.clickLogin()

        self.targetPage = self.lp.productPageExists()
        if self.targetPage == "Products":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir) + "\\screenshots\\" + "test_login001.png")
            self.driver.close()
            assert False