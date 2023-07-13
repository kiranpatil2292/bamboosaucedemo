from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class CartPage():
    cart_link_xpath = "//a[@class='shopping_cart_link']"

    but_ContShop_xpath = "//button[@id='continue-shopping']"
    pd_SacLaBone_xpath = "//div[normalize-space()='Sauce Labs Onesie']"
    cartAdd_SacLaBone_xpath = "//button[@id='add-to-cart-sauce-labs-onesie']"
    but_checkout_xpath = "//button[@id='checkout']"
    confMsg_checkout_xpath = "//span[@class='title']"
    drp_pd_sort_container = "//select[@class='product_sort_container']"
    cart_Link_xpath="//span[@class='shopping_cart_badge']"

    def __init__(self, driver):
        self.driver = driver

    def clickSauceLabOneSie(self):
        self.driver.find_element(By.XPATH, self.pd_SacLaBone_xpath).click()

    def clickAddCartSauceLab(self):
        self.driver.find_element(By.XPATH,self.cartAdd_SacLaBone_xpath).click()

    def clickCartLink(self):
        self.driver.find_element(By.XPATH,self.cart_link_xpath).click()

    def clickCheckOut(self):
        self.driver.find_element(By.XPATH, self.but_checkout_xpath).click()

    def seleDropOpt(self):
        Product_sort = Select(self.driver.find_element(By.XPATH, self.drp_pd_sort_container))
        Product_sort.select_by_visible_text("Price (low to high)")

