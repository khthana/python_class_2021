"""
### ตัวอย่าง 
* ให้รับเวลาเข้าและออกของรถคันหนึ่ง (เปิดบริการตั้งแต่ 7:00 - 23:00) จากนั้นคำนวณค่าที่จอดรถที่ต้องจ่าย
* โดยหลักเกณฑ์การคำนวณมีดังนี้
        1. จอดรถไม่เกิน 15 นาที ไม่คิดค่าบริการ
        2. จอดรถเกิน 15 นาที แต่ไม่เกิน 3 ชั่วโมง คิดค่าบริการชั่วโมงละ 10 บาท เศษของชั่วโมงคิดเป็นหนึ่งชั่วโมง
        3. จอดรถตั้งแต่ 4 ชั่วโมง ถึง 6 ชั่วโมง คิดค่าบริการชั่วโมงที่ 4-6 ชั่วโมงละ 20 บาท เศษของชั่วโมงคิดเป็นหนึ่งชั่วโมง
        4. จอดรถเกิน 6 ชั่วโมงขึ้นไป เหมาจ่ายวันละ 200 บาท
"""
# -------------- Input --------------------------
hour_enter = int(input("Enter hour enter : "))
if hour_enter < 7 or hour_enter >=23 :
    print("Car park is not open.")

min_enter = int(input("Enter minute enter : "))
if min_enter < 0 or min_enter >=59 :
    print("Invalid number.")

hour_exit = int(input("Enter hour exit : "))
if hour_exit < 7 or hour_exit >=23 :
    print("Car park is not open.")
if hour_exit < hour_enter:
    print("Invalid hour")

min_exit = int(input("Enter minite exit : "))
if min_exit < 0 or min_exit >=59 :
    print("Invalid number.")

#--------------- Calculate min -------------------
if min_enter == min_exit:    # เช่น 8.30 - 9.15
    total_min = (hour_exit - hour_enter) * 60
elif min_exit > min_enter:
    total_min = ((hour_exit - hour_enter) * 60) + min_exit - min_enter # นาทีออก > นาทีเข้า 
else:
    total_min = ((hour_exit - hour_enter-1) * 60) + 60 - (min_enter - min_exit)

#print(total_min)
#------------- Calculate money -------------------
fee = 0
if total_min < 15:
    fee = 0
else:
    total_hour = int((total_min/60)+0.99)
    print(total_hour)
    if total_hour <= 3:
        fee = 10*total_hour
    elif total_hour <=6:
        fee = 20*total_hour
    else:
        fee = 200

print(fee)

