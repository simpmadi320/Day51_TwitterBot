from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

Download_Down = 500
Download_Up = 30

CHROM_DRIVER_PATH = "/"


username = "simpmadi3226132"
password = "FakePassword!1234"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://twitter.com/home")

username_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='text']")))
username_input.send_keys(username)

# Find the button element by its role attribute
buttons = driver.find_elements(By.XPATH, "//div[contains(@class, 'css-175oi2r') and @role='button']")
buttons[2].click()

password_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='password']")))
password_input.send_keys(password)

password_button = driver.find_elements(By.XPATH, "//div[contains(@class, 'css-175oi2r') and @role='button']")
password_button[2].click()

#div_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='css-175oi2r r-xoduu5 r-xyw6el r-13qz1uu r-mk0yit']")))
time.sleep(5)

tweet_compose = driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div')
tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
tweet_compose.send_keys(tweet)
#div_element.click()

#text_entry = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//span[@data-text='true']")))
#text_entry.send_keys("TEST")
