from selenium.webdriver.common.by import By

from selenium.webdriver.support.select import Select


class Requirement:
    def __init__(self, driver):
        self.driver = driver
        # User Information
        self.user_id_xpath = "//input[@id='stripes-1421210197']"
        self.pswrd_xpath = "//input[@name='password']"
        self.reapet_pswrd_xpath = "//input[@name='repeatedPassword']"
        # Account Information
        self.frst_name_xpath = "//input[@name='account.firstName']"
        self.last_name_xpath = "//input[@name='account.lastName']"
        self.email_xpath = "//input[@name='account.email']"
        self.phone_xpath = "//input[@name='account.phone']"
        self.add_1_xpath = "//input[@name='account.address1']"
        self.add_2_xpath = "//input[@name='account.address2']"
        self.city_xpath = "//input[@name='account.city']"
        self.state_xpath = "//input[@name='account.state']"
        self.zip_xpath = "//input[@name='account.zip']"
        self.counry_xpath = "//input[@name='account.country']"
        self.drp_down_xpath = "//select[@name='account.languagePreference']"
        self.drp_down2_xpath = "//select[@name='account.favouriteCategoryId']"
        self.checkbox1_xpath = "//input[@name='account.listOption']"
        self.checkbox2_xpath = "//input[@name='account.bannerOption']"
        self.save_btn_xpath = "//input[@name='newAccount']"

    # User Information
    def user_id(self):
        self.driver.find_element(By.XPATH, self.user_id_xpath).send_keys("hariom12")

    def password(self):
        self.driver.find_element(By.XPATH, self.pswrd_xpath).send_keys("hariom@123")

    def repeat_password(self):
        self.driver.find_element(By.XPATH, self.reapet_pswrd_xpath).send_keys("hariom@123")
        # Account Information

    def first_name(self):
        self.driver.find_element(By.XPATH, self.frst_name_xpath).send_keys("hari")

    def lst_name(self):
        self.driver.find_element(By.XPATH, self.last_name_xpath).send_keys("om")

    def email(self):
        self.driver.find_element(By.XPATH, self.email_xpath).send_keys("hariomkumararya270799@gmail.com")

    def phone(self):
        self.driver.find_element(By.XPATH, self.phone_xpath).send_keys("09917393992")

    def address1(self):
        self.driver.find_element(By.XPATH, self.add_1_xpath).send_keys("BADHERI")

    def address2(self):
        self.driver.find_element(By.XPATH, self.add_2_xpath).send_keys("BADHERI")

    def city(self):
        self.driver.find_element(By.XPATH, self.city_xpath).send_keys("mzn")

    def state(self):
        self.driver.find_element(By.XPATH, self.state_xpath).send_keys("UP")

    def zip(self):
        self.driver.find_element(By.XPATH, self.zip_xpath).send_keys("251307")

    def country(self):
        self.driver.find_element(By.XPATH, self.counry_xpath).send_keys("INDIA")

    def drop_down1(self):
        Select(self.driver.find_element(By.XPATH, self.drp_down_xpath)).select_by_visible_text("english")

    def drop_down2(self):
        Select(self.driver.find_element(By.XPATH, self.drp_down2_xpath)).select_by_visible_text("FISH")

    def checkbox1(self):
        self.driver.find_element(By.XPATH, self.checkbox1_xpath).click()

    def checkbox2(self):
        self.driver.find_element(By.XPATH, self.checkbox2_xpath).click()

    def save_btn(self):
        self.driver.find_element(By.XPATH, self.save_btn_xpath).click()
