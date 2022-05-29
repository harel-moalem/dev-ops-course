from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

driver.get('C:/Users/harel.moalem/PycharmProjects/tip_calc/index.html')
driver.find_element_by_id("billamt").send_keys('100')
driver.find_element_by_xpath('//*[@id="serviceQual"]/option[3]').click()
driver.find_element_by_id("peopleamt").send_keys("5")
driver.find_element_by_id("musicamt").send_keys("2")
driver.find_element_by_id("calculate").click()

expected = "8.00"
actual = driver.find_element_by_id('tip').text
assert actual == expected
