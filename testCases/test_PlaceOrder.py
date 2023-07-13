import os
import time

import pytest

from pageObjects.CartPage import CartPage
from pageObjects.CheckOutPage import CheckOutPage
from pageObjects.LoginPage import LoginPage
from utilities.CustomLoger import LogGen
from utilities.ReadProperties import ReadConfig


class Test_BillingAmountOfOrderedProduct():
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.Regression
    def test_Billing_priceOfOrdered_product(self, setup):
        self.logger.info("**** started test_Billing_priceOfOrdered_product ****")
        self.driver = setup
        self.driver.implicitly_wait(10)
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.logger.info("***** browser is initializing *****")
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("***** successfully logged into product page *****")
        self.cp = CartPage(self.driver)
        self.cp.seleDropOpt()

        self.logger.info("**** sorting the product ****")
        self.cp.clickSauceLabOneSie()
        self.cp.clickAddCartSauceLab()

        self.cp.clickCartLink()
        self.cp.clickCheckOut()
        self.logger.info("**** clicking on checkout button ***")
        self.co = CheckOutPage(self.driver)
        self.co.setFirstName('John')
        self.co.setLastName('Doe')
        self.co.setPostalCode('123')
        self.co.clickContinueBt()
        self.logger.info("**** adding input to the checkoutPage ")
        # self.co.scroll_action_price_ele()
        self.targetPage = self.co.ConfMsgTotalPrice()
        time.sleep(4)
        if self.targetPage == "$7.99":
            assert True
            self.logger.info("**** successfully billing amount is verified ****")
            self.co.clickFinishBt()
            self.targetPage= self.co.confMsgOrderSuc()
            if self.targetPage=="Thank you for your order!":
                time.sleep(4)
                assert True
                self.driver.close()
            else:
                self.driver.save_screenshot(os.path.abspath(os.curdir) + "\\screenshots\\" + "order_Fail.png")
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir) + "\\screenshots\\" + "price_amount.png")

            time.sleep(4)
            self.driver.close()
            self.logger.info("**** price amount is not successfully verified ****")

            assert False
