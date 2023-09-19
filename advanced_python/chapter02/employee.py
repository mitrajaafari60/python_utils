import mysql.connector


def sort_employees(employees):
    # تعریف تابع مرتب‌سازی بر اساس قد و وزن
    def compare(emp):
        return (-emp['Height'], emp['Weight'])

    # مرتب‌سازی لیست کارمندان با استفاده از تابع compare
    sorted_employees = sorted(employees, key=compare)

    # چاپ نتایج مرتب‌سازی
    for emp in sorted_employees:
        print(f"{emp['Name']} {emp['Height']} {emp['Weight']}")

# اطلاعات اتصال به دیتابیس
config = {
    'user': 'root',
    'password': '1234',
    'host': '127.0.0.1:3306',
    'database': 'employee',
    'raise_on_warnings': True
}

try:
    # ایجاد اتصال به دیتابیس
    connection = mysql.connector.connect(**config)

    if connection.is_connected():
        cursor = connection.cursor()

        # اجرای کوئری برای خواندن داده‌ها
        query = "SELECT Name, Height, Weight FROM employees ORDER BY Height DESC, Weight ASC"
        cursor.execute(query)

        employees = []
        for (name, height, weight) in cursor:
            f2T=dict
            f2T['Name']= name
            f2T['Height']= height
            f2T['Weight']=weight
            employees = employees.append(f2T)

        sort_employees()
except mysql.connector.Error as e:
    print(f"خطا در اتصال به دیتابیس: {e}")

finally:
    # بستن اتصال به دیتابیس
    if 'connection' in locals():
        connection.close()
