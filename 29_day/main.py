from tkinter import *
import random
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    pass_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    for char in range(nr_symbols):
        password_list += random.choice(symbols)

    for char in range(nr_numbers):
        password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char
    pass_entry.insert(0, password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = pass_entry.get()
    with open('passwords.txt', 'a') as file:
        file.write(f"{website} | {email} | {password}\n")
        website_entry.delete(0, END)
        pass_entry.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

website_label = Label(text='Website:', font=('Courier', 12, 'bold'))
website_label.grid(column=0, row=1, sticky='e')

website_entry = Entry(width=54)
website_entry.grid(column=1, row=1, columnspan=2, sticky='w')
website_entry.focus()

email_label = Label(text='Email/Username:', font=('Courier', 12, 'bold'))
email_label.grid(column=0, row=2, sticky='e')

email_entry = Entry(width=54)
email_entry.grid(column=1, row=2, columnspan=2, sticky='w')
email_entry.insert(0, "suchastupidme@gmail.com")

pass_label = Label(text='Password:', font=('Courier', 12, 'bold'))
pass_label.grid(column=0, row=3, sticky='e')

pass_entry = Entry(width=33)
pass_entry.grid(column=1, row=3, sticky='w')

generate_pass_btn = Button(text='Generate Password', width=16, command=generate_password)
generate_pass_btn.grid(column=2, row=3, sticky='w')

add_btn = Button(text='Add', width=46, command=save_password)
add_btn.grid(column=1, row=4, columnspan=2, sticky='w')

window.mainloop()
