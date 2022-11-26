from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

import time

driver = Chrome("drivers/chromedriver")


driver.get("https://www.house.kg/")
time.sleep(5)
button = driver.find_element(
    By.XPATH,  
    '//*[@id="homepage"]/header/div/div[2]/ul/li[2]/a'
)
button.click()
time.sleep(5)

# Поиск в house.kg
# search = driver.find_element(By.XPATH, '//*[@id="quick-search-fake-form"]/div[1]/input' )
# text = input("Введите текст поиска: ")
# search.send_keys(text)
# search.submit()

# option = driver.find_element(By.XPATH, '//*[@id="homepage"]/div[7]/div[2]/div[1]/div[3]/form/div[1]/div[2]/div/button/div/div/div').click()
# time.sleep(2)
# choice = driver.find_element(By.XPATH,'//*[@id="bs-select-2-1"]/span[2]').click

title = driver.find_element(By.XPATH, '//*[@id="homepage"]/div[7]/div[2]/div[1]/div[6]/div[1]/div[2]/div[1]/div[1]/p[1]/a')

posts = driver.find_elements(By.CLASS_NAME, 'listing')
for post in posts:
    title = post.find_element(By.CLASS_NAME, 'title')
    print(title.text)

time.sleep(5)

driver.close()