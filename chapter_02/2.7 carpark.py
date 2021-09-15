"""
### ตัวอย่าง 
* ให้รับเวลาเข้าและออกของรถคันหนึ่ง (เปิดบริการตั้งแต่ 7:00 - 23:00) จากนั้นคำนวณค่าที่จอดรถที่ต้องจ่าย
* โดยหลักเกณฑ์การคำนวณมีดังนี้ (สมมติว่าไม่มีการจอดข้ามวัน)
        1. จอดรถไม่เกิน 15 นาที ไม่คิดค่าบริการ
        2. จอดรถเกิน 15 นาที แต่ไม่เกิน 3 ชั่วโมง คิดค่าบริการชั่วโมงละ 10 บาท เศษของชั่วโมงคิดเป็นหนึ่งชั่วโมง
        3. จอดรถตั้งแต่ 4 ชั่วโมง ถึง 6 ชั่วโมง คิดค่าบริการชั่วโมงที่ 4-6 ชั่วโมงละ 20 บาท เศษของชั่วโมงคิดเป็นหนึ่งชั่วโมง
        4. จอดรถเกิน 6 ชั่วโมงขึ้นไป เหมาจ่ายวันละ 200 บาท
## ข้อมูลนำเข้า
        มี 4 บรรทัด แต่ละบรรทัดมีจำนวนเต็มหนึ่งจำนวน
        โดยบรรทัดที่ 1-2 เป็นชั่วโมงและนาทีของเวลาเข้า และบรรทัดที่ 3-4 เป็นชั่วโมงและนาทีของเวลาออก
## ข้อมูลส่งออก
        มีบรรทัดเดียว เป็นค่าที่จอดรถที่ต้องจ่าย ให้แสดงผลลัพธ์เป็นจำนวนเต็ม
|ตัวอย่าง
        7
        0
        7
        15
*       => 0
        7
        0
        7
        16
*       => 10
        7
        30
        10
        31
*       => 50
        7
        30
        13
        31
*       => 200
"""