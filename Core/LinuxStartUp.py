from tkinter import *

def Linux():
    win = Tk()
    win.geometry("350x70")
    win.title('Password')
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    window_width = 380
    window_height = 80
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2

    win.geometry(f"{window_width}x{window_height}+{x}+{y}")
    win.maxsize(380, 80)
    win.minsize(380, 80)

    def printInput():
        global pwd
        pwd = password.get()
        win.destroy()

    Label(win, text="sudo Password:", font=('Helvetica', 12)).grid(row=0,column=0, padx=10)
    password = Entry(win, show="*", width=20)
    password.grid(row=0,column=1, padx=20, pady=5)

    Button(win, text="Enter", font=('Helvetica bold',
                                   10), command = printInput).grid(row=1,column=1)
    win.mainloop()

    return pwd