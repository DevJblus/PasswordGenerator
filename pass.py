# coding: utf:8

import string
from random import randint, choice
from tkinter import *

def generate_password():
    password_min = 20
    password_max = 30
    all_chars = string.ascii_letters + string.punctuation + string.digits
    password = "".join(choice(all_chars) for x in range(randint(password_min, password_max)))
    password_entry.delete(0, END)
    password_entry.insert(0, password)

window = Tk()
window.title("PasswordGenerator - Version 1.0")
window.geometry("720x480")
window.iconbitmap("images/logo.ico")
window.config(background='#4065A4')

frame = Frame(window, bg='#4065A4')

width = 300
height = 300
image = PhotoImage(file="images/passcrack.png").zoom(35).subsample(32)
canvas = Canvas(frame, width=width, height=height, bg='#4065A4', bd=0, highlightthickness=0)
canvas.create_image(width/2, height/2, image=image)
canvas.grid(row=0, column=0, sticky=W)

right_frame = Frame(frame, bg='#4065A4')

label_title = Label(right_frame, text="Password", font=("Helvetica", 20), bg='#4065A4', fg='white')
label_title.pack()

password_entry = Entry(right_frame, font=("Helvetica", 20), bg='#4065A4', fg='white')
password_entry.pack()

generate_password_button = Button(right_frame, text="Generate", font=("Helvetica", 20), bg='#4065A4', fg='white', command=generate_password)
generate_password_button.pack(fill=X)

right_frame.grid(row=0, column=1, sticky=W)

frame.pack(expand=YES)

window.mainloop()