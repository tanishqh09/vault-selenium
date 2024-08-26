from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import time
import os
import shutil

# Define the path for downloads and repo directories
downloads_path = os.path.join(os.getcwd(), 'downloads')
repo_path = os.path.join(os.getcwd(), 'repo')

# Ensure the directories exist
os.makedirs(downloads_path, exist_ok=True)
os.makedirs(repo_path, exist_ok=True)

chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--window-size=1920,1080")

# Set Chrome preferences to download files to the specified directory
prefs = {
    "download.default_directory": downloads_path,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
}
chrome_options.add_experimental_option("prefs", prefs)

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

driver.get("https://www.screener.in/company/RELIANCE/consolidated/")

export = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[contains(concat( " ", @class, " " ), concat( " ", "icon-download", " " ))]'))
)
export.click()

login("tanishq@gmail.co.in", "tanishq@gmail.co.in")

export = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[contains(concat( " ", @class, " " ), concat( " ", "icon-download", " " ))]'))
)
export.click()

# Wait for the download to complete
time.sleep(10)

# List files in the download directory
print("Files in download directory before wait:", os.listdir(downloads_path))

# Ensure the downloaded file is present
downloaded_file = 'Reliance Industr.xlsx'
downloaded_file_path = os.path.join(downloads_path, downloaded_file)
if os.path.isfile(downloaded_file_path):
    # Move the downloaded file to the repo directory
    shutil.move(downloaded_file_path, os.path.join(repo_path, downloaded_file))
    print(f"Moved {downloaded_file} to repo directory.")
else:
    print(f"File {downloaded_file} not found in download directory.")
