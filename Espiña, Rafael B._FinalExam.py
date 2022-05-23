from tkinter import *

window = Tk()
window.title("Find The Least Number")
window.geometry("400x300+20+10")

# definition to find the smallest number
def findLeast():
    Numbers = []
    Numbers.append(eval(firstNumber.get()))
    Numbers.append(eval(secondNumber.get()))
    Numbers.append(eval(thirdNumber.get()))
    smallestNumber.set(min(Numbers))

# Labels, Input and Output
Label_1 = Label(window, text = "A Program That Finds The Smallest Number")
Label_1.grid(row=0, column=1, columnspan=2,sticky=EW)

Label_2 = Label(window,text = "Enter the first number:")
Label_2.grid(row=1, column = 0,sticky=W)
firstNumber = StringVar()
input_2 = Entry(window,bd=3,textvariable=firstNumber)
input_2.grid(row=1, column = 1)

Label_3 = Label(window,text = "Enter the second number:")
Label_3.grid(row=2, column=0)
secondNumber=StringVar()
input_3 = Entry(window,bd=3,textvariable=secondNumber)
input_3.grid(row=2,column=1)

Label_4 = Label(window,text="Enter the third number:")
Label_4.grid(row=3,column =0, sticky=W)
thirdNumber = StringVar()
input_4 = Entry(window,bd=3,textvariable=thirdNumber)
input_4.grid(row=3, column=1)

#button to start the function
buttonSmallest = Button(window,text = "Find The Smallest Number",command=findLeast)
buttonSmallest.grid(row=4, column = 1)

#output
Label_5 = Label(window,text="The Least Number: ")
Label_5.grid(row=5,column=0,sticky=W)
smallestNumber = StringVar()
input_5 = Entry(window,bd=3,state="readonly",textvariable=smallestNumber)
input_5.grid(row=5,column=1)


mainloop()
