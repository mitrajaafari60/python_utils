import requests
from bs4 import BeautifulSoup
import re
from unidecode import unidecode

base_url = 'https://divar.ir/s/tehran/vehicles?page='

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'Referer': 'https://www.example.com',  # Replace with the actual referer if needed
}


for page in range (0,1):

    url = base_url + str(page)
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        car_ads = soup.find_all('div', class_='kt-post-card__info')
       
        if car_ads:
            for car_ad in car_ads:
                txt = car_ad.find('h2', class_='kt-post-card__title').text.strip()  
                x = txt.split("،") 
                car_name = x[0]
                car_year = 1402
                car_price = 0
                x3= re.findall(r'\b\d+\b', unidecode(txt))
                if len(x3)>=1:
                    car_year = x3[len(x3)-1]
                
                car_use=car_ad.find_all('div', class_='kt-post-card__description')
                car_mileage= '0'
                
                if len(car_use)>=2:
                    car_price = car_use[1].text.strip()
                    car_mileage= car_use[0].text.strip()
                else:
                    car_price = car_use[0].text.strip()

                car_price_d = re.findall(r'\b\d+\b', unidecode(car_price.replace(",", "")))
                if len(car_price_d) <1:
                    car_price_d=['توافقی']
                car_mileage_d = re.findall(r'\b\d+\b', unidecode(car_mileage.replace(",", "")))
                if len(car_mileage_d)<1:
                    car_mileage_d=[0]
                print( car_name , car_year, car_mileage_d[0], car_price_d[0] )
        
        
    else:
        print(response.status_code)
