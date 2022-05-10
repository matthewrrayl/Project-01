# Matthew Rayl Project 1
from Project_1_GUI import *

def main():
    window = Tk()
    window.title('Project 01')
    window.geometry('300x100')
    window.resizable(False, False)

    widgets = GUI(window)
    window.mainloop()

if __name__ == '__main__':
    main()