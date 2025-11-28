from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)
    
    def visit (self, url):
        self.driver.get(url)

    def find(self, by, locator):
        return self.wait.until(EC.visibility_of_element_located((by, locator)))
    
    def click(self, by, locator):
        cl = self.find(by, locator)
        cl.click()
    
    def type(self, by, locator, text):
        ty = self.find(by, locator)
        ty.clear()
        ty.send_keys(text)

    def get_text(self, by, locator):
        return self.wait.until(EC.visibility_of_element_located((by, locator))).text