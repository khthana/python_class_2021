# นอกเหนือจาก __init__ แล้ว ยังมี method พิเศษ

# method __str__ เป็น method ที่จะถูกเรียกมาทำงาน เมื่อมีการใช้คำสั่ง print กับ object

# คลาส Book สร้างอ็อบเจกต์ที่เก็บข้อมูลของหนังสือ (ชื่อ ราคา ของหนังสือ)
class Book:
    def __init__(self, title, price, author):
        self.title = title
        self.price = price
        self.author = author

    def __str__(self):
        return self.title + " ราคา " + str(self.price) + " บาท"

    def update_price(self, new_price):
        self.price = new_price

    # method __lt__ใช้เปรียบเทียบ object
    def __lt__(self, rhs):
        if self.price != rhs.price:
            return self.price < rhs.price
        else:
            return self.title < rhs.title


# เมื่อใช้ print กับ object จะเป็นการเรียกใช้ method __str__

book1 = Book("Harry Potter", 395, "J.K. Rowling")
print(book1)

# ลองใช้ __lt__ ในการเปรียบเทียบ

book2 = Book("พระอภัยมณี", 355, "สุนทรภู่")

print(book1 > book2)
