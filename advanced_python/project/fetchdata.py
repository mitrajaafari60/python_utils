import requests
from bs4 import BeautifulSoup
import re
from unidecode import unidecode
import sqlite3

# Establish a connection to the SQLite database
conn = sqlite3.connect('car_data.db')
cursor = conn.cursor()

# Create a table (if it doesn't exist)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS car_data (
        car_name TEXT,
        car_year INTEGER,
        car_mileage INTEGER,
        car_price TEXT
    )
''')

base_url = 'https://divar.ir/s/tehran/vehicles?page='

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'Referer': 'https://www.example.com',  # Replace with the actual referer if needed
}

for page in range(0, 201):
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
                car_price = 'توافقی'
                parts = car_name.split("مدل")
                if len(parts) >=2:
                    car_name=parts[0]
                    x2 = re.findall(r'\b\d+\b', unidecode(parts[1]))
                    if len(x2) >= 1:
                        car_year = int(x2[0])
                else:
                    x3 = re.findall(r'\b\d+\b', unidecode(txt))
                    if len(x3) >= 1:
                        car_year = int(x3[len(x3) - 1])
                if car_year<100:
                    car_year = 1300+car_year

                car_use = car_ad.find_all('div', class_='kt-post-card__description')
                car_mileage = '0'

                if len(car_use) >= 2:
                    car_price = car_use[1].text.strip()
                    car_mileage = car_use[0].text.strip()
                elif len(car_use) >= 1:
                    car_price = car_use[0].text.strip()

                car_price_d = re.findall(r'\b\d+\b', unidecode(car_price.replace(",", "")))
                if len(car_price_d) < 1:
                    car_price_d = ['توافقی']
                car_mileage_d = re.findall(r'\b\d+\b', unidecode(car_mileage.replace(",", "")))
                if len(car_mileage_d) < 1:
                    car_mileage_d = [0]

                # Insert data into the database
                cursor.execute('''
                    INSERT INTO car_data (car_name, car_year, car_mileage, car_price)
                    VALUES (?, ?, ?, ?)
                ''', (car_name, car_year, car_mileage_d[0], car_price_d[0]))

                # Commit changes
                conn.commit()

    else:
        print("error Get URL:",response.status_code)

# Close the database connection
conn.close()
