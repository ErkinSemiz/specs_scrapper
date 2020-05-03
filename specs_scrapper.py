#pip install requests pandas selenium six random_user_agent

import os
import requests
import pandas as pd

from selenium import webdriver
from six.moves.urllib.parse import urlparse
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem

#This request is special for bypassing hepsiburada bot protection
#In this function scrapingbee api has been used. (You should enter your "api-key".)

def send_request(url):
    while True:
        print("Response Http Status Code : 200 dönene kadar bekleniyor.")
        response = requests.get(
            url="https://app.scrapingbee.com/api/v1/",
            params={
                "api_key": "5AXFMSOHHY97OW3PFMWVQDNEB1BIGN7NPFFOLKMFWI84V1WR05EF6ZLDB4DZIN93BIDNQE8N6Q0A4NFP",
                "url": url,
            },
        )
        response.encoding = 'utf-8'
        print('Response HTTP Status Code : ', response.status_code)
        if (response.status_code == 200):
            break

    return response.text

#hepsiburada_scrapper works differently than the two other scrapping functions in this script it is using
#local page approach because of the hosts better detection.
def hepsiburada_scrapper(url, driver):

    #xpath1 for the keys xpath2 for the values
    xpath1 = "//table[@class = 'data-list tech-spec']//tbody//tr//th"
    xpath2 = "//table[@class = 'data-list tech-spec']//tbody//tr//td"

    response = send_request(url)
    print("Selenium yerel dosya üzerinden bilgileri topluyor lütfen bekleyiniz")
    with open('page.html', 'w', encoding='utf8') as fd:
        fd.write(response)
    pagefile = os.path.dirname(__file__) + "\\page.html"
    driver.get(pagefile)
    scrap_and_out(xpath1, xpath2)

def n11_scrapper(url, driver):

    # xpath1 for the keys xpath2 for the values
    xpath1 = "//p[@class = 'unf-prop-list-title']"
    xpath2 = "//p[@class = 'unf-prop-list-prop']"

    driver.get(url)

    #Button clicking necessary for scrapping all specs during n11 scrapping.

    submit_button = driver.find_element_by_xpath("//span[@class = 'unf-prop-more-button']").click()

    scrap_and_out(xpath1,xpath2)

def trendyol_scrapper(url, driver):

    # xpath1 for the keys xpath2 for the values
    xpath1 = "//div[@class = 'item-key']"
    xpath2 = "//div[@class = 'item-value']"

    driver.get(url)
    scrap_and_out(xpath1, xpath2)

def scrap_and_out(xpath1,xpath2):
    keys = []
    values = []
    ozellik = []
    deger = []

    while len(keys) == 0:
        try:
            keys = driver.find_elements_by_xpath(xpath1)
        except:
            pass

    while len(values) == 0:
        try:
            values = driver.find_elements_by_xpath(xpath2)
        except:
            pass

    for key in keys:
        ozellik.append(key.text)

    for value in values:
        deger.append(value.text)

    datas = dict(zip(ozellik, deger))

    print(datas)

    df = pd.DataFrame(list(datas.items()), columns=['Özellikler', 'Değerleri'])
    df.to_excel('specs.xlsx')

if "__main__" == __name__:

    # Global variables

    hostname = ""
    url = ""
    argument=""

    # Custom user-agent values for block bypass

    software_names = [SoftwareName.CHROME.value]
    operating_systems = [OperatingSystem.WINDOWS.value, OperatingSystem.LINUX.value]
    user_agent_rotator = UserAgent(software_names=software_names, operating_systems=operating_systems, limit=100)
    user_agent = user_agent_rotator.get_random_user_agent()

    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--window-size=1920,1080')
    options.add_argument('--disable-gpu')
    options.add_argument(f'user-agent={user_agent}')
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)

    # Driver path control
    while True:
        try:
            drivercheck = input("chromedriver.exe'nin bulunduğu pathi giriniz (Örnek: C:\\bin\\chromedriver.exe): ")
            driver = webdriver.Chrome(options=options, executable_path=drivercheck)
            if driver.capabilities['browserVersion'] != "":
                break
        except:
            print("chromedriver.exe'nin bulunduğu pathi yanlış girdiniz.")

    # Expected goods url input and scrapping.

    while True:
        try:
            url = input("Özelliklerini öğrenmek istediğiniz hepsiburada/trendyol/n11 ürününün linkini giriniz: ")
            u = urlparse(url)
            hostname = u.hostname
            print("Site host adı:"+hostname)
            if u.hostname == "www.trendyol.com" or u.hostname == "www.hepsiburada.com" or u.hostname == "www.n11.com":
                print("Özelliklerin alınması için" + hostname +"'e özel fonksiyon çağırılıyor.")
                if hostname == "www.hepsiburada.com":
                    hepsiburada_scrapper(url, driver)
                elif hostname == "www.trendyol.com":
                    trendyol_scrapper(url, driver)
                elif hostname == "www.n11.com":
                    n11_scrapper(url, driver)
                break
        except:
            print("Girdiğiniz ürün hepsiburada/trendyol veya n11 ürünü değildir. Lütfen tekrar ürün girişi yapınız.")
