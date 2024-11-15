# Calculator.net Test Case 01: Calculate Valid Private IPv4

# Update apt cache and install pre-reqs
!apt-get update
!pip install selenium
!apt install chromium-chromedriver

# Load Selenium Web Driver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--window-size=2050,2050')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(options=chrome_options)

# Define URL to test
base_url = "https://www.calculator.net/ip-subnet-calculator.html"
driver.get(base_url)
driver.title

# Import functions to locate form elements
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

subnetFieldXpath = '//*[@id="csubnet"]'
ipv4FieldXpath = '//*[@id="cip"]'
calculateBtnXpath = '/html/body/div[3]/div[1]/div[2]/form/table/tbody/tr[4]/td/input[2]'
subnetField = driver.find_element(By.XPATH, subnetFieldXpath)
selectSubnetField = Select(subnetField)
ipv4Field = driver.find_element(By.XPATH, ipv4FieldXpath)
calculateBtn = driver.find_element(By.XPATH, calculateBtnXpath)

# Test Valid Private IP address
selectSubnetField.select_by_visible_text("255.255.255.0 /24")
ipv4Field.clear()
ipv4Field.send_keys("192.168.25.27")
calculateBtn.click()
ipv4AddressXpath = '/html/body/div[3]/div[1]/table[1]/tbody/tr[1]/td[2]'
networkAddressXpath = '/html/body/div[3]/div[1]/table[1]/tbody/tr[2]/td[2]'
usableHostsXpath = '/html/body/div[3]/div[1]/table[1]/tbody/tr[6]/td[2]'
ipv4Address = driver.find_element(By.XPATH, ipv4AddressXpath).text
networkAddress = driver.find_element(By.XPATH, networkAddressXpath).text
usableHosts = driver.find_element(By.XPATH, usableHostsXpath).text

# Print outputs and test results
testResult = "PASS"
print(f'Entered Address was:        {ipv4Address}')
print(f'\nNetwork Address should be:  192.168.25.0')
print(f'Network Address calculated: {networkAddress}')
print(f'  Network Address Result:   ', end='')
if networkAddress == "192.168.25.0":
  print("PASS")
else:
  print("FAIL")
  testResult = "FAIL"
print(f'\nNum Usable Hosts expected:  254')
print(f'Usable Hosts calculated:    {usableHosts}')
print(f'  Num Usable Hosts Result:  ', end='')
if usableHosts == "254":
  print("PASS")
else:
  print("FAIL")
  testResult = "FAIL"
print(f'\nCulmulative result of Test: {testResult}')