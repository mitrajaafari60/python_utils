n = int(input()) 
participants = []

# خواندن ورودی و ذخیره اطلاعات قبول شدگان در لیست
for _ in range(n):
    data = input().split('.')
    gender = data[0]  # جنسیت شرکت کننده
    name = data[1].capitalize()  # استاندارد سازی نام شرکت کننده
    language = data[2]
    participants.append((gender, name, language))

# مرتب سازی لیست قبول شدگان بر اساس جنسیت و سپس نام
sorted_participants = sorted(participants)

# چاپ نتایج
for participant in sorted_participants:
    gender, name, language = participant
    print(f"{gender} {name} {language}")
