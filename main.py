from tkinter import *
from tkinter import messagebox
import random
import pyperclip

LOWERCASE_LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
UPPERCASE_LETTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SPECIAL_CHARACTERS = ["!", "(", ")", "-", ".", "?", "$", "%", "*"]


def create_random_password():
    random_characters = []
    for x in range(5):
        random_characters.append(random.choice(LOWERCASE_LETTERS))
        random_characters.append(random.choice(UPPERCASE_LETTERS))
        random_characters.append(random.choice(NUMBERS))
        random_characters.append(random.choice(SPECIAL_CHARACTERS))
    random.shuffle(random_characters)
    random_characters.insert(0, random.choice(LOWERCASE_LETTERS))
    password = "".join(random_characters)
    password_entry.insert(0, password)
    pyperclip.copy(password)


def add_button_clicked():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    formatted_entry = f"{website} | {username} | {password}\n"
    continue_on = True
    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        continue_on = False
        if len(website) == 0:
            messagebox.showwarning(title="Error", message="Make sure to enter a website")
        elif len(username) == 0:
            messagebox.showwarning(title="Error", message="Make sure to enter a email/username")
        elif len(password) == 0:
            messagebox.showwarning(title="Error", message="Make sure to enter a password")
    if continue_on:
        answer = messagebox.askyesno(message=f"Does this information look correct?\nWebsite: {website}\nUsername: {username}\nPassword: {password}")
        if answer == YES:
            with open(f"./password_list.txt", mode="a") as password_list:
                password_list.write(formatted_entry)
            website_entry.delete(0, END)
            password_entry.delete(0, END)

window = Tk()
window.title("Password Manager")
window.minsize(width=600, height=500)
window.config(padx=100, pady=100)
canvas = Canvas(width=200, height=200, highlightthickness=0)
password_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=password_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
username_label = Label(text="Email/Username:")
username_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

website_entry = Entry(width=38)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
username_entry = Entry(width=38)
username_entry.grid(row=2, column=1, columnspan=2)
username_entry.insert(0, "abc123@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

generate_password_button = Button(text="Generate Password", command=create_random_password)
generate_password_button.grid(row=3, column=2)
add_password = Button(text="Add", width=36, command=add_button_clicked)
add_password.grid(row=4, column=1, columnspan=2)

window.mainloop()
