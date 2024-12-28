import os
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

# membuat driver browser
driver = webdriver.Firefox()

# mengakses website WhatsApp Web
driver.get("https://web.whatsapp.com/")

# menunggu user untuk scan QR code
input("Tunggu sampai QR code discan, lalu tekan enter...")

# mencari semua elemen gambar (foto) pada halaman WhatsApp Web
# images = driver.find_elements_by_xpath("//img[@class='_3LWZlK']")
# images = driver.find_elements_by_css_selector("img._3LWZlK")
# images = driver.find_element_by_xpath("//img[@class='img-thumbnail']")
images = driver.find_element(by=By.XPATH, value="//img[@class='img-thumbnail']")

# mengunduh setiap foto dan menamai file sesuai dengan teks pada foto
for i, image in enumerate(images):
    file_name = image.get_attribute("alt") + ".jpeg"
    src = image.get_attribute("src")
    print("Mengunduh foto ke-{}: {}".format(i + 1, file_name))
    os.system("wget -O {} {}".format(file_name, src))

# menutup driver browser
driver.quit()
