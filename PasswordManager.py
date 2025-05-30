from tkinter import *
from tkinter import messagebox
from GeneratePassword import get_password
from pyperclip import copy


def write_data():
    is_good_entry = True
    website = website_input.get()
    if len(website) == 0:
        is_good_entry = False
    username = username_input.get()
    if len(username) == 0:
        is_good_entry = False
    password = password_input.get()
    if len(password) == 0:
        is_good_entry = False
    if not is_good_entry:
        messagebox.showinfo(title="Error", message="Please don't leave empty fields!")
        return
    is_to_save = messagebox.askokcancel(title=website,
                                        message=f"These are the details:\nUser name: {username}\nPassword: {password}\n Is it OK to save?")
    if is_to_save:
        with open("./data.txt", 'a') as file:
            file.write(f"{website} | {username} | {password}\n")
            website_input.delete(0, END)
            password_input.delete(0, END)
        messagebox.showinfo(title="Success", message="Information added.")


def generate_password():
    pw = get_password()
    password_input.insert(END, pw)
    copy(pw)


window = Tk()
window.title("Password Manager")
window.config(padx=25, pady=25)
canvas = Canvas(width=200, height=200)
lock = PhotoImage(file="./logo.png")
canvas.create_image(100, 100, image=lock)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
username_label = Label(text="Email/Username:")
username_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

website_input = Entry(width=55)
website_input.grid(row=1, column=1, columnspan=2)
website_input.focus()
username_input = Entry(width=55)
username_input.grid(row=2, column=1, columnspan=2)
username_input.insert(index=0, string="fireonearth35@gmail.com")
password_input = Entry(width=30)
password_input.grid(row=3, column=1, columnspan=1)

generate = Button(text="Generate Password", command=generate_password)
generate.grid(row=3, column=2)
add = Button(text="Add", command=write_data,
             width=55)
add.grid(row=4, column=1, columnspan=2)
window.mainloop()
