from tkinter import *

window = Tk()
window.title("Find The Least Number")
window.geometry("400x300+20+10")

#
def findLeast():
    Numbers = []
    Numbers.append(eval(firstNumber.get()))
    Numbers.append(eval(secondNumber.get()))
    Numbers.append(eval(thirdNumber.get()))
    smallestNumber.set(min(Numbers))

lbl1 = Label(window, text = "A Program That Finds The Smallest Number")
lbl1.grid(row=0, column=1, columnspan=2,sticky=EW)

lbl2 = Label(window,text = "Enter the first number:")
lbl2.grid(row=1, column = 0,sticky=W)
firstNumber = StringVar()
ent2 = Entry(window,bd=3,textvariable=firstNumber)
ent2.grid(row=1, column = 1)

lbl3 = Label(window,text = "Enter the second number:")
lbl3.grid(row=2, column=0)
secondNumber=StringVar()
ent3 = Entry(window,bd=3,textvariable=secondNumber)
ent3.grid(row=2,column=1)

lbl4 = Label(window,text="Enter the third number:")
lbl4.grid(row=3,column =0, sticky=W)
thirdNumber = StringVar()
ent4 = Entry(window,bd=3,textvariable=thirdNumber)
ent4.grid(row=3, column=1)

btn1 = Button(window,text = "Find The Smallest Number",command=findLeast)
btn1.grid(row=4, column = 1)

lbl5 = Label(window,text="The Least Number: ")
lbl5.grid(row=5,column=0,sticky=W)
smallestNumber = StringVar()
ent5 = Entry(window,bd=3,state="readonly",textvariable=smallestNumber)
ent5.grid(row=5,column=1)


mainloop()
