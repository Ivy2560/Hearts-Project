from gui import *

def main() -> None:
    """
    Runs the game hearts
    :return: None
    """
    window = Tk()
    window.title('Hearts')
    window.geometry('1300x700')
    window.resizable(False, False)
    Gui(window)
    window.mainloop()

if __name__ == '__main__':
    main()

