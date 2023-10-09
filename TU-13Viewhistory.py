from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import unittest
from selenium.webdriver.support.ui import Select

class Viewhistory(unittest.TestCase):

    def setUp(self):
        # Initialize the Chrome WebDriver
        s = Service('D:\webdriver\chromedriver.exe')
        self.driver = webdriver.Chrome(service=s)

    def tearDown(self):
        # Close the browser
        self.driver.quit()

    def test_Viewhistory_in_Q_Online(self):
        # Open the web application
        self.driver.get("https://online-web-mauve.vercel.app/")
        # คลิกปุ่ม "เข้าสู่ระบบ"
        open_modal_button = self.driver.find_element(By.ID, "loginNavbar")
        open_modal_button.click()
     
        # ระบุ element ของรหัสประจำตัวประชาชนและรหัสผ่านใน Modal
        id_input = self.driver.find_element(By.ID, "LoginID_Card")
        password_input = self.driver.find_element(By.ID, "LoginPassword")

        # กรอกข้อมูลใน input field
        id_input.send_keys("7897895555123")
        password_input.send_keys("123456789")

        # Wait for the search results to load
        time.sleep(5)

        # คลิกปุ่ม "เข้าสู่ระบบ"
        login_button = self.driver.find_element(By.ID, "Login")
        login_button.click()

        time.sleep(4)

        icon = self.driver.find_element(By.ID, 'Home-Queue')
        icon.click()
        time.sleep(5)

        # Select the queue status from the dropdown (e.g., "4" for history)
        queue_status_dropdown = Select(self.driver.find_element(By.XPATH, "//div[@class='col-2']//select[@class='form-select']"))
        queue_status_dropdown.select_by_value("4")
        time.sleep(5)

    def test_Viewhistory_in_Q_Online2(self):
        # Open the web application
        self.driver.get("https://online-web-mauve.vercel.app/")
        # คลิกปุ่ม "เข้าสู่ระบบ"
        open_modal_button = self.driver.find_element(By.ID, "loginNavbar")
        open_modal_button.click()
     
        # ระบุ element ของรหัสประจำตัวประชาชนและรหัสผ่านใน Modal
        id_input = self.driver.find_element(By.ID, "LoginID_Card")
        password_input = self.driver.find_element(By.ID, "LoginPassword")

        # กรอกข้อมูลใน input field
        id_input.send_keys("7897895555123")
        password_input.send_keys("123456789")

        # Wait for the search results to load
        time.sleep(5)

        # คลิกปุ่ม "เข้าสู่ระบบ"
        login_button = self.driver.find_element(By.ID, "Login")
        login_button.click()

        time.sleep(4)

        icon = self.driver.find_element(By.ID, 'Home-Queue')
        icon.click()
        time.sleep(5)

        # Select the queue status from the dropdown (e.g., "4" for history)
        queue_status_dropdown = Select(self.driver.find_element(By.XPATH, "//div[@class='col-2']//select[@class='form-select']"))
        queue_status_dropdown.select_by_value("2")
        time.sleep(5)

if __name__ == "__main__":
        unittest.main()