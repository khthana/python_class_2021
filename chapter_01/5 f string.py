"""
* F string ใช้ในการจัด format 
* การใช้ f-string ทำได้โดยเติม f เปิดไว้ที่ด้านหน้าเครื่องหมาย
* คำพูด แล้วใช้ {} ล้อมส่วนที่ต้องการแทรกค่าลงไป
"""
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
message = f"Hello, {full_name.title()}!"
print(message)
print(f"Hello, {full_name.title()}!")

