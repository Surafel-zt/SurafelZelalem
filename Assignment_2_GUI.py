from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Assignment 2 GUI')

# Answers in order ( d , g , f , e , 3 )

def answer():
    a = entry_a.get().upper()
    b = entry_b.get().upper()
    c = entry_c.get().upper()
    d = entry_d.get().upper()
    e = int(entry_e.get())
    if a == "D" and b == "G" and c == "F" and d == "E" and e == 3:
        correct = Label(top, text="You are correct!", font=('Verdana', 12), fg="green")
        correct.grid(row=6, column=1)
    else:
        not_correct = Label(top, text="you are Incorrect! Close both windows and try again", font=('Verdana', 12), fg="Red")
        not_correct.grid(row=6, column=1)


def popup():
    response = messagebox.askyesno("Choose yes or no", "Do you want to continue?")
    if response == 1:
        global answer
        global a
        global b
        global c
        global d
        global e
        global entry_a
        global entry_b
        global entry_c
        global entry_d
        global entry_e
        global top

        top = Toplevel()
        top.title('Answers')
        question_1 = Label(top, text="Who lives in the second corner?", font=('Verdana', 12))
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

    else:
        Label(root, text='You have chose NO, Good bye!').pack()


instruction = Label(root, text="""Read the following Scenario. If you understand the Scenario and want to continue click Yes.
If you do not understand the scenario and do not want to continue click No. There is 1 house between D and 
F. C is between E and G. F is neighbor of G.There are two houses between A and G.""",
                    font=('verdana, 13'), bg='white')
instruction.pack()

Button(root, text='Click to choose yes/no', font=('verdana, 13'), bg='#345DE4', fg='white', command=popup).pack()



root.mainloop()
