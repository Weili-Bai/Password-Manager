from tkinter import *
from tkinter import messagebox
from GeneratePassword import get_password
from pyperclip import copy
import json

BIG_WIDTH = 35
SMALL_WIDTH = 30
FILE_PATH = "./data.json"


def write_data():
    is_good_entry = True
    website = website_input.get().lower()
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
    new_data = {website: {"username": username, "password": password}}
    is_to_save = messagebox.askokcancel(title=website,
                                        message=f"These are the details:\nUser name: {username}\nPassword: {password}\n Is it OK to save?")
    if is_to_save:
        try:
            with open(FILE_PATH, 'r') as file:
                data = json.load(file)
                data.update(new_data)
        except FileNotFoundError:
            with open(FILE_PATH, 'w') as file:
                json.dump(new_data, file, indent=4)
        else:
            with open(FILE_PATH, 'w') as file:
                json.dump(data, file, indent=4)
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)
            messagebox.showinfo(title="Success", message="Information added.")


def generate_password():
    pw = get_password()
    password_input.delete(0, END)
    password_input.insert(END, pw)
    copy(pw)


def search_info():
    website = website_input.get().lower()
    if len(website) == 0:
        messagebox.showinfo(title="Error", message="Please enter a website!")
        return
    try:
        with open(FILE_PATH) as file:
            data = json.load(file)
            info = data[website]
            messagebox.showinfo(title=website,
                                message=f"username:   {info["username"]}\npassword:   {info["password"]}")
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="File not found!")
    except KeyError:
        messagebox.showinfo(title="Error", message="No such website on file!")


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

website_input = Entry(width=BIG_WIDTH)
website_input.grid(row=1, column=1, columnspan=2)
website_input.focus()
username_input = Entry(width=BIG_WIDTH)
username_input.grid(row=2, column=1, columnspan=2)
username_input.insert(index=0, string="fireonearth35@gmail.com")
password_input = Entry(width=SMALL_WIDTH)
password_input.grid(row=3, column=1, columnspan=1)

generate = Button(text="Generate", command=generate_password)
generate.grid(row=3, column=4)
add = Button(text="Add", command=write_data,
             width=BIG_WIDTH)
add.grid(row=4, column=1, columnspan=2)
search_button = Button(text="Search", command=search_info)
search_button.grid(row=1, column=4)
window.mainloop()
