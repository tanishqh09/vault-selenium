from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import os
import time
import shutil

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--window-size=1920,1080")

# Create 'downloads' directory if it doesn't exist
downloads_dir = os.path.join(os.getcwd(), 'downloads')
os.makedirs(downloads_dir, exist_ok=True)

# Set download directory preferences
prefs = {
    "download.default_directory": downloads_dir,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
}
chrome_options.add_experimental_option("prefs", prefs)

# Initialize the Chrome driver
service = Service('/usr/local/bin/chromedriver')
driver = webdriver.Chrome(service=service, options=chrome_options)

def login(username, password):
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[contains(concat( " ", @class, " " ), concat( " ", "account", " " ))]'))
    )
    login_button.click()

    email_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[(@id = "id_username")]'))
    )
    password_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[(@id = "id_password")]'))
    )

    email_input.send_keys(username)
    password_input.send_keys(password)

    second_login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[contains(concat( " ", @class, " " ), concat( " ", "icon-user", " " ))]'))
    )
    second_login_button.click()

# Open the page and perform actions
driver.get("https://www.screener.in/company/RELIANCE/consolidated/")

# Wait for export button and click
export = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[contains(concat( " ", @class, " " ), concat( " ", "icon-download", " " ))]'))
)
export.click()

# Log in and click export again
login("tanishq@gmail.co.in", "tanishq@gmail.co.in")

export = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[contains(concat( " ", @class, " " ), concat( " ", "icon-download", " " ))]'))
)
export.click()

# Wait for download to complete
download_complete = False
start_time = time.time()
timeout = 60  # Timeout in seconds

while not download_complete and (time.time() - start_time < timeout):
    files = os.listdir(downloads_dir)
    for file in files:
        if file.endswith('.xlsx'):
            print(f"Found downloaded file: {file}")
            download_complete = True
            break
    if not download_complete:
        time.sleep(5)  # Check every 5 seconds

if not download_complete:
    print("Download did not complete within the timeout period.")
else:
    print("Files in download directory after wait:", os.listdir(downloads_dir))

driver.quit()
