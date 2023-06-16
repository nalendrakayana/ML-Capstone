from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import io
from PIL import Image
import time
import os
PATH = r"C:\Users\User\Documents\VS\scrapping_data_capstone\chromedriver.exe"

MAX_IMAGES = 25
QUERY = "kentang goreng"
FOLDER = f"{QUERY}/"
if FOLDER not in os.listdir():
    os.mkdir(FOLDER)
wd = webdriver.Chrome(PATH)

def get_images_from_google(driver, delay, max_images):
    def scroll_down(driver):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(delay)
    url = f"https://www.google.com/search?q={QUERY}&tbm=isch&ved=2ahUKEwiG4OnaoKn_AhWLgmMGHT97A_cQ2-cCegQIABAA&oq={QUERY}&gs_lcp=CgNpbWcQAzIICAAQgAQQsQMyCAgAEIAEELEDMggIABCABBCxAzIICAAQgAQQsQMyCAgAEIAEELEDMggIABCABBCxAzIICAAQgAQQsQMyCAgAEIAEELEDMgUIABCABDIICAAQgAQQsQM6BAgjECc6BwgAEIoFEEM6BQgAELEDOgcIIxDqAhAnOgoIABCKBRCxAxBDUOsFWIMNYJ8OaAFwAHgAgAE-iAGIA5IBATeYAQCgAQGqAQtnd3Mtd2l6LWltZ7ABCsABAQ&sclient=img&ei=H1N8ZMbUGouFjuMPv_aNuA8"

    driver.get(url)

    image_urls = set()
    skips = 0
    while len(image_urls) + skips < max_images:
        scroll_down(driver)

        thumbnails = driver.find_elements(By.CLASS_NAME, "Q4LuWd")
        
        for img in thumbnails[len(image_urls) + skips:max_images]:
            try:
                img.click()
                time.sleep(delay)
            except:
                continue
            
            images = driver.find_elements(By.CLASS_NAME, "r48jcc")
            for image in images:
                if image.get_attribute("src") in image_urls:
                    max_images += 1
                    skips += 1
                    break

                if image.get_attribute("src") and 'http' in image.get_attribute("src"):
                    image_urls.add(image.get_attribute("src"))
                    print(f"Found {len(image_urls)}")
    return image_urls

def download_image(download_path, url, file_name):
    try:
        image_content = requests.get(url).content
        image_file = io.BytesIO(image_content)
        image = Image.open(image_file)
        file_path = download_path + file_name

        with open(file_path, 'wb') as f:
            image.save(f, "JPEG")
        print(f"Sucessfully downloaded {url} to {file_path}")
    except Exception as e:
        print(f"ERROR - Could not download {url} - {e}")


urls = get_images_from_google(driver=wd, delay=1, max_images=MAX_IMAGES)

for i, url in enumerate(urls):
    download_image(FOLDER, url, str(i) + ".jpg")