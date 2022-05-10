from tkinter import *

class GUI:
    def __init__(self, window):
        self.window = window
        self.num_list = []
        self.label_input = Label(self.window, text='Input Variable')
        self.entry_input = Entry(self.window)
        self.button_done = Button(self.window, text='DONE', command=self.done)
        self.button_enter = Button(self.window, text='ENTER', command=self.enter)

        self.label_input.pack(side='top')
        self.entry_input.pack(side='left', padx=10)
        self.button_enter.pack(side='left', padx=10)
        self.button_done.pack(side='left', padx=10)

    def enter(self):
        num = int(self.entry_input.get())
        self.num_list.append(num)
        self.entry_input.delete(0, END)

    def done(self):
        self.window.destroy()
        print(f'Minimum: {min(self.num_list)}')
        print(f'Maximum: {max(self.num_list)}')
        print(f'Sum: {sum(self.num_list)}')
        print(f'Count: {len(self.num_list)}')