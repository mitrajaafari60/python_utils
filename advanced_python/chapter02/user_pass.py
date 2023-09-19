import re
import mysql.connector

def validate_email(email):
    pattern = r'^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,3})+$'
    return re.match(pattern, email)

def validate_password(password):
    if any(char.isdigit() for char in password) and any(char.isalpha() for char in password):
        return True
    return False

def save_user(username, password):
    try:
        # اطلاعات اتصال به دیتابیس
        config = {
            'user': 'root',
            'password': '1234',
            'host': '127.0.0.1:3306',
            'database': 'employee',
            'raise_on_warnings': True
        }

        # ایجاد اتصال به دیتابیس
        connection = mysql.connector.connect(**config)

        if connection.is_connected():
            cursor = connection.cursor()

            # اجرای کوئری برای ذخیره کاربر در دیتابیس
            query = "INSERT INTO users (username, password) VALUES (%s, %s)"
            values = (username, password)
            cursor.execute(query, values)

            # ثبت تغییرات در دیتابیس
            connection.commit()


    except mysql.connector.Error as e:
        print(f"{e}")

    finally:
        # بستن اتصال به دیتابیس
        if 'connection' in locals():
            connection.close()

# ورودی ایمیل و رمز عبور
email = input()
# اعتبارسنجی ایمیل
while not validate_email(email):
    print("expression@string.string")
    email = input()

password = input()
save_user(email, password)