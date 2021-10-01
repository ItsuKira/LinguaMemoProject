import tkinter as tk                # python 3
from tkinter import font as tkfont  # python 3
import random
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import pandas
from menu import MenuBar


BACKGROUND_COLOR = "#B1DDC6"
curr_card = {}
to_learn = {}
name = [""]
lang1 = ["French"]
lang2 = ["English"]
# applangs = ["English", "French", "Russian"]
applang = ["English"]



class LMP(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        menubar = MenuBar(self)
        # self.geometry('1100x600')
        self.config(menu=menubar)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
        container.grid()
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (MainPage, AppLangSel, NameSel, LangPairSel):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("AppLangSel", applang, name, lang1, lang2)


    def show_frame(self, page_name, page_lang, username, lang1, lang2):
        '''Show a frame for the given page name'''
        inserted_user = username
        name.clear()
        applang.append(inserted_user)
        sel_lang1 = lang1
        lang1.clear()
        applang.append(sel_lang1)
        sel_lang2 = lang2
        lang2.clear()
        applang.append(sel_lang2)
        selected_lang = page_lang
        applang.clear()
        applang.append(selected_lang)
        frame = self.frames[page_name]
        frame.tkraise()


class AppLangSel(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        # declaring string variable
        # for storing name
        app_lang_var = tk.StringVar()

        def submit():
            applang_entered = app_lang_var.get()
            # applang.clear()
            # applang.append(applang_entered)
            controller.show_frame("NameSel", applang_entered, username="")
            self.destroy()
            # self.destroy()

        # label text for title
        title_label = ttk.Label(self, text="Choose application language, please."
                                             "\n"
                                             "\nChoisissez la langue de l'application, s'il vous plaît. "
                                             "\n"
                                             "\nВыберите язык приложения, пожалуйста.",
                                background='green', foreground="white",
                                font=("Times New Roman", 17))

        # Combobox creation
        applangchosen = ttk.Combobox(self, state="readonly", textvariable=app_lang_var, width=27,
                                     font=("Times New Roman", 14))

        # Adding combobox drop down list
        applangchosen['values'] = ('English',
                                   'French',
                                   'Russian')
        applangchosen.current(0)

        # creating a button using the widget
        # Button that will call the submit function
        sub_btn = tk.Button(self, text='Submit', background='green', foreground="white", font=("Times New Roman", 14),
                            command=submit)
        # placing the label entry and button in
        # the required position using grid
        # method
        title_label.grid(row=0, columnspan=2)
        applangchosen.grid(row=1, column=0, pady=30)
        sub_btn.grid(row=1, column=1, padx=10)


class NameSel(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        # declaring string variable
        # for storing name
        name_var = tk.StringVar()

        def submit():
            name_entered = name_var.get()
            name.append(name_entered)
            controller.show_frame("LangPairSel", applang[0], username=name_var)

        # label text for title
        if applang[0] == "English":
            title_label = ttk.Label(self, text="Enter your name so the program will create words to learn "
                                                 "\nlist special for you."
                                                 "\n"
                                                 "\nNext time you launch the program, just enter your name again."
                                                 "\n"
                                                 "\nThank you!",
                                    background='green', foreground="white",
                                    font=("Times New Roman", 17))

            # label
            name_label = ttk.Label(self, text="Your name here, please :",
                                   background='green', foreground="white",
                                   font=("Times New Roman", 14))

        elif applang[0] == "French":
            title_label = ttk.Label(self, text="Entrez votre nom et le programme créera une liste de mots"
                                                 "\nà apprendre spécialement pour vous."
                                                 "\n"
                                                 "\nLa prochaine fois que vous démarrez le programme, entrez simplement "
                                                 "\nà nouveau votre nom."
                                                 "\n"
                                                 "\nMerci!",
                                    background='green', foreground="white",
                                    font=("Times New Roman", 17))

            # label
            name_label = ttk.Label(self, text="Votre nom ici, s'il vous plaît :",
                                   background='green', foreground="white",
                                   font=("Times New Roman", 14))
        elif applang[0] == "Russian":
            title_label = ttk.Label(self,
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
            name_label = ttk.Label(self, text="Ваше имя, пожалуйста :",
                                   background='green', foreground="white",
                                   font=("Times New Roman", 14))

        # Entry creation
        name_entry = ttk.Entry(self, textvariable=name_var, font=('calibre', 17, 'normal'))

        # creating a button using the widget
        # Button that will call the submit function
        sub_btn = tk.Button(self, text='Submit', background='green', foreground="white", font=("Times New Roman", 14),
                            command=submit)
        # placing the label entry and button in
        # the required position using grid
        # method
        title_label.grid(row=0, columnspan=2)
        name_label.grid(row=1, column=0, padx=10, pady=30)
        name_entry.grid(row=1, column=1, padx=10)
        sub_btn.grid(row=2, columnspan=2, padx=10)



class LangPairSel(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        # declaring string variable
        # for storing name
        lang1_var = tk.StringVar()
        lang2_var = tk.StringVar()

        def submit():
            lang1selected = lang1_var.get()
            lang2selected = lang2_var.get()
            lang1.append(lang1selected)
            lang2.append(lang2selected)
            controller.show_frame("MainPage", applang[0])

        if applang[0] == "English":
            # label text for title
            title_label = ttk.Label(self, text="Here you can chose language pair to learn!",
                                    background='green', foreground="white",
                                    font=("Times New Roman", 17))

            # label
            select_label = ttk.Label(self, text="Select language pair :",
                                     background='green', foreground="white",
                                     font=("Times New Roman", 15))
        elif applang[0] == "French":
            # label text for title
            title_label = ttk.Label(self, text="Ici, vous pouvez choisir la paire de langues à apprendre !",
                                    background='green', foreground="white",
                                    font=("Times New Roman", 17))

            # label
            select_label = ttk.Label(self, text="Sélectionnez la paire de langues :",
                                     background='green', foreground="white",
                                     font=("Times New Roman", 15))
        elif applang[0] == "Russian":
            # label text for title
            title_label = ttk.Label(self, text="Здесь вЫ можете выбрать языковую пару для изучения",
                                    background='green', foreground="white",
                                    font=("Times New Roman", 17))

            # label
            select_label = ttk.Label(self, text="Выберите желаемые языки :",
                                     background='green', foreground="white",
                                     font=("Times New Roman", 15))

        # creating a button using the widget
        # Button that will call the submit function
        sub_btn = tk.Button(self, text='Submit', background='green', foreground="white", font=("Times New Roman", 14),
                            command=submit)

        # Combobox creation
        lang1chosen = ttk.Combobox(self, state="readonly", textvariable=lang1_var, width=27,
                                   font=("Times New Roman", 14))

        # Adding combobox drop down list
        lang1chosen['values'] = ('English',
                                 'French',
                                 'Russian')
        lang1chosen.current(0)

        lang2chosen = ttk.Combobox(self, state="readonly", textvariable=lang2_var, width=27,
                                   font=("Times New Roman", 14))

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



class MainPage(tk.Frame):


    def __init__(self, parent, controller):
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
            self.after_cancel(self.flip_timer)
            curr_card = random.choice(to_learn)
            canvas.itemconfig(card_img, image=front_img)
            canvas.itemconfig(card_lang, text=f"{lang1[0]}", fill="black")
            canvas.itemconfig(card_word, text=curr_card[f"{lang1[0]}"], fill="black")
            self.flip_timer = self.after(5000, flip_card)

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

        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.flip_timer = self.after(3000, flip_card)

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





if __name__ == "__main__":
    app = LMP()
    app.mainloop()