from tkinter import *
import requests


def get_quote():
    response = requests.get('https://api.kanye.rest')
    if response.ok:
        canvas.itemconfig(quote_text, text=response.json()['quote'])


window = Tk()
window.title('Kanye Says...')
window.config(padx=20, pady=20)

canvas = Canvas(width=300, height=414)
canvas.config(highlightthickness=0)
quote_img = PhotoImage(file='background.png')
canvas.create_image(150, 207, image=quote_img)
canvas.grid(row=0, column=0)
quote_text = canvas.create_text(150, 207, width=250, font=('Ariel', 20, 'bold'), fill='white')

kanye_img = PhotoImage(file='kanye.png')
kanye_btn = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_btn.grid(row=1, column=0)


window.mainloop()
