import requests
from bs4 import BeautifulSoup

base_url = 'https://bama.ir/car?page='

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'Referer': 'https://www.example.com',  # Replace with the actual referer if needed
}


url = base_url + str(1)
response = requests.get(url, headers=headers)
count=0

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    car_ads_container = soup.find('div', class_='bama-adlist-container')
    for count in range (0,200):
        car_ads = car_ads_container.find_all('div', class_='bama-ad-holder')
        if car_ads:
            for car_ad in car_ads:
                car_name = car_ad.find('p', class_='bama-ad__title').text.strip()
                
                # Extract additional information as needed
                car_detail_row = car_ad.find('div', class_='bama-ad__detail-row')
                if car_detail_row:
                    car_year = car_detail_row.find_all('span')[0].text.strip()
                    car_mileage = car_detail_row.find_all('span')[1].text.strip().replace(" کیلومتر", "")
                
                car_address_box = car_ad.find('div', class_='bama-ad__address-box')
                if car_address_box:
                    car_city = car_address_box.find('span').text.strip()

                car_price_span = car_ad.find('div', class_='bama-ad__price-row')
                if car_price_span:
                    car_price = car_price_span.find('div', class_='bama-ad__price-holder').find_all('span')[0].text.strip()

                # Print or store the extracted data
                print("Car Name:", car_name)
                if car_detail_row:
                    print("Car Year:", car_year)
                    print("Car Mileage:", car_mileage)
                if car_address_box:
                    print("Car City:", car_city)
                print("Car Price:", car_price)
                print("\n---\n")
        count+=1
    else:
        print(response.status_code)
