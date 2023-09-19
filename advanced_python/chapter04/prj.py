import requests
from bs4 import BeautifulSoup
import mysql.connector


def get_truecar_data(search_term, num_results=20):
    url = f"https://www.truecar.com/used-cars-for-sale/listings/{search_term.lower()}/location-ANY/"
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        cars = soup.find_all("div", class_="vehicle-card")

        config = {
                'user': 'root',
                'password': '1234',
                'host': '127.0.0.1:3306',
                'database': 'employee',
                'raise_on_warnings': True
        }
        connection = mysql.connector.connect(**config)

        if connection.is_connected():
            cursor = connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS cars (make TEXT, model TEXT, price TEXT, mileage TEXT)''')

        for car in cars[:num_results]:
            make = car.find("div", class_="vehicle-card-make").text.strip()
            model = car.find("div", class_="vehicle-card-model").text.strip()
            price = car.find("div", class_="vehicle-card-price").text.strip()
            mileage = car.find("div", class_="vehicle-card-mileage").text.strip()
            
            
            cursor.execute("INSERT INTO cars VALUES (?, ?, ?, ?)", (make, model, price, mileage))
        
        connection.commit()
        connection.close()
   
search_term = input()
get_truecar_data(search_term)
print(f"{search_term}")
