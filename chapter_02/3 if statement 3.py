"""
ในการใช้ if ความยากอย่างหนึ่ง คือ กรณีเจอเงื่อนไขที่ซับซ้อน 
โดย Operator ที่ใช้ได้ คือ 
! หมายถึง Not
AND หมายถึง และ
OR หมายถึง หรือ 

การเขียนโปรแกรม if-else ควรตรวจสอบทีละเงื่อนไข
"""

"""
* Probation = GPA ก่อนหน้า > 2.0 และ GPS เทอมปัจจุบัน < 2.0
* หรือ GPA ก่อนหน้า < 2.0 แต่ GPS เทอมปัจจุบัน >= 2.0 แต่ GPA ปัจจุบัน ก็ยัง < 2.0
* ให้ลองเขียน if statement ที่บอกว่าโปรหรือไม่
"""
GPA_prior = 1.8
GPS_Now = 2.1
GPA_Now = 1.9



"""
* ปีอธิกสุรทิน หมายถึง ปีที่หารด้วย 4 แต่ปีที่หารด้วย 100 ลงตัวมิใช่ปีอธิกสุรทิน แต่ยกเว้นปีที่หารด้วย 400 ลงตัว
* ค.ศ. 1600 และ 2000 เป็นปีอธิกสุรทิน แต่ ค.ศ. 1700, 1800 และ 1900 ไม่ใช่ 
* ให้เขียนโปรแกรมรับปี แล้วบอกว่าเป็น ปีอธิกสุรทิน (Leap year) หรือไม่
"""



"""
* รับจำนวนเต็ม 5 จำนวน คั่นด้วยช่องว่าง
* ตรวจว่าลำดับจากซ้ายไปขวาของจำนวนที่รับมา
* เรียงจากน้อยไปมากหรือไม่
* ตอบ True, False
"""
x1,x2,x3,x4,x5 = [int(e) for e in input().split()]

"""
* รับจำนวนเต็ม 4 จำนวน คั่นด้วยช่องว่าง
* หาผลรวมของจำนวนที่รับมา โดยไม่รวมจำนวนที่
* มากสุด และ น้อยสุด ทุกจำนวนไม่ซ้ำ
"""

