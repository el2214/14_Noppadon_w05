from datetime import datetime, date, timedelta
import time

today = date.today()

# print(f"วันที่ {today}")
# print(f"วัน {today.day}")
# print(f"เดือน {today.month}")
# print(f"ปี {today.year}")

now = datetime.now()

# print(now)
# print(f"เวลาปัจจุบัน Hr : {now.hour}")
# print(f"เวลาปัจจุบัน m : {now.minute}")
# print(f"เวลาปัจจุบัน s : {now.second}")

# จัด Format ว ด ป

formatted_date = now.strftime("%d/%m/%Y")
formatted_time = now.strftime("%H-%M-%S")

# print(formatted_date,formatted_time)

# คำนวณวันที่
tomorow = today + timedelta(days=1)
yesterday = today - timedelta(days=1)
next_week = today + timedelta(days=7)
next_mount = today + timedelta(days=30)

def calculate_age(birth_date):
    today = date.today()
    age = today.year - birth_date.year
    return age

day = int(input("Day : "))
mount = int(input("Mount : "))
year = int(input("Year : "))
birth_date = date(year,mount,day)

age = calculate_age(birth_date)
print("อายุของคุณ",age,"ปีแล้วนะ")