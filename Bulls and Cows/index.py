import random
from tkinter import *


class CowsAndBulls:
    def __init__(self):
        self.code = []
        self.window = Tk()
        self.frame = Frame(self.window)
        self.width = 300
        self.height = 250
        self.plus_height = 0
        self.guesses = 10
        self.input = None

    def setup(self):
        self.window.title('Bulls & Cows')
        width = (self.window.winfo_screenwidth() - self.width) / 2
        height = (self.window.winfo_screenheight() - self.height) / 2
        self.window.geometry(f'{self.width}x{self.height}+{int(width)}+{int(height)}')

        start_button = Button(self.window, text='START GAME', font='Calibri',
                              command=lambda: self.start_game_btn(start_button))
        start_button.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.code = self.generate_code()
        self.window.mainloop()

    def generate_code(self):
        random_code = list(str(random.randint(1000, 9999)))
        has_duplicates = self.duplicates_checker(random_code)
        if has_duplicates:
            return self.generate_code()
        return random_code

    @staticmethod
    def duplicates_checker(number):
        list_length = len(number)
        set_length = len(set(number))

        if list_length != set_length:
            return True
        return False

    def start_game_btn(self, start_button):
        # self.frame.grid(row=0, column=0)
        self.frame.place(relx=0.5, rely=0.5, anchor=CENTER)
        label = Label(self.frame, text='ENTER GUESS', font='Calibri', width=15).grid(row=0, column=0, pady=10, padx=10)
        self.input = Entry(self.frame, font='Calibri', width=15)
        self.input.grid(row=1, column=0, pady=10, padx=10)
        submit_guess_btn = Button(self.frame, text='SUBMIT', font='Calibri', width=10, command=self.play).grid(row=2, column=0, pady=10, padx=10)
        start_button.destroy()
        # self.frame.update()
        # print(self.frame.winfo_width())
        # print(self.frame.winfo_height())
        # code_label = Label(self.window, text=self.code, font='Calibri')
        # code_label.place(x=150, rely=0.05, anchor=CENTER)

    def play(self):
        if not self.guesses:
            [child.destroy() for child in self.frame.winfo_children()]
            self.window.geometry(f'{self.width}x{self.height}')
            message_label = Label(self.frame,
                                  text=f'You ran out of tries.\nThe correct code is {"".join(self.code)}',
                                  font='Calibri')
            message_label.place(relx=0.5, rely=0.4, anchor=CENTER)
            self.start_new_game()
        else:
            self.guesses -= 1
            guess = list(self.input.get())
            bulls = 0
            cows = 0

            if guess == self.code:
                [child.destroy() for child in self.frame.winfo_children()]
                message_label = Label(self.frame,
                                      text=f'Correct! The code is {"".join(self.code)}',
                                      font='Calibri')
                message_label.place(x=150, y=100, anchor=CENTER)
                self.start_new_game()

            else:
                for index, digit in enumerate(guess):
                    if digit == self.code[index]:
                        bulls += 1
                    elif digit in self.code:
                        cows += 1

                message_label = Label(self.frame, text=f'Guess: {"".join(guess)} (Bulls: {bulls}, Cows: {cows})',
                                      font='Calibri')
                # message_label.place(x=150, y=self.label_y, anchor=CENTER)
                message_label.grid()
                self.plus_height += 20
                self.window.geometry(f'300x{self.height + self.plus_height}')

    def start_new_game(self):
        retry_btn = Button(self.frame, text='RETRY', font='Calibri', command=self.new_game_setup)
        retry_btn.place(relx=0.5, rely=0.65, anchor=CENTER)

    def new_game_setup(self):
        [child.destroy() for child in self.frame.winfo_children()]
        self.guesses = 10
        self.plus_height = 0
        self.setup()
