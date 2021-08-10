
### ตัวอย่าง : จงเขียนโปรแกรมรับค่าคะแนนเพื่อตัดเกรด 
###          ข้อมูลที่รับมาเป็น float ให้ปรับเป็นจำนวนเต็มก่อน
###          โดย หาก 0.5 ขึ้นไปให้ปัดขึ้น เช่น 50.7 -> 51
###          หากน้อยกว่า 50 ให้ปัดลง 50.49 -> 50
###          จากนั้นค่อยเอามาตัดเกรดดังนี้
###          < 50 : F
###          50 -> 55 : D
###          55 -> 60 : D+
###          60 -> 65 : C
###          65 -> 70 : C+
###          70 -> 75 : B
###          75 -> 80 : B+
###          > 80 : A

score = float(input("Enter score = "))

if (score % 1) >= 0.5:
      Before_point = score // 1
      score = Before_point + 1
      print("Round up score =", score)

if(score < 50):
      print("Your grade is 0.0")
elif (score >= 50 and score < 55):
      print("Your grade is 1.0")
elif (score >= 55 and score < 60):
      print("Your grade is 1.5")
elif (score >= 60 and score < 65):
      print("Your grade is 2.0")
elif (score >= 65 and score < 70):
      print("Your grade is 2.5")
elif (score >= 70 and score < 75):
      print("Your grade is 3.0")
elif (score >= 75 and score < 80):
      print("Your grade is 3.5")
elif (score >= 80):
      print("Your grade is 4.0")
else:
      print("Your score is incorrect")


#-------------------------------------------
#*  การเปรียบเทียบที่ใช้บ่อย
#*  if a%2 == 0 :               a เป็นเลขคู่หรือไม่
#*  if a%100 == 0 :             a หารด้วย 100 ลงตัวหรือไม่
#*  if (a//100)%10 == 9 :       เลขหลักร้อยของ a คือ 9 หรือไม่ หรือ
#*  if (a%1000)//100 == 9:      ก็เหมือนกัน
#*  if a <= x <= b :            x มีค่าในช่วงตั้งแต่ a ถึง b หรือไม่
#*
#-------------------------------------------


#-------------------------------------------
#* แนวทางที่ดีในการใช้ if แบบขั้นบันได
#-------------------------------------------
s = 50
if s >= 80 :
    g = 'A'
elif 70 <= s < 80 :
    g = 'B'
elif 60 <= s < 70 :
    g = 'C'
elif 50 <= s < 60 :
    g = 'D'
else :
    g = 'F'

#-------------------------------------------
#*  สามารถเขียนเป็น
#-------------------------------------------
if s >= 80 :
    g = 'A'
elif s >= 70 :
    g = 'B'
elif s >= 60 :
    g = 'C'
elif s >= 50 :
    g = 'D'
else :
    g = 'F'

#|Ex. 2.4 จากโปรแกรม BMI Calcularor 
#|       = weight(kg) / height(m)^2 
#| Input:
#|      Enter weight : 80
#|      Enter height : 1.75
#| Output:
#|      BMI = 26
#| นอกจากจะบอกค่า BMI แล้ว ยังให้คำแนะนำดังนี้

#|    Under 18.5 they are underweight
#|    Over 18.5 but below 25 they have a normal weight
#|    Over 25 but below 30 they are slightly overweight
#|    Over 30 but below 35 they are obese
#|    Above 35 they are clinically obese.

weight = input("Enter your weight in kg: ")
height = input("Enter your height in m: ")


#|Ex. 2.4* รับจำนวนเต็ม 4 จำนวน คั่นด้วยช่องว่าง
#|         หาผลรวมของจำนวนที่รับมา โดยไม่รวมจำนวนที่
#|         มากสุด และ น้อยสุด ทุกจำนวนไม่ซ้ำ

x1,x2,x3,x4,x5 = [int(e) for e in input().split()]



