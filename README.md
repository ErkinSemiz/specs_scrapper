[![GPL 3.0](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)


Python Version

[![Python 3.7](https://img.shields.io/badge/python-3.7.7-blue.svg)](https://www.python.org/downloads/release/python-377/)

Package Versions

[![wheel 0.34.2](https://img.shields.io/badge/wheel-0.34.2-red.svg)](https://pypi.org/project/wheel/)
[![pandas 1.0.3](https://img.shields.io/badge/pandas-1.0.3-red.svg)](https://pypi.org/project/pandas/)
[![selenium 3.141.0](https://img.shields.io/badge/selenium-3.141.0-red.svg)](https://pypi.org/project/pandas/)
[![random_user_agent 1.0.1](https://img.shields.io/badge/random_user_agent-1.0.1-red.svg)](https://pypi.org/project/random-user-agent/)
[![requests 2.23.0](https://img.shields.io/badge/requests-2.23.0-red.svg)](https://pypi.org/project/selenium/)
[![xlsxwriter 1.2.8](https://img.shields.io/badge/xlsxwriter-1.2.8-red.svg)](https://pypi.org/project/xlsxwriter/)



# specs_scrapper

Web scrapper script for specifications of tech goods (for hepsiburada, n11, trendyol hosts).

[![Warning](https://img.shields.io/badge/WARNING-!!!-red.svg)]()

For the N11 host, it only works for "www.n11.com" domain.

urun.n11.com subdomain of it has no usual pattern to scrap because of the independent sellers recklesness.

Also, for locally approach it will take some time to get data from downloaded page with selenium. Of course there is better alternatives than selenium for this approach but **here is the purpose is not creating most efficient script but doing it with selenium.**

## Installation

Script created in Python 3.7.7 environment

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install necessary packages for the script.

```bash
pip install wheel pandas selenium random_user_agent requests xlsxwriter
```

You also need to create scrappingbee account to get api-key for bypassing sites with better detection like hepsiburada.

```python
def send_request(url):
    while True:
        print("Response Http Status Code : 200 dönene kadar bekleniyor.")
        response = requests.get(
            url="https://app.scrapingbee.com/api/v1/",
            params={
                "api_key": "YOU NEED TO COPY YOUR API-KEY HERE",
                "url": url,
            },
        )
        response.encoding = 'utf-8'
        print('Response HTTP Status Code : ', response.status_code)
        if (response.status_code == 200):
            break

    return response.text
```
--------------------------------------------------------------------------------------------------------


In this script **$cdc_** variable replaced version of chromedriver.exe has been used. I also pushed that version to master but it is wise thing to download from source and change by yourself. Any hex editor does the job. Just look for **$cdc_** variable and change it **xxxx** or any same length string you want. Some sites detects the driver with searching that string.

[![chromedriver 81.0.4044.69](https://img.shields.io/badge/chromedriver.exe-81.0.4044.69-red.svg)](https://chromedriver.storage.googleapis.com/index.html?path=81.0.4044.69/)


Take that chromedriver.exe and move that executable to the **"C:\bin\"** directory. 

## Usage

Firstly, when you run the script it will ask you the chromedriver.exe's path in Turkish just copy the path of the  **chromedriver.exe**. If you put the executable in to the **"C:\bin\"** directory as adviced. You can easily copy the path from helpful hint which is **C:\bin\chromedriver.exe**

Script will ask you the path until you enter the right path.

You can bypass it with changing this part of code
```python
driver = webdriver.Chrome(options=options, executable_path=drivercheck)
```
with
```python
driver = webdriver.Chrome(options=options, executable_path="Your chromedriver.exe path")
``` 

Secondly, it will ask you the url of the tech goods from the sites which are hepsiburada, n11 and trendyol. 

Script will ask you the url until you enter the expected url from these three sites.

If you enter hepsiburada related link it will use local file approach with scrappingbee instead of directly from the site because of the better bot detection. Otherwise it will directly scrap from the sites.

In the end it will create specs.xlsx file with the goods specifications.
 



## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate and if you across try except loop check the package versions.

## License
[GPL](https://www.gnu.org/licenses/gpl-3.0)