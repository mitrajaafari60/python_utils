from datetime import datetime

def calculate_age(date_string):
    try:
        # تبدیل تاریخ ورودی به شی datetime
        birth_date = datetime.strptime(date_string, "%Y/%m/%d")

        # تاریخ فعلی
        current_date = datetime.now()

        # محاسبه سن
        age = current_date.year - birth_date.year

        # بررسی اینکه آیا تاریخ تولد در آینده است یا نه
        if current_date.month < birth_date.month or (current_date.month == birth_date.month and current_date.day < birth_date.day):
            age -= 1

        return age
    except ValueError:
        return "WRONG"

# خواندن تاریخ ورودی از کاربر
date_of_birth = input()

# محاسبه سن
age = calculate_age(date_of_birth)

# چاپ نتیجه
print(age)
