from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up Chrome WebDriver
chrome_options = Options()
chrome_options.add_argument('--headless')  # Run Chrome in headless mode (no GUI)
chrome_service = ChromeService(executable_path='/path/to/chromedriver')
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

# Navigate to the website
url = 'https://bama.ir/car?page=1'
driver.get(url)

# Wait for page content to load (adjust timeout as needed)
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'bama-ad__title')))

# Extract the desired data
car_name = driver.find_element(By.CLASS_NAME, 'bama-ad__title').text.strip()
car_year = driver.find_elements(By.CLASS_NAME, 'bama-ad__detail-row span')[0].text.strip()
car_mileage = driver.find_elements(By.CLASS_NAME, 'bama-ad__detail-row span')[2].text.strip()
car_city = driver.find_element(By.CLASS_NAME, 'bama-ad__address span').text.strip()
car_price = driver.find_element(By.CLASS_NAME, 'bama-ad__price').text.strip()

# Print the extracted data
print(car_name)
print(car_year)
print(car_mileage)
print(car_city)
print(car_price)

# Close the WebDriver
driver.quit()
