import requests
from bs4 import BeautifulSoup
url = "https://divar.ir/tehran"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    ads = soup.find_all("div", class_="kt-post-card__footer")
    for ad in ads:
        if "قیمت توافقی" in ad.get_text():
            print(ad.get_text())
