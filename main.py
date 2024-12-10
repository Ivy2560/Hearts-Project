from gui import *

def main():
    """

    :return:
    """
    window = Tk()
    window.title('Hearts')
    window.geometry('1100x700')
    window.resizable(False, False)
    Gui(window)
    window.mainloop()

if __name__ == '__main__':
    main()

