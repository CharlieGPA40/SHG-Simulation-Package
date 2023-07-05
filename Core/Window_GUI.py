'''
Author  :Chunli Tang, Hussam Mustafa
Project :Polar Plot GUI
FileName: SHG Simulation.py
Affiliation: Auburn University
'''

# import packages
import numpy as np
import matplotlib.pyplot as plt
from sympy import *
from tkinter import *
from tkinter import ttk
import tkinter.messagebox as messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import math
from tkscrolledframe import ScrolledFrame
from PIL import ImageTk, Image
import webbrowser
import os
from sympy.parsing.sympy_parser import parse_expr
import sv_ttk
from idlelib.tooltip import Hovertip
from tkinter.filedialog import asksaveasfilename
from Core.Dict.CharTable import characterTable
import Core.Dict.CharTable as ct
from Core.Dict.Dict import SetUpDict
from Core.function import TensorMath as tm
from Core.function import rotation as rt
from timeit import default_timer as clock
import symengine as se
import Core.Dict.Misc as Misc

def run():
# ************************************** #
# construct a class used to generate the polar plot
    class Win2:
        def __init__(self, _root):
            self.root = _root
            width = 670  # Width (670)
            height = 630  # Height
            screen_width = root.winfo_screenwidth()  # Width of the screen
            screen_height = root.winfo_screenheight()  # Height of the screen

            # Calculate Starting X and Y coordinates for Window
            x = (screen_width / 2) - (width / 2)
            y = (screen_height / 2) - (height / 2)

            self.root.geometry('%dx%d+%d+%d' % (width, height, x, y))
            self.root.title("About SHG Simulation Tool")
            self.root.maxsize(width, height)
            # self.root.configure(bg='#F2F3F4')
            self.root.protocol("WM_DELETE_WINDOW", self.close)
            au_logo = Image.open("Core/Image/vect.png")
            au_logo = au_logo.resize((400, 200))
            au_logo = ImageTk.PhotoImage(au_logo)
            label_au = Label(self.root, image=au_logo)
            label_au.image = au_logo
            label_au.grid(column=0, row=0)
            lbl = Label(self.root, text="This Package is developed by Chunli Tang (Code, Design & Build) & Hussam Mustafa (Term Verification)",
                        font=40)
            lbl.grid(column=0, row=1, padx=10)
            lbl = Label(self.root,
                        text="Advisor: Dr. Wencan Jin & Dr.Masoud Mahjouri-Samani", font=40)
            lbl.grid(column=0, row=2)
            lbl = Label(self.root,
                        text="Affiliation: Auburn University", font=40)
            lbl.grid(column=0, row=3)
            lbl = Label(self.root, text="Contact info:", font=40)
            lbl.grid(column=0, row=4)
            lbl = Label(self.root, text="chunli.tang@auburn.edu & hnm0037@auburn.edu", font=40)
            lbl.grid(column=0, row=5)
            lbl = Label(self.root, text="wjin@auburn.edu & mzm0185@auburn.edu", font=40)
            lbl.grid(column=0, row=6)


            def callback(url):
                webbrowser.open_new_tab(url)

            wb_label = Label(self.root, text="Website", font=40, fg="blue", cursor="hand2")
            wb_label.bind("<Button-1>", lambda e: callback("https://github.com/CharlieGPA40/SHG-Simulation-Package-Beta"))
            wb_label.grid(column=0, row=8)

            self.paned = Frame(master=self.root)
            self.paned.grid(row=9, column=0, ipadx=0, ipady=0)
            self.notebook = ttk.Notebook(self.paned)
            self.notebook.grid(row=0, column=0)
            self.tab_1 = Frame(self.notebook)
            self.tab_2 = Frame(self.notebook)
            self.tab_3 = Frame(self.notebook)

            license_box = Text(self.tab_1, height=10, width=80, relief='sunken')
            license_box.grid(column=0, row=10)
            disclaimer = Misc.disclaimer()
            license_box.insert(END, disclaimer)
            license_box.config(state='disabled')

            Ack_box = Text(self.tab_2, height=10, width=80, relief='sunken')
            Ack_box.grid(column=0, row=10)
            acknowledge = Misc.ack()
            Ack_box.insert(END, acknowledge)
            Ack_box.config(state='disabled')


            ref_box = Text(self.tab_3, height=10, width=80, relief='sunken')
            ref_box.grid(column=0, row=10)
            reference = Misc.reference()
            ref_box.insert(END, reference)
            ref_box.config(state='disabled')

            self.notebook.add(self.tab_1, text="License")
            self.notebook.add(self.tab_2, text="Acknowledge")
            self.notebook.add(self.tab_3, text="Reference")
        def close(self):
            self.root.destroy()

    class Win3:
        def __init__(self, _root):
            self.root = _root
            width = 197  # Width (197)
            height = 255  # Height
            screen_width = root.winfo_screenwidth()  # Width of the screen
            screen_height = root.winfo_screenheight()  # Height of the screen

            # Calculate Starting X and Y coordinates for Window
            x = (screen_width / 2) - (width / 2)
            y = (screen_height / 2) - (height / 2)

            self.root.geometry('%dx%d+%d+%d' % (width, height, x, y))
            self.root.maxsize(197, 255)
            self.root.title("Group Website")
            self.root.protocol("WM_DELETE_WINDOW", self.close)
            qr_code = Image.open("Core/Image/frame.png")
            qr_code = qr_code.resize((193, 250))
            qr_code = ImageTk.PhotoImage(qr_code)
            label_qr = Label(self.root, image=qr_code)
            label_qr.image = qr_code
            label_qr.grid(column=0, row=0)

        def close(self):
            self.root.destroy()

    class Win4:
        def __init__(self, _root):
            self.root = _root
            width = 800  # Width (800)
            height = 605  # Height
            screen_width = root.winfo_screenwidth()  # Width of the screen
            screen_height = root.winfo_screenheight()  # Height of the screen

            # Calculate Starting X and Y coordinates for Window
            x = (screen_width / 2) - (width / 2)
            y = (screen_height / 2) - (height / 2)

            self.root.geometry('%dx%d+%d+%d' % (width, height, x, y))
            self.root.maxsize(800, 605)
            self.root.title("Calculation Model")
            self.root.protocol("WM_DELETE_WINDOW", self.close)

            def image_forward():
                var.set(1)
                if self.click_loop < 2:
                    self.click_loop += 1
                else:
                    self.click_loop = self.click_loop

            def image_backward():
                var.set(2)
                if self.click_loop >= 1:
                    self.click_loop -= 1

            self.click_loop = 0
            while 0 <= self.click_loop < 4:
                image = Image.open('Image/Model{}.png'.format(self.click_loop+1))
                resize_image = image.resize((800, 550))
                lst_img = ImageTk.PhotoImage(resize_image)
                self.image_label_Model = Label(self.root, image=lst_img)
                self.image_label_Model.image = lst_img
                self.image_label_Model.grid(row=0, column=0,columnspan=3)
                var = IntVar()
                self.img_button_nxt = Button(self.root,text=">>>", command=lambda: image_forward())
                self.img_button_bk = Button(self.root,text="<<<", command=lambda: image_backward())
                self.img_button_nxt.grid(row=1, column=2)
                self.img_button_bk.grid(row=1, column=0, padx=22)
                self.img_button_nxt.wait_variable(var)

        def close(self):
            self.root.destroy()

    class Win5:
        def __init__(self, _root):
            self.root = _root
            width = 312  # Width
            height = 232  # Height
            screen_width = root.winfo_screenwidth()  # Width of the screen
            screen_height = root.winfo_screenheight()  # Height of the screen

            # Calculate Starting X and Y coordinates for Window
            x = (screen_width / 2) - (width / 2)
            y = (screen_height / 2) - (height / 2)

            self.root.geometry('%dx%d+%d+%d' % (width, height, x, y))
            self.root.maxsize(312,232)
            self.root.title("About SHG Simulation Tool")
            self.root.protocol("WM_DELETE_WINDOW", self.close)
            au_logo = Image.open("Image/About.png")
            au_logo = au_logo.resize((160, 80))
            au_logo = ImageTk.PhotoImage(au_logo)
            label_au = Label(self.root, image=au_logo)
            label_au.image = au_logo
            label_au.grid(column=0, row=0,padx=70)
            lbl = Label(self.root, text="SHG Simulation Package",font='Helvetica 14 bold')
            lbl.grid(column=0, row=1, padx=10)
            lbl = Label(self.root,
                        text="Version 0.0.5", font='Helvetica 11', fg='#5b5b5b')
            lbl.grid(column=0, row=2)
            lbl = Label(self.root,
                        text="Auburn University", font='Helvetica 11', fg='#5b5b5b')
            lbl.grid(column=0, row=3)
            lbl = Label(self.root,
                        text="Ultrafast Nonlinear Optics Lab 2023", font='Helvetica 11', fg='#5b5b5b')
            lbl.grid(column=0, row=4)
            lbl = Label(self.root,
                        text="All rights reserved", font='Helvetica 11', fg='#5b5b5b')
            lbl.grid(column=0, row=5)
            def callback(url):
                webbrowser.open_new_tab(url)

            wb_label = Label(self.root, text="Github", font=22, fg="blue", cursor="hand2")
            wb_label.bind("<Button-1>", lambda e: callback("https://github.com/CharlieGPA40/SHG-Simulation-Package-Beta"))
            wb_label.grid(column=0, row=6)


        def close(self):
            self.root.destroy()

    class polarplotGUI(Frame):
        def __init__(self, root):
            super().__init__(root)
            # This line is for packaging
            # os.chdir(sys._MEIPASS)
            self.master = root
            self.app_size(self.master, 641, 306)
            self.win2_status = 0
            self.win3_status = 0
            self.win4_status = 0
            self.win5_status = 0
            self.chr_data = characterTable.charTable(self)
            self.dic, self.dic_qud, self.dic_mag_dip = SetUpDict.setupdict(self)
            self.menu_bar()
            self.master.rowconfigure(0, weight=1)
            self.master.columnconfigure(0, weight=1)
            self.top2 = None
            self.createWidget()

        def app_size(self, widget, width, height):
            screen_width = widget.winfo_screenwidth()
            screen_height = widget.winfo_screenheight()
            window_width = width
            window_height = height
            x = (screen_width - window_width) // 2
            y = (screen_height - window_height) // 2

            widget.geometry(f"{window_width}x{window_height}+{x}+{y}")
            widget.maxsize(width, height)
            widget.minsize(width, height)

        def menu_bar(self):
            menu_bar = Menu(self.master)
            self.master['menu'] = menu_bar
            self.IntroMenu = Menu(menu_bar)
            self.IntroMenu.add_command(label="About SHG Simulation Package", command=lambda: self.about_page_version())
            self.IntroMenu.add_separator()
            self.IntroMenu.add_command(label="Quit", command=lambda: self.quit(), accelerator='⌘+Q')
            menu_bar.add_cascade(label='SHG', menu=self.IntroMenu)

            edit = Menu(menu_bar)
            edit.add_command(label="Calculation Model", command=lambda: self.Cal_Mod())
            menu_bar.add_cascade(label='Model', menu=edit)

            Help = Menu(menu_bar)
            Help.add_command(label='Contact Us', command=lambda: self.contact())
            Help.add_separator()
            Help.add_command(label="About...", command=lambda: self.about_page_detail())
            Help.add_separator()
            Help.add_command(label="Feedback", command=lambda: self.feedback())
            menu_bar.add_cascade(label='Help', menu=Help)

        def feedback(self):
            url = 'https://docs.google.com/forms/d/e/1FAIpQLSeZaArKngIQY92mIbnvNzsSUnLj1lpbLrIfYdkwj-OzhzBg_w/viewform?usp=sf_link'
            webbrowser.open(url)

        def contact(self):
            try:
                if self.win3.status == 'normal':  # if it's not created yet
                    self.win3.focus_force()
            except:
                self.win3 = Toplevel(root)  # create
                Win3(self.win3)  # populate

        def Cal_Mod(self):
            try:
                if self.win4.status == 'normal':  # if it's not created yet
                    self.win4.focus_force()
            except:
                self.win4 = Toplevel(root)  # create
                Win4(self.win4)  # populate

        def about_page_detail(self):
            try:
                if self.win2.status == 'normal':  # if it's not created yet
                    self.win2.focus_force()
            except:
                self.win2 = Toplevel(root)  # create
                Win2(self.win2)  # populate

        def about_page_version(self):
            try:
                if self.win5.status == 'normal':  # if it's not created yet
                    self.win5.focus_force()
            except:
                self.win5 = Toplevel(root)  # create
                Win5(self.win5)  # populate

        def view_init(self):
            self.fr_input_up = Frame(master=self.master, bg='#F2F3F4')
            self.fr_input_up.grid(row=1, column=0, ipadx=320, ipady=162, sticky='NW')
            self.fr_input_up.grid_propagate(False)

        def createWidget(self):
            self.list_init()
            self.view_init()
            self.option_var = []
            self.option_var_1 = []
            self.option_var_2 = []
            pointGroup = ttk.Label(self.fr_input_up, text='Radiation Source:', background='#F2F3F4',
                               font=('Arial bold', 12))
            pointGroup.place(x=19, y=40)

            crystalSystem = ttk.Label(self.fr_input_up, text='Crystal System:', background='#F2F3F4',
                                  font=('Arial bold', 12))
            crystalSystem.place(x=181, y=40)

            crystalClass = ttk.Label(self.fr_input_up, text='Point Group:', background='#F2F3F4',
                                 font=('Arial bold', 12))
            crystalClass.place(x=335, y=40)
            self.group_box_group = Listbox(self.fr_input_up, width=16, justify="left", height=11, font=('Arial', 13),
                                           yscrollcommand='Vertical', selectmode=SINGLE, relief='sunken', exportselection=False)
            self.group_box_group.place(x=335, y=60)

            self.group_box = Listbox(self.fr_input_up, width=16, justify="left", height=11, yscrollcommand='Vertical',
                                     selectmode=SINGLE, relief='sunken', font=('Arial', 13), exportselection=False)
            self.group_box.place(x=19, y=60)
            self.group_box.insert(1, 'Electric Dipole')
            self.group_box.insert(2, 'Electric Quadrupole')
            self.group_box.insert(3, 'Magnetic Dipole')
            self.group_box.insert(4, 'Coming Soon...')
            self.group_box.bind('<Return>', lambda x: self.show_crystal_system())
            self.group_box.bind('<Double-Button-1>', lambda x: self.show_crystal_system())
            self.group_box.bind('<<ListboxSelect>>', lambda x: self.show_crystal_system())
            self.crystal_system = Listbox(self.fr_input_up, width=16, justify="left", height=11, font=('Arial', 13),
                                          yscrollcommand='Vertical', selectmode=SINGLE, relief='sunken', exportselection=False)
            self.crystal_system.place(x=181, y=60)
            self.nex_bt = ttk.Button(self.fr_input_up, text='Calculate', command=lambda: self.pop_up_warning(), width=10,
                                     style='Accent.TButton')
            self.nex_bt.bind('<Return>', lambda: self.show_crystal_system())
            self.nex_bt.grid(row=0, column=0, padx=377, pady=288)
            self.myBtn = ttk.Button(self.fr_input_up, text='?')
            self.myBtn.place(x=335, y=288)
            myTip = Hovertip(self.myBtn, 'Please select all the elements to do the calculation. '
                                    '\nThe calculation model can be found at menu->Model->Calculation Model'
                                         '\n(001), (010), (100), (011), and (111) refer to the plane perpendicular to the incident '
                                         'light using Miller indices.\n(001) is the initial measurement axis based on the '
                                         'IEEE standard settings. \nFor the Trigonal and Hexagonal crystal systems, [100]'
                                         ' and [010] refer to the mirror plane in the x or y direction, respectively. '
                                         '\nFor the Monoclinic crystal system, {010} and {001} refer to the twofold axis '
                                         'parallel to the y or z axis, respectively', hover_delay=1000)
            self.nex_bt['state'] = DISABLED

            self.sample_rot_label = ttk.Label(self.fr_input_up, text='Sample Rotation:', background='#F2F3F4',
                                              font=('Arial bold', 12))
            self.sample_rot_label.place(x=470, y=40)
            self.sample_rot = Listbox(self.fr_input_up, width=16, justify="left", height=11, font=('Arial', 13),
                                      yscrollcommand='Vertical', selectmode=SINGLE, relief='sunken',
                                      exportselection=False)
            self.sample_rot.place(x=470, y=60)

            self.nex_bt.grid(row=0, column=0, padx=490, pady=260)
            self.myBtn.place(y=260, x=447)
            self.beta_back_bt = ttk.Button(self.fr_input_up, text='Back', command=lambda: self.beta_back(),
                                           width=5, )
            self.beta_back_bt.place(y=260, x=367)

        def show_crystal_system(self):
            self.input_matrix_g = []
            itm_c = self.group_box.get(self.group_box.curselection())
            self.option_var_2 = [itm_c]

            self.group_box_group = Listbox(self.fr_input_up, width=16, justify="left", height=11, font=('Arial', 13),
                                           yscrollcommand='Vertical', selectmode=SINGLE, relief='sunken',
                                           exportselection=False)
            self.group_box_group.place(x=335, y=60)
            self.group_box_group.delete(0, END)
            self.input_matrix_c = self.option_var_2[0]

            self.crystal_box = Listbox(self.fr_input_up, width=16, justify="left", height=11, font=('Arial', 13),
                                       yscrollcommand='Vertical', selectmode=SINGLE, relief='sunken', exportselection=False)
            self.crystal_box.place(x=181, y=60)
            if self.input_matrix_c == 'Electric Dipole':
                for x in self.dic:
                    self.crystal_box.insert(END, x)
            elif self.input_matrix_c == 'Electric Quadrupole':
                for x in self.dic_qud:
                    self.crystal_box.insert(END, x)
            elif self.input_matrix_c == 'Magnetic Dipole':
                for x in self.dic_mag_dip:
                    self.crystal_box.insert(END, x)
            elif self.input_matrix_c == 'Coming Soon...':
                self.crystal_box.insert(1, 'EFISH/MFISH')

            self.cal_bt = ttk.Button(self.fr_input_up, text='Calculate', command=lambda: self.pop_up_warning(), width=10,
                                     style='Accent.TButton')

            self.crystal_box.bind('<Return>', lambda x: self.show_group())
            self.crystal_box.bind('<Double-Button-1>', lambda x: self.show_group())
            self.crystal_box.bind('<<ListboxSelect>>', lambda x: self.show_group())
            self.cal_bt.bind('<Double-1>', lambda: self.calculate())
            self.cal_bt.grid(row=0, column=0, padx=350, pady=260)
            self.cal_bt['state'] = DISABLED

        def show_group(self):
            itm_g = self.crystal_box.get(self.crystal_box.curselection())
            self.option_var_1 = [itm_g]
            self.input_matrix_g = self.option_var_1[0]
            self.group_box_group = Listbox(self.fr_input_up, width=16, justify="left", height=11, font=('Arial', 13),
                                           yscrollcommand='Vertical', selectmode=SINGLE, relief='sunken',
                                           exportselection=False)
            self.group_box_group.place(x=335, y=60)

            c_sys = list(self.dic.keys())

            if self.input_matrix_g in c_sys and self.input_matrix_c == 'Electric Dipole':
                ed_class = list(self.dic[self.input_matrix_g].keys())
                for x in range(len(ed_class)):
                    self.group_box_group.insert(END, ed_class[x])
            elif self.input_matrix_c == 'Electric Quadrupole':
                eq_class = list(self.dic_qud[self.input_matrix_g].keys())
                for x in range(len(eq_class)):
                    self.group_box_group.insert(END, eq_class[x])
            elif self.input_matrix_c == 'Magnetic Dipole':
                md_class = list(self.dic_mag_dip[self.input_matrix_g].keys())
                for x in range(len(md_class)):
                    self.group_box_group.insert(END, md_class[x])

            elif self.input_matrix_c == 'Coming Soon...':
                self.group_box_group.insert(1, 'Coming Soon...')
            self.opened = false
            self.sample_rot.delete(0, END)
            self.cal_bt_dis = ttk.Button(self.fr_input_up, text='Calculate', command=lambda: self.calculate(), width=10,
                                         style='Accent.TButton')
            self.group_box_group.bind('<Return>', lambda x: self.SampleRotation())
            self.group_box_group.bind('<Double-Button-1>', lambda x: self.SampleRotation())
            self.group_box_group.bind('<<ListboxSelect>>', lambda x: self.SampleRotation())
            self.cal_bt_dis.bind('<Double-1>', lambda: self.SampleRotation())
            self.cal_bt_dis.grid(row=0, column=0, padx=350, pady=260)
            self.cal_bt_dis['state'] = DISABLED

        def SampleRotation(self):
            if self.input_matrix_g == 'Triclinic':
                self.sample_rot.delete(0, END)
                self.sample_rot.insert(1, '(001)')
            elif self.input_matrix_g == 'Monoclinic':
                self.sample_rot.delete(0, END)
                self.sample_rot.insert(1, '{010}')
                self.sample_rot.insert(2, '{001}')
            elif self.input_matrix_g == 'Orthorhombic':
                self.sample_rot.delete(0, END)
                self.sample_rot.insert(1, '(001)')
                self.sample_rot.insert(2, '(010)')
                self.sample_rot.insert(3, '(100)')
            elif self.input_matrix_g == 'Tetragonal':
                self.sample_rot.delete(0, END)
                self.sample_rot.insert(1, '(001)')
                self.sample_rot.insert(2, '(010)')
            elif self.input_matrix_g == 'Cubic':
                self.sample_rot.delete(0, END)
                self.sample_rot.insert(1, '(001)')
                self.sample_rot.insert(2, '(011)')
                self.sample_rot.insert(3, '(111)')
            elif self.input_matrix_g == 'Trigonal':
                self.sample_rot.delete(0, END)
                self.sample_rot.insert(1, '[100]')
                self.sample_rot.insert(2, '[010]')
            elif self.input_matrix_g == 'Hexagonal':
                self.sample_rot.delete(0, END)
                self.sample_rot.insert(1, '[100]')
                self.sample_rot.insert(2, '[010]')

            self.cal_bt_dis = ttk.Button(self.fr_input_up, text='Calculate', command=lambda: self.calculate(),
                                         width=10,
                                         style='Accent.TButton')
            self.sample_rot.bind('<Return>', lambda x: self.calculate())
            self.sample_rot.bind('<Double-Button-1>', lambda x: self.calculate())
            self.sample_rot.bind('<<ListboxSelect>>', lambda x: self.buffer())
            self.cal_bt_dis.bind('<Double-1>', lambda: self.calculate())
            self.cal_bt_dis.grid(row=0, column=0, padx=350, pady=260)
            self.cal_bt_dis['state'] = DISABLED

        def list_init(self):
            self.valueList_ss = []
            self.valueList_sp = []
            self.valueList_ps = []
            self.valueList_pp = []
            self.entryList_ss = []
            self.entryList_sp = []
            self.entryList_ps = []
            self.entryList_pp = []
            self.polarList_ss = []
            self.polarList_sp = []
            self.polarList_ps = []
            self.polarList_pp = []

        def beta_back(self):
            self.beta = False
            self.fr_input_up.destroy()
            self.fr_input_up = Frame(master=root, bg='#F2F3F4')
            self.createWidget()

        def resetCanvas(self):
            self.ax[0].clear()
            self.ax[0].set_title("Polar Plot: SS", fontsize=15, pad=15)
            self.ax[1].clear()
            self.ax[1].set_title("Polar Plot: SP", fontsize=15, pad=15)
            self.ax[2].clear()
            self.ax[2].set_title("Polar Plot: PS", fontsize=15, pad=15)
            self.ax[3].clear()
            self.ax[3].set_title("Polar Plot: PP", fontsize=15, pad=15)
            self.canvs.draw()




        def autoPlot(self):
            self.resetCanvas()
            self.plot()

        def plot(self):
            self.polarList_ss = []
            self.check_list_ss = [float(self.entryList_ss[i].get()) for i in range(len(self.entryList_ss))]
            if all(v == 0 for v in self.check_list_ss):
                str = 'THIS IS BAD!'
            else:
                self.valueList_ss = [float(self.entryList_ss[i].get()) for i in range(len(self.entryList_ss))]
                if chr(952) == Misc.showSymbol(self.symbolList_ss[0]):
                    self.valueList_ss[0] = math.radians(self.valueList_ss[0])
                self.substitute = [(self.symbolList_ss[i], self.valueList_ss[i]) for i in range(len(self.symbolList_ss))]
                for i in range(len(phi_value)):
                    self.substitute.append((phi, phi_value[i]))
                    self.polarList_ss.append(self.exprss.subs(self.substitute))
                    self.substitute.remove((phi, phi_value[i]))
                self.ax[0].plot(phi_value, self.polarList_ss)
                self.canvs.draw()

            self.polarList_sp = []
            self.check_list_sp = [float(self.entryList_sp[i].get()) for i in range(len(self.entryList_sp))]
            if all(u == 0 for u in self.check_list_sp):
                str = 'THIS IS BAD!'
            else:
                self.valueList_sp = [float(self.entryList_sp[i].get()) for i in range(len(self.entryList_sp))]
                if chr(952) == Misc.showSymbol(self.symbolList_sp[0]):
                    self.valueList_sp[0] = math.radians(self.valueList_sp[0])
                self.substitute = [(self.symbolList_sp[i], self.valueList_sp[i]) for i in range(len(self.symbolList_sp))]
                for i in range(len(phi_value)):
                    self.substitute.append((phi, phi_value[i]))
                    self.polarList_sp.append(self.exprsp.subs(self.substitute))
                    self.substitute.remove((phi, phi_value[i]))
                self.ax[1].plot(phi_value, self.polarList_sp)
                self.canvs.draw()

            self.polarList_ps = []
            self.check_list_ps = [float(self.entryList_ps[i].get()) for i in range(len(self.entryList_ps))]
            if all(w == 0 for w in self.check_list_ps):
                str = 'THIS IS BAD!'
            else:
                self.valueList_ps = [float(self.entryList_ps[i].get()) for i in range(len(self.entryList_ps))]
                if chr(952) == Misc.showSymbol(self.symbolList_ps[0]):
                    self.valueList_ps[0] = math.radians(self.valueList_ps[0])
                self.substitute = [(self.symbolList_ps[i], self.valueList_ps[i]) for i in range(len(self.symbolList_ps))]
                for i in range(len(phi_value)):
                    self.substitute.append((phi, phi_value[i]))
                    self.polarList_ps.append(self.exprps.subs(self.substitute))
                    self.substitute.remove((phi, phi_value[i]))
                self.ax[2].plot(phi_value, self.polarList_ps)
                self.canvs.draw()

            self.polarList_pp = []
            self.check_list_pp = [float(self.entryList_pp[i].get()) for i in range(len(self.entryList_pp))]
            if all(s == 0 for s in self.check_list_pp):
                str = 'THIS IS BAD!'
            else:
                self.valueList_pp = [float(self.entryList_pp[i].get()) for i in range(len(self.entryList_pp))]
                if chr(952) == Misc.showSymbol(self.symbolList_pp[0]):
                    self.valueList_pp[0] = math.radians(self.valueList_pp[0])
                self.substitute = [(self.symbolList_pp[i], self.valueList_pp[i]) for i in range(len(self.symbolList_pp))]
                for i in range(len(phi_value)):
                    self.substitute.append((phi, phi_value[i]))
                    self.polarList_pp.append(self.exprpp.subs(self.substitute))
                    self.substitute.remove((phi, phi_value[i]))
                self.ax[3].plot(phi_value, self.polarList_pp)
                self.canvs.draw()

            def save():
                filename = asksaveasfilename(initialfile='Untitled.png', defaultextension=".png",
                                             filetypes=[("All Files", "*.*"), ("Portable Graphics Format", "*.png")])
                plt.savefig(filename)

        def _quit(self):
            self.master.quit()  # stops mainloop
            self.master.destroy()  # this is necessary on Windows to prevent
            # Fatal Python Error: PyEval_RestoreThread: NULL tstate

        def _back(self):
            self.newWindow.destroy()
            plt.close()
            self.cal_bt['state'] = ACTIVE
            self.createWidget()

        def getList(self, expression):
            if self.input_matrix_c == 'Electric Dipole' or self.input_matrix_c == 'Magnetic Dipole':
                lst = [theta, phi, xxx, xxy, xxz, xyx, xyy, xyz, xzx, xzy, xzz, yxx, yxy, yxz, yyx, yyy, yyz, yzx, yzy,
                       yzz, zxx, zxy, zxz, zyx, zyy, zyz, zzx, zzy, zzz]
            elif self.input_matrix_c == 'Electric Quadrupole':
            # find the corresponding variable in the expression and return a list containing all the appeared elements
                lst = [theta, phi, xxxx, xxxy, xxxz, xyxx, xyxy, xyxz, xzxx, xzxy, xzxz, xxyx, xxyy, xxyz, xyyx, xyyy, xyyz,
                       xzyx, xzyy, xzyz, xxzx, xxzy, xxzz, xyzx, xyzy, xyzz,
                       xzzx, xzzy, xzzz, yxxx, yxxy, yxxz, yyxx, yyxy, yyxz, yzxx, yzxy, yzxz, yxyx, yxyy, yxyz, yyyx, yyyy,
                       yyyz, yzyx, yzyy, yzyz, yxzx, yxzy, yxzz,
                       yyzx, yyzy, yyzz, yzzx, yzzy, yzzz, zxxx, zxxy, zxxz, zyxx, zyxy, zyxz, zzxx, zzxy, zzxz, zxyx, zxyy,
                       zxyz, zyyx, zyyy, zyyz, zzyx, zzyy, zzyz,
                       zxzx, zxzy, zxzz, zyzx, zyzy, zyzz, zzzx, zzzy, zzzz]
            else:
                lst=[]
            new_lst = []
            for e in lst:
                if str(e) in str(expression):
                    new_lst.append(e)
            return new_lst

        def symbolList(self, exprpp, exprps, exprss, exprsp):
            symbolList_pp = self.getList(exprpp)
            symbolList_ps = self.getList(exprps)
            symbolList_ss = self.getList(exprss)
            symbolList_sp = self.getList(exprsp)

            # remove variable phi since no need of it
            if phi in symbolList_pp:
                symbolList_pp.remove(phi)
            if phi in symbolList_ps:
                symbolList_ps.remove(phi)
            if phi in symbolList_ss:
                symbolList_ss.remove(phi)
            if phi in symbolList_sp:
                symbolList_sp.remove(phi)
            return symbolList_pp, symbolList_ps, symbolList_ss, symbolList_sp

        def Rank3Matrix(self):
            rank3Matrix = Matrix(
                [[xxx, xyx, xzx], [xxy, xyy, xzy], [xxz, xyz, xzz], [yxx, yyx, yzx], [yxy, yyy, yzy], [yxz, yyz, yzz],
                 [zxx, zyx, zzx], [zxy, zyy, zzy], [zxz, zyz, zzz]])
            return rank3Matrix

        def Rank4Matrix(self):
            rank4Matrix = Matrix([[xxxx, xxxy, xxxz, xyxx, xyxy, xyxz, xzxx, xzxy, xzxz],
                                  [xxyx, xxyy, xxyz, xyyx, xyyy, xyyz, xzyx, xzyy, xzyz],
                                  [xxzx, xxzy, xxzz, xyzx, xyzy, xyzz, xzzx, xzzy, xzzz],
                                  [yxxx, yxxy, yxxz, yyxx, yyxy, yyxz, yzxx, yzxy, yzxz],
                                  [yxyx, yxyy, yxyz, yyyx, yyyy, yyyz, yzyx, yzyy, yzyz],
                                  [yxzx, yxzy, yxzz, yyzx, yyzy, yyzz, yzzx, yzzy, yzzz],
                                  [zxxx, zxxy, zxxz, zyxx, zyxy, zyxz, zzxx, zzxy, zzxz],
                                  [zxyx, zxyy, zxyz, zyyx, zyyy, zyyz, zzyx, zzyy, zzyz],
                                  [zxzx, zxzy, zxzz, zyzx, zyzy, zyzz, zzzx, zzzy, zzzz]])
            return rank4Matrix


        def calculate(self):
            self.cal_bt_dis['state'] = DISABLED
            if self.opened == false:
                self.newWindow = Toplevel(root)
                self.newWindow.title("SHG Simulation Package")
                self.opened = True
                self.app_size(self.newWindow, 1520, 872)
            else:
                self.newWindow.destroy()

            itm_rot = self.sample_rot.get(self.sample_rot.curselection())
            self.option_var_3 = [itm_rot]
            itm = self.group_box_group.get(self.group_box_group.curselection())
            self.option_var = [itm]
            self.fr_button_dw_message = Frame(self.newWindow)
            self.fr_button_dw_message.grid(row=4, column=0,)
            self.text_box = Text(self.fr_button_dw_message, height=1, width=200, bg='#D3D3D3')

            self.path_exp = 'Core/ExpressAndLatex/' + str(self.input_matrix_c) + '/' + str(
                self.option_var_1[0]) + '/' + str(
                self.option_var[0]) + '/' + str(
                self.option_var_3[0]) + '/Expfile.txt'

            self.path = 'Core/ExpressAndLatex/' + str(self.input_matrix_c) + '/' + str(
                self.option_var_1[0]) + '/' + str(
                self.option_var[0]) + '/' + str(
                self.option_var_3[0])
            epin = Matrix([[-cos(theta), 0, sin(theta)]])
            # epin = se.sympify(epin)
            esin = Matrix([[0, 1, 0]])
            # esin = se.sympify(esin)
            rot = Matrix([[cos(phi), -sin(phi), 0], [sin(phi), cos(phi), 0], [0, 0, 1]])
            # rot = se.sympify(rot)
            k = Matrix([[-sin(theta), 0, -cos(theta)]])
            # k = se.sympify(k)
            if self.input_matrix_c == 'Electric Dipole':
                rank = 3
                isExist = os.path.exists(self.path_exp)
                if not isExist:  # Create a new directory because it does not exist
                    input_matrix = self.dic[self.option_var_1[0]][self.option_var[0]]

                    input_matrix = rt.rotationCal(rank, self.option_var_3[0], input_matrix, self.Rank3Matrix())

                    rs_matrix = trigsimp(tm.trans(tm.sTB(rot, tm.trans(tm.sTB(rot, tm.bTS(input_matrix, rot.T))))))
                    # PP
                    # rs_matrix = se.sympify(rs_matrix)
                    pxp = epin * rs_matrix[0:3, 0:3] * epin.T
                    pzp = epin * rs_matrix[6:9, 0:3] * epin.T
                    self.exprpp = se.sympify((pxp * cos(theta)) ** 2 + (pzp * sin(theta)) ** 2)[0]
                    # PS
                    pys = epin * rs_matrix[3:6, 0:3] * epin.T
                    self.exprps = se.sympify((pys ** 2)[0])
                    # SP
                    sxp = esin * rs_matrix[0:3, 0:3] * esin.T
                    szp = esin * rs_matrix[6:9, 0:3] * esin.T
                    self.exprsp = se.sympify((sxp * cos(theta)) ** 2 + (szp * sin(theta)) ** 2)[0]
                    # SS
                    sys = esin * rs_matrix[3:6, 0:3] * esin.T
                    self.exprss = se.sympify((sys ** 2)[0])
                    self.exprss = str(self.exprss)
                    self.exprsp = str(self.exprsp)
                    self.exprps = str(self.exprps)
                    self.exprpp = str(self.exprpp)
                    self.exprss = parse_expr(self.exprss, evaluate=False)
                    self.exprsp = parse_expr(self.exprsp, evaluate=False)
                    self.exprps = parse_expr(self.exprps, evaluate=False)
                    self.exprpp = parse_expr(self.exprpp, evaluate=False)
                else:
                    express_txt = open(self.path_exp, 'rt')
                    lines = express_txt.read().split('\n')
                    dict_exp_extract = {}
                    i = 0
                    for l in lines:
                        if l != '':
                            dict_exp_extract[i] = Misc.parse(l)
                            i += 1
                    express_txt.close()
                    # sympy
                    self.exprss = parse_expr(dict_exp_extract[0]['SS'], evaluate=False)
                    self.exprsp = parse_expr(dict_exp_extract[1]['SP'], evaluate=False)
                    self.exprps = parse_expr(dict_exp_extract[2]['PS'], evaluate=False)
                    self.exprpp = parse_expr(dict_exp_extract[3]['PP'], evaluate=False)

                self.symbolList_pp, self.symbolList_ps, self.symbolList_ss, self.symbolList_sp = self.symbolList(self.exprpp, self.exprps, self.exprss, self.exprsp)
            elif self.input_matrix_c == 'Electric Quadrupole':
                isExist = os.path.exists(self.path_exp)
                if isExist == False:  # Create a new directory because it does not exist
                    rank = 4
                    input_matrix_quad = self.dic_qud[self.option_var_1[0]][self.option_var[0]]

                    input_matrix_quad = rt.rotationCal(rank, self.option_var_3[0], input_matrix_quad,
                                                       self.Rank4Matrix())
                    rs_matrix_quad = se.sympify(tm.trans_quad_2Swap(tm.trans_quad(tm.bTS_quad(tm.trans_quad_2Swap(
                        tm.sTB_quad(rot, tm.trans_quad(tm.sTB_quad(rot, tm.bTS_quad(input_matrix_quad, rot.T))))),
                        rot.T))))

                    # PP
                    pxp = 0
                    pys = 0
                    pzp = 0
                    for i in range(0, 9, 3):
                        i += 3
                        for j in range(0, 3):
                            for l in range(0, 3):
                                pxp_temp = rs_matrix_quad[0:3, i - 3:i][j, l] * epin[int((i - 3) / 3)] * epin[l] * k[j]
                                pys_temp = rs_matrix_quad[3:6, i - 3:i][j, l] * epin[int((i - 3) / 3)] * epin[l] * k[j]
                                pzp_temp = rs_matrix_quad[6:9, i - 3:i][j, l] * epin[int((i - 3) / 3)] * epin[l] * k[j]
                                pxp = pxp + pxp_temp
                                pys = pys + pys_temp
                                pzp = pzp + pzp_temp

                    # Sympy
                    t1 = clock()
                    self.exprpp = se.sympify((pxp * cos(theta)) ** 2 + (pzp * sin(theta)) ** 2)
                    self.exprps = se.sympify((pys ** 2))
                    sxp = 0
                    sys = 0
                    szp = 0
                    for i in range(0, 9, 3):
                        i += 3
                        for j in range(0, 3):
                            for l in range(0, 3):
                                sxp_temp = rs_matrix_quad[0:3, i - 3:i][j, l] * esin[int((i - 3) / 3)] * esin[l] * k[j]
                                sys_temp = rs_matrix_quad[3:6, i - 3:i][j, l] * esin[int((i - 3) / 3)] * esin[l] * k[j]
                                szp_temp = rs_matrix_quad[6:9, i - 3:i][j, l] * esin[int((i - 3) / 3)] * esin[l] * k[j]
                                sxp = sxp + sxp_temp
                                sys = sys + sys_temp
                                szp = szp + szp_temp

                    self.exprsp = se.sympify((sxp * cos(theta)) ** 2 + (szp * sin(theta)) ** 2)
                    self.exprss = se.sympify((sys ** 2))
                    t2 = clock()
                    print("%s s" % ((t2 - t1)))
                    self.exprss = str(self.exprss)
                    self.exprsp = str(self.exprsp)
                    self.exprps = str(self.exprps)
                    self.exprpp = str(self.exprpp)
                    self.exprss = parse_expr(self.exprss, evaluate=False)
                    self.exprsp = parse_expr(self.exprsp, evaluate=False)
                    self.exprps = parse_expr(self.exprps, evaluate=False)
                    self.exprpp = parse_expr(self.exprpp, evaluate=False)
                else:
                    express_txt = open(self.path_exp, 'rt')
                    lines = express_txt.read().split('\n')
                    dict_exp_extract = {}
                    i = 0
                    for l in lines:
                        if l != '':
                            dict_exp_extract[i] = Misc.parse(l)
                            i += 1
                    express_txt.close()
                    ss_temp = dict_exp_extract[0]['SS']
                    # sympy
                    self.exprss = parse_expr(ss_temp, evaluate=False)

                    sp_temp = dict_exp_extract[1]['SP']
                    # sympy
                    self.exprsp = parse_expr(sp_temp, evaluate=False)

                    ps_temp = dict_exp_extract[2]['PS']
                    # sympy
                    self.exprps = parse_expr(ps_temp, evaluate=False)
                    pp_temp = dict_exp_extract[3]['PP']
                    # sympy
                    self.exprpp = parse_expr(pp_temp, evaluate=False)

                # every change should clear the symbolList at first
                self.symbolList_pp, self.symbolList_ps, self.symbolList_ss, self.symbolList_sp = self.symbolList(self.exprpp, self.exprps, self.exprss, self.exprsp)
            elif self.input_matrix_c == 'Magnetic Dipole':
                isExist = os.path.exists(self.path_exp)
                rank = 3
                if not isExist:  # Create a new directory because it does not exist
                    input_matrix = self.dic_mag_dip[self.option_var_1[0]][self.option_var[0]]
                    input_matrix = rt.rotationCal(rank, self.option_var_3[0], input_matrix, self.Rank3Matrix())
                    # calculate the expression
                    rs_matrix_md = se.sympify(tm.trans(tm.sTB(rot, tm.trans(tm.sTB(rot, tm.bTS(input_matrix, rot.T))))))

                    Mpx = 0
                    Mpy = 0
                    Mpz = 0
                    for i in range(0, 9, 3):
                        i += 3
                        for j in range(0, 3):
                            Mpx_temp = rs_matrix_md[0:3, int((i - 3) / 3)][j] * epin[int((i - 3) / 3)] * epin[j]
                            Mpy_temp = rs_matrix_md[3:6, int((i - 3) / 3)][j] * epin[int((i - 3) / 3)] * epin[j]
                            Mpz_temp = rs_matrix_md[6:9, int((i - 3) / 3)][j] * epin[int((i - 3) / 3)] * epin[j]
                            Mpx = Mpx + Mpx_temp
                            Mpy = Mpy + Mpy_temp
                            Mpz = Mpz + Mpz_temp

                    Mp = Matrix([[Mpx, Mpy, Mpz]])
                    Sp = Matrix(np.cross(k, Mp))
                    Spx = Sp[0]
                    Spy = Sp[1]
                    Spz = Sp[2]

                    self.exprpp = se.sympify((Spx * cos(theta)) ** 2 + (Spz * sin(theta)) ** 2)
                    self.exprps = se.sympify((Spy ** 2))
                    Msx = 0
                    Msy = 0
                    Msz = 0
                    for i in range(0, 9, 3):
                        i += 3
                        for j in range(0, 3):
                            Msx_temp = rs_matrix_md[0:3, int((i - 3) / 3)][j] * esin[int((i - 3) / 3)] * esin[j]
                            Msy_temp = rs_matrix_md[3:6, int((i - 3) / 3)][j] * esin[int((i - 3) / 3)] * esin[j]
                            Msz_temp = rs_matrix_md[6:9, int((i - 3) / 3)][j] * esin[int((i - 3) / 3)] * esin[j]
                            Msx = Msx + Msx_temp
                            Msy = Msy + Msy_temp
                            Msz = Msz + Msz_temp

                    Ms = Matrix([[Msx, Msy, Msz]])
                    Ss = Matrix(np.cross(k, Ms))
                    Ssx = Ss[0]
                    Ssy = Ss[1]
                    Ssz = Ss[2]

                    self.exprsp = se.sympify((Ssx * cos(theta)) ** 2 + (Ssz * sin(theta)) ** 2)
                    # # SS
                    self.exprss = se.sympify((Ssy ** 2))
                    self.exprss = str(self.exprss)
                    self.exprsp = str(self.exprsp)
                    self.exprps = str(self.exprps)
                    self.exprpp = str(self.exprpp)
                    self.exprss = parse_expr(self.exprss, evaluate=False)
                    self.exprsp = parse_expr(self.exprsp, evaluate=False)
                    self.exprps = parse_expr(self.exprps, evaluate=False)
                    self.exprpp = parse_expr(self.exprpp, evaluate=False)
                else:
                    express_txt = open(self.path_exp, 'rt')
                    lines = express_txt.read().split('\n')
                    dict_exp_extract = {}
                    i = 0
                    for l in lines:
                        if l != '':
                            dict_exp_extract[i] = Misc.parse(l)
                            i += 1
                    express_txt.close()

                    # sympy
                    self.exprss = parse_expr(dict_exp_extract[0]['SS'], evaluate=False)
                    self.exprsp = parse_expr(dict_exp_extract[1]['SP'], evaluate=False)
                    self.exprps = parse_expr(dict_exp_extract[2]['PS'], evaluate=False)
                    self.exprpp = parse_expr(dict_exp_extract[3]['PP'], evaluate=False)

                # every change should clear the symbolList at first
                self.symbolList_pp, self.symbolList_ps, self.symbolList_ss, self.symbolList_sp = self.symbolList(self.exprpp, self.exprps, self.exprss, self.exprsp)
                self.display_GUI()
        def display_GUI(self):
            self.text_box.delete('1.0', 'end')
            message = str(self.input_matrix_c) + '  :  ' + str(self.option_var_1[0]) + ' - ' + str(self.option_var[0])
            self.text_box.insert('end', message)
            self.text_box.grid()
            self.paned = Frame(self.newWindow)
            self.paned.grid(row=0, column=0, ipadx=0, ipady=0)
            self.notebook = ttk.Notebook(self.paned)
            self.notebook.grid(row=0, column=0)

            self.tab_1 = Frame(self.notebook)
            self.tab_2 = Frame(self.notebook)
            self.tab_3 = Frame(self.notebook)
            self.tab_4 = Frame(self.notebook)
            self.tab_1.pack()

            self.f, self.ax = plt.subplots(1, 4, subplot_kw={'projection': 'polar'}, figsize=(15, 4))
            self.ax[0].set_title("Polar Plot: SS", fontsize=15, pad=15)
            self.ax[1].set_title("Polar Plot: SP", fontsize=15, pad=15)
            self.ax[2].set_title("Polar Plot: PS", fontsize=15, pad=15)
            self.ax[3].set_title("Polar Plot: PP", fontsize=15, pad=15)
            plt.subplots_adjust(wspace=0.6)
            self.f.patch.set_facecolor('#FAFAFA')
            self.canvs = FigureCanvasTkAgg(self.f, self.tab_1)
            self.canvs._tkcanvas.pack()

            # Tab #2
            # tab 1
            self.tab2_scrollable = ScrolledFrame(self.tab_2)
            self.tab2_scrollable.grid(column=0, row=1, ipadx=600, ipady=50)
            self.tab2_scrollable.bind_arrow_keys(root)
            self.tab2_scrollable.bind_scroll_wheel(root)

            # Create a frame within the ScrolledFrame
            self.tab2_scrollable_inside = self.tab2_scrollable.display_widget(Frame)

            self.f_e, self.wx = plt.subplots(4, 1, figsize=(200, 4))
            plt.subplots_adjust(left=0)
            self.wx[0].set_title("Expression SS:", fontsize=15, pad=15, loc='left')
            self.wx[1].set_title("Expression SP:", fontsize=15, pad=15, loc='left')
            self.wx[2].set_title("Expression PS:", fontsize=15, pad=15, loc='left')
            self.wx[3].set_title("Expression PP:", fontsize=15, pad=15, loc='left')
            plt.subplots_adjust(hspace=1)
            self.canvs_e = FigureCanvasTkAgg(self.f_e, self.tab2_scrollable_inside)
            self.canvs_e._tkcanvas.grid(column=0, row=0)

            # Set the visibility of the Canvas figure
            self.wx[0].get_xaxis().set_visible(False)
            self.wx[0].get_yaxis().set_visible(False)
            self.wx[0].spines['top'].set_visible(False)
            self.wx[0].spines['right'].set_visible(False)
            self.wx[0].spines['bottom'].set_visible(False)
            self.wx[0].spines['left'].set_visible(False)

            self.wx[1].get_xaxis().set_visible(False)
            self.wx[1].get_yaxis().set_visible(False)
            self.wx[1].spines['top'].set_visible(False)
            self.wx[1].spines['right'].set_visible(False)
            self.wx[1].spines['bottom'].set_visible(False)
            self.wx[1].spines['left'].set_visible(False)

            self.wx[2].get_xaxis().set_visible(False)
            self.wx[2].get_yaxis().set_visible(False)
            self.wx[2].spines['top'].set_visible(False)
            self.wx[2].spines['right'].set_visible(False)
            self.wx[2].spines['bottom'].set_visible(False)
            self.wx[2].spines['left'].set_visible(False)

            self.wx[3].get_xaxis().set_visible(False)
            self.wx[3].get_yaxis().set_visible(False)
            self.wx[3].spines['top'].set_visible(False)
            self.wx[3].spines['right'].set_visible(False)
            self.wx[3].spines['bottom'].set_visible(False)
            self.wx[3].spines['left'].set_visible(False)

            plt.rcParams.update({
                "text.usetex": True,
                "font.family": "Helvetica"
            })

            self.path = 'ExpressAndLatex/' + str(self.input_matrix_c) + '/' + str(self.option_var_1[0]) + '/' + str(self.option_var[0]) + '/'
            isExist = os.path.exists(self.path)
            if not isExist:  # Create a new directory because it does not exist
                os.makedirs(self.path)

            FileisExist = os.path.isfile(self.path_exp)
            if not FileisExist:
                self.wx[0].text(0.01, 0.8, "$" + latex(eval(str(self.exprss)), fold_frac_powers=False, fold_short_frac=False) + "$", fontsize=15, va='center', ha='left')
                dict_latex = {"SS": latex(eval(str(self.exprss)), fold_frac_powers=False, fold_short_frac=False)}
                latex_file = open(self.path + '/latexfile.txt', 'a')
                latex_file.write(str(dict_latex))
                latex_file.write('\n')
                latex_file.close()
                dict = {"SS": str(self.exprss)}
                dict_file = open(self.path + '/Expfile.txt', 'a')
                dict_file.write(str(dict))
                dict_file.write('\n')
                dict_file.close()
                self.wx[1].text(0.01, 0.8, "$" + latex(eval(str(self.exprsp)), fold_frac_powers=False, fold_short_frac=False) + "$", fontsize=15, va='center', ha='left')
                dict_latex = {"SP": latex(eval(str(self.exprsp)), fold_frac_powers=False, fold_short_frac=False)}
                latex_file = open(self.path + '/latexfile.txt', 'a')
                latex_file.write(str(dict_latex))
                latex_file.write('\n')
                latex_file.close()
                dict = {"SP": str(self.exprsp)}
                dict_file = open(self.path + '/Expfile.txt', 'a')
                dict_file.write(str(dict))
                dict_file.write('\n')
                dict_file.close()
                self.wx[2].text(0.01, 0.8, "$" + latex(eval(str(self.exprps)), fold_frac_powers=False, fold_short_frac=False) + "$", fontsize=15, va='center', ha='left')
                dict_latex = {"PS": latex(eval(str(self.exprps)), fold_frac_powers=False, fold_short_frac=False)}
                latex_file = open(self.path + '/latexfile.txt', 'a')
                latex_file.write(str(dict_latex))
                latex_file.write('\n')
                latex_file.close()
                dict = {"PS": str(self.exprps)}
                dict_file = open(self.path + '/Expfile.txt', 'a')
                dict_file.write(str(dict))
                dict_file.write('\n')
                dict_file.close()
                self.wx[3].text(0.01, 0.8, "$" + latex(eval(str(self.exprpp)), fold_frac_powers=False, fold_short_frac=False) + "$", fontsize=15, va='center', ha='left')
                dict_latex = {"PP": latex(eval(str(self.exprpp)), fold_frac_powers=False, fold_short_frac=False)}
                latex_file = open(self.path + '/latexfile.txt', 'a')
                latex_file.write(str(dict_latex))
                latex_file.write('\n')
                latex_file.close()
                dict = {"PP": str(self.exprpp)}
                dict_file = open(self.path + '/Expfile.txt', 'a')
                dict_file.write(str(dict))
                dict_file.write('\n')
                dict_file.close()
            else:
                latex_txt = open(self.path + '/latexfile.txt', 'rt')
                lines = latex_txt.read().split('\n')
                dict_extract = {}
                i = 0
                for l in lines:
                    if l != '':
                        dict_extract[i] = Misc.parse(l)
                        i += 1
                latex_txt.close()
                dict_SS = dict_extract[0]['SS'].replace('\\\\','\\')
                self.wx[0].text(0.01, 0.8, "$" + dict_SS + "$", fontsize=15, va='center', ha='left')
                dict_SP = dict_extract[1]['SP'].replace('\\\\', '\\')
                self.wx[1].text(0.01, 0.8, "$" + dict_SP + "$", fontsize=15, va='center', ha='left')
                dict_PS = dict_extract[2]['PS'].replace('\\\\', '\\')
                self.wx[2].text(0.01, 0.8, "$" + dict_PS + "$", fontsize=15, va='center', ha='left')
                dict_PP = dict_extract[3]['PP'].replace('\\\\', '\\')
                self.wx[3].text(0.01, 0.8, "$" + dict_PP + "$", fontsize=15, va='center', ha='left')
            self.canvs_e.draw()


            # Tab #3
            footer_text = 'Data acquired from http://symmetry.jacobs-university.de'
            title_text, self.charSelect = ct.charTableInit(self.option_var[0])
            cell_text = []
            for row in self.chr_data[self.charSelect]:
                cell_text.append([f'{x}' for x in row])
            self.f_char, self.ax_char = plt.subplots(figsize=(15, 4))
            self.canvs_char = FigureCanvasTkAgg(self.f_char, self.tab_3)
            the_table = self.ax_char.table(cellText=cell_text,
                                  cellLoc='center',
                                  rowLoc='center',
                                  loc='center')

            if self.option_var[0] == 'C1':
                the_table.scale(2, 2)

            if self.option_var[0] == 'S2':
                the_table.scale(2, 2.5)

            if self.option_var[0] == 'C2':
                the_table.scale(2, 2.5)

            if self.option_var[0] == 'C1h':
                the_table.scale(2.5, 2.5)

            if self.option_var[0] == 'C2h':
                the_table.scale(2.5, 2.5)

            if self.option_var[0] == 'D2':
                the_table.scale(2.5, 2.5)

            if self.option_var[0] == 'C2v':
                the_table.scale(2.5, 2.5)

            if self.option_var[0] == 'D2h':
                the_table.scale(2.5, 2)

            if self.option_var[0] == 'C4':
                the_table.scale(2.5, 2.5)

            if self.option_var[0] == 'S4':
                the_table.scale(2.5, 2.5)

            if self.option_var[0] == 'C4h':
                the_table.scale(2.5, 2.5)

            if self.option_var[0] == 'D4':
                the_table.scale(3, 1.6)

            if self.option_var[0] == 'C4v':
                the_table.scale(2.5, 2.5)

            if self.option_var[0] == 'D2d':
                the_table.scale(2.5, 2.5)

            if self.option_var[0] == 'D4h':
                the_table.scale(2.5, 1.25)

            if self.option_var[0] == 'C3':
                the_table.scale(2.5, 2.3)

            if self.option_var[0] == 'S6':
                the_table.scale(2.9, 2.25)

            if self.option_var[0] == 'D3':
                the_table.scale(2.5, 2.5)

            if self.option_var[0] == 'C3v':
                the_table.scale(2.5, 2.5)

            if self.option_var[0] == 'D3d':
                the_table.scale(3, 2.5)

            if self.option_var[0] == 'C6':
                the_table.scale(2.5, 2.5)

            if self.option_var[0] == 'C3h':
                the_table.scale(2.5, 2.5)

            if self.option_var[0] == 'C6h':
                the_table.scale(2.8, 1.6)

            if self.option_var[0] == 'D6':
                the_table.scale(2.5, 2.5)

            if self.option_var[0] == 'C6v':
                the_table.scale(2.5, 2.5)

            if self.option_var[0] == 'D3h':
                the_table.scale(2.5, 2.5)

            if self.option_var[0] == 'D6h':
                the_table.scale(3.5, 1.4)

            if self.option_var[0] == 'T':
                the_table.scale(2.5, 2.5)

            if self.option_var[0] == 'Th':
                the_table.scale(3.5, 2)

            if self.option_var[0] == 'O':
                the_table.scale(2.5, 2.5)

            if self.option_var[0] == 'Td':
                the_table.scale(2.5, 2.5)

            if self.option_var[0] == 'Oh':
                the_table.scale(4, 1.6)

            the_table.set_fontsize(16)
            the_table.auto_set_column_width(col=list(range(len(cell_text))))
            self.ax_char.get_xaxis().set_visible(False)
            self.ax_char.get_yaxis().set_visible(False)
            # Hide axes border
            self.ax_char.spines['top'].set_visible(False)
            self.ax_char.spines['right'].set_visible(False)
            self.ax_char.spines['bottom'].set_visible(False)
            self.ax_char.spines['left'].set_visible(False)
            # Add title
            self.ax_char.set_title(title_text, {'fontsize':18,'fontweight':'bold'})
            plt.figtext(0.85, 0.05, footer_text, horizontalalignment='center', size=8, weight='bold')
            self.canvs_char._tkcanvas.grid(column=0, row=0)
            self.canvs_char.draw()

            self.notebook.add(self.tab_1, text="Graph")
            self.notebook.add(self.tab_2, text="Expression")
            self.notebook.add(self.tab_3, text="Character Table")
            self.notebook.add(self.tab_4, text="General Tensor (Coming Soon...)")

            self.fr_input_dw = ScrolledFrame(self.newWindow)
            self.fr_input_dw.grid(column=0, row=1, ipadx=600, ipady=70)
            self.fr_button_dw = Frame(self.newWindow)
            self.fr_button_dw.grid(row=2, column=0, ipadx=760, ipady=20)

            self.fr_input_dw.bind_arrow_keys(root)
            self.fr_input_dw.bind_scroll_wheel(root)

            # Create a frame within the ScrolledFrame
            self.fr_input_dw_inside = self.fr_input_dw.display_widget(Frame)

            if len(self.symbolList_pp) < len(self.symbolList_ps):
                num_rows = len(self.symbolList_ps)+1
            else:
                num_rows = len(self.symbolList_pp)+1
            num_cols = 15
            for row in range(num_rows):
                for column in range(num_cols):
                    w = Label(self.fr_input_dw_inside,
                              width=15,
                              height=2,
                              borderwidth=0,
                              relief="groove",
                              anchor="center",
                              justify="center")

                    w.grid(row=row,
                           column=column,
                           padx=4,
                           pady=4)

            self.entryList_ss = []
            self.entryList_sp = []
            self.entryList_ps = []
            self.entryList_pp = []

            # loop over the symbolList and create labels and entries for each symbol within it
            count = 0
            self.label = Label(self.fr_input_dw_inside, text="SS", borderwidth=2, justify="left", font=('Arial', 18))
            self.label_position = 275
            self.label_gap = 320
            self.label.place(x=self.label_position, y=4)
            self.label_position += self.label_gap
            range_validation = (root.register(self.validate), '%P', '%W')

            SlideStr_theta = DoubleVar()

            for i in range(len(self.symbolList_ss)):
                # create labels
                self.label = Label(self.fr_input_dw_inside, text=Misc.showSymbol(self.symbolList_ss[i]),
                                   borderwidth=2, justify="left", font=('Arial', 14))
                self.label.place(x=191, y=34 + i * 40, width=40, height=40)

                inputStr = StringVar()
                SlideStr = IntVar()
                if i == 0:
                    if chr(952) == Misc.showSymbol(self.symbolList_ss[0]):
                        self.Spin = Spinbox(self.fr_input_dw_inside, from_=-360, to=360, textvariable=SlideStr_theta, relief='groove',
                                            validate='key', validatecommand=range_validation,
                                            command=lambda: self.autoPlot())
                        self.Spin.bind('<Return>', lambda x: self.autoPlot())

                        self.entryList_ss.append(self.Spin)
                        self.Spin.place(x=241, y=34, width=100, height=40)
                    else:
                        self.Spin = Spinbox(self.fr_input_dw_inside, from_=-10, to=10, textvariable=SlideStr, relief='groove',
                                            validate='key', validatecommand=range_validation,
                                            command=lambda: self.autoPlot())
                        self.entryList_ss.append(self.Spin)
                        self.Spin.bind('<Return>', lambda x: self.autoPlot())
                        self.Spin.place(x=241, y=34 + i * 40, width=100, height=40)
                else:
                    self.Spin = Spinbox(self.fr_input_dw_inside, from_=-10, to=10, textvariable=SlideStr, relief='groove',
                                        validate='key', validatecommand=range_validation, command=lambda: self.autoPlot())
                    self.entryList_ss.append(self.Spin)
                    self.Spin.bind('<Return>', lambda x: self.autoPlot())
                    self.Spin.place(x=241, y=34 + i * 40, width=100, height=40)

                count = count + 1
                value = self.Spin.get()

            self.label = Label(self.fr_input_dw_inside, text="SP", borderwidth=2, justify="left", font=('Arial', 18))
            self.label.place(x=self.label_position, y=4)
            self.label_position += self.label_gap
            for j in range(len(self.symbolList_sp)):

                # create labels
                self.label = Label(self.fr_input_dw_inside, text=Misc.showSymbol(self.symbolList_sp[j]),
                                   borderwidth=2, justify="left", font=('Arial', 14))
                self.label.place(x=509, y=34 + j * 40, width=40, height=40)

                inputStr = StringVar()
                SlideStr = DoubleVar()

                if j == 0:
                    if chr(952) == Misc.showSymbol(self.symbolList_sp[0]):
                        self.Spin = Spinbox(self.fr_input_dw_inside, from_=-360, to=360, textvariable=SlideStr_theta, relief='groove',
                                            validate='key', validatecommand=range_validation,
                                            command=lambda: self.autoPlot())
                        self.Spin.bind('<Return>', lambda x: self.autoPlot())

                        self.entryList_sp.append(self.Spin)
                        self.Spin.place(x=559, y=34, width=100, height=40)
                    else:
                        self.Spin = Spinbox(self.fr_input_dw_inside, from_=-10, to=10, textvariable=SlideStr, relief='groove',
                                            validate='key', validatecommand=range_validation,
                                            command=lambda: self.autoPlot())
                        self.entryList_sp.append(self.Spin)
                        self.Spin.bind('<Return>', lambda x: self.autoPlot())
                        self.Spin.place(x=559, y=34 + j * 40, width=100, height=40)
                else:
                    self.Spin = Spinbox(self.fr_input_dw_inside, from_=-10, to=10, textvariable=SlideStr, relief='groove',
                                        validate='key', validatecommand=range_validation, command=lambda: self.autoPlot())
                    self.entryList_sp.append(self.Spin)
                    self.Spin.bind('<Return>', lambda x: self.autoPlot())
                    self.Spin.place(x=559, y=34 + j * 40, width=100, height=40)

                count = count + 1
                value = self.Spin.get()

            count = 0
            self.label = Label(self.fr_input_dw_inside, text="PS", borderwidth=2, justify="left", font=('Arial', 18))
            self.label.place(x=self.label_position, y=4)
            self.label_position += self.label_gap
            for k in range(len(self.symbolList_ps)):
                # create labels
                self.label = Label(self.fr_input_dw_inside, text=Misc.showSymbol(self.symbolList_ps[k]),
                                   borderwidth=2, justify="left", font=('Arial', 14))
                self.label.place(x=835, y=34 + k * 40, width=40, height=40)

                SlideStr = DoubleVar()

                if k == 0:
                    if chr(952) == Misc.showSymbol(self.symbolList_ps[0]):
                        self.Spin = Spinbox(self.fr_input_dw_inside, from_=-360, to=360, textvariable=SlideStr_theta, relief='groove',
                                            validate='key', validatecommand=range_validation,
                                            command=lambda: self.autoPlot())
                        self.Spin.bind('<Return>', lambda x: self.autoPlot())

                        self.entryList_ps.append(self.Spin)
                        self.Spin.place(x=885, y=34, width=100, height=40)
                    else:
                        self.Spin = Spinbox(self.fr_input_dw_inside, from_=-10, to=10, textvariable=SlideStr, relief='groove',
                                            validate='key', validatecommand=range_validation,
                                            command=lambda: self.autoPlot())
                        self.entryList_ps.append(self.Spin)
                        self.Spin.bind('<Return>', lambda x: self.autoPlot())
                        self.Spin.place(x=885, y=34 + k * 40, width=100, height=40)
                else:
                    self.Spin = Spinbox(self.fr_input_dw_inside, from_=-10, to=10, textvariable=SlideStr, relief='groove',
                                        validate='key', validatecommand=range_validation, command=lambda: self.autoPlot())
                    self.entryList_ps.append(self.Spin)
                    self.Spin.bind('<Return>', lambda x: self.autoPlot())
                    self.Spin.place(x=885, y=34 + k * 40, width=100, height=40)

                count = count + 1

            count = 0
            self.label = Label(self.fr_input_dw_inside, text="PP", borderwidth=2, justify="left", font=('Arial', 18))
            self.label.place(x=self.label_position, y=4)
            self.label_position += self.label_gap
            for h in range(len(self.symbolList_pp)):
                # create labels

                self.label = Label(self.fr_input_dw_inside, text=Misc.showSymbol(self.symbolList_pp[h]),
                                   borderwidth=2, justify="left", font=('Arial', 14))
                self.label.place(x=1153, y=34 + h * 40, width=40, height=40)

                inputStr = StringVar()
                SlideStr = DoubleVar()
                if h == 0:
                    if chr(952) == Misc.showSymbol(self.symbolList_pp[0]):
                        self.Spin = Spinbox(self.fr_input_dw_inside, from_=-360, to=360, textvariable=SlideStr_theta, relief='groove',
                                            validate='key', validatecommand=range_validation,
                                            command=lambda: self.autoPlot())
                        self.Spin.bind('<Return>', lambda x: self.autoPlot())
                        self.entryList_pp.append(self.Spin)
                        self.Spin.place(x=1203, y=34, width=100, height=40)
                    else:
                        self.Spin = Spinbox(self.fr_input_dw_inside, from_=-10, to=10, textvariable=SlideStr, relief='groove',
                                            validate='key', validatecommand=range_validation,
                                            command=lambda: self.autoPlot())
                        self.entryList_pp.append(self.Spin)
                        self.Spin.bind('<Return>', lambda x: self.autoPlot())
                        self.Spin.place(x=1203, y=34 + h * 40, width=100, height=40)

                else:
                    self.Spin = Spinbox(self.fr_input_dw_inside, from_=-10, to=10, textvariable=SlideStr, relief='groove',
                                        validate='key', validatecommand=range_validation, command=lambda: self.autoPlot())
                    self.entryList_pp.append(self.Spin)
                    self.Spin.bind('<Return>', lambda x: self.autoPlot())
                    self.Spin.place(x=1203, y=34 + h * 40, width=100, height=40)
                    self.Spin.place(x=1203, y=34 + h * 40, width=100, height=40)

                count = count + 1
                value = self.Spin.get()

            self.button3 = ttk.Checkbutton(self.fr_button_dw, text='Quit', command=lambda: self._quit(), style="Toggle.TButton")

            self.button3.place(x=1420, y=10)
            self.button4 = ttk.Button(self.fr_button_dw, text='Back', command=lambda: self._back())

            self.button4.place(x=1344, y=10)
            self.button5 = ttk.Button(self.fr_button_dw, text='?')
            self.button5.place(x=5, y=10)
            myTip = Hovertip(self.button5, 'Switch through different tabs to check plot, equations and character table. '
                                           '\nExport the graph, expression (latex), and character table through Menu->File.', hover_delay=1000)

            def doSomething():
                self.newWindow.destroy()
                self.opened=false

            self.newWindow.protocol('WM_DELETE_WINDOW', doSomething)  # root is your root window

        def validate(self, user_input, widget_name):
            def isfloat(num):
                try:
                    float(num)
                    return True
                except ValueError:
                    return False

            if isfloat(user_input) or user_input == '-':
                # Fetching minimum and maximum value of the spinbox
                minval = int(root.nametowidget(widget_name).config('from')[4])
                maxval = int(root.nametowidget(widget_name).config('to')[4])

                # check if the number is within the range
                if int(float(user_input)) not in range(minval - 1, maxval + 1):
                    messagebox.showinfo(title="Out of Range Warning",
                                        message='The input range is from {} to {}!'.format(minval, maxval), icon='warning')
                    return False
                return True

            # if input is blank string
            elif user_input == "":
                return True

            else:
                messagebox.showinfo(title="Invalid Inputs Warning",
                                    message='Please enter a valid number', icon='warning')
                return False

        def pop_up_warning(self):
            messagebox.showinfo(title="Warning", message='Please select all the option!', icon='warning')

        # initialize the global variables
        def buffer(self):
            self.cal_bt_dis['state'] = ACTIVE


    # construct the main window
    try:
        root = Tk()
        sv_ttk.set_theme('light')
        root.title("SHG Simulation Tool v0.0.5")
        window1 = polarplotGUI(root)
        window1.grid(row=0, column=0)
        root.mainloop()
    except:
        import traceback
        traceback.print_exc()
        input("Press Enter to end...")


theta, phi, xxx, xxy, xxz, xyx, xyy, xyz, xzx, xzy, xzz, yxx, yxy, yxz, yyx, yyy, yyz, yzx, yzy, yzz, zxx, zxy, zxz, zyx, zyy, zyz, zzx, zzy, zzz, \
xxxx, xxxy, xxxz, xyxx, xyxy, xyxz, xzxx, xzxy, xzxz, xxyx, xxyy, xxyz, xyyx, xyyy, xyyz, xzyx, xzyy, xzyz, xxzx, xxzy, xxzz, xyzx, xyzy, xyzz, \
xzzx, xzzy, xzzz, yxxx, yxxy, yxxz, yyxx, yyxy, yyxz, yzxx, yzxy, yzxz, yxyx, yxyy, yxyz, yyyx, yyyy, yyyz, yzyx, yzyy, yzyz, yxzx, yxzy, yxzz, \
yyzx, yyzy, yyzz, yzzx, yzzy, yzzz, zxxx, zxxy, zxxz, zyxx, zyxy, zyxz, zzxx, zzxy, zzxz, zxyx, zxyy, zxyz, zyyx, zyyy, zyyz, zzyx, zzyy, zzyz, \
zxzx, zxzy, zxzz, zyzx, zyzy, zyzz, zzzx, zzzy, zzzz = symbols(
    'theta phi xxx xxy xxz xyx xyy xyz xzx xzy xzz yxx yxy yxz yyx yyy yyz yzx yzy yzz zxx zxy zxz zyx zyy zyz zzx '
    'zzy zzz xxxx xxxy xxxz xyxx xyxy xyxz xzxx xzxy xzxz xxyx xxyy xxyz xyyx xyyy xyyz xzyx xzyy xzyz xxzx xxzy '
    'xxzz xyzx xyzy xyzz xzzx xzzy xzzz yxxx yxxy yxxz yyxx yyxy yyxz yzxx yzxy yzxz yxyx yxyy yxyz yyyx yyyy yyyz '
    'yzyx yzyy yzyz yxzx yxzy yxzz yyzx yyzy yyzz yzzx yzzy yzzz zxxx zxxy zxxz zyxx zyxy zyxz zzxx zzxy zzxz zxyx '
    'zxyy zxyz zyyx zyyy zyyz zzyx zzyy zzyz zxzx zxzy zxzz zyzx zyzy zyzz zzzx zzzy zzzz')

phi_value = np.arange(0, 2 * np.pi, .01)[1:]
run()