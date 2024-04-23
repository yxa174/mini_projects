import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def work_cite():
    try:
        time.sleep(100)
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("http://192.168.1.1")
        time.sleep(7)
    
        textarea = driver.find_element(By.CSS_SELECTOR, ".text-text.password-text.password-hidden")
        textarea.send_keys("admin123")
        time.sleep(1)

        password_inputs = driver.find_elements(By.CSS_SELECTOR, 'input[type="password"].text-text.password-text.password-hidden')

        if len(password_inputs) >= 2:
            textarea1 = password_inputs[1]
        else:
            print("Недостаточно совпадающих элементов")
        textarea1.send_keys("admin123")
        time.sleep(1)

        checkbox_label = driver.find_element(By.CLASS_NAME, 'checkbox-label')
        checkbox_label.click()
        time.sleep(1)

        button_element = driver.find_element(By.XPATH, '//a[@class="button-button" and @title="Приступим к работе"]')
        # Perform actions on the button element, such as clicking on it
        button_element.click()
        time.sleep(5)
        ##############################################################################

        time.sleep(3)
        element = driver.find_element(By.CSS_SELECTOR, '.page-content-container.su-scroll.ps.ps--active-y')
        driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight;", element)

        time.sleep(1)

        button_element = driver.find_element(By.XPATH, '//a[@class="button-button" and @title="ДАЛЕЕ"]')
        button_element.click()
        time.sleep(1)

        element = driver.find_element(By.XPATH, '//a[@class="button-button" and @title="ДА"]')
        element.click()
        time.sleep(3)

        element1 = driver.find_elements(By.XPATH, '//a[@class="button-button" and @type="button" and @title="ДАЛЕЕ"]')
        if len(element1) >= 2:
            dalee = element1[1]
        else:
            print("Недостаточно совпадающих элементов")
        dalee.click()
        time.sleep(3)
        driver.quit()
        time.sleep(20)
    except:
        driver.quit()
        print("Ошибка браузера")
while True:
    try:
        
            time.sleep(10)
            s = requests.get('http://ya.ru')
            s1 = requests.get('http://192.168.1.1')

            if s.status_code == 200 and s1.status_code == 200:
                work_cite()
            else:      
                print("Нет сети")
                continue
    except requests.exceptions.RequestException as e:
        print("Нет сети")

# s = requests.get('http://ya.ru')
# print(s.status_code)