from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.ui import Select


# ระบุพาธของ ChromeDriver 
chrome_driver_path = "C:\\Users\\siwak\\python\\chromedriver.exe"


# เริ่มต้น WebDriver
driver = webdriver.Chrome()
# ขยายหน้าต่างเบราว์เซอร์ให้เต็มหน้าจอ
driver.maximize_window()

# เปิดเว็บไซต์ของคุณ
driver.get("https://online-web-mauve.vercel.app/")

# คลิกปุ่ม "เข้าสู่ระบบ"
open_modal_button = driver.find_element(By.XPATH, "//span[text()='เข้าสู่ระบบ']")
open_modal_button.click()

# ระบุ element ของรหัสประจำตัวประชาชนและรหัสผ่านใน Modal
id_input = driver.find_element(By.XPATH, "//label[text()='รหัสประจำตัวประชาชน']/following-sibling::input")
password_input = driver.find_element(By.XPATH, "//label[text()='รหัสผ่าน']/following-sibling::input")

# กรอกข้อมูลใน input field
id_input.send_keys("7897895555123")
password_input.send_keys("123456789")

time.sleep(2)

# คลิกปุ่ม "เข้าสู่ระบบ" ด้วย XPath
login_button = driver.find_element(By.XPATH, "//button[text()='เข้าสู่ระบบ']")
login_button.click()

# รอสักครู่เพื่อให้หน้าเว็บโหลดและดำเนินการต่อ
time.sleep(5)  # รอ 5 วินาที (หรือตามที่คุณต้องการ)


# คลิกปุ่ม "รายการจองคิว" โดยใช้ XPath
queue_list_button = driver.find_element(By.XPATH, "//h4[text()='รายการจองคิว']")
queue_list_button.click()

time.sleep(2)

# คลิกเพื่อเปิดกล่องเลือกวันที่
date_input = driver.find_element(By.XPATH, "//input[@type='date']")
date_input.click()

# รอสักครู่เพื่อให้กล่องเลือกวันที่เปิด
time.sleep(2)

# ใช้ send_keys() เพื่อป้อนวันที่ที่คุณต้องการ
date_input.send_keys("11-20-2023")  # เปลี่ยนเป็นวันที่ที่คุณต้องการ
time.sleep(5)



queue_status_dropdown = Select(driver.find_element(By.XPATH, "//div[@class='col-2']//select[@class='form-select']"))

# เลือกคิวที่คุณต้องการ (เช่น "คิวที่จอง") ( "1" คิวที่จอง ) ("2" คิวที่กำลังดำเนินการ ) ("4"  ประวัติการจองคิว )
queue_status_dropdown.select_by_value("4")

time.sleep(4)
