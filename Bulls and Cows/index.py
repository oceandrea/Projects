import random
from tkinter import *


class CowsAndBulls:
    def __init__(self):
        self.code = []
        self.window = None
        self.height = 250
        self.guess = None
        self.guesses = 10
        self.label_y = 225
        self.input_label = None
        self.input = None
        self.submit_btn = None

    @classmethod
    def new_game(cls):
        return cls()

    def setup(self):
        self.window = Tk()
        self.window.title('Bulls & Cows')
        self.window.geometry(f'300x{self.height}')
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
        label = Label(self.window, text='ENTER GUESS', font='Calibri')
        self.input_label = label
        label.place(x=150, y=75, anchor=CENTER)
        self.guess = StringVar()
        input_for_label = Entry(self.window, textvariable=self.guess, font='Calibri')
        self.input = input_for_label
        input_for_label.place(x=150, y=125, anchor=CENTER)
        submit_guess_btn = Button(self.window, text='SUBMIT', font='Calibri', command=self.play)
        self.submit_btn = submit_guess_btn
        submit_guess_btn.place(x=150, y=175, anchor=CENTER)
        start_button.destroy()
        # code_label = Label(self.window, text=self.code, font='Calibri')
        # code_label.place(x=150, rely=0.05, anchor=CENTER)
        # code_label.place_forget()

    def play(self):
        if not self.guesses:
            self.destroy_input()
            message_label = Label(self.window,
                                  text=f'You ran out of tries.\nThe correct code is {"".join(self.code)}',
                                  font='Calibri')
            message_label.place(x=150, y=100, anchor=CENTER)
            self.start_new_game()
        else:
            self.guesses -= 1
            guess = list(self.guess.get())
            bulls = 0
            cows = 0

            if guess == self.code:
                self.destroy_input()
                message_label = Label(self.window,
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

                message_label = Label(self.window, text=f'Guess: {"".join(guess)} (Bulls: {bulls}, Cows: {cows})',
                                      font='Calibri')
                message_label.place(x=150, y=self.label_y, anchor=CENTER)
                self.label_y += 20
                self.height += 20
                self.window.geometry(f'300x{self.height}')

    def destroy_input(self):
        self.input_label.destroy()
        self.input.destroy()
        self.submit_btn.destroy()

    def start_new_game(self):
        retry_btn = Button(self.window, text='RETRY', font='Calibri', command=self.new_game_setup)
        retry_btn.place(x=150, y=150, anchor=CENTER)

    def new_game_setup(self):
        self.window.update()
        game = self.new_game()
        game.setup()
