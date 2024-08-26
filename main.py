from tkinter import *
import pandas
import random
import time
BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 60, "bold")
current_word = {}
removed_word = {}


try:
    df = pandas.read_csv("words_to_learn.csv")
except FileNotFoundError:
    df = pandas.read_csv("data/english_to_turkish.csv")
    data = df.to_dict(orient="records")
    # print(data)
else:
    data = df.to_dict(orient="records")

def next_card():
    global current_word, flip_timer
    # num = random.randint(0,199)
    window.after_cancel(flip_timer)
    current_word = random.choice(data)
    canvas.itemconfig(card_title, text="English", fill="black")
    canvas.itemconfig(card_word, text=current_word["English"], fill="black")
    canvas.itemconfig(card_img, image=card_front_img)
    flip_timer = window.after(3000, flip_card)

def flip_card():
    canvas.itemconfig(card_img, image=card_back_img)
    canvas.itemconfig(card_title, text="Turkish", fill="white")
    canvas.itemconfig(card_word, text=current_word["Turkish"].lower(), fill="white")

def check_button():
    data.remove(current_word)
    wrds_to_learn = pandas.DataFrame(data)
    wrds_to_learn.to_csv("data/words_to_learn", index=False)
    next_card()


window = Tk()
window.title("Flash Card App")
window.minsize(300,300)
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

#Buttons
r_image = PhotoImage(file=r"images\right.png")
r_button = Button(image=r_image, highlightthickness=0, command=check_button)
r_button.grid(row=1, column=1, pady=15)

w_image = PhotoImage(file=r"images\wrong.png")
w_button = Button(image=w_image, highlightthickness=0, command=next_card)
w_button.grid(row=1, column=0, pady=15)

#Flash Card
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file=r"images\card_front.png")
card_img = canvas.create_image(400,265, image=card_front_img)
card_title = canvas.create_text(400, 150, text="", fill="black", font=LANGUAGE_FONT)
card_word = canvas.create_text(400, 280, text="", fill="black", font=WORD_FONT)
card_back_img = PhotoImage(file=r"images\card_back.png")
canvas.grid(row=0, column=0, columnspan=2)

next_card()



window.mainloop()