import random
import tkinter as tk
from tkinter import font as tkfont
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from menu import MenuBar

import pandas

BACKGROUND_COLOR = "#B1DDC6"
curr_card = {}
to_learn = {}
name = []
lang1 = []
lang2 = []
applang = []

### WINDOW FOR CHOSING APP LANGUAGE ###
window = tk.Tk()
window.title('Your Name')
# window.geometry('590x350')
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
menubar = MenuBar(window)
window.config(menu=menubar)

# declaring string variable
# for storing name
app_lang_var = tk.StringVar()


def submit():
    applang_entered = app_lang_var.get()
    applang.append(applang_entered)
    window.destroy()


# label text for title
title_label = ttk.Label(window, text="Choose application language, please."
                                     "\n"
                                     "\nChoisissez la langue de l'application, s'il vous plaît. "
                                     "\n"
                                     "\nВыберите язык приложения, пожалуйста.",
                        background='green', foreground="white",
                        font=("Times New Roman", 17))

# Combobox creation
applangchosen = ttk.Combobox(window, state="readonly", textvariable=app_lang_var, width=27,
                             font=("Times New Roman", 14))

# Adding combobox drop down list
applangchosen['values'] = ('English',
                           'French',
                           'Russian')
applangchosen.current(0)

# creating a button using the widget
# Button that will call the submit function
sub_btn = tk.Button(window, text='Submit', background='green', foreground="white", font=("Times New Roman", 14),
                    command=submit)
# placing the label entry and button in
# the required position using grid
# method
title_label.grid(row=0, columnspan=2)
applangchosen.grid(row=1, column=0, pady=30)
sub_btn.grid(row=1, column=1, padx=10)

window.mainloop()

### WINDOW FOR CHOSING USERNAME ###
window = tk.Tk()
window.title('Your Name')
# window.geometry('720x500')
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
menubar = MenuBar(window)
window.config(menu=menubar)

# declaring string variable
# for storing name
name_var = tk.StringVar()


def submit():
    name_entered = name_var.get()
    if name_entered == "":
        pass
    else:
        name.append(name_entered)
        window.destroy()


# label text for title
if applang[0] == "English":
    title_label = ttk.Label(window, text="Enter your name so the program will create words to learn "
                                         "\nlist special for you."
                                         "\n"
                                         "\nNext time you launch the program, just enter your name again."
                                         "\n"
                                         "\nThank you!",
                            background='green', foreground="white",
                            font=("Times New Roman", 17))

    # label
    name_label = ttk.Label(window, text="Your name here, please :",
                           background='green', foreground="white",
                           font=("Times New Roman", 14))

elif applang[0] == "French":
    title_label = ttk.Label(window, text="Entrez votre nom et le programme créera une liste de mots"
                                         "\nà apprendre spécialement pour vous."
                                         "\n"
                                         "\nLa prochaine fois que vous démarrez le programme, entrez simplement "
                                         "\nà nouveau votre nom."
                                         "\n"
                                         "\nMerci!",
                            background='green', foreground="white",
                            font=("Times New Roman", 17))

    # label
    name_label = ttk.Label(window, text="Votre nom ici, s'il vous plaît :",
                           background='green', foreground="white",
                           font=("Times New Roman", 14))
elif applang[0] == "Russian":
    title_label = ttk.Label(window,
                            text="Введите ваше имя, и программа создаст список слов, "
                                 "\nкоторые нужно выучить специально для вас. "
                                 "\n"
                                 "\nВ следующий раз, когда вы запустите программу, "
                                 "\nпросто введите свое имя еще раз."
                                 "\n"
                                 "\nСпасибо!",
                            background='green', foreground="white",
                            font=("Times New Roman", 17))

    # label
    name_label = ttk.Label(window, text="Ваше имя, пожалуйста :",
                           background='green', foreground="white",
                           font=("Times New Roman", 14))

# Entry creation
name_entry = ttk.Entry(window, textvariable=name_var, font=('calibre', 17, 'normal'))

# creating a button using the widget
# Button that will call the submit function
sub_btn = tk.Button(window, text='Submit', background='green', foreground="white", font=("Times New Roman", 14),
                    command=submit)
# placing the label entry and button in
# the required position using grid
# method
title_label.grid(row=0, columnspan=2)
name_label.grid(row=1, column=0, padx=10, pady=30)
name_entry.grid(row=1, column=1, padx=10)
sub_btn.grid(row=2, columnspan=2, padx=10)

window.mainloop()

### WINDOW FOR CHOSING LANGUAGE PAIR ###
window = tk.Tk()
window.title('Chose Language Pair')
# window.geometry('700x250')
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
menubar = MenuBar(window)
window.config(menu=menubar)

# declaring string variable
# for storing name
lang1_var = tk.StringVar()
lang2_var = tk.StringVar()


def submit():
    lang1selected = lang1_var.get()
    lang2selected = lang2_var.get()
    lang1.append(lang1selected)
    lang2.append(lang2selected)
    window.destroy()


if applang[0] == "English":
    # label text for title
    title_label = ttk.Label(window, text="Here you can chose language pair to learn!",
                            background='green', foreground="white",
                            font=("Times New Roman", 17))

    # label
    select_label = ttk.Label(window, text="Select language pair :",
                             background='green', foreground="white",
                             font=("Times New Roman", 15))
elif applang[0] == "French":
    # label text for title
    title_label = ttk.Label(window, text="Ici, vous pouvez choisir la paire de langues à apprendre !",
                            background='green', foreground="white",
                            font=("Times New Roman", 17))

    # label
    select_label = ttk.Label(window, text="Sélectionnez la paire de langues :",
                             background='green', foreground="white",
                             font=("Times New Roman", 15))
elif applang[0] == "Russian":
    # label text for title
    title_label = ttk.Label(window, text="Здесь вЫ можете выбрать языковую пару для изучения",
                            background='green', foreground="white",
                            font=("Times New Roman", 17))

    # label
    select_label = ttk.Label(window, text="Выберите желаемые языки :",
                             background='green', foreground="white",
                             font=("Times New Roman", 15))

# creating a button using the widget
# Button that will call the submit function
sub_btn = tk.Button(window, text='Submit', background='green', foreground="white", font=("Times New Roman", 14),
                    command=submit)

# Combobox creation
lang1chosen = ttk.Combobox(window, state="readonly", textvariable=lang1_var, width=27, font=("Times New Roman", 14))

# Adding combobox drop down list
lang1chosen['values'] = ('English',
                         'French',
                         'Russian')
lang1chosen.current(0)

lang2chosen = ttk.Combobox(window, state="readonly", textvariable=lang2_var, width=27, font=("Times New Roman", 14))

# Adding combobox drop down list
lang2chosen['values'] = ('English',
                         'French',
                         'Russian')
lang2chosen.current(1)

title_label.grid(row=0, columnspan=3)
select_label.grid(row=1, column=0, padx=10, pady=30)
lang1chosen.grid(row=1, column=1, padx=10)
lang2chosen.grid(row=1, column=2, padx=10)
lang1chosen.current()
sub_btn.grid(row=2, columnspan=3)

window.mainloop()



### WINDOW FOR MAIN PROGRAMM ###
window = Tk()
window.title("Lingua Cards")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
menubar = MenuBar(window)
window.config(menu=menubar)


### LMP LOGIC CODE ###

### open data file or create it if not existing ###
try:
    data = pandas.read_csv(f"data/{name[0]}_words_to_learn_{lang1[0]}_{lang2[0]}.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


### choosing next card to show ###
def next_card():
    global curr_card, flip_timer
    window.after_cancel(flip_timer)
    curr_card = random.choice(to_learn)
    canvas.itemconfig(card_img, image=front_img)
    canvas.itemconfig(card_lang, text=f"{lang1[0]}", fill="black")
    canvas.itemconfig(card_word, text=curr_card[f"{lang1[0]}"], fill="black")
    flip_timer = window.after(5000, flip_card)


### flip a card  ###
def flip_card():
    canvas.itemconfig(card_img, image=back_img)
    canvas.itemconfig(card_lang, text=f"{lang2[0]}", fill="white")
    canvas.itemconfig(card_word, text=curr_card[f"{lang2[0]}"], fill="white")


### handle words you already know ###
def i_know():
    if applang[0] == "English":
        try:
            to_learn.remove(curr_card)
            data = pandas.DataFrame(to_learn)
            data.to_csv(f"data/{name[0]}_words_to_learn_{lang1[0]}_{lang2[0]}.csv", index=False)
            next_card()

        except ValueError:
            messagebox.showinfo(title="Oops", message="Seems you've learned all the words!")
        except IndexError:
            messagebox.showinfo(title="Oops", message="Seems you've learned all the words!")
    elif applang[0] == "French":
        try:
            to_learn.remove(curr_card)
            data = pandas.DataFrame(to_learn)
            data.to_csv(f"data/{name[0]}_words_to_learn_{lang1[0]}_{lang2[0]}.csv", index=False)
            next_card()

        except ValueError:
            messagebox.showinfo(title="Oops", message="On dirait que vous avez appris tous les mots !")
        except IndexError:
            messagebox.showinfo(title="Oops", message="On dirait que vous avez appris tous les mots !")

    elif applang[0] == "Russian":
        try:
            to_learn.remove(curr_card)
            data = pandas.DataFrame(to_learn)
            data.to_csv(f"data/{name[0]}_words_to_learn_{lang1[0]}_{lang2[0]}.csv", index=False)
            next_card()

        except ValueError:
            messagebox.showinfo(title="Упс", message="Похоже, вы выучили все слова!")
        except IndexError:
            messagebox.showinfo(title="Упс", message="Похоже, вы выучили все слова!")

### Next card and check if any card left ###
def i_dont_know():
    if applang[0] == "English":
        try:
            next_card()
        except IndexError:
            messagebox.showinfo(title="Oops", message="There is no words left!")
    elif applang[0] == "French":
        try:
            next_card()
        except IndexError:
            messagebox.showinfo(title="Oops", message="Il n'y a plus de mots !")
    elif applang[0] == "Russian":
        try:
            next_card()
        except IndexError:
            messagebox.showinfo(title="Упс", message="Не осталось слов!")


flip_timer = window.after(3000, flip_card)

canvas = Canvas(bg=BACKGROUND_COLOR, width=800, height=526, highlightthickness=0)
front_img = PhotoImage(file="images/card_front.png")
back_img = PhotoImage(file="images/card_back.png")
card_img = canvas.create_image(400, 263, image=front_img)
card_lang = canvas.create_text(400, 150, text="Language", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# buttons
right_img = PhotoImage(file="images/right.png")
wrong_img = PhotoImage(file="images/wrong.png")

right_b = Button(image=right_img, highlightthickness=0, command=i_know)
right_b.grid(column=0, row=1, padx=50)
wrong_b = Button(image=wrong_img, highlightthickness=0, command=i_dont_know)
wrong_b.grid(column=1, row=1, padx=50)

next_card()

window.mainloop()
