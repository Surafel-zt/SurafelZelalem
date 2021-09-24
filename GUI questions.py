from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Assignment 2 GUI')


question_1 = Label(root, text="Who lives in the second corner?", font=('Verdana', 12))
question_1.grid(row=0, column=0)
question_2 = Label(top, text="Who lives in the middle?", font=('Verdana', 12))
question_2.grid(row=1, column=0)
question_3 = Label(top, text="Who lives between B and G?", font=('Verdana', 12))
question_3.grid(row=2, column=0)
question_4 = Label(top, text="Who is the neighbor of A?", font=('Verdana', 12))
question_4.grid(row=3, column=0)
question_5 = Label(top, text="How many houses are there between B and E? (only numbers)", font=('Verdana', 12))
question_5.grid(row=4, column=0)

entry_a = Entry(top, width=25, borderwidth=8)
entry_a.grid(row=0, column=1)
entry_b = Entry(top, width=25, borderwidth=8)
entry_b.grid(row=1, column=1)
entry_c = Entry(top, width=25, borderwidth=8)
entry_c.grid(row=2, column=1)
entry_d = Entry(top, width=25, borderwidth=8)
entry_d.grid(row=3, column=1)
entry_e = Entry(top, width=25, borderwidth=8)
entry_e.grid(row=4, column=1)
answer = Button(top, text='Answer', font=('Verdana', 12), command=answer)
answer.grid(row=5, column=1)



instruction = Label(root, text="""Read the following Scenario. If you understand the Scenario and want to continue click Yes.
If you do not understand the scenario and do not want to continue click No. There is 1 house between D and 
F. C is between E and G. F is neighbor of G.There are two houses between A and G.""",
                    font=('verdana, 13'), bg='white')
instruction.pack()

Button(root, text='Click to choose yes/no', font=('verdana, 13'), bg='#345DE4', fg='white', command=popup).pack()



root.mainloop()
