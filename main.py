from gui import *

def main():
    window = Tk()
    window.title('Hearts')
    window.geometry('240x220')
    window.resizable(False, False)
    Gui(window)
    window.mainloop()

if __name__ == '__main__':
    main()

