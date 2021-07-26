'''
ในการทำงานบางอย่างที่ต้องการทำงานซ้ำๆ เราสามารถสร้างเป็น Function ได้ 

def function_name(parameters):
        docstring
        statement(s)
        return x
'''

def hello(name):
        '''
        Function to print ส่วนนี้เรียกว่า docstring เอาไว้อธิบายการทำงานของ function
        '''
        print ("Good afternoon, " + name)

in_name =  "Thana"
print (hello(in_name))
in_name =  "Bob"
print (hello(in_name))

# จงเขียน Function absolute value

'''
จงเขียนโปรแกรมรับค่าตัวเลข และบอกว่าเป็น square number หรือไม่
โดยให้ทำเป็นฟังก์ชัน 

def is_square(n):
        return False;

-1 : False
0 : True
4 : True
5 : False
25 : True
'''

def Sum(data):
            sum = 0
    for i in data:
        sum = sum + i
    return sum

lst = [2, 5, 1, 6, 7, 9, 10, 4]
print("Sum of lst =", Sum(lst)) 