import requests
from bs4 import BeautifulSoup
import csv

base_url = 'https://bama.ir/car'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'Referer': 'https://www.example.com',  # Replace with the actual referer if needed
}

# ایجاد یک فایل CSV برای ذخیره نتایج
with open('car_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['نام خودرو', 'سال', 'کارکرد', 'شهر', 'قیمت']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    # نوشتن سرصفحه‌های فایل CSV
    writer.writeheader()

    # 200 صفحه از وب‌سایت را پیمایش می‌کنیم
    url = base_url 
    response = requests.get(url,headers=headers)

    soup = BeautifulSoup(response.text, 'html.parser')
    car_ads_container = soup.find('div', class_='bama-adlist-container')
    for count in range (0,200):
        car_ad = car_ads_container.findNext('div', class_='bama-ad-holder')
        if car_ad:
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
            # نوشتن اطلاعات به فایل CSV
            writer.writerow({'نام خودرو': car_name, 'سال': car_year, 'کارکرد': car_mileage, 'شهر': car_city, 'قیمت': car_price})
        count +=1
    else:
        print(f"درخواست ناموفق بود. کد وضعیت: {response.status_code}")
