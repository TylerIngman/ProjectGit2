from tkinter import *

from voting_logic import check_id


class Gui:
    def __init__(self, window) -> None:
        """
        Method to create gui
        :param window:
        """
        self.window = window

        #Frame one, label and id
        self.frame_one = Frame(self.window)
        self.label_frame_one = Label(self.frame_one, text='Voting Application', font=('Arial,', 15), pady = 5)
        self.label_frame_one.pack()
        self.label_id = Label(self.frame_one, text = "ID", font = ('Arial', 13), pady=20, padx = 5)
        self.entry_id = Entry(self.frame_one, width=20)
        self.label_id.pack(side = 'left')
        self.entry_id.pack(side = 'left')
        self.frame_one.pack()

        #Frame two, candidates
        self.frame_two = Frame(self.window)
        self.label_candidates = Label(self.frame_two, text = 'CANDIDATES', font = ('Arial', 10))
        self.radio1 = IntVar()
        self.radio1.set(0)
        self.candidate_1 = Radiobutton(self.frame_two, text='Jane', variable=self.radio1, value=1)
        self.candidate_2 = Radiobutton(self.frame_two, text= 'John', variable= self.radio1, value = 2)
        self.label_candidates.pack()
        self.candidate_1.pack()
        self.candidate_2.pack()
        self.frame_two.pack()

        #Frame three, vote button and label
        self.frame_button = Frame(self.window)
        self.button_vote = Button(self.frame_button, text='Submit Vote', command = self.vote)
        self.button_vote.pack(pady=10)
        self.frame_button.pack()

        #Frame four, result label
        self.frame_result = Frame(self.window)
        self.label_result = Label(self.frame_result)
        self.label_result.pack(pady=10)
        self.frame_result.pack()





    def vote(self) -> None:
        """
        Method for vote button, sets return message and calls voting logic to be executed
        """
        try:
            id = int(self.entry_id.get())
            candidate = self.radio1.get()
            if candidate == 0:
                self.label_result.config(text = "Select a candidate", fg = 'red')
                return
            if len(str(id)) != 6:
                self.label_result.config(text = "ID must be 6 numbers", fg = 'red')
                return
            if check_id(id, candidate) == "Already Voted":
                self.label_result.config(text = "Already voted", fg='red')
            else:
                self.label_result.config(text = "Voted successfully", fg = 'black')


        except ValueError:
            self.label_result.config(text='Enter numeric values', fg = 'red')
        except TypeError:
            self.label_result.config(text='Values must be positive', fg = 'red')

