import os
import sys
import tkinter

root = tkinter.Tk()
root.title("Hello")
root.iconbitmap(os.path.join(sys.path[0],"./thinking.ico"))
root.geometry('400x400')
root.resizable(0,0)
root.config(bg='blue')

name_label_1 = tkinter.Label(root,text='Hello', font=('Arial', 18, 'bold'))
name_label_1.pack()

name_label_2 = tkinter.Label(root)
name_label_2.config

root.mainloop()
