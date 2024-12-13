from gui import *



def main():
    create_window()





def create_window() -> None:
    """
    Method to create tkinter gui window
    """
    window = Tk()
    window.title('Voting App')
    window.geometry('200x300')
    window.resizable(False, False)

    Gui(window)
    window.mainloop()




if __name__ == "__main__":
    main()

