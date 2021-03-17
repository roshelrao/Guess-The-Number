import random 
from tkinter import * 
from tkinter import messagebox 

window = Tk()

window.geometry("150x100")

num =0

Label1 = Label(window, text="Guess the number")
Label1.pack()

#generate random number

random_num = random.randint(0,100)
print(random_num)

input_box = Entry(window,bd = 5)
input_box.pack()

def getNum():
    num=int(input_box.get())
    print(num)
    if random_num==num:
        messagebox.showinfo("Result", "Correct")
    else:
        messagebox.showinfo("Result", "Incorrect")

button = Button(window,text="Enter",command=getNum)

button.pack()
window.mainloop()
