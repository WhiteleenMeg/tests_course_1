from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/explicit_wait2.html"
browser.get(link)
browser.implicitly_wait(5)
WebDriverWait(browser, 15).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'h5#price'), '$100'))
button = browser.find_element(By.CSS_SELECTOR, 'button')
button.click()
# new_window = browser.window_handles[1]
# browser.switch_to.window(new_window)
# confirm = browser.switch_to.alert
# confirm.accept()

x = browser.find_element(By.CSS_SELECTOR, 'span#input_value')
y = calc(x.text)
inp = browser.find_element(By.CSS_SELECTOR, 'input.form-control')
inp.send_keys(y)
button = browser.find_element(By.CSS_SELECTOR, 'button#solve')
button.click()

# file = r'C:\Users\eermo\OneDrive\Рабочий стол\selenium.txt'
# fir.send_keys('Соня')
# sec.send_keys('Ермолаева')
# email.send_keys('e@y.ru')
# forFile.send_keys(file)
# browser.execute_script("return arguments[0].scrollIntoView(true);", button)
time.sleep(10)
browser.quit()
