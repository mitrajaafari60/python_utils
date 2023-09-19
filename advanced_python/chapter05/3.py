import requests
from bs4 import BeautifulSoup

base_url = 'https://bama.ir/car?page='

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'Referer': 'https://www.example.com',  # Replace with the actual referer if needed
}

for page in range (0,200):

    url = base_url + str(page)
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
      
        dec= soup.find_all('div',class_='brands-solution-in-list')
        car_ads = soup.find_all('div', class_='bama-ad-holder')
        if car_ads:
            for car_ad in car_ads:
                car_name = car_ad.find('p', class_='bama-ad__title').text.strip()    
                    # Extract additional information as needed
                
                    # Print or store the extracted data
                print("Car Name:", car_name)
        
        
    else:
        print(response.status_code)
