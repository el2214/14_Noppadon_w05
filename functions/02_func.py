# รับ Parameter
'''def ชื่อฟังก์ชั่น(parameter):
    parameter1 + parameter2 = xxx

'''

def get_name(name):
    '''Show name from parameter'''
    print(f"Hello !!! : {name}")

def add_num(a,b):
    '''ฟังก์ชันบวกเลข'''
    result = a + b
    return result

# a = int(input())
# b = int(input())
# sum = add_num(a,b)
# print(sum)

def rect_cal(width, length):
    '''ฟังก์ชันหาพื้นที่สี่เหลี่ยมและเส้นกรอบ'''
    area = width * length
    frame = 2 * (width + length)
    return area, frame

width = 3
length = 10

area, frame = rect_cal(width,length)
print(f"พื้นที่สี่เหลี่ยม = {area} เส้นกรอบ = {frame}")
