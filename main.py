from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    password_letters = [choice(letters) for letter in range(nr_letters)]

    password_symbols = [choice(symbols) for symbol in range(nr_symbols)]

    password_numbers = [choice(numbers) for number in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)

    entry_password.delete(0, END)
    entry_password.insert(END, string=password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_data():
    website = entry_website.get()
    email = entry_email_username.get()
    password = entry_password.get()
    if website == '' or email == '' or password == '':
        messagebox.showinfo(title="Error", message="Please don't leave any fields empty!")
        return
    is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: "
                                                          f"{email}\nPassword: {password}\nIs it okay to save?")
    if is_ok:
        with open("data.txt", mode="a") as file:
            file.write(f"{website} | {email} | {password}\n")
        entry_website.delete(0, END)
        entry_email_username.delete(0, END)
        entry_password.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")

canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(column=1, row=0)

label_website = Label(text="Website:", bg="white")
label_website.grid(column=0, row=1)

label_email_username = Label(text="Email/Username:", bg="white")
label_email_username.grid(column=0, row=2)

label_password = Label(text="Password:", bg="white")
label_password.grid(column=0, row=3)

entry_website = Entry(width=43)
entry_website.grid(column=1, columnspan=2, row=1, sticky=(N, E))
entry_website.focus()

entry_email_username = Entry(width=43)
entry_email_username.grid(column=1, columnspan=2, row=2, sticky=(N, E))

entry_password = Entry(width=25)
entry_password.grid(column=1, row=3, sticky=(N, E))

button_generate_password = Button(text="Generate Password", width=14, command=generate_password)
button_generate_password.grid(column=2, row=3)

button_add = Button(text="Add", width=36, command=save_data)
button_add.grid(column=1, columnspan=2, row=4, sticky=(N, E))

window.mainloop()
