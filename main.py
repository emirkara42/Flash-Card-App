from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 60, "bold")




df = pandas.read_csv("english_to_turkish.csv")
data = df.to_dict()
num = random.randint(0,199)
english_word = data["English"][num]
turkish_word = data["Turkish"][num]


window = Tk()
window.title("Flash Card App")
window.minsize(300,300)
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

#Buttons
r_image = PhotoImage(file=r"..\..\GitHub\Flash-Card-App\images\right.png")
r_button = Button(image=r_image, highlightthickness=0)
r_button.grid(row=1, column=1, pady=15)

w_image = PhotoImage(file=r"..\..\GitHub\Flash-Card-App\images\wrong.png")
w_button = Button(image=w_image, highlightthickness=0)
w_button.grid(row=1, column=0, pady=15)

#Flash Card
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file=r"..\..\GitHub\Flash-Card-App\images\card_front.png")
canvas.create_image(400,265, image=card_front_img)
canvas.create_text(400, 150, text="English", fill="black", font=LANGUAGE_FONT)
canvas.create_text(400, 280, text=english_word, fill="black", font=WORD_FONT)
canvas.grid(row=0, column=0, columnspan=2)





window.mainloop()