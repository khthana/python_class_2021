#---------------------------------------------------
#* while เป็นการทำ loop แบบหนึ่ง โดยมีเงื่อนไขเพียงถ้าเป็น False
#* จะออกจาก loop
#* รูปแบบ
#* while (condition):
#*      statement
#---------------------------------------------------

prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}!")


### จงเขียนโปรแกรมแสดงผลตั้งแต่ 1 ถึงตัวเลขที่รับเข้ามาโดยใช้ while 
n = int(input("Enter your number: "))
count = 0
while (count <= n):
    print(count)
    count = count + 1

### หาผลรวมของข้อมูลที่ป้อนเข้ามา 
n = 5
sum = 0
while n > 0:
    data = int(input("Enter your number ="))
    sum = sum + data
    n = n - 1    # update counter

# print the sum
print("The sum is", sum)

