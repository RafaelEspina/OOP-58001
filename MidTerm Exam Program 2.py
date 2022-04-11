from tkinter import *
window=Tk()

def InputName():
    name['text'] = 'Enter your name here'

label = Label(text='Enter your Fullname:', fg='red')
label.place(x=30, y=50)

button = Button(text='Click to display your Fullname', fg='red', command=InputName)
button.place(x=30, y=100)

entername = Entry(textvariable='Enter your name here', bd='5')
entername.place(x=230, y=50)

name = Entry(text='place name here', bd='5')
name.place(x=230, y=100)

window.title('Midterm in OOP')
window.geometry("500x200+10+10")
window.mainloop()