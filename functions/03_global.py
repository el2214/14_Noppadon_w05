counter = 0

def increment():
    '''เพิ่มค่า counter ที่ละ 1'''
    global counter
    counter += 1
    print(f"Counter : {counter}")

def reset_counter():
    '''Reset Counter ให้เป็น 0'''
    global counter
    counter = 0
    print(f"Counter รีเซ็ตแล้วววว")

increment()
increment()
increment()
reset_counter()
increment()
