#
#| Ex 6.4 ให้แก้ไขโปรแกรมให้สามารถประมวลผลต่อเนื่อง
#|        เช่น เมื่อ + เรียบร้อย ให้ถามว่าต้องการทำอะไรต่อไปหรือไม่
#|        ถ้ากด y ก็รับข้อมูลต่อไป ถ้ากด n ก็ออกจากโปรแกรม
#|        และแก้โปรแกรมให้ใช้เลขทศนิยมได้ด้วย

def add(n1, n2):
    return n1+n2

def subtract(n1, n2):
    return n1-n2

def multiply(n1, n2):
    return n1*n2

def devide(n1, n2):
    return n1/n2

operations = {'+':add,
              '-':subtract,
              '*':multiply,
              '/':devide,
              }

num1 = int(input("What's the first number? : "))

for symbol in operations:
    print(symbol)
operation_symbol = input("Pick an operation from the line above : ")

num2 = int(input("What's the second number? : "))

calculation_function = operations[operation_symbol]
answer = calculation_function(num1,num2)

print(f"{num1} {operation_symbol} {num2} = {answer}")