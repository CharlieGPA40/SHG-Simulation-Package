'''
Author  :Chunli Tang, Hussam Mustqfa
Project :Polar Plot GUI
FileName:
Time    :
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
import webview
from tkscrolledframe import ScrolledFrame
from PIL import ImageTk, Image
import webbrowser
import os
from sympy.parsing.sympy_parser import parse_expr
import sv_ttk
import sys
from idlelib.tooltip import Hovertip
from tkinter import filedialog
from tkinter.filedialog import asksaveasfilename, asksaveasfile

# ************************************** #
# construct a class used to generate the polar plot
class Win2:
    def __init__(self, _root):
        self.root = _root
        width = 670  # Width
        height = 570  # Height
        screen_width = root.winfo_screenwidth()  # Width of the screen
        screen_height = root.winfo_screenheight()  # Height of the screen

        # Calculate Starting X and Y coordinates for Window
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)

        self.root.geometry('%dx%d+%d+%d' % (width, height, x, y))
        self.root.title("About SHG Simulation Tool")
        self.root.maxsize(670, 570)
        # self.root.configure(bg='#F2F3F4')
        self.root.protocol("WM_DELETE_WINDOW", self.close)
        au_logo = Image.open("Image/vect.png")
        au_logo = au_logo.resize((400, 200))
        au_logo = ImageTk.PhotoImage(au_logo)
        label_au = Label(self.root, image=au_logo)
        label_au.image = au_logo
        label_au.grid(column=0, row=0)
        lbl = Label(self.root, text="This Package is developed by Chunli Tang (Code, Design & Build) and Hussam Mustafa (Term Verification)",
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
        wb_label.bind("<Button-1>", lambda e: callback("http://wp.auburn.edu/JinLab/"))
        wb_label.grid(column=0, row=8)

        # lbl = Label(self.root, text="LICENSE", font=80)
        # lbl.grid(column=0, row=9, pady=20)

        self.paned = Frame(master=self.root)
        self.paned.grid(row=9, column=0, ipadx=0, ipady=0)
        self.notebook = ttk.Notebook(self.paned)
        self.notebook.grid(row=0, column=0)
        self.tab_1 = Frame(self.notebook)
        self.tab_2 = Frame(self.notebook)
        self.tab_3 = Frame(self.notebook)

        license_box = Text(self.tab_1, height=10, width=80, relief='sunken')
        license_box.grid(column=0, row=10)
        disclaimer = 'Apache License' \
                     '\nVersion 2.0, January 2004' \
                     '\nhttp://www.apache.org/licenses/' \
                     '\n\nTERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION' \
                     '\n1. Definitions.' \
                     '\n"License" shall mean the terms and conditions for use, reproduction,' \
                     'and distribution as defined by Sections 1 through 9 of this document.' \
                     '\n\n"Licensor" shall mean the copyright owner or entity authorized by' \
                     'the copyright owner that is granting the License.' \
                     '\n\n"Legal Entity" shall mean the union of the acting entity and all' \
                     'other entities that control, are controlled by, or are under common' \
                     'control with that entity. For the purposes of this definition,' \
                     '\n\n"control" means (i) the power, direct or indirect, to cause the ' \
                     'direction or management of such entity, whether by contract or ' \
                     'otherwise, or (ii) ownership of fifty percent (50%) or more of the' \
                     'outstanding shares, or (iii) beneficial ownership of such entity.' \
                     '\n\n"You" (or "Your") shall mean an individual or Legal Entity ' \
                     'exercising permissions granted by this License.' \
                     '\n\n"Source" form shall mean the preferred form for making modifications, ' \
                     'including but not limited to software source code, documentation ' \
                     'source, and configuration files. ' \
                     '\n\n"Object" form shall mean any form resulting from mechanical ' \
                     'transformation or translation of a Source form, including but' \
                     ' not limited to compiled object code, generated documentation,' \
                     ' and conversions to other media types.' \
                     '\n\n"Work" shall mean the work of authorship, whether in Source or' \
                     ' Object form, made available under the License, as indicated by a ' \
                     'copyright notice that is included in or attached to the work' \
                     ' (an example is provided in the Appendix below). ' \
                     '\n\n"Derivative Works" shall mean any work, whether in Source or Object' \
                     ' form, that is based on (or derived from) the Work and for which the' \
                     ' editorial revisions, annotations, elaborations, or other modifications ' \
                     'represent, as a whole, an original work of authorship. For the purposes ' \
                     'of this License, Derivative Works shall not include works that remain ' \
                     'separable from, or merely link (or bind by name) to the interfaces of, ' \
                     'the Work and Derivative Works thereof.' \
                     '\n\n"Contribution" shall mean any work of authorship, including ' \
                     'the original version of the Work and any modifications or additions ' \
                     'to that Work or Derivative Works thereof, that is intentionally ' \
                     'submitted to Licensor for inclusion in the Work by the copyright owner ' \
                     'or by an individual or Legal Entity authorized to submit on behalf of ' \
                     'the copyright owner. For the purposes of this definition, "submitted" ' \
                     'means any form of electronic, verbal, or written communication sent ' \
                     'to the Licensor or its representatives, including but not limited to ' \
                     'communication on electronic mailing lists, source code control systems ,' \
                     'and issue tracking systems that are managed by, or on behalf of, the ' \
                     'Licensor for the purpose of discussing and improving the Work, but ' \
                     'excluding communication that is conspicuously marked or otherwise ' \
                     'designated in writing by the copyright owner as "Not a Contribution."' \
                     '\n\n"Contributor" shall mean Licensor and any individual or Legal Entity on ' \
                     'behalf of whom a Contribution has been received by Licensor and ' \
                     'subsequently incorporated within the Work.' \
                     '\n\n2. Grant of Copyright License. Subject to the terms and conditions of' \
                     ' this License, each Contributor hereby grants to You a perpetual, ' \
                     'worldwide, non-exclusive, no-charge, royalty-free, irrevocable ' \
                     'copyright license to reproduce, prepare Derivative Works of, ' \
                     'publicly display, publicly perform, sublicense, and distribute the ' \
                     'Work and such Derivative Works in Source or Object form. ' \
                     '\n\n3. Grant of Patent License. Subject to the terms and conditions of ' \
                     'this License, each Contributor hereby grants to You a perpetual, ' \
                     'worldwide, non-exclusive, no-charge, royalty-free, irrevocable ' \
                     '(except as stated in this section) patent license to make, have made, ' \
                     'use, offer to sell, sell, import, and otherwise transfer the Work, ' \
                     'where such license applies only to those patent claims licensable ' \
                     'by such Contributor that are necessarily infringed by their ' \
                     'Contribution(s) alone or by combination of their Contribution(s) ' \
                     'with the Work to which such Contribution(s) was submitted. If You ' \
                     'institute patent litigation against any entity (including a ' \
                     'cross-claim or counterclaim in a lawsuit) alleging that the Work ' \
                     'or a Contribution incorporated within the Work constitutes direct ' \
                     'or contributory patent infringement, then any patent licenses ' \
                     'granted to You under this License for that Work shall terminate ' \
                     'as of the date such litigation is filed. ' \
                     '\n\n4. Redistribution. You may reproduce and distribute copies of the ' \
                     'Work or Derivative Works thereof in any medium, with or without ' \
                     'modifications, and in Source or Object form, provided that You' \
                     ' meet the following conditions: ' \
                     '\n(a) You must give any other recipients of the Work or' \
                     'Derivative Works a copy of this License; and' \
                     '\n\n(b) You must cause any modified files to carry prominent notices ' \
                     'stating that You changed the files; and ' \
                     '\n\n(c) You must retain, in the Source form of any Derivative Works' \
                     ' that You distribute, all copyright, patent, trademark, and ' \
                     'attribution notices from the Source form of the Work,' \
                     'excluding those notices that do not pertain to any part of ' \
                     'the Derivative Works; and ' \
                     '\n\n(d) If the Work includes a "NOTICE" text file as part of its ' \
                     'distribution, then any Derivative Works that You distribute must ' \
                     'include a readable copy of the attribution notices contained ' \
                     'within such NOTICE file, excluding those notices that do not ' \
                     'pertain to any part of the Derivative Works, in at least one ' \
                     'of the following places: within a NOTICE text file distributed ' \
                     'as part of the Derivative Works; within the Source form or ' \
                     'documentation, if provided along with the Derivative Works; or, ' \
                     'within a display generated by the Derivative Works, if and ' \
                     'wherever such third-party notices normally appear. The contents ' \
                     'of the NOTICE file are for informational purposes only and ' \
                     'do not modify the License. You may add Your own attribution ' \
                     'notices within Derivative Works that You distribute, alongside' \
                     ' or as an addendum to the NOTICE text from the Work, provided ' \
                     'that such additional attribution notices cannot be construed ' \
                     'as modifying the License.' \
                     '\n\nYou may add Your own copyright statement to Your modifications and ' \
                     'may provide additional or different license terms and conditions ' \
                     'for use, reproduction, or distribution of Your modifications, or ' \
                     'for any such Derivative Works as a whole, provided Your use, ' \
                     'reproduction, and distribution of the Work otherwise complies with' \
                     ' the conditions stated in this License.' \
                     '\n\n5. Submission of Contributions. Unless You explicitly state otherwise, ' \
                     'any Contribution intentionally submitted for inclusion in the Work ' \
                     'by You to the Licensor shall be under the terms and conditions of ' \
                     'this License, without any additional terms or conditions. ' \
                     'Notwithstanding the above, nothing herein shall supersede or modify ' \
                     'the terms of any separate license agreement you may have executed ' \
                     'with Licensor regarding such Contributions. ' \
                     '\n\n6. Trademarks. This License does not grant permission to use the trade ' \
                     'names, trademarks, service marks, or product names of the Licensor, ' \
                     'except as required for reasonable and customary use in describing the ' \
                     'origin of the Work and reproducing the content of the NOTICE file.' \
                     '\n\n7. Disclaimer of Warranty. Unless required by applicable law or ' \
                     'agreed to in writing, Licensor provides the Work (and each ' \
                     'Contributor provides its Contributions) on an "AS IS" BASIS, ' \
                     ' WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or ' \
                     'implied, including, without limitation, any warranties or conditions ' \
                     'of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A ' \
                     'PARTICULAR PURPOSE. You are solely responsible for determining the ' \
                     'appropriateness of using or redistributing the Work and assume any ' \
                     'risks associated with Your exercise of permissions under this License.' \
                     '\n\n8. Limitation of Liability. In no event and under no legal theory, ' \
                     'whether in tort (including negligence), contract, or otherwise, ' \
                     'unless required by applicable law (such as deliberate and grossly ' \
                     'negligent acts) or agreed to in writing, shall any Contributor be ' \
                     'liable to You for damages, including any direct, indirect, special, ' \
                     'incidental, or consequential damages of any character arising as a ' \
                     'result of this License or out of the use or inability to use the ' \
                     'Work (including but not limited to damages for loss of goodwill, ' \
                     'work stoppage, computer failure or malfunction, or any and all ' \
                     'other commercial damages or losses), even if such Contributor ' \
                     'has been advised of the possibility of such damages. ' \
                     '\n\n9. Accepting Warranty or Additional Liability. While redistributing ' \
                     'the Work or Derivative Works thereof, You may choose to offer, ' \
                     'and charge a fee for, acceptance of support, warranty, indemnity, ' \
                     'or other liability obligations and/or rights consistent with this ' \
                     'License. However, in accepting such obligations, You may act only ' \
                     'on Your own behalf and on Your sole responsibility, not on behalf ' \
                     'of any other Contributor, and only if You agree to indemnify, ' \
                     'defend, and hold each Contributor harmless for any liability ' \
                     'incurred by, or claims asserted against, such Contributor by reason ' \
                     'of your accepting any such warranty or additional liability.' \
                     '\n\nEND OF TERMS AND CONDITIONS' \
                     '\n\nCopyright 2023 Chunli Tang' \
                     '\n\nLicensed under the Apache License, Version 2.0 (the "License");' \
                     '\nyou may not use this file except in compliance with the License.' \
                     '\nYou may obtain a copy of the License at' \
                     '\n\n\thttp://www.apache.org/licenses/LICENSE-2.0' \
                     '\n\nUnless required by applicable law or agreed to in writing, software' \
                     ' distributed under the License is distributed on an "AS IS" BASIS, ' \
                     'WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. ' \
                     'See the License for the specific language governing permissions and ' \
                     'limitations under the License.'
        license_box.insert(END, disclaimer)
        license_box.config(state='disabled')

        Ack_box = Text(self.tab_2, height=10, width=80, relief='sunken')
        Ack_box.grid(column=0, row=10)
        acknowledge = 'This work was supported by NSF EPM Grant No. DMR-2129879 ' \
                      '\n\nWe would like to give a special thanks to: \nBrian Opatosky, Matt Galinger'
        Ack_box.insert(END, acknowledge)
        license_box.config(state='disabled')


        ref_box = Text(self.tab_3, height=10, width=80, relief='sunken')
        ref_box.grid(column=0, row=10)
        reference = '[1] Li, Yilei et al. "Probing symmetry properties of few-layer MoS2 and h-BN by optical second-harmonic generation." Nano letters vol. 13,7 (2013): 3329-33. doi: 10.1021/n/401561г.' \
                    '\n[2] Fiebig, Manfred et al. "Second-harmonic generation as a tool for studying electronic and magnetic structures of crystals: review."Journalof The Optical Societyof America B-optical Physics 22 (2005): 96-118.' \
                    '\n[3] http://symmetry.jacobs-university.de/group.html.' \
                    '\n[4] Gallego et al. "Automatic calculation of symmetry-adapted tensors in magnetic and non-magnetic materials: a new tool of the Bilbao Crystallographic Server" Acta Cryst. A (2019) 75, 438-447.' \
                    '\n[5] Boyd, Robert W. Nonlinear optics. Academic press, 2020.'
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
        width = 197  # Width
        height = 255  # Height
        screen_width = root.winfo_screenwidth()  # Width of the screen
        screen_height = root.winfo_screenheight()  # Height of the screen

        # Calculate Starting X and Y coordinates for Window
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)

        self.root.geometry('%dx%d+%d+%d' % (width, height, x, y))
        # self.root.geometry("197x255+500+300")
        self.root.maxsize(197, 255)
        self.root.title("Group Website")
        # self.root.configure(bg='#F2F3F4')
        self.root.protocol("WM_DELETE_WINDOW", self.close)
        qr_code = Image.open("Image/frame.png")
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
        width = 800  # Width
        height = 605  # Height
        screen_width = root.winfo_screenwidth()  # Width of the screen
        screen_height = root.winfo_screenheight()  # Height of the screen

        # Calculate Starting X and Y coordinates for Window
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)

        self.root.geometry('%dx%d+%d+%d' % (width, height, x, y))
        # self.root.geometry("800x605+100+300")
        self.root.maxsize(800, 605)
        self.root.title("Caculation Model")
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
        while 0 <= self.click_loop < 3:
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
        width = 300  # Width
        height = 200  # Height
        screen_width = root.winfo_screenwidth()  # Width of the screen
        screen_height = root.winfo_screenheight()  # Height of the screen

        # Calculate Starting X and Y coordinatesr for Window
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)

        self.root.geometry('%dx%d+%d+%d' % (width, height, x, y))
        self.root.maxsize(300,200)
        self.root.title("About SHG Simulation Tool")
        # self.root.configure(bg='#F2F3F4')
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
                    text="Version 1.0", font='Helvetica 11', fg='#5b5b5b')
        lbl.grid(column=0, row=2)
        lbl = Label(self.root,
                    text="Auburn University Ultrafast Nonlinear Optics Lab 2023", font='Helvetica 11', fg='#5b5b5b')
        lbl.grid(column=0, row=3)
        lbl = Label(self.root,
                    text="All rights reserved", font='Helvetica 11', fg='#5b5b5b')
        lbl.grid(column=0, row=4)
        def callback(url):
            webbrowser.open_new_tab(url)

        wb_label = Label(self.root, text="Github", font=22, fg="blue", cursor="hand2")
        wb_label.bind("<Button-1>", lambda e: callback("http://wp.auburn.edu/JinLab/"))
        wb_label.grid(column=0, row=5)


    def close(self):
        self.root.destroy()

class polarplotGUI(Frame):
    """
    polarplotGUI inherits the class Frame

    Returns:
        nothing, just do the ploting
    """
    def __init__(self, master=None):
        super().__init__(master)
        # This line is for packaging
        # os.chdir(sys._MEIPASS)

        self.master = master
        self.win2_status = 0
        self.win3_status = 0
        self.win4_status = 0
        self.win5_status = 0
        # Only work for windows
        menu_bar = Menu(self.master)
        self.master['menu'] = menu_bar

        self.IntroMenu = Menu(menu_bar)
        self.IntroMenu.add_command(label="About SHG Simulation Package", command=lambda: self.about_page_version())
        self.IntroMenu.add_separator()
        self.IntroMenu.add_command(label="Quit", command=lambda: self.quit(), accelerator='⌘+Q')
        menu_bar.add_cascade(label='SHG', menu=self.IntroMenu)

        # self.file_menu = Menu(menu_bar)
        # self.file_menu.add_command(label="Export Polar Graph...", command=lambda: self.plot().export_graph())
        # self.file_menu.add_command(label="Export Expression Latex...", command=lambda: self.export_expression_latex())
        # self.file_menu.add_command(label="Export Expression Text...", command=lambda: self.export_expression())
        # self.file_menu.add_command(label="Export Table...", command=lambda: self.quit())
        #
        # menu_bar.add_cascade(label='File', menu=self.file_menu)

        edit = Menu(menu_bar)
        edit.add_command(label="Calculation Model", command=lambda: self.Cal_Mod())
        menu_bar.add_cascade(label='Model', menu=edit)

        Help = Menu(menu_bar)
        Help.add_command(label='Contact Us', command=lambda: self.contact())
        Help.add_separator()
        Help.add_command(label="About...", command=lambda: self.about_page_detail())
        menu_bar.add_cascade(label='Help', menu=Help)

        # self.file_menu.entryconfig("Export Polar Graph...", state="disabled")
        # self.file_menu.entryconfig("Export Expression Latex...", state="disabled")
        # self.file_menu.entryconfig("Export Expression Text...", state="disabled")
        # self.file_menu.entryconfig("Export Table...", state="disabled")

        # p1 = PhotoImage(file='auburn.png')
        # Icon set for program window
        # self.master.iconphoto(False, p1)

        self.setupDict()
        self.charTable()
        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=1)

        self.top2 = None
        self.createWidget()

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

    def setupDict(self):
        self.dic = {'Triclinic': {
            'C1': Matrix(
                [[xxx, xyx, xzx], [xxy, xyy, xzy], [xxz, xyz, xzz], [yxx, yyx, yzx], [yxy, yyy, yzy], [yxz, yyz, yzz],
                 [zxx, zyx, zzx], [zxy, zyy, zzy], [zxz, zyz, zzz]]).subs([(xxy, xyx), (xxz, xzx), (xyz, xzy),
                                                                           (yxy, yyx), (yxz, yzx), (yyz, yzy),
                                                                           (zxy, zyx), (zxz, zzx), (zyz, zzy)]),
            'S2': Matrix([[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0],
                          [0, 0, 0]])},
            'Monoclinic': {'C2': Matrix(
                [[0, xyx, 0], [xxy, 0, xzy], [0, xyz, 0], [yxx, 0, yzx], [0, yyy, 0], [yxz, 0, yzz], [0, zyx, 0],
                 [zxy, 0, zzy], [0, zyz, 0]]).subs([(xxy, xyx), (xyz, xzy), (yxz, yzx), (zxy, zyx), (zyz, zzy)]),
                           'C1h': Matrix(
                               [[xxx, 0, xzx], [0, xyy, 0], [xxz, 0, xzz], [0, yyx, 0], [yxy, 0, yzy], [0, yyz, 0],
                                [zxx, 0, zzx], [0, zyy, 0], [zxz, 0, zzz]]).subs([(xxz, xzx), (yxy, yyx), (yyz, yzy),
                                                                                  (zxz, zzx)]),
                           'C2h': Matrix(
                               [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0],
                                [0, 0, 0]])},
            'Orthorhombic': {
                'D2': Matrix([[0, 0, 0], [0, 0, xzy], [0, xyz, 0], [0, 0, yzx], [0, 0, 0], [yxz, 0, 0], [0, zyx, 0],
                              [zxy, 0, 0], [0, 0, 0]]).subs([(xyz, xzy), (yxz, yzx), (zxy, zyx)]),
                'C2v': Matrix(
                    [[0, 0, xzx], [0, 0, 0], [xxz, 0, 0], [0, 0, 0], [0, 0, yzy], [0, yyz, 0], [zxx, 0, 0],
                     [0, zyy, 0], [0, 0, zzz]]).subs([(xxz, xzx), (yyz, yzy)]),
                'D2h': Matrix([[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0],
                               [0, 0, 0]])},
            'Tetragonal': {
                'C4': Matrix([[0, 0, xzx], [0, 0, xzy], [xxz, xyz, 0], [0, 0, yzx], [0, 0, yzy], [yxz, yyz, 0],
                              [zxx, zyx, 0], [zxy, zyy, 0], [0, 0, zzz]]).subs([(xyz, -yxz), (xzy, -yzx), (xzx, yzy),
                                                                                (xxz, yyz), (zxx, zyy), (zxy, -zyx),
                                                                                (yyz, yzy), (yxz, yzx)]),
                'S4': Matrix([[0, 0, xzx], [0, 0, xzy], [xxz, xyz, 0], [0, 0, yzx], [0, 0, yzy], [yxz, yyz, 0],
                              [zxx, zyx, 0], [zxy, zyy, 0], [0, 0, 0]]).subs([(xyz, yxz), (xzy, yzx), (xzx, -yzy),
                                                                              (xxz, -yyz), (zxx, -zyy), (zxy, zyx),
                                                                              (yyz, yzy), (yxz, yzx)]),
                'D4': Matrix([[0, 0, 0], [0, 0, xzy], [0, xyz, 0], [0, 0, yzx], [0, 0, 0], [yxz, 0, 0],
                              [0, zyx, 0], [zxy, 0, 0], [0, 0, 0]]).subs([(xyz, -yxz), (xzy, -yzx), (zxy, -zyx),
                                                                          (yxz, yzx)]),
                'C4v': Matrix([[0, 0, xzx], [0, 0, 0], [xxz, 0, 0], [0, 0, 0], [0, 0, yzy], [0, yyz, 0],
                               [zxx, 0, 0], [0, zyy, 0], [0, 0, zzz]]).subs([(xzx, yzy), (xxz, yyz), (zxx, zyy),
                                                                             (yyz, yzy)]),
                'D2d': Matrix([[0, 0, 0], [0, 0, xzy], [0, xyz, 0], [0, 0, yzx], [0, 0, 0], [yxz, 0, 0],
                               [0, zyx, 0], [zxy, 0, 0], [0, 0, 0]]).subs([(xyz, yxz), (xzy, yzx), (zxy, zyx),
                                                                           (yxz, yzx)]),
                'C4h': Matrix([[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0],
                               [0, 0, 0]]),
                'D4h': Matrix([[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0],
                               [0, 0, 0]])},
            'Cubic': {'O': Matrix([[0, 0, 0], [0, 0, xzy], [0, xyz, 0], [0, 0, yzx], [0, 0, 0], [yxz, 0, 0],
                                   [0, zyx, 0], [zxy, 0, 0], [0, 0, 0]]).subs([(xzy, -xyz), (yzx, xyz), (yxz, -xyz),
                                                                               (zxy, xyz), (zyx, -xyz)]),
                      'Td': Matrix([[0, 0, 0], [0, 0, xzy], [0, xyz, 0], [0, 0, yzx], [0, 0, 0], [yxz, 0, 0],
                                    [0, zyx, 0], [zxy, 0, 0], [0, 0, 0]]).subs([(xzy, xyz), (yzx, xyz), (yxz, xyz),
                                                                                (zxy, xyz), (zyx, xyz)]),
                      'T': Matrix([[0, 0, 0], [0, 0, xzy], [0, xyz, 0], [0, 0, yzx], [0, 0, 0], [yxz, 0, 0],
                                   [0, zyx, 0], [zxy, 0, 0], [0, 0, 0]]).subs([(yzx, xyz), (zxy, xyz), (yxz, xzy),
                                                                               (zyx, xzy), (xyz, xzy)]),
                      'Th': Matrix(
                          [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0],
                           [0, 0, 0]]),
                      'Oh': Matrix(
                          [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0],
                           [0, 0, 0]])},
            'Trigonal': {'C3': Matrix([[xxx, xyx, xzx], [xxy, xyy, xzy], [xxz, xyz, 0], [yxx, 0, yzx], [yxy, yyy, yzy],
                                       [yxz, yyz, 0], [zxx, zyx, 0], [zxy, zyy, 0], [0, 0, zzz]]).subs(
                [(xyy, -xxx), (yyz, -xxx),
                 (yxy, -xxx), (xyz, -yxz),
                 (xzy, -yzx), (xzx, yzy),
                 (xxz, yyz), (yxx, -yyy),
                 (xxy, -yyy), (xyx, -yyy),
                 (zxx, zyy), (zxy, -zyx),
                 (yyz, yzy), (yxz, yzx)]),
                'D3': Matrix([[xxx, 0, 0], [0, xyy, xzy], [0, xyz, 0], [0, yyx, yzx], [yxy, 0, 0], [yxz, 0, 0],
                              [0, zyx, 0], [zxy, 0, 0], [0, 0, 0]]).subs(
                    [(xyy, -xxx), (yyx, -xxx), (yxy, -xxx),
                     (xyz, -yxz), (xzy, -yzx), (zxy, -zyx),
                     (yxz, yzx)]),
                'C3v': Matrix(
                    [[0, xyx, xzx], [xxy, 0, 0], [xxz, 0, 0], [yxx, 0, 0], [0, yyy, yzy], [0, yyz, 0],
                     [zxx, 0, 0],
                     [0, zyy, 0], [0, 0, zzz]]).subs(
                    [(xzx, yzy), (xxz, yyz), (zxx, zyy), (yyz, yzy), (yxx, -yyy),
                     (xxy, -yyy), (xyx, -yyy)]),
                'S6': Matrix(
                    [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0],
                     [0, 0, 0]]),
                'D3d': Matrix(
                    [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0],
                     [0, 0, 0]])},
            'Hexagonal': {
                'C6': Matrix([[0, 0, xzx], [0, 0, xzy], [xxz, xyz, 0], [0, 0, yzx], [0, 0, yzy], [yxz, yyz, 0],
                              [zxx, zyx, 0], [zxy, zyy, 0], [0, 0, zzz]]).subs([(xyz, -yxz), (xzy, -yzx), (xzx, yzy),
                                                                                (xxz, yyz), (zxx, zyy), (zxy, -zyx),
                                                                                (yyz, yzy), (yxz, yzx)]),
                'C3h': Matrix([[xxx, xyx, 0], [xxy, xyy, 0], [0, 0, 0], [yxx, yyx, 0], [yxy, yyy, 0], [0, 0, 0],
                               [0, 0, 0], [0, 0, 0], [0, 0, 0]]).subs([(xyy, -xxx), (yxy, -xxx), (yyx, -xxx),
                                                                       (yxx, -yyy), (xyx, -yyy), (xxy, -yyy)]),
                'D6': Matrix([[0, 0, 0], [0, 0, xzy], [0, xyz, 0], [0, 0, 0], [0, 0, 0], [yxz, 0, 0],
                              [0, zyx, 0], [zxy, 0, 0], [0, 0, 0]]).subs([(xyz, -yxz), (xzy, -yxz), (zxy, -zyx)]),
                'C6v': Matrix([[0, 0, xzx], [0, 0, 0], [xxz, 0, 0], [0, 0, 0], [0, 0, yzy], [0, yyz, 0],
                               [zxx, 0, 0], [0, zyy, 0], [0, 0, zzz]]).subs([(xzx, yzy), (xxz, yyz), (zxx, zyy),
                                                                             (yyz, yzy)]),
                'D3h': Matrix(
                    [[0, xyx, 0], [xxy, 0, 0], [0, 0, 0], [yxx, 0, 0], [0, yyy, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0],
                     [0, 0, 0]]).subs([(yxx, -yyy), (xxy, -yyy), (xyx, -yyy)]),
                'C6h': Matrix([[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0],
                               [0, 0, 0]]),
                'D6h': Matrix([[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0],
                               [0, 0, 0]])}
        }

        self.dic_qud = {'Isotropic': {'Iso': Matrix([[xxxx, 0, 0, 0, xyxy, 0, 0, 0, xzxz],
                                                     [0, xxyy, 0, xyyx, 0, 0, 0, 0, 0],
                                                     [0, 0, xxzz, 0, 0, 0, xzzx, 0, 0],
                                                     [0, yxxy, 0, yyxx, 0, 0, 0, 0, 0],
                                                     [yxyx, 0, 0, 0, yyyy, 0, 0, 0, yzyz],
                                                     [0, 0, 0, 0, 0, yyzz, 0, yzzy, 0],
                                                     [0, 0, zxxz, 0, 0, 0, zzxx, 0, 0],
                                                     [0, 0, 0, 0, 0, zyyz, 0, zzyy, 0],
                                                     [zxzx, 0, 0, 0, zyzy, 0, 0, 0, zzzz]]).subs(
            [(zzyy, yyzz),
             (zzxx, yyzz),
             (xxzz, yyzz),
             (xxyy, yyzz),
             (yyxx, yyzz),
             (zyzy, yzyz),
             (zxzx, yzyz),
             (xzxz, yzyz),
             (xyxy, yzyz),
             (yxyx, yzyz),
             (zyyz, zyyz),
             (zxxz, zyyz),
             (xzzx, zyyz),
             (xyyx, zyyz),
             (yxxy, zyyz),
             (xxxx, xxyy + xyxy + xyyx),
             (yyyy, xxyy + xyxy + xyyx),
             (zzzz, xxyy + xyxy + xyyx),
             (yyzz, yzzy)])},
            'Cubic': {'Th – m3': Matrix([[xxxx, 0, 0, 0, xyxy, 0, 0, 0, xzxz],
                                         [0, xxyy, 0, xyyx, 0, 0, 0, 0, 0],
                                         [0, 0, xxzz, 0, 0, 0, xzzx, 0, 0],
                                         [0, yxxy, 0, yyxx, 0, 0, 0, 0, 0],
                                         [yxyx, 0, 0, 0, yyyy, 0, 0, 0, yzyz],
                                         [0, 0, 0, 0, 0, yyzz, 0, yzzy, 0],
                                         [0, 0, zxxz, 0, 0, 0, zzxx, 0, 0],
                                         [0, 0, 0, 0, 0, zyyz, 0, zzyy, 0],
                                         [zxzx, 0, 0, 0, zyzy, 0, 0, 0, zzzz]]).subs([(zzzz, xxxx),
                                                                                      (yyyy, xxxx),
                                                                                      (xxyy, yyzz),
                                                                                      (zzxx, yyzz),
                                                                                      (yyxx, zzyy),
                                                                                      (xxzz, zzyy),
                                                                                      (xyxy, yzyz),
                                                                                      (zxzx, yzyz),
                                                                                      (yxyx, zyzy),
                                                                                      (xzxz, zyzy),
                                                                                      (xyyx, yzzy),
                                                                                      (zxxz, yzzy),
                                                                                      (yxxy, zyyz),
                                                                                      (xzzx, zyyz),
                                                                                      (yyzz, yzzy),
                                                                                      (zyyz, zzyy)]),
                      'T – 23': Matrix([[xxxx, 0, 0, 0, xyxy, 0, 0, 0, xzxz],
                                        [0, xxyy, 0, xyyx, 0, 0, 0, 0, 0],
                                        [0, 0, xxzz, 0, 0, 0, xzzx, 0, 0],
                                        [0, yxxy, 0, yyxx, 0, 0, 0, 0, 0],
                                        [yxyx, 0, 0, 0, yyyy, 0, 0, 0, yzyz],
                                        [0, 0, 0, 0, 0, yyzz, 0, yzzy, 0],
                                        [0, 0, zxxz, 0, 0, 0, zzxx, 0, 0],
                                        [0, 0, 0, 0, 0, zyyz, 0, zzyy, 0],
                                        [zxzx, 0, 0, 0, zyzy, 0, 0, 0, zzzz]]).subs([(zzzz, xxxx),
                                                                                     (yyyy, xxxx),
                                                                                     (xxyy, yyzz),
                                                                                     (zzxx, yyzz),
                                                                                     (yyxx, zzyy),
                                                                                     (xxzz, zzyy),
                                                                                     (xyxy, yzyz),
                                                                                     (zxzx, yzyz),
                                                                                     (yxyx, zyzy),
                                                                                     (xzxz, zyzy),
                                                                                     (xyyx, yzzy),
                                                                                     (zxxz, yzzy),
                                                                                     (yxxy, zyyz),
                                                                                     (xzzx, zyyz),
                                                                                     (yyzz, yzzy),
                                                                                     (zyyz, zzyy)]),
                      'O - 432': Matrix([[xxxx, 0, 0, 0, xyxy, 0, 0, 0, xzxz],
                                         [0, xxyy, 0, xyyx, 0, 0, 0, 0, 0],
                                         [0, 0, xxzz, 0, 0, 0, xzzx, 0, 0],
                                         [0, yxxy, 0, yyxx, 0, 0, 0, 0, 0],
                                         [yxyx, 0, 0, 0, yyyy, 0, 0, 0, yzyz],
                                         [0, 0, 0, 0, 0, yyzz, 0, yzzy, 0],
                                         [0, 0, zxxz, 0, 0, 0, zzxx, 0, 0],
                                         [0, 0, 0, 0, 0, zyyz, 0, zzyy, 0],
                                         [zxzx, 0, 0, 0, zyzy, 0, 0, 0, zzzz]]).subs([(zzzz, xxxx),
                                                                                      (yyyy, xxxx),
                                                                                      (zzyy, yyzz),
                                                                                      (zzxx, yyzz),
                                                                                      (xxzz, yyzz),
                                                                                      (xxyy, yyzz),
                                                                                      (yyxx, yyzz),
                                                                                      (zyzy, yzyz),
                                                                                      (zxzx, yzyz),
                                                                                      (xzxz, yzyz),
                                                                                      (xyxy, yzyz),
                                                                                      (yxyx, yzyz),
                                                                                      (zyyz, yzzy),
                                                                                      (zxxz, yzzy),
                                                                                      (xzzx, yzzy),
                                                                                      (xyyx, yzzy),
                                                                                      (yxxy, yzzy),
                                                                                      (yyzz, yzzy)]),
                      'Td – 4(Bar)3m': Matrix([[xxxx, 0, 0, 0, xyxy, 0, 0, 0, xzxz],
                                               [0, xxyy, 0, xyyx, 0, 0, 0, 0, 0],
                                               [0, 0, xxzz, 0, 0, 0, xzzx, 0, 0],
                                               [0, yxxy, 0, yyxx, 0, 0, 0, 0, 0],
                                               [yxyx, 0, 0, 0, yyyy, 0, 0, 0, yzyz],
                                               [0, 0, 0, 0, 0, yyzz, 0, yzzy, 0],
                                               [0, 0, zxxz, 0, 0, 0, zzxx, 0, 0],
                                               [0, 0, 0, 0, 0, zyyz, 0, zzyy, 0],
                                               [zxzx, 0, 0, 0, zyzy, 0, 0, 0, zzzz]]).subs([(zzzz, xxxx),
                                                                                            (yyyy, xxxx),
                                                                                            (zzyy, yyzz),
                                                                                            (zzxx, yyzz),
                                                                                            (xxzz, yyzz),
                                                                                            (xxyy, yyzz),
                                                                                            (yyxx, yyzz),
                                                                                            (zyzy, yzyz),
                                                                                            (zxzx, yzyz),
                                                                                            (xzxz, yzyz),
                                                                                            (xyxy, yzyz),
                                                                                            (yxyx, yzyz),
                                                                                            (zyyz, yzzy),
                                                                                            (zxxz, yzzy),
                                                                                            (xzzx, yzzy),
                                                                                            (xyyx, yzzy),
                                                                                            (yxxy, yzzy),
                                                                                            (yyzz, yzzy)]),
                      'Oh – m3m': Matrix([[xxxx, 0, 0, 0, xyxy, 0, 0, 0, xzxz],
                                          [0, xxyy, 0, xyyx, 0, 0, 0, 0, 0],
                                          [0, 0, xxzz, 0, 0, 0, xzzx, 0, 0],
                                          [0, yxxy, 0, yyxx, 0, 0, 0, 0, 0],
                                          [yxyx, 0, 0, 0, yyyy, 0, 0, 0, yzyz],
                                          [0, 0, 0, 0, 0, yyzz, 0, yzzy, 0],
                                          [0, 0, zxxz, 0, 0, 0, zzxx, 0, 0],
                                          [0, 0, 0, 0, 0, zyyz, 0, zzyy, 0],
                                          [zxzx, 0, 0, 0, zyzy, 0, 0, 0, zzzz]]).subs([(zzzz, xxxx),
                                                                                       (yyyy, xxxx),
                                                                                       (zzyy, yyzz),
                                                                                       (zzxx, yyzz),
                                                                                       (xxzz, yyzz),
                                                                                       (xxyy, yyzz),
                                                                                       (yyxx, yyzz),
                                                                                       (zyzy, yzyz),
                                                                                       (zxzx, yzyz),
                                                                                       (xzxz, yzyz),
                                                                                       (xyxy, yzyz),
                                                                                       (yxyx, yzyz),
                                                                                       (zyyz, yzzy),
                                                                                       (zxxz, yzzy),
                                                                                       (xzzx, yzzy),
                                                                                       (xyyx, yzzy),
                                                                                       (yxxy, yzzy),
                                                                                       (yyzz, yzzy)]),

                      },
            'Hexagonal': {'C6 – 6': Matrix([[xxxx, xxxy, 0, xyxx, xyxy, 0, 0, 0, xzxz],
                                            [xxyx, xxyy, 0, xyyx, xyyy, 0, 0, 0, xzyz],
                                            [0, 0, xxzz, 0, 0, xyzz, xzzx, xzzy, 0],
                                            [yxxx, yxxy, 0, yyxx, yyxy, 0, 0, 0, yzxz],
                                            [yxyx, yxyy, 0, yyyx, yyyy, 0, 0, 0, yzyz],
                                            [0, 0, yxzz, 0, 0, yyzz, yzzx, yzzy, 0],
                                            [0, 0, zxxz, 0, 0, zyxz, zzxx, zzxy, 0],
                                            [0, 0, zxyz, 0, 0, zyyz, zzyx, zzyy, 0],
                                            [zxzx, zxzy, 0, zyzx, zyzy, 0, 0, 0, zzzz]]).subs(
                [(xxyy, yyxx),
                 (xyyx, yxxy),
                 (xyxy, yxyx),
                 (yyzz, xxzz),
                 (zzyy, zzxx),
                 (zyyz, zxxz),
                 (yzzy, xzzx),
                 (yzyz, xzxz),
                 (zyzy, zxzx),
                 (xyzz, -yxzz),
                 (zzxy, -zzyx),
                 (zxyz, -zyxz),
                 (xzzy, -yzzx),
                 (xzyz, -yzxz),
                 (zxzy, -zyzx),
                 (yyxy, -xxyx),
                 (yxyy, -xyxx),
                 (xyyy, -yxxx),
                 (xxxy, yyxy + yxyy + xyyy),
                 (yyyx, -yyxy - yxyy - xyyy),
                 (xxxx, xxyy + xyyx + xyxy),
                 (yyyy, xxyy + xyyx + xyxy),
                 (yyxx, yxxy),
                 (xxzz, xzzx),
                 (zzxx, zxxz),
                 (yxzz, yzzx)
                 ]),
                'C3h – 6(Bar)': Matrix([[xxxx, xxxy, 0, xyxx, xyxy, 0, 0, 0, xzxz],
                                        [xxyx, xxyy, 0, xyyx, xyyy, 0, 0, 0, xzyz],
                                        [0, 0, xxzz, 0, 0, xyzz, xzzx, xzzy, 0],
                                        [yxxx, yxxy, 0, yyxx, yyxy, 0, 0, 0, yzxz],
                                        [yxyx, yxyy, 0, yyyx, yyyy, 0, 0, 0, yzyz],
                                        [0, 0, yxzz, 0, 0, yyzz, yzzx, yzzy, 0],
                                        [0, 0, zxxz, 0, 0, zyxz, zzxx, zzxy, 0],
                                        [0, 0, zxyz, 0, 0, zyyz, zzyx, zzyy, 0],
                                        [zxzx, zxzy, 0, zyzx, zyzy, 0, 0, 0, zzzz]]).subs(
                    [(xxyy, yyxx),
                     (xyyx, yxxy),
                     (xyxy, yxyx),
                     (yyzz, xxzz),
                     (zzyy, zzxx),
                     (zyyz, zxxz),
                     (yzzy, xzzx),
                     (yzyz, xzxz),
                     (zyzy, zxzx),
                     (xyzz, -yxzz),
                     (zzxy, -zzyx),
                     (zxyz, -zyxz),
                     (xzzy, -yzzx),
                     (xzyz, -yzxz),
                     (zxzy, -zyzx),
                     (yyxy, -xxyx),
                     (yxyy, -xyxx),
                     (xyyy, -yxxx),
                     (xxxy, yyxy + yxyy + xyyy),
                     (yyyx, -yyxy - yxyy - xyyy),
                     (xxxx, xxyy + xyyx + xyxy),
                     (yyyy, xxyy + xyyx + xyxy),
                     (yyxx, yxxy),
                     (xxzz, xzzx),
                     (zzxx, zxxz),
                     (yxzz, yzzx)
                     ]),
                'C6h – 6|m': Matrix([[xxxx, xxxy, 0, xyxx, xyxy, 0, 0, 0, xzxz],
                                     [xxyx, xxyy, 0, xyyx, xyyy, 0, 0, 0, xzyz],
                                     [0, 0, xxzz, 0, 0, xyzz, xzzx, xzzy, 0],
                                     [yxxx, yxxy, 0, yyxx, yyxy, 0, 0, 0, yzxz],
                                     [yxyx, yxyy, 0, yyyx, yyyy, 0, 0, 0, yzyz],
                                     [0, 0, yxzz, 0, 0, yyzz, yzzx, yzzy, 0],
                                     [0, 0, zxxz, 0, 0, zyxz, zzxx, zzxy, 0],
                                     [0, 0, zxyz, 0, 0, zyyz, zzyx, zzyy, 0],
                                     [zxzx, zxzy, 0, zyzx, zyzy, 0, 0, 0, zzzz]]).subs(
                    [(xxyy, yyxx),
                     (xyyx, yxxy),
                     (xyxy, yxyx),
                     (yyzz, xxzz),
                     (zzyy, zzxx),
                     (zyyz, zxxz),
                     (yzzy, xzzx),
                     (yzyz, xzxz),
                     (zyzy, zxzx),
                     (xyzz, -yxzz),
                     (zzxy, -zzyx),
                     (zxyz, -zyxz),
                     (xzzy, -yzzx),
                     (xzyz, -yzxz),
                     (zxzy, -zyzx),
                     (yyxy, -xxyx),
                     (yxyy, -xyxx),
                     (xyyy, -yxxx),
                     (xxxy, yyxy + yxyy + xyyy),
                     (yyyx, -yyxy - yxyy - xyyy),
                     (xxxx, xxyy + xyyx + xyxy),
                     (yyyy, xxyy + xyyx + xyxy),
                     (yyxx, yxxy),
                     (xxzz, xzzx),
                     (zzxx, zxxz),
                     (yxzz, yzzx)
                     ]),
                'D6 – 622': Matrix([[xxxx, 0, 0, 0, xyxy, 0, 0, 0, xzxz],
                                    [0, xxyy, 0, xyyx, 0, 0, 0, 0, 0],
                                    [0, 0, xxzz, 0, 0, 0, xzzx, 0, 0],
                                    [0, yxxy, 0, yyxx, 0, 0, 0, 0, 0],
                                    [yxyx, 0, 0, 0, yyyy, 0, 0, 0, yzyz],
                                    [0, 0, 0, 0, 0, yyzz, 0, yzzy, 0],
                                    [0, 0, zxxz, 0, 0, 0, zzxx, 0, 0],
                                    [0, 0, 0, 0, 0, zyyz, 0, zzyy, 0],
                                    [zxzx, 0, 0, 0, zyzy, 0, 0, 0, zzzz]]).subs(
                    [(xxyy, yyxx),
                     (xyyx, yxxy),
                     (xyxy, yxyx),
                     (yyzz, xxzz),
                     (zzyy, zzxx),
                     (zyyz, zxxz),
                     (yzzy, xzzx),
                     (yzyz, xzxz),
                     (zyzy, zxzx),
                     (xxxx, xxyy + xyyx + xyxy),
                     (yyyy, xxyy + xyyx + xyxy),
                     (yyxx, yxxy),
                     (xxzz, xzzx),
                     (zzxx, zxxz)
                     ]),
                'C6v – 6mm': Matrix([[xxxx, 0, 0, 0, xyxy, 0, 0, 0, xzxz],
                                     [0, xxyy, 0, xyyx, 0, 0, 0, 0, 0],
                                     [0, 0, xxzz, 0, 0, 0, xzzx, 0, 0],
                                     [0, yxxy, 0, yyxx, 0, 0, 0, 0, 0],
                                     [yxyx, 0, 0, 0, yyyy, 0, 0, 0, yzyz],
                                     [0, 0, 0, 0, 0, yyzz, 0, yzzy, 0],
                                     [0, 0, zxxz, 0, 0, 0, zzxx, 0, 0],
                                     [0, 0, 0, 0, 0, zyyz, 0, zzyy, 0],
                                     [zxzx, 0, 0, 0, zyzy, 0, 0, 0, zzzz]]).subs(
                    [(xxyy, yyxx),
                     (xyyx, yxxy),
                     (xyxy, yxyx),
                     (yyzz, xxzz),
                     (zzyy, zzxx),
                     (zyyz, zxxz),
                     (yzzy, xzzx),
                     (yzyz, xzxz),
                     (zyzy, zxzx),
                     (xxxx, xxyy + xyyx + xyxy),
                     (yyyy, xxyy + xyyx + xyxy),
                     (yyxx, yxxy),
                     (xxzz, xzzx),
                     (zzxx, zxxz)
                     ]),
                'D6h – 6|mmm': Matrix([[xxxx, 0, 0, 0, xyxy, 0, 0, 0, xzxz],
                                       [0, xxyy, 0, xyyx, 0, 0, 0, 0, 0],
                                       [0, 0, xxzz, 0, 0, 0, xzzx, 0, 0],
                                       [0, yxxy, 0, yyxx, 0, 0, 0, 0, 0],
                                       [yxyx, 0, 0, 0, yyyy, 0, 0, 0, yzyz],
                                       [0, 0, 0, 0, 0, yyzz, 0, yzzy, 0],
                                       [0, 0, zxxz, 0, 0, 0, zzxx, 0, 0],
                                       [0, 0, 0, 0, 0, zyyz, 0, zzyy, 0],
                                       [zxzx, 0, 0, 0, zyzy, 0, 0, 0, zzzz]]).subs(
                    [(xxyy, yyxx),
                     (xyyx, yxxy),
                     (xyxy, yxyx),
                     (yyzz, xxzz),
                     (zzyy, zzxx),
                     (zyyz, zxxz),
                     (yzzy, xzzx),
                     (yzyz, xzxz),
                     (zyzy, zxzx),
                     (xxxx, xxyy + xyyx + xyxy),
                     (yyyy, xxyy + xyyx + xyxy),
                     (yyxx, yxxy),
                     (xxzz, xzzx),
                     (zzxx, zxxz)
                     ]),
                'D3h – 6(Bar)m2': Matrix([[xxxx, 0, 0, 0, xyxy, 0, 0, 0, xzxz],
                                          [0, xxyy, 0, xyyx, 0, 0, 0, 0, 0],
                                          [0, 0, xxzz, 0, 0, 0, xzzx, 0, 0],
                                          [0, yxxy, 0, yyxx, 0, 0, 0, 0, 0],
                                          [yxyx, 0, 0, 0, yyyy, 0, 0, 0, yzyz],
                                          [0, 0, 0, 0, 0, yyzz, 0, yzzy, 0],
                                          [0, 0, zxxz, 0, 0, 0, zzxx, 0, 0],
                                          [0, 0, 0, 0, 0, zyyz, 0, zzyy, 0],
                                          [zxzx, 0, 0, 0, zyzy, 0, 0, 0, zzzz]]).subs(
                    [(xxyy, yyxx),
                     (xyyx, yxxy),
                     (xyxy, yxyx),
                     (yyzz, xxzz),
                     (zzyy, zzxx),
                     (zyyz, zxxz),
                     (yzzy, xzzx),
                     (yzyz, xzxz),
                     (zyzy, zxzx),
                     (xxxx, xxyy + xyyx + xyxy),
                     (yyyy, xxyy + xyyx + xyxy),
                     (yyxx, yxxy),
                     (xxzz, xzzx),
                     (zzxx, zxxz)
                     ])

            },

            'Trigonal': {'C3 – 3': Matrix([[xxxx, xxxy, xxxz, xyxx, xyxy, xyxz, xzxx, xzxy, xzxz],
                                           [xxyx, xxyy, xxyz, xyyx, xyyy, xyyz, xzyx, xzyy, xzyz],
                                           [xxzx, xxzy, xxzz, xyzx, xyzy, xyzz, xzzx, xzzy, 0],
                                           [yxxx, yxxy, yxxz, yyxx, yyxy, yyxz, yzxx, yzxy, yzxz],
                                           [yxyx, yxyy, yxyz, yyyx, yyyy, yyyz, yzyx, yzyy, yzyz],
                                           [yxzx, yxzy, yxzz, yyzx, yyzy, yyzz, yzzx, yzzy, 0],
                                           [zxxx, zxxy, zxxz, zyxx, zyxy, zyxz, zzxx, zzxy, 0],
                                           [zxyx, zxyy, zxyz, zyyx, zyyy, zyyz, zzyx, zzyy, 0],
                                           [zxzx, zxzy, 0, zyzx, zyzy, 0, 0, 0, zzzz]]).subs(
                [(xxyy, yyxx),
                 (xyyx, yxxy),
                 (xyxy, yxyx),
                 (yyzz, xxzz),
                 (zzyy, zzxx),
                 (zyyz, zxxz),
                 (yzzy, xzzx),
                 (yzyz, xzxz),
                 (zyzy, zxzx),
                 (xyzz, -yxzz),
                 (zzxy, -zzyx),
                 (zxyz, -zyxz),
                 (xzzy, -yzzx),
                 (xzyz, -yzxz),
                 (zxzy, -zyzx),
                 (yyxy, -xxyx),
                 (yxyy, -xyxx),
                 (xyyy, -yxxx),
                 (xxyz, -yyyz),
                 (xyxz, -yyyz),
                 (yxxz, -yyyz),
                 (xxzy, -yyzy),
                 (xyzx, -yyzy),
                 (yxzx, -yyzy),
                 (xzxy, -yzyy),
                 (xzyx, -yzyy),
                 (yzxx, -yzyy),
                 (zxxy, -zyyy),
                 (zxyx, -zyyy),
                 (zyxx, -zyyy),
                 (yyxz, -xxxz),
                 (yxyz, -xxxz),
                 (xyyz, -xxxz),
                 (yyzx, -xxzx),
                 (yxzy, -xxzx),
                 (xyzy, -xxzx),
                 (xzyy, -xzxx),
                 (yzyx, -xzxx),
                 (yzxy, -xzxx),
                 (zyyx, -zxxx),
                 (zyxy, -zxxx),
                 (zxyy, -zxxx),
                 (xxxx, xxyy + xyyx + xyxy),
                 (yyyy, xxyy + xyyx + xyxy),
                 (xxxy, yyxy + yxyy + xyyy),
                 (yyyx, -(yyxy + yxyy + xyyy)),
                 (yyxx, yxxy),
                 (xxzz, xzzx),
                 (zzxx, zxxz),
                 (yxzz, yzzx),
                 (yyyz, yzyy),
                 (xxxz, xxzx)
                 ]),

                'S6 – 3(Bar)': Matrix([[xxxx, xxxy, xxxz, xyxx, xyxy, xyxz, xzxx, xzxy, xzxz],
                                       [xxyx, xxyy, xxyz, xyyx, xyyy, xyyz, xzyx, xzyy, xzyz],
                                       [xxzx, xxzy, xxzz, xyzx, xyzy, xyzz, xzzx, xzzy, 0],
                                       [yxxx, yxxy, yxxz, yyxx, yyxy, yyxz, yzxx, yzxy, yzxz],
                                       [yxyx, yxyy, yxyz, yyyx, yyyy, yyyz, yzyx, yzyy, yzyz],
                                       [yxzx, yxzy, yxzz, yyzx, yyzy, yyzz, yzzx, yzzy, 0],
                                       [zxxx, zxxy, zxxz, zyxx, zyxy, zyxz, zzxx, zzxy, 0],
                                       [zxyx, zxyy, zxyz, zyyx, zyyy, zyyz, zzyx, zzyy, 0],
                                       [zxzx, zxzy, 0, zyzx, zyzy, 0, 0, 0, zzzz]]).subs(
                    [(xxyy, yyxx),
                     (xyyx, yxxy),
                     (xyxy, yxyx),
                     (yyzz, xxzz),
                     (zzyy, zzxx),
                     (zyyz, zxxz),
                     (yzzy, xzzx),
                     (yzyz, xzxz),
                     (zyzy, zxzx),
                     (xyzz, -yxzz),
                     (zzxy, -zzyx),
                     (zxyz, -zyxz),
                     (xzzy, -yzzx),
                     (xzyz, -yzxz),
                     (zxzy, -zyzx),
                     (yyxy, -xxyx),
                     (yxyy, -xyxx),
                     (xyyy, -yxxx),
                     (xxyz, -yyyz),
                     (xyxz, -yyyz),
                     (yxxz, -yyyz),
                     (xxzy, -yyzy),
                     (xyzx, -yyzy),
                     (yxzx, -yyzy),
                     (xzxy, -yzyy),
                     (xzyx, -yzyy),
                     (yzxx, -yzyy),
                     (zxxy, -zyyy),
                     (zxyx, -zyyy),
                     (zyxx, -zyyy),
                     (yyxz, -xxxz),
                     (yxyz, -xxxz),
                     (xyyz, -xxxz),
                     (yyzx, -xxzx),
                     (yxzy, -xxzx),
                     (xyzy, -xxzx),
                     (xzyy, -xzxx),
                     (yzyx, -xzxx),
                     (yzxy, -xzxx),
                     (zyyx, -zxxx),
                     (zyxy, -zxxx),
                     (zxyy, -zxxx),
                     (xxxx, xxyy + xyyx + xyxy),
                     (yyyy, xxyy + xyyx + xyxy),
                     (xxxy, yyxy + yxyy + xyyy),
                     (yyyx, -(yyxy + yxyy + xyyy)),
                     (yyxx, yxxy),
                     (xxzz, xzzx),
                     (zzxx, zxxz),
                     (yxzz, yzzx),
                     (yyyz, yzyy),
                     (xxxz, xxzx)
                     ]),

                'C3v – 3m': Matrix([[xxxx, 0, xxxz, 0, xyxy, 0, xzxx, 0, xzxz],
                                    [0, xxyy, 0, xyyx, 0, xyyz, 0, xzyy, 0],
                                    [xxzx, 0, xxzz, 0, xyzy, 0, xzzx, 0, 0],
                                    [0, yxxy, 0, yyxx, 0, yyxz, 0, yzxy, 0],
                                    [yxyx, 0, yxyz, 0, yyyy, 0, yzyx, 0, yzyz],
                                    [0, yxzy, 0, yyzx, 0, yyzz, 0, yzzy, 0],
                                    [zxxx, 0, zxxz, 0, zyxy, 0, zzxx, 0, 0],
                                    [0, zxyy, 0, zyyx, 0, zyyz, 0, zzyy, 0],
                                    [zxzx, 0, 0, 0, zyzy, 0, 0, 0, zzzz]]).subs(
                    [(xxyy, yyxx),
                     (xyyx, yxxy),
                     (xyxy, yxyx),
                     (yyzz, xxzz),
                     (zzyy, zzxx),
                     (zyyz, zxxz),
                     (yzzy, xzzx),
                     (yyxz, -xxxz),
                     (yxyz, -xxxz),
                     (xyyz, -xxxz),
                     (yyzx, -xxzx),
                     (yxzy, -xxzx),
                     (xyzy, -xxzx),
                     (yzyx, -xzxx),
                     (yzxy, -xzxx),
                     (xzyy, -xzxx),
                     (zyyx, -zxxx),
                     (zyxy, -zxxx),
                     (zxyy, -zxxx),
                     (yzyz, xzxz),
                     (zyzy, zxzx),
                     (xxxx, xxyy + xyyx + xyxy),
                     (yyyy, xxyy + xyyx + xyxy),
                     (yyxx, yxxy),
                     (xxzz, xzzx),
                     (zzxx, zxxz),
                     (xxxz, xzxx)
                     ]),

                'D3d – 3(Bar)m': Matrix([[xxxx, 0, xxxz, 0, xyxy, 0, xzxx, 0, xzxz],
                                         [0, xxyy, 0, xyyx, 0, xyyz, 0, xzyy, 0],
                                         [xxzx, 0, xxzz, 0, xyzy, 0, xzzx, 0, 0],
                                         [0, yxxy, 0, yyxx, 0, yyxz, 0, yzxy, 0],
                                         [yxyx, 0, yxyz, 0, yyyy, 0, yzyx, 0, yzyz],
                                         [0, yxzy, 0, yyzx, 0, yyzz, 0, yzzy, 0],
                                         [zxxx, 0, zxxz, 0, zyxy, 0, zzxx, 0, 0],
                                         [0, zxyy, 0, zyyx, 0, zyyz, 0, zzyy, 0],
                                         [zxzx, 0, 0, 0, zyzy, 0, 0, 0, zzzz]]).subs(
                    [(xxyy, yyxx),
                     (xyyx, yxxy),
                     (xyxy, yxyx),
                     (yyzz, xxzz),
                     (zzyy, zzxx),
                     (zyyz, zxxz),
                     (yzzy, xzzx),
                     (yyxz, -xxxz),
                     (yxyz, -xxxz),
                     (xyyz, -xxxz),
                     (yyzx, -xxzx),
                     (yxzy, -xxzx),
                     (xyzy, -xxzx),
                     (yzyx, -xzxx),
                     (yzxy, -xzxx),
                     (xzyy, -xzxx),
                     (zyyx, -zxxx),
                     (zyxy, -zxxx),
                     (zxyy, -zxxx),
                     (yzyz, xzxz),
                     (zyzy, zxzx),
                     (xxxx, xxyy + xyyx + xyxy),
                     (yyyy, xxyy + xyyx + xyxy),
                     (yyxx, yxxy),
                     (xxzz, xzzx),
                     (zzxx, zxxz),
                     (xxxz, xzxx)
                     ]),

                'D3 – 32': Matrix([[xxxx, 0, xxxz, 0, xyxy, 0, xzxx, 0, xzxz],
                                   [0, xxyy, 0, xyyx, 0, xyyz, 0, xzyy, 0],
                                   [xxzx, 0, xxzz, 0, xyzy, 0, xzzx, 0, 0],
                                   [0, yxxy, 0, yyxx, 0, yyxz, 0, yzxy, 0],
                                   [yxyx, 0, yxyz, 0, yyyy, 0, yzyx, 0, yzyz],
                                   [0, yxzy, 0, yyzx, 0, yyzz, 0, yzzy, 0],
                                   [zxxx, 0, zxxz, 0, zyxy, 0, zzxx, 0, 0],
                                   [0, zxyy, 0, zyyx, 0, zyyz, 0, zzyy, 0],
                                   [zxzx, 0, 0, 0, zyzy, 0, 0, 0, zzzz]]).subs(
                    [(xxyy, yyxx),
                     (xyyx, yxxy),
                     (xyxy, yxyx),
                     (yyzz, xxzz),
                     (zzyy, zzxx),
                     (zyyz, zxxz),
                     (yzzy, xzzx),
                     (yyxz, -xxxz),
                     (yxyz, -xxxz),
                     (xyyz, -xxxz),
                     (yyzx, -xxzx),
                     (yxzy, -xxzx),
                     (xyzy, -xxzx),
                     (yzyx, -xzxx),
                     (yzxy, -xzxx),
                     (xzyy, -xzxx),
                     (zyyx, -zxxx),
                     (zyxy, -zxxx),
                     (zxyy, -zxxx),
                     (yzyz, xzxz),
                     (zyzy, zxzx),
                     (xxxx, xxyy + xyyx + xyxy),
                     (yyyy, xxyy + xyyx + xyxy),
                     (yyxx, yxxy),
                     (xxzz, xzzx),
                     (zzxx, zxxz),
                     (xxxz, xzxx)
                     ])
            },
            'Tetragonal': {
                'C4 – 4': Matrix([[xxxx, xxxy, 0, xyxx, xyxy, 0, 0, 0, xzxz],
                                  [yxxx, yxxy, 0, yyxx, yyxy, 0, 0, 0, yzxz],
                                  [0, 0, xxzz, 0, 0, xyzz, xzzx, xzzy, 0],
                                  [yxxx, yxxy, 0, yyxx, yyxy, 0, 0, 0, yzxz],
                                  [yxyx, yxyy, 0, yyyx, yyyy, 0, 0, 0, yzyz],
                                  [0, 0, yxzz, 0, 0, 0, yzzx, yzzy, 0],
                                  [0, 0, zxxz, 0, 0, zyxz, zzxx, zzxy, 0],
                                  [0, 0, zxyz, 0, 0, zyyz, zzyx, zzyy, 0],
                                  [zxzx, zxzy, 0, zyzx, zyzy, 0, 0, 0, zzzz]]).subs(
                    [(xxxx, yyyy),
                     (zzxx, zzyy),
                     (xxzz, zzyy),
                     (zxzx, zyzy),
                     (xzxz, yzyz),
                     (zxxz, zyyz),
                     (xzzx, yzzy),
                     (xyzz, -yxzz),
                     (zzxy, -zzyx),
                     (xzyz, -yzxz),
                     (zxzy, -zyzx),
                     (zxyz, -zyxz),
                     (xzzy, -yzzx),
                     (xxyy, yyxx),
                     (xyxy, yxyx),
                     (xyyx, yxxy),
                     (xxxy, -yyyx),
                     (xxyx, -yyxy),
                     (xyxx, -yxyy),
                     (yxxx, -xyyy),
                     (zzyy, zyyz),
                     (yxzz, yzzx),
                     (yyxx, yxxy),
                     (yyyx, yxyy)]),
                'S4 – 4(Bar)': Matrix([[xxxx, xxxy, 0, xyxx, xyxy, 0, 0, 0, xzxz],
                                       [yxxx, yxxy, 0, yyxx, yyxy, 0, 0, 0, yzxz],
                                       [0, 0, xxzz, 0, 0, xyzz, xzzx, xzzy, 0],
                                       [yxxx, yxxy, 0, yyxx, yyxy, 0, 0, 0, yzxz],
                                       [yxyx, yxyy, 0, yyyx, yyyy, 0, 0, 0, yzyz],
                                       [0, 0, yxzz, 0, 0, 0, yzzx, yzzy, 0],
                                       [0, 0, zxxz, 0, 0, zyxz, zzxx, zzxy, 0],
                                       [0, 0, zxyz, 0, 0, zyyz, zzyx, zzyy, 0],
                                       [zxzx, zxzy, 0, zyzx, zyzy, 0, 0, 0, zzzz]]).subs([(xxxx, yyyy),
                                                                                          (zzxx, zzyy),
                                                                                          (xxzz, zzyy),
                                                                                          (zxzx, zyzy),
                                                                                          (xzxz, yzyz),
                                                                                          (zxxz, zyyz),
                                                                                          (xzzx, yzzy),
                                                                                          (xyzz, -yxzz),
                                                                                          (zzxy, -zzyx),
                                                                                          (xzyz, -yzxz),
                                                                                          (zxzy, -zyzx),
                                                                                          (zxyz, -zyxz),
                                                                                          (xzzy, -yzzx),
                                                                                          (xxyy, yyxx),
                                                                                          (xyxy, yxyx),
                                                                                          (xyyx, yxxy),
                                                                                          (xxxy, -yyyx),
                                                                                          (xxyx, -yyxy),
                                                                                          (xyxx, -yxyy),
                                                                                          (yxxx, -xyyy),
                                                                                          (zzyy, zyyz),
                                                                                          (yxzz, yzzx),
                                                                                          (yyxx, yxxy),
                                                                                          (yyyx, yxyy)]),
                'C4h – 4|m': Matrix([[xxxx, xxxy, 0, xyxx, xyxy, 0, 0, 0, xzxz],
                                     [yxxx, yxxy, 0, yyxx, yyxy, 0, 0, 0, yzxz],
                                     [0, 0, xxzz, 0, 0, xyzz, xzzx, xzzy, 0],
                                     [yxxx, yxxy, 0, yyxx, yyxy, 0, 0, 0, yzxz],
                                     [yxyx, yxyy, 0, yyyx, yyyy, 0, 0, 0, yzyz],
                                     [0, 0, yxzz, 0, 0, 0, yzzx, yzzy, 0],
                                     [0, 0, zxxz, 0, 0, zyxz, zzxx, zzxy, 0],
                                     [0, 0, zxyz, 0, 0, zyyz, zzyx, zzyy, 0],
                                     [zxzx, zxzy, 0, zyzx, zyzy, 0, 0, 0, zzzz]]).subs([(xxxx, yyyy),
                                                                                        (zzxx, zzyy),
                                                                                        (xxzz, zzyy),
                                                                                        (zxzx, zyzy),
                                                                                        (xzxz, yzyz),
                                                                                        (zxxz, zyyz),
                                                                                        (xzzx, yzzy),
                                                                                        (xyzz, -yxzz),
                                                                                        (zzxy, -zzyx),
                                                                                        (xzyz, -yzxz),
                                                                                        (zxzy, -zyzx),
                                                                                        (zxyz, -zyxz),
                                                                                        (xzzy, -yzzx),
                                                                                        (xxyy, yyxx),
                                                                                        (xyxy, yxyx),
                                                                                        (xyyx, yxxy),
                                                                                        (xxxy, -yyyx),
                                                                                        (xxyx, -yyxy),
                                                                                        (xyxx, -yxyy),
                                                                                        (yxxx, -xyyy),
                                                                                        (zzyy, zyyz),
                                                                                        (yxzz, yzzx),
                                                                                        (yyxx, yxxy),
                                                                                        (yyyx, yxyy)]),
                'D4 – 422': Matrix([[xxxx, 0, 0, 0, xyxy, 0, 0, 0, xzxz],
                                    [0, xxyy, 0, xyyx, 0, 0, 0, 0, 0],
                                    [0, 0, xxzz, 0, 0, 0, xzzx, 0, 0],
                                    [0, yxxy, 0, yyxx, 0, 0, 0, 0, 0],
                                    [yxyx, 0, 0, 0, yyyy, 0, 0, 0, yzyz],
                                    [0, 0, 0, 0, 0, yyzz, 0, yzzy, 0],
                                    [0, 0, zxxz, 0, 0, 0, zzxx, 0, 0],
                                    [0, 0, 0, 0, 0, zyyz, 0, zzyy, 0],
                                    [zxzx, 0, 0, 0, zyzy, 0, 0, 0, zzzz]]).subs([(xxxx, yyyy),
                                                                                 (yyzz, xxzz),
                                                                                 (yzzy, xzzx),
                                                                                 (xxyy, yyxx),
                                                                                 (zzyy, zzxx),
                                                                                 (yzyz, xzxz),
                                                                                 (xyxy, yxyx),
                                                                                 (zyyz, zxxz),
                                                                                 (zyzy, zxzx),
                                                                                 (xyyx, yxxy),
                                                                                 (xxzz, xzzx),
                                                                                 (zzxx, zxxz),
                                                                                 (yxxy, yyxx)]),

                'C4v – 4mm': Matrix([[xxxx, 0, 0, 0, xyxy, 0, 0, 0, xzxz],
                                     [0, xxyy, 0, xyyx, 0, 0, 0, 0, 0],
                                     [0, 0, xxzz, 0, 0, 0, xzzx, 0, 0],
                                     [0, yxxy, 0, yyxx, 0, 0, 0, 0, 0],
                                     [yxyx, 0, 0, 0, yyyy, 0, 0, 0, yzyz],
                                     [0, 0, 0, 0, 0, yyzz, 0, yzzy, 0],
                                     [0, 0, zxxz, 0, 0, 0, zzxx, 0, 0],
                                     [0, 0, 0, 0, 0, zyyz, 0, zzyy, 0],
                                     [zxzx, 0, 0, 0, zyzy, 0, 0, 0, zzzz]]).subs([(xxxx, yyyy),
                                                                                  (yyzz, xxzz),
                                                                                  (yzzy, xzzx),
                                                                                  (xxyy, yyxx),
                                                                                  (zzyy, zzxx),
                                                                                  (yzyz, xzxz),
                                                                                  (xyxy, yxyx),
                                                                                  (zyyz, zxxz),
                                                                                  (zyzy, zxzx),
                                                                                  (xyyx, yxxy),
                                                                                  (xxzz, xzzx),
                                                                                  (zzxx, zxxz),
                                                                                  (yxxy, yyxx)]),

                'D4h – 4|mmm': Matrix([[xxxx, 0, 0, 0, xyxy, 0, 0, 0, xzxz],
                                       [0, xxyy, 0, xyyx, 0, 0, 0, 0, 0],
                                       [0, 0, xxzz, 0, 0, 0, xzzx, 0, 0],
                                       [0, yxxy, 0, yyxx, 0, 0, 0, 0, 0],
                                       [yxyx, 0, 0, 0, yyyy, 0, 0, 0, yzyz],
                                       [0, 0, 0, 0, 0, yyzz, 0, yzzy, 0],
                                       [0, 0, zxxz, 0, 0, 0, zzxx, 0, 0],
                                       [0, 0, 0, 0, 0, zyyz, 0, zzyy, 0],
                                       [zxzx, 0, 0, 0, zyzy, 0, 0, 0, zzzz]]).subs([(xxxx, yyyy),
                                                                                    (yyzz, xxzz),
                                                                                    (yzzy, xzzx),
                                                                                    (xxyy, yyxx),
                                                                                    (zzyy, zzxx),
                                                                                    (yzyz, xzxz),
                                                                                    (xyxy, yxyx),
                                                                                    (zyyz, zxxz),
                                                                                    (zyzy, zxzx),
                                                                                    (xyyx, yxxy),
                                                                                    (xxzz, xzzx),
                                                                                    (zzxx, zxxz),
                                                                                    (yxxy, yyxx)]),

                'D2d – 4(Bar)2m': Matrix([[xxxx, 0, 0, 0, xyxy, 0, 0, 0, xzxz],
                                          [0, xxyy, 0, xyyx, 0, 0, 0, 0, 0],
                                          [0, 0, xxzz, 0, 0, 0, xzzx, 0, 0],
                                          [0, yxxy, 0, yyxx, 0, 0, 0, 0, 0],
                                          [yxyx, 0, 0, 0, yyyy, 0, 0, 0, yzyz],
                                          [0, 0, 0, 0, 0, yyzz, 0, yzzy, 0],
                                          [0, 0, zxxz, 0, 0, 0, zzxx, 0, 0],
                                          [0, 0, 0, 0, 0, zyyz, 0, zzyy, 0],
                                          [zxzx, 0, 0, 0, zyzy, 0, 0, 0, zzzz]]).subs([(xxxx, yyyy),
                                                                                       (yyzz, xxzz),
                                                                                       (yzzy, xzzx),
                                                                                       (xxyy, yyxx),
                                                                                       (zzyy, zzxx),
                                                                                       (yzyz, xzxz),
                                                                                       (xyxy, yxyx),
                                                                                       (zyyz, zxxz),
                                                                                       (zyzy, zxzx),
                                                                                       (xyyx, yxxy),
                                                                                       (xxzz, xzzx),
                                                                                       (zzxx, zxxz),
                                                                                       (yxxy, yyxx)])
            },
            'Monoclinic': {'C2 – 2': Matrix([[xxxx, 0, xxxz, 0, xyxy, 0, xzxx, 0, xzxz],
                                             [0, xxyy, 0, xyyx, 0, xyyz, 0, xzyy, 0],
                                             [xxzx, 0, xxzz, 0, xyzy, 0, xzzx, 0, xzzz],
                                             [0, yxxy, 0, yyxx, 0, yyxz, 0, yzxy, 0],
                                             [yxyx, 0, yxyz, 0, yyyy, 0, yzyx, 0, yzyz],
                                             [0, yxzy, 0, yyzx, 0, yyzz, 0, yzzy, 0],
                                             [zxxx, 0, zxxz, 0, zyxy, 0, zzxx, 0, zzxz],
                                             [0, zxyy, 0, zyyx, 0, zyyz, 0, zzyy, 0],
                                             [zxzx, 0, zxzz, 0, zyzy, 0, zzzx, 0, zzzz]]).subs([(xxyy, xyyx),
                                                                                                (yxxy, yyxx),
                                                                                                (yxzy, yyzx),
                                                                                                (zxyy, zyyx),
                                                                                                (xxxz, xzxx),
                                                                                                (xxzz, xzzx),
                                                                                                (yxyz, yzyx),
                                                                                                (zxxz, zzxx),
                                                                                                (zxzz, zzzx),
                                                                                                (xyyz, xzyy),
                                                                                                (yyxz, yzxy),
                                                                                                (yyzz, yzzy),
                                                                                                (zyyz, zzyy)]),

                           'C1h – m': Matrix([[xxxx, 0, xxxz, 0, xyxy, 0, xzxx, 0, xzxz],
                                              [0, xxyy, 0, xyyx, 0, xyyz, 0, xzyy, 0],
                                              [xxzx, 0, xxzz, 0, xyzy, 0, xzzx, 0, xzzz],
                                              [0, yxxy, 0, yyxx, 0, yyxz, 0, yzxy, 0],
                                              [yxyx, 0, yxyz, 0, yyyy, 0, yzyx, 0, yzyz],
                                              [0, yxzy, 0, yyzx, 0, yyzz, 0, yzzy, 0],
                                              [zxxx, 0, zxxz, 0, zyxy, 0, zzxx, 0, zzxz],
                                              [0, zxyy, 0, zyyx, 0, zyyz, 0, zzyy, 0],
                                              [zxzx, 0, zxzz, 0, zyzy, 0, zzzx, 0, zzzz]]).subs([(xxyy, xyyx),
                                                                                                 (yxxy, yyxx),
                                                                                                 (yxzy, yyzx),
                                                                                                 (zxyy, zyyx),
                                                                                                 (xxxz, xzxx),
                                                                                                 (xxzz, xzzx),
                                                                                                 (yxyz, yzyx),
                                                                                                 (zxxz, zzxx),
                                                                                                 (zxzz, zzzx),
                                                                                                 (xyyz, xzyy),
                                                                                                 (yyxz, yzxy),
                                                                                                 (yyzz, yzzy),
                                                                                                 (zyyz, zzyy)]),
                           'C2h – 2|m': Matrix([[xxxx, 0, xxxz, 0, xyxy, 0, xzxx, 0, xzxz],
                                                [0, xxyy, 0, xyyx, 0, xyyz, 0, xzyy, 0],
                                                [xxzx, 0, xxzz, 0, xyzy, 0, xzzx, 0, xzzz],
                                                [0, yxxy, 0, yyxx, 0, yyxz, 0, yzxy, 0],
                                                [yxyx, 0, yxyz, 0, yyyy, 0, yzyx, 0, yzyz],
                                                [0, yxzy, 0, yyzx, 0, yyzz, 0, yzzy, 0],
                                                [zxxx, 0, zxxz, 0, zyxy, 0, zzxx, 0, zzxz],
                                                [0, zxyy, 0, zyyx, 0, zyyz, 0, zzyy, 0],
                                                [zxzx, 0, zxzz, 0, zyzy, 0, zzzx, 0, zzzz]]).subs([(xxyy, xyyx),
                                                                                                   (yxxy, yyxx),
                                                                                                   (yxzy, yyzx),
                                                                                                   (zxyy, zyyx),
                                                                                                   (xxxz, xzxx),
                                                                                                   (xxzz, xzzx),
                                                                                                   (yxyz, yzyx),
                                                                                                   (zxxz, zzxx),
                                                                                                   (zxzz, zzzx),
                                                                                                   (xyyz, xzyy),
                                                                                                   (yyxz, yzxy),
                                                                                                   (yyzz, yzzy),
                                                                                                   (zyyz, zzyy)])
                           },

            'Orthorhombic': {'D2 – 222': Matrix([[xxxx, 0, 0, 0, xyxy, 0, 0, 0, xzxz],
                                                 [0, xxyy, 0, xyyx, 0, 0, 0, 0, 0],
                                                 [0, 0, xxzz, 0, 0, 0, xzzx, 0, 0],
                                                 [0, yxxy, 0, yyxx, 0, 0, 0, 0, 0],
                                                 [yxyx, 0, 0, 0, yyyy, 0, 0, 0, yzyz],
                                                 [0, 0, 0, 0, 0, yyzz, 0, yzzy, 0],
                                                 [0, 0, zxxz, 0, 0, 0, zzxx, 0, 0],
                                                 [0, 0, 0, 0, 0, zyyz, 0, zzyy, 0],
                                                 [zxzx, 0, 0, 0, zyzy, 0, 0, 0, zzzz]]).subs([(xxyy, xyyx),
                                                                                              (yxxy, yyxx),
                                                                                              (xxzz, xzzx),
                                                                                              (zxxz, zzxx),
                                                                                              (yyzz, yzzy),
                                                                                              (zyyz, zzyy)]),

                             'C2v – mm2': Matrix([[xxxx, 0, 0, 0, xyxy, 0, 0, 0, xzxz],
                                                  [0, xxyy, 0, xyyx, 0, 0, 0, 0, 0],
                                                  [0, 0, xxzz, 0, 0, 0, xzzx, 0, 0],
                                                  [0, yxxy, 0, yyxx, 0, 0, 0, 0, 0],
                                                  [yxyx, 0, 0, 0, yyyy, 0, 0, 0, yzyz],
                                                  [0, 0, 0, 0, 0, yyzz, 0, yzzy, 0],
                                                  [0, 0, zxxz, 0, 0, 0, zzxx, 0, 0],
                                                  [0, 0, 0, 0, 0, zyyz, 0, zzyy, 0],
                                                  [zxzx, 0, 0, 0, zyzy, 0, 0, 0, zzzz]]).subs([(xxyy, xyyx),
                                                                                               (yxxy, yyxx),
                                                                                               (xxzz, xzzx),
                                                                                               (zxxz, zzxx),
                                                                                               (yyzz, yzzy),
                                                                                               (zyyz, zzyy)]),

                             'D2h – mmm': Matrix([[xxxx, 0, 0, 0, xyxy, 0, 0, 0, xzxz],
                                                  [0, xxyy, 0, xyyx, 0, 0, 0, 0, 0],
                                                  [0, 0, xxzz, 0, 0, 0, xzzx, 0, 0],
                                                  [0, yxxy, 0, yyxx, 0, 0, 0, 0, 0],
                                                  [yxyx, 0, 0, 0, yyyy, 0, 0, 0, yzyz],
                                                  [0, 0, 0, 0, 0, yyzz, 0, yzzy, 0],
                                                  [0, 0, zxxz, 0, 0, 0, zzxx, 0, 0],
                                                  [0, 0, 0, 0, 0, zyyz, 0, zzyy, 0],
                                                  [zxzx, 0, 0, 0, zyzy, 0, 0, 0, zzzz]]).subs([(xxyy, xyyx),
                                                                                               (yxxy, yyxx),
                                                                                               (xxzz, xzzx),
                                                                                               (zxxz, zzxx),
                                                                                               (yyzz, yzzy),
                                                                                               (zyyz, zzyy)])
                             },

            'Triclinic': {'C1 – I': Matrix([[xxxx, xxxy, xxxz, xyxx, xyxy, xyxz, xzxx, xzxy, xzxz],
                                            [xxyx, xxyy, xxyz, xyyx, xyyy, xyyz, xzyx, xzyy, xzyz],
                                            [xxzx, xxzy, xxzz, xyzx, xyzy, xyzz, xzzx, xzzy, xzzz],
                                            [yxxx, yxxy, yxxz, yyxx, yyxy, yyxz, yzxx, yzxy, yzxz],
                                            [yxyx, yxyy, yxyz, yyyx, yyyy, yyyz, yzyx, yzyy, yzyz],
                                            [yxzx, yxzy, yxzz, yyzx, yyzy, yyzz, yzzx, yzzy, yzzz],
                                            [zxxx, zxxy, zxxz, zyxx, zyxy, zyxz, zzxx, zzxy, zzxz],
                                            [zxyx, zxyy, zxyz, zyyx, zyyy, zyyz, zzyx, zzyy, zzyz],
                                            [zxzx, zxzy, zxzz, zyzx, zyzy, zyzz, zzzx, zzzy, zzzz]]).subs([(xxxy, xyxx),
                                                                                                           (xxyy, xyyx),
                                                                                                           (xxzy, xyzx),
                                                                                                           (yxxy, yyxx),
                                                                                                           (yxyy, yyyx),
                                                                                                           (yxzy, yyzx),
                                                                                                           (zxxy, zyxx),
                                                                                                           (zxyy, zyyx),
                                                                                                           (zxzy, zyzx),
                                                                                                           (xxxz, xzxx),
                                                                                                           (xxyz, xzyx),
                                                                                                           (xxzz, xzzx),
                                                                                                           (yxxz, yzxx),
                                                                                                           (yxyz, yzyx),
                                                                                                           (yxzz, yzzx),
                                                                                                           (zxxz, zzxx),
                                                                                                           (zxyz, zzyx),
                                                                                                           (zxzz, zzzx),
                                                                                                           (xyxz, xzxy),
                                                                                                           (xyyz, xzyy),
                                                                                                           (xyzz, xzzy),
                                                                                                           (yyxz, yzxy),
                                                                                                           (yyyz, yzyy),
                                                                                                           (yyzz, yzzy),
                                                                                                           (zyxz, zzxy),
                                                                                                           (zyyz, zzyy),
                                                                                                           (zyzz,
                                                                                                            zzzy)]),
                          'S2 – I(Bar)': Matrix([[xxxx, xxxy, xxxz, xyxx, xyxy, xyxz, xzxx, xzxy, xzxz],
                                                 [xxyx, xxyy, xxyz, xyyx, xyyy, xyyz, xzyx, xzyy, xzyz],
                                                 [xxzx, xxzy, xxzz, xyzx, xyzy, xyzz, xzzx, xzzy, xzzz],
                                                 [yxxx, yxxy, yxxz, yyxx, yyxy, yyxz, yzxx, yzxy, yzxz],
                                                 [yxyx, yxyy, yxyz, yyyx, yyyy, yyyz, yzyx, yzyy, yzyz],
                                                 [yxzx, yxzy, yxzz, yyzx, yyzy, yyzz, yzzx, yzzy, yzzz],
                                                 [zxxx, zxxy, zxxz, zyxx, zyxy, zyxz, zzxx, zzxy, zzxz],
                                                 [zxyx, zxyy, zxyz, zyyx, zyyy, zyyz, zzyx, zzyy, zzyz],
                                                 [zxzx, zxzy, zxzz, zyzx, zyzy, zyzz, zzzx, zzzy, zzzz]]).subs(
                              [(xxxy, xyxx),
                               (xxyy, xyyx),
                               (xxzy, xyzx),
                               (yxxy, yyxx),
                               (yxyy, yyyx),
                               (yxzy, yyzx),
                               (zxxy, zyxx),
                               (zxyy, zyyx),
                               (zxzy, zyzx),
                               (xxxz, xzxx),
                               (xxyz, xzyx),
                               (xxzz, xzzx),
                               (yxxz, yzxx),
                               (yxyz, yzyx),
                               (yxzz, yzzx),
                               (zxxz, zzxx),
                               (zxyz, zzyx),
                               (zxzz, zzzx),
                               (xyxz, xzxy),
                               (xyyz, xzyy),
                               (xyzz, xzzy),
                               (yyxz, yzxy),
                               (yyyz, yzyy),
                               (yyzz, yzzy),
                               (zyxz, zzxy),
                               (zyyz, zzyy),
                               (zyzz, zzzy)])
                          }
        }

        self.dic_mag_dip = {
            'Triclinic': {
                'C1': Matrix(
                    [[xxx, xyx, xzx], [xxy, xyy, xzy], [xxz, xyz, xzz], [yxx, yyx, yzx], [yxy, yyy, yzy],
                     [yxz, yyz, yzz],
                     [zxx, zyx, zzx], [zxy, zyy, zzy], [zxz, zyz, zzz]]).subs([(xyx, xxy), (xzx, xxz), (xzy, xyz),
                                                                               (yyx, yxy), (yzx, yxz), (yzy, yyz),
                                                                               (zyx, zxy), (zzx, zxz), (zzy, zyz)]),
                'S2': Matrix(
                    [[xxx, xyx, xzx], [xxy, xyy, xzy], [xxz, xyz, xzz], [yxx, yyx, yzx], [yxy, yyy, yzy],
                     [yxz, yyz, yzz],
                     [zxx, zyx, zzx], [zxy, zyy, zzy], [zxz, zyz, zzz]]).subs([(xyx, xxy), (xzx, xxz), (xzy, xyz),
                                                                               (yyx, yxy), (yzx, yxz), (yzy, yyz),
                                                                               (zyx, zxy), (zzx, zxz), (zzy, zyz)])
            },

            'Monoclinic': {
                'C2': Matrix(
                    [[0, xyx, 0], [xxy, 0, xzy], [0, xyz, 0], [yxx, 0, yzx], [0, yyy, 0], [yxz, 0, yzz], [0, zyx, 0],
                     [zxy, 0, zzy], [0, zyz, 0]]).subs([(xyx, xxy), (xzy, xyz), (yzx, yxz), (zyx, zxy), (zzy, zyz)]),

                'C1h': Matrix(
                    [[0, xyx, 0], [xxy, 0, xzy], [0, xyz, 0], [yxx, 0, yzx], [0, yyy, 0], [yxz, 0, yzz], [0, zyx, 0],
                     [zxy, 0, zzy], [0, zyz, 0]]).subs([(xyx, xxy), (xzy, xyz), (yzx, yxz), (zyx, zxy), (zzy, zyz)]),

                'C2h': Matrix(
                    [[0, xyx, 0], [xxy, 0, xzy], [0, xyz, 0], [yxx, 0, yzx], [0, yyy, 0], [yxz, 0, yzz], [0, zyx, 0],
                     [zxy, 0, zzy], [0, zyz, 0]]).subs([(xyx, xxy), (xzy, xyz), (yzx, yxz), (zyx, zxy), (zzy, zyz)])
            },

            'Orthorhombic': {
                'D2': Matrix([[0, 0, 0], [0, 0, xzy], [0, xyz, 0], [0, 0, yzx], [0, 0, 0], [yxz, 0, 0], [0, zyx, 0],
                              [zxy, 0, 0], [0, 0, 0]]).subs([(xzy, xyz), (yzx, yxz), (zyx, zxy)]),

                'C2v': Matrix([[0, 0, 0], [0, 0, xzy], [0, xyz, 0], [0, 0, yzx], [0, 0, 0], [yxz, 0, 0], [0, zyx, 0],
                               [zxy, 0, 0], [0, 0, 0]]).subs([(xzy, xyz), (yzx, yxz), (zyx, zxy)]),

                'D2h': Matrix([[0, 0, 0], [0, 0, xzy], [0, xyz, 0], [0, 0, yzx], [0, 0, 0], [yxz, 0, 0], [0, zyx, 0],
                               [zxy, 0, 0], [0, 0, 0]]).subs([(xzy, xyz), (yzx, yxz), (zyx, zxy)])
            },

            'Tetragonal': {
                'C4': Matrix([[0, 0, xzx], [0, 0, xzy], [xxz, xyz, 0], [0, 0, yzx], [0, 0, yzy], [yxz, yyz, 0],
                              [zxx, 0, 0], [0, zyy, 0], [0, 0, zzz]]).subs([(xzx, xxz), (yzy, xxz), (yyz, xxz),
                                                                            (xzy, xyz), (yxz, -xyz), (yzx, -xyz),
                                                                            (zyy, zxx)]),

                'S4': Matrix([[0, 0, xzx], [0, 0, xzy], [xxz, xyz, 0], [0, 0, yzx], [0, 0, yzy], [yxz, yyz, 0],
                              [zxx, 0, 0], [0, zyy, 0], [0, 0, zzz]]).subs([(xzx, xxz), (yzy, xxz), (yyz, xxz),
                                                                            (xzy, xyz), (yxz, -xyz), (yzx, -xyz),
                                                                            (zyy, zxx)]),

                'D4': Matrix([[0, 0, 0], [0, 0, xzy], [0, xyz, 0], [0, 0, yzx], [0, 0, 0], [yxz, 0, 0],
                              [0, 0, 0], [0, 0, 0], [0, 0, 0]]).subs([(xzy, xyz), (yxz, -xyz), (yzx, -xyz)]),

                'C4v': Matrix([[0, 0, 0], [0, 0, xzy], [0, xyz, 0], [0, 0, yzx], [0, 0, 0], [yxz, 0, 0],
                               [0, 0, 0], [0, 0, 0], [0, 0, 0]]).subs([(xzy, xyz), (yxz, -xyz), (yzx, -xyz)]),

                'D2d': Matrix([[0, 0, 0], [0, 0, xzy], [0, xyz, 0], [0, 0, yzx], [0, 0, 0], [yxz, 0, 0],
                               [0, 0, 0], [0, 0, 0], [0, 0, 0]]).subs([(xzy, xyz), (yxz, -xyz), (yzx, -xyz)]),

                'C4h': Matrix([[0, 0, xzx], [0, 0, xzy], [xxz, xyz, 0], [0, 0, yzx], [0, 0, yzy], [yxz, yyz, 0],
                               [zxx, 0, 0], [0, zyy, 0], [0, 0, zzz]]).subs([(xzx, xxz), (yzy, xxz), (yyz, xxz),
                                                                             (xzy, xyz), (yxz, -xyz), (yzx, -xyz),
                                                                             (zyy, zxx)]),

                'D4h': Matrix([[0, 0, 0], [0, 0, xzy], [0, xyz, 0], [0, 0, yzx], [0, 0, 0], [yxz, 0, 0],
                               [0, 0, 0], [0, 0, 0], [0, 0, 0]]).subs([(xzy, xyz), (yxz, -xyz), (yzx, -xyz)])
            },

            'Cubic': {
                'O': Matrix([[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0],
                             [0, 0, 0]]),

                'Td': Matrix([[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0],
                              [0, 0, 0]]),

                'T': Matrix([[0, 0, 0], [0, 0, xzy], [0, xyz, 0], [0, 0, yzx], [0, 0, 0], [yxz, 0, 0],
                             [0, zyx, 0], [zxy, 0, 0], [0, 0, 0]]).subs([(yzx, xyz), (zxy, xyz), (yxz, xyz),
                                                                         (zyx, xyz), (xzy, xyz)]),

                'Th': Matrix([[0, 0, 0], [0, 0, xzy], [0, xyz, 0], [0, 0, yzx], [0, 0, 0], [yxz, 0, 0],
                              [0, zyx, 0], [zxy, 0, 0], [0, 0, 0]]).subs([(yzx, xyz), (zxy, xyz), (yxz, xyz),
                                                                          (zyx, xyz), (xzy, xyz)]),

                'Oh': Matrix([[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0],
                              [0, 0, 0]])
            },

            'Trigonal': {
                'C3': Matrix([[xxx, xyx, xzx], [xxy, xyy, xzy], [xxz, xyz, 0], [yxx, yyx, yzx], [yxy, yyy, yzy],
                              [yxz, yyz, 0], [zxx, 0, 0], [0, zyy, 0], [0, 0, zzz]]).subs(
                    [(xyy, -xxx), (yxy, -xxx), (yyx, -xxx),
                     (xyx, xxy), (yxx, xxy), (yyy, -xxy),
                     (xzx, xxz), (yyz, xxz), (yzy, xxz),
                     (xzy, xyz), (yxz, -xyz), (yzx, -xyz),
                     (zyy, zxx)]),

                'D3': Matrix([[xxx, 0, 0], [0, xyy, xzy], [0, xyz, 0], [0, yyx, yzx], [yxy, 0, 0], [yxz, 0, 0],
                              [0, 0, 0], [0, 0, 0], [0, 0, 0]]).subs(
                    [(xyy, -xxx), (yxy, -xxx), (yyx, -xxx),
                     (xzy, xyz), (yxz, -xyz), (yzx, -xyz)]),

                'C3v': Matrix([[xxx, 0, 0], [0, xyy, xzy], [0, xyz, 0], [0, yyx, yzx], [yxy, 0, 0], [yxz, 0, 0],
                               [0, 0, 0], [0, 0, 0], [0, 0, 0]]).subs(
                    [(xyy, -xxx), (yxy, -xxx), (yyx, -xxx),
                     (xzy, xyz), (yxz, -xyz), (yzx, -xyz)]),

                'S6': Matrix([[xxx, xyx, xzx], [xxy, xyy, xzy], [xxz, xyz, 0], [yxx, yyx, yzx], [yxy, yyy, yzy],
                              [yxz, yyz, 0], [zxx, 0, 0], [0, zyy, 0], [0, 0, zzz]]).subs(
                    [(xyy, -xxx), (yxy, -xxx), (yyx, -xxx),
                     (xyx, xxy), (yxx, xxy), (yyy, -xxy),
                     (xzx, xxz), (yyz, xxz), (yzy, xxz),
                     (xzy, xyz), (yxz, -xyz), (yzx, -xyz),
                     (zyy, zxx)]),

                'D3d': Matrix([[xxx, 0, 0], [0, xyy, xzy], [0, xyz, 0], [0, yyx, yzx], [yxy, 0, 0], [yxz, 0, 0],
                               [0, 0, 0], [0, 0, 0], [0, 0, 0]]).subs(
                    [(xyy, -xxx), (yxy, -xxx), (yyx, -xxx),
                     (xzy, xyz), (yxz, -xyz), (yzx, -xyz)])

            },

            'Hexagonal': {
                'C6': Matrix([[0, 0, xzx], [0, 0, xzy], [xxz, xyz, 0], [0, 0, yzx], [0, 0, yzy], [yxz, yyz, 0],
                              [zxx, 0, 0], [0, zyy, 0], [0, 0, zzz]]).subs([(xzx, xxz), (yzy, xxz), (yyz, xxz),
                                                                            (xzy, xyz), (yxz, -xyz), (yzx, -xyz),
                                                                            (zyy, zxx)]),
                'C3h': Matrix([[0, 0, xzx], [0, 0, xzy], [xxz, xyz, 0], [0, 0, yzx], [0, 0, yzy], [yxz, yyz, 0],
                               [zxx, 0, 0], [0, zyy, 0], [0, 0, zzz]]).subs([(xzx, xxz), (yzy, xxz), (yyz, xxz),
                                                                             (xzy, xyz), (yxz, -xyz), (yzx, -xyz),
                                                                             (zyy, zxx)]),
                'D6': Matrix([[0, 0, 0], [0, 0, xzy], [0, xyz, 0], [0, 0, yzx], [0, 0, 0], [yxz, 0, 0],
                              [0, 0, 0], [0, 0, 0], [0, 0, 0]]).subs([(xzy, xyz), (yxz, -xyz), (yzx, -xyz)]),
                'C6v': Matrix([[0, 0, 0], [0, 0, xzy], [0, xyz, 0], [0, 0, yzx], [0, 0, 0], [yxz, 0, 0],
                               [0, 0, 0], [0, 0, 0], [0, 0, 0]]).subs([(xzy, xyz), (yxz, -xyz), (yzx, -xyz)]),
                'D3h': Matrix([[0, 0, 0], [0, 0, xzy], [0, xyz, 0], [0, 0, yzx], [0, 0, 0], [yxz, 0, 0],
                               [0, 0, 0], [0, 0, 0], [0, 0, 0]]).subs([(xzy, xyz), (yxz, -xyz), (yzx, -xyz)]),
                'C6h': Matrix([[0, 0, xzx], [0, 0, xzy], [xxz, xyz, 0], [0, 0, yzx], [0, 0, yzy], [yxz, yyz, 0],
                               [zxx, 0, 0], [0, zyy, 0], [0, 0, zzz]]).subs([(xzx, xxz), (yzy, xxz), (yyz, xxz),
                                                                             (xzy, xyz), (yxz, -xyz), (yzx, -xyz),
                                                                             (zyy, zxx)]),
                'D6h': Matrix([[0, 0, 0], [0, 0, xzy], [0, xyz, 0], [0, 0, yzx], [0, 0, 0], [yxz, 0, 0],
                               [0, 0, 0], [0, 0, 0], [0, 0, 0]]).subs([(xzy, xyz), (yxz, -xyz), (yzx, -xyz)])
            }
        }

    def createWidget(self):

        self.list_init()
        self.view_init()
        # set up a navigation toolbar

        # create an optionMenu
        self.option_var = []
        self.option_var_1 = []
        self.option_var_2 = []
        # Laebl position/ bg='#283747'/bg='#f6f6f6'
        pointGroup = ttk.Label(self.fr_input_up, text='Radiation Source:', background='#F2F3F4',
                           font=('Arial bold', 15))
        pointGroup.place(x=34, y=32)

        crystalSystem = ttk.Label(self.fr_input_up, text='Crystal System:', background='#F2F3F4',
                              font=('Arial bold', 15))
        crystalSystem.place(x=196, y=32)

        crystalClass = ttk.Label(self.fr_input_up, text='Point Group:', background='#F2F3F4',
                             font=('Arial bold', 15))
        crystalClass.place(x=332, y=32)
        self.group_box_group = Listbox(self.fr_input_up, width=16, justify="left", height=11, font=('Arial', 13),
                                       yscrollcommand='Vertical', selectmode=SINGLE, relief='sunken', exportselection=False)
        self.group_box_group.place(x=335, y=60)

        self.group_box = Listbox(self.fr_input_up, width=17, justify="left", height=11, yscrollcommand='Vertical',
                                 selectmode=SINGLE, relief='sunken', font=('Arial', 13), exportselection=False)
        self.group_box.place(x=38, y=60)
        self.group_box.insert(1, 'Electric Dipole')
        self.group_box.insert(2, 'Electric Quadrupole')
        self.group_box.insert(3, 'Magnetic Dipole')
        self.group_box.insert(4, 'Coming Soon...')
        self.group_box.bind('<Return>', lambda x: self.show_crystal_system())
        self.group_box.bind('<Double-Button-1>', lambda x: self.show_crystal_system())
        self.group_box.bind('<<ListboxSelect>>', lambda x: self.show_crystal_system())
        self.crystal_system = Listbox(self.fr_input_up, width=16, justify="left", height=11, font=('Arial', 13),
                                      yscrollcommand='Vertical', selectmode=SINGLE, relief='sunken', exportselection=False)
        self.crystal_system.place(x=200, y=60)

        self.nex_bt = ttk.Button(self.fr_input_up, text='Calculate', command=lambda: self.pop_up_warning(), width=10,
                                 style='Accent.TButton')
        self.nex_bt.bind('<Return>', lambda: self.show_crystal_system())
        self.nex_bt.grid(row=0, column=0, padx=355, pady=260)
        myBtn = ttk.Button(self.fr_input_up, text='?')
        myBtn.place(y=260, x=312)
        myTip = Hovertip(myBtn, 'Please select all the elements to do the calculation. '
                                '\nThe calculation model can be found at menu->Model->Calculation Model', hover_delay=1000)

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

    def showSymbol(self, symbol):
        if str(symbol) == 'theta':
            return chr(952)
        else:
            return symbol

    def view_init(self):
        # self.fr_input_up = Frame(master=root, bg='#f6f6f6')
        # root.geometry(250,152)
        self.fr_input_up = Frame(master=root, bg='#F2F3F4')
        self.fr_input_up.grid(row=1, column=0, ipadx=250, ipady=152, sticky='NW')
        self.fr_input_up.grid_propagate(False)
        self.fr_input_dw = Frame(master=root)
        self.fr_plot = Frame(master=root)

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
            # print(self.valueList_ss)
            if chr(952) == self.showSymbol(self.symbolList_ss[0]):
                self.valueList_ss[0] = math.radians(self.valueList_ss[0])
            self.substitute = [(self.symbolList_ss[i], self.valueList_ss[i]) for i in range(len(self.symbolList_ss))]
            for i in range(len(phi_value)):
                self.substitute.append((phi, phi_value[i]))
                self.polarList_ss.append(self.exprss.subs(self.substitute))
                self.substitute.remove((phi, phi_value[i]))
            self.ax[0].plot(phi_value, self.polarList_ss)
            # self.toolbar.update()
            self.canvs.draw()

        self.polarList_sp = []
        self.check_list_sp = [float(self.entryList_sp[i].get()) for i in range(len(self.entryList_sp))]
        if all(u == 0 for u in self.check_list_sp):
            str = 'THIS IS BAD!'
        else:
            self.valueList_sp = [float(self.entryList_sp[i].get()) for i in range(len(self.entryList_sp))]
            # print(self.valueList_sp)
            if chr(952) == self.showSymbol(self.symbolList_sp[0]):
                self.valueList_sp[0] = math.radians(self.valueList_sp[0])
            self.substitute = [(self.symbolList_sp[i], self.valueList_sp[i]) for i in range(len(self.symbolList_sp))]
            for i in range(len(phi_value)):
                self.substitute.append((phi, phi_value[i]))
                self.polarList_sp.append(self.exprsp.subs(self.substitute))
                self.substitute.remove((phi, phi_value[i]))
            self.ax[1].plot(phi_value, self.polarList_sp)
            # self.toolbar.update()
            self.canvs.draw()

        self.polarList_ps = []
        self.check_list_ps = [float(self.entryList_ps[i].get()) for i in range(len(self.entryList_ps))]
        if all(w == 0 for w in self.check_list_ps):
            str = 'THIS IS BAD!'
        else:
            self.valueList_ps = [float(self.entryList_ps[i].get()) for i in range(len(self.entryList_ps))]
            # print(self.valueList_ps)
            if chr(952) == self.showSymbol(self.symbolList_ps[0]):
                self.valueList_ps[0] = math.radians(self.valueList_ps[0])
            self.substitute = [(self.symbolList_ps[i], self.valueList_ps[i]) for i in range(len(self.symbolList_ps))]
            for i in range(len(phi_value)):
                self.substitute.append((phi, phi_value[i]))
                self.polarList_ps.append(self.exprps.subs(self.substitute))
                self.substitute.remove((phi, phi_value[i]))

            self.ax[2].plot(phi_value, self.polarList_ps)
            # self.toolbar.update()
            self.canvs.draw()

        self.polarList_pp = []
        self.check_list_pp = [float(self.entryList_pp[i].get()) for i in range(len(self.entryList_pp))]
        if all(s == 0 for s in self.check_list_pp):
            str = 'THIS IS BAD!'
        else:
            self.valueList_pp = [float(self.entryList_pp[i].get()) for i in range(len(self.entryList_pp))]
            # print(self.valueList_pp)
            if chr(952) == self.showSymbol(self.symbolList_pp[0]):
                self.valueList_pp[0] = math.radians(self.valueList_pp[0])
            self.substitute = [(self.symbolList_pp[i], self.valueList_pp[i]) for i in range(len(self.symbolList_pp))]

            for i in range(len(phi_value)):
                self.substitute.append((phi, phi_value[i]))
                self.polarList_pp.append(self.exprpp.subs(self.substitute))
                self.substitute.remove((phi, phi_value[i]))
            self.ax[3].plot(phi_value, self.polarList_pp)
            # self.toolbar.update()
            self.canvs.draw()

        def save():
            filename = asksaveasfilename(initialfile='Untitled.png', defaultextension=".png",
                                         filetypes=[("All Files", "*.*"), ("Portable Graphics Format", "*.png")])

            plt.savefig(filename)

    # def export_expression_latex(self):
    #     self.path = 'ExpressAndLatex/' + str(self.input_matrix_c) + '/' + str(self.option_var_1[0]) + '/' + str(
    #         self.option_var[0]) + '/'
    #     latex_txt = open(self.path + '/latexfile.txt', 'rt')
    #     f = asksaveasfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])


    # def export_expression(self):
    #     latex_txt = open(self.path + '/latexfile.txt', 'rt')
    #     filename = asksaveasfilename(initialfile='Untitled.png', defaultextension=".png",
    #                                  filetypes=[("All Files", "*.*"), ("Portable Graphics Format", "*.png")])

    def _quit(self):
        self.master.quit()  # stops mainloop
        self.master.destroy()  # this is necessary on Windows to prevent
        # Fatal Python Error: PyEval_RestoreThread: NULL tstate

    def _back(self):
        self.paned.destroy()
        self.fr_input_dw.destroy()
        self.fr_button_dw.destroy()
        self.fr_button_dw_message.destroy()
        self.createWidget()


    def trans(self, matrix):
        # input is a 9 by 3 matrix, consider a 3 by 1 vector as an element
        matrix[0:3, 1], matrix[3:6, 0] = matrix[3:6, 0], matrix[0:3, 1]
        matrix[0:3, 2], matrix[6:9, 0] = matrix[6:9, 0], matrix[0:3, 2]
        matrix[3:6, 2], matrix[6:9, 1] = matrix[6:9, 1], matrix[3:6, 2]
        return matrix

    def trans_quad(self, matrix):
        # input is a 9 by 3 matrix, consider a 3 by 1 vector as an element
        matrix[0:3, 3:6], matrix[3:6, 0:3] = matrix[3:6, 0:3], matrix[0:3, 3:6]
        matrix[0:3, 6:9], matrix[6:9, 0:3] = matrix[6:9, 0:3], matrix[0:3, 6:9]
        matrix[3:6, 6:9], matrix[6:9, 3:6] = matrix[6:9, 3:6], matrix[3:6, 6:9]
        return matrix

    def trans_quad_2Swap(self, matrix):
        # input is a 9 by 3 matrix, consider a 3 by 1 vector as an element
        matrix[0, 1], matrix[1, 0] = matrix[1, 0], matrix[0, 1]
        matrix[0, 2], matrix[2, 0] = matrix[2, 0], matrix[0, 2]
        matrix[2, 1], matrix[1, 2] = matrix[1, 2], matrix[2, 1]

        matrix[0, 4], matrix[1, 3] = matrix[1, 3], matrix[0, 4]
        matrix[0, 5], matrix[2, 3] = matrix[2, 3], matrix[0, 5]
        matrix[2, 4], matrix[1, 5] = matrix[1, 5], matrix[2, 4]

        matrix[0, 7], matrix[1, 6] = matrix[1, 6], matrix[0, 7]
        matrix[0, 8], matrix[2, 6] = matrix[2, 6], matrix[0, 8]
        matrix[2, 7], matrix[1, 8] = matrix[1, 8], matrix[2, 7]

        matrix[3, 1], matrix[4, 0] = matrix[4, 0], matrix[3, 1]
        matrix[3, 2], matrix[5, 0] = matrix[5, 0], matrix[3, 2]
        matrix[5, 1], matrix[4, 2] = matrix[4, 2], matrix[5, 1]

        matrix[3, 4], matrix[4, 3] = matrix[4, 3], matrix[3, 4]
        matrix[5, 3], matrix[3, 5] = matrix[5, 3], matrix[3, 5]
        matrix[4, 5], matrix[5, 4] = matrix[5, 4], matrix[4, 5]

        matrix[3, 7], matrix[4, 6] = matrix[4, 6], matrix[3, 7]
        matrix[5, 6], matrix[3, 8] = matrix[3, 8], matrix[5, 6]
        matrix[4, 8], matrix[5, 7] = matrix[5, 7], matrix[4, 8]

        matrix[6, 1], matrix[7, 0] = matrix[7, 0], matrix[6, 1]
        matrix[6, 2], matrix[8, 0] = matrix[8, 0], matrix[6, 2]
        matrix[8, 1], matrix[7, 2] = matrix[7, 2], matrix[8, 1]

        matrix[6, 4], matrix[7, 3] = matrix[7, 3], matrix[6, 4]
        matrix[6, 5], matrix[8, 3] = matrix[8, 3], matrix[6, 5]
        matrix[7, 5], matrix[8, 4] = matrix[8, 4], matrix[7, 5]

        matrix[6, 7], matrix[7, 6] = matrix[7, 6], matrix[6, 7]
        matrix[6, 8], matrix[8, 6] = matrix[8, 6], matrix[6, 8]
        matrix[8, 7], matrix[7, 8] = matrix[7, 8], matrix[8, 7]
        return matrix

        # define a function to do operation of 3*3 matrix times 9*3 matrix

    def sTB(self, sm, bm):
        # new matrix is 9 by 3
        a, b, c, d, e, f, g, h, k = sm[0, 0], sm[0, 1], sm[0, 2], sm[1, 0], sm[1, 1], sm[1, 2], sm[2, 0], sm[2, 1], sm[
            2, 2]
        A1, A2, A3, D1, D2, D3, G1, G2, G3 = bm[0, 0], bm[1, 0], bm[2, 0], bm[3, 0], bm[4, 0], bm[5, 0], bm[6, 0], bm[
            7, 0], bm[8, 0]
        B1, B2, B3, E1, E2, E3, H1, H2, H3 = bm[0, 1], bm[1, 1], bm[2, 1], bm[3, 1], bm[4, 1], bm[5, 1], bm[6, 1], bm[
            7, 1], bm[8, 1]
        C1, C2, C3, F1, F2, F3, K1, K2, K3 = bm[0, 2], bm[1, 2], bm[2, 2], bm[3, 2], bm[4, 2], bm[5, 2], bm[6, 2], bm[
            7, 2], bm[8, 2]
        nm = zeros(9, 3)
        nm[0, 0] = a * A1 + b * D1 + c * G1
        nm[1, 0] = a * A2 + b * D2 + c * G2
        nm[2, 0] = a * A3 + b * D3 + c * G3
        nm[3, 0] = d * A1 + e * D1 + f * G1
        nm[4, 0] = d * A2 + e * D2 + f * G2
        nm[5, 0] = d * A3 + e * D3 + f * G3
        nm[6, 0] = g * A1 + h * D1 + k * G1
        nm[7, 0] = g * A2 + h * D2 + k * G2
        nm[8, 0] = g * A3 + h * D3 + k * G3
        nm[0, 1] = a * B1 + b * E1 + c * H1
        nm[1, 1] = a * B2 + b * E2 + c * H2
        nm[2, 1] = a * B3 + b * E3 + c * H3
        nm[3, 1] = d * B1 + e * E1 + f * H1
        nm[4, 1] = d * B2 + e * E2 + f * H2
        nm[5, 1] = d * B3 + e * E3 + f * H3
        nm[6, 1] = g * B1 + h * E1 + k * H1
        nm[7, 1] = g * B2 + h * E2 + k * H2
        nm[8, 1] = g * B3 + h * E3 + k * H3
        nm[0, 2] = a * C1 + b * F1 + c * K1
        nm[1, 2] = a * C2 + b * F2 + c * K2
        nm[2, 2] = a * C3 + b * F3 + c * K3
        nm[3, 2] = d * C1 + e * F1 + f * K1
        nm[4, 2] = d * C2 + e * F2 + f * K2
        nm[5, 2] = d * C3 + e * F3 + f * K3
        nm[6, 2] = g * C1 + h * F1 + k * K1
        nm[7, 2] = g * C2 + h * F2 + k * K2
        nm[8, 2] = g * C3 + h * F3 + k * K3
        return nm

        # define a function to do operation of 3*3 matrix times 9*9 matrix

    def sTB_quad(self, sm, bm):
        # new matrix is 9 by 3
        a, b, c, d, e, f, g, h, k = sm[0, 0], sm[0, 1], sm[0, 2], sm[1, 0], sm[1, 1], sm[1, 2], sm[2, 0], sm[2, 1], sm[
            2, 2]
        A1, A2, A3, A4, A5, A6, A7, A8, A9 = bm[0, 0], bm[1, 0], bm[2, 0], bm[3, 0], bm[4, 0], bm[5, 0], bm[6, 0], bm[
            7, 0], bm[8, 0]
        B1, B2, B3, B4, B5, B6, B7, B8, B9 = bm[0, 1], bm[1, 1], bm[2, 1], bm[3, 1], bm[4, 1], bm[5, 1], bm[6, 1], bm[
            7, 1], bm[8, 1]
        C1, C2, C3, C4, C5, C6, C7, C8, C9 = bm[0, 2], bm[1, 2], bm[2, 2], bm[3, 2], bm[4, 2], bm[5, 2], bm[6, 2], bm[
            7, 2], bm[8, 2]
        D1, D2, D3, D4, D5, D6, D7, D8, D9 = bm[0, 3], bm[1, 3], bm[2, 3], bm[3, 3], bm[4, 3], bm[5, 3], bm[6, 3], bm[
            7, 3], bm[8, 3]
        E1, E2, E3, E4, E5, E6, E7, E8, E9 = bm[0, 4], bm[1, 4], bm[2, 4], bm[3, 4], bm[4, 4], bm[5, 4], bm[6, 4], bm[
            7, 4], bm[8, 4]
        F1, F2, F3, F4, F5, F6, F7, F8, F9 = bm[0, 5], bm[1, 5], bm[2, 5], bm[3, 5], bm[4, 5], bm[5, 5], bm[6, 5], bm[
            7, 5], bm[8, 5]
        G1, G2, G3, G4, G5, G6, G7, G8, G9 = bm[0, 6], bm[1, 6], bm[2, 6], bm[3, 6], bm[4, 6], bm[5, 6], bm[6, 6], bm[
            7, 6], bm[8, 6]
        H1, H2, H3, H4, H5, H6, H7, H8, H9 = bm[0, 7], bm[1, 7], bm[2, 7], bm[3, 7], bm[4, 7], bm[5, 7], bm[6, 7], bm[
            7, 7], bm[8, 7]
        I1, I2, I3, I4, I5, I6, I7, I8, I9 = bm[0, 8], bm[1, 8], bm[2, 8], bm[3, 8], bm[4, 8], bm[5, 8], bm[6, 8], bm[
            7, 8], bm[8, 8]
        nm = zeros(9, 9)
        # First 9x3
        nm[0, 0] = a * A1 + b * A4 + c * A7
        nm[1, 0] = a * A2 + b * A5 + c * A8
        nm[2, 0] = a * A3 + b * A6 + c * A9
        nm[3, 0] = d * A1 + e * A4 + f * A7
        nm[4, 0] = d * A2 + e * A5 + f * A8
        nm[5, 0] = d * A3 + e * A6 + f * A9
        nm[6, 0] = g * A1 + h * A4 + k * A7
        nm[7, 0] = g * A2 + h * A5 + k * A8
        nm[8, 0] = g * A3 + h * A6 + k * A9
        nm[0, 1] = a * B1 + b * B4 + c * B7
        nm[1, 1] = a * B2 + b * B5 + c * B8
        nm[2, 1] = a * B3 + b * B6 + c * B9
        nm[3, 1] = d * B1 + e * B4 + f * B7
        nm[4, 1] = d * B2 + e * B5 + f * B8
        nm[5, 1] = d * B3 + e * B6 + f * B9
        nm[6, 1] = g * B1 + h * B4 + k * B7
        nm[7, 1] = g * B2 + h * B5 + k * B8
        nm[8, 1] = g * B3 + h * B6 + k * B9
        nm[0, 2] = a * C1 + b * C4 + c * C7
        nm[1, 2] = a * C2 + b * C5 + c * C8
        nm[2, 2] = a * C3 + b * C6 + c * C9
        nm[3, 2] = d * C1 + e * C4 + f * C7
        nm[4, 2] = d * C2 + e * C5 + f * C8
        nm[5, 2] = d * C3 + e * C6 + f * C9
        nm[6, 2] = g * C1 + h * C4 + k * C7
        nm[7, 2] = g * C2 + h * C5 + k * C8
        nm[8, 2] = g * C3 + h * C6 + k * C9
        # Second 9x3
        nm[0, 3] = a * D1 + b * D4 + c * D7
        nm[1, 3] = a * D2 + b * D5 + c * D8
        nm[2, 3] = a * D3 + b * D6 + c * D9
        nm[3, 3] = d * D1 + e * D4 + f * D7
        nm[4, 3] = d * D2 + e * D5 + f * D8
        nm[5, 3] = d * D3 + e * D6 + f * D9
        nm[6, 3] = g * D1 + h * D4 + k * D7
        nm[7, 3] = g * D2 + h * D5 + k * D8
        nm[8, 3] = g * D3 + h * D6 + k * D9
        nm[0, 4] = a * E1 + b * E4 + c * E7
        nm[1, 4] = a * E2 + b * E5 + c * E8
        nm[2, 4] = a * E3 + b * E6 + c * E9
        nm[3, 4] = d * E1 + e * E4 + f * E7
        nm[4, 4] = d * E2 + e * E5 + f * E8
        nm[5, 4] = d * E3 + e * E6 + f * E9
        nm[6, 4] = g * E1 + h * E4 + k * E7
        nm[7, 4] = g * E2 + h * E5 + k * E8
        nm[8, 4] = g * E3 + h * E6 + k * E9
        nm[0, 5] = a * F1 + b * F4 + c * F7
        nm[1, 5] = a * F2 + b * F5 + c * F8
        nm[2, 5] = a * F3 + b * F6 + c * F9
        nm[3, 5] = d * F1 + e * F4 + f * F7
        nm[4, 5] = d * F2 + e * F5 + f * F8
        nm[5, 5] = d * F3 + e * F6 + f * F9
        nm[6, 5] = g * F1 + h * F4 + k * F7
        nm[7, 5] = g * F2 + h * F5 + k * F8
        nm[8, 5] = g * F3 + h * F6 + k * F9
        # Third 9x3
        nm[0, 6] = a * G1 + b * G4 + c * G7
        nm[1, 6] = a * G2 + b * G5 + c * G8
        nm[2, 6] = a * G3 + b * G6 + c * G9
        nm[3, 6] = d * G1 + e * G4 + f * G7
        nm[4, 6] = d * G2 + e * G5 + f * G8
        nm[5, 6] = d * G3 + e * G6 + f * G9
        nm[6, 6] = g * G1 + h * G4 + k * G7
        nm[7, 6] = g * G2 + h * G5 + k * G8
        nm[8, 6] = g * G3 + h * G6 + k * G9
        nm[0, 7] = a * H1 + b * H4 + c * H7
        nm[1, 7] = a * H2 + b * H5 + c * H8
        nm[2, 7] = a * H3 + b * H6 + c * H9
        nm[3, 7] = d * H1 + e * H4 + f * H7
        nm[4, 7] = d * H2 + e * H5 + f * H8
        nm[5, 7] = d * H3 + e * H6 + f * H9
        nm[6, 7] = g * H1 + h * H4 + k * H7
        nm[7, 7] = g * H2 + h * H5 + k * H8
        nm[8, 7] = g * H3 + h * H6 + k * H9
        nm[0, 8] = a * I1 + b * I4 + c * I7
        nm[1, 8] = a * I2 + b * I5 + c * I8
        nm[2, 8] = a * I3 + b * I6 + c * I9
        nm[3, 8] = d * I1 + e * I4 + f * I7
        nm[4, 8] = d * I2 + e * I5 + f * I8
        nm[5, 8] = d * I3 + e * I6 + f * I9
        nm[6, 8] = g * I1 + h * I4 + k * I7
        nm[7, 8] = g * I2 + h * I5 + k * I8
        nm[8, 8] = g * I3 + h * I6 + k * I9
        return nm

    def bTS(self, bm, sm):
        # new matrix is 9 by 3
        a, b, c, d, e, f, g, h, k = sm[0, 0], sm[0, 1], sm[0, 2], sm[1, 0], sm[1, 1], sm[1, 2], sm[2, 0], sm[2, 1], sm[
            2, 2]
        A1, A2, A3, D1, D2, D3, G1, G2, G3 = bm[0, 0], bm[1, 0], bm[2, 0], bm[3, 0], bm[4, 0], bm[5, 0], bm[6, 0], bm[
            7, 0], bm[8, 0]
        B1, B2, B3, E1, E2, E3, H1, H2, H3 = bm[0, 1], bm[1, 1], bm[2, 1], bm[3, 1], bm[4, 1], bm[5, 1], bm[6, 1], bm[
            7, 1], bm[8, 1]
        C1, C2, C3, F1, F2, F3, K1, K2, K3 = bm[0, 2], bm[1, 2], bm[2, 2], bm[3, 2], bm[4, 2], bm[5, 2], bm[6, 2], bm[
            7, 2], bm[8, 2]
        nm = zeros(9, 3)
        nm[0, 0] = a * A1 + d * A2 + g * A3
        nm[1, 0] = b * A1 + e * A2 + h * A3
        nm[2, 0] = c * A1 + f * A2 + k * A3
        nm[3, 0] = a * D1 + d * D2 + g * D3
        nm[4, 0] = b * D1 + e * D2 + h * D3
        nm[5, 0] = c * D1 + f * D2 + k * D3
        nm[6, 0] = a * G1 + d * G2 + g * G3
        nm[7, 0] = b * G1 + e * G2 + h * G3
        nm[8, 0] = c * G1 + f * G2 + k * G3
        nm[0, 1] = a * B1 + d * B2 + g * B3
        nm[1, 1] = b * B1 + e * B2 + h * B3
        nm[2, 1] = c * B1 + f * B2 + k * B3
        nm[3, 1] = a * E1 + d * E2 + g * E3
        nm[4, 1] = b * E1 + e * E2 + h * E3
        nm[5, 1] = c * E1 + f * E2 + k * E3
        nm[6, 1] = a * H1 + d * H2 + g * H3
        nm[7, 1] = b * H1 + e * H2 + h * H3
        nm[8, 1] = c * H1 + f * H2 + k * H3
        nm[0, 2] = a * C1 + d * C2 + g * C3
        nm[1, 2] = b * C1 + e * C2 + h * C3
        nm[2, 2] = c * C1 + f * C2 + k * C3
        nm[3, 2] = a * F1 + d * F2 + g * F3
        nm[4, 2] = b * F1 + e * F2 + h * F3
        nm[5, 2] = c * F1 + f * F2 + k * F3
        nm[6, 2] = a * K1 + d * K2 + g * K3
        nm[7, 2] = b * K1 + e * K2 + h * K3
        nm[8, 2] = c * K1 + f * K2 + k * K3
        return nm

    def bTS_quad(self, bm, sm):
        # new matrix is 9 by 3
        a, b, c, d, e, f, g, h, k = sm[0, 0], sm[0, 1], sm[0, 2], sm[1, 0], sm[1, 1], sm[1, 2], sm[2, 0], sm[2, 1], sm[
            2, 2]
        A1, A2, A3, A4, A5, A6, A7, A8, A9 = bm[0, 0], bm[1, 0], bm[2, 0], bm[3, 0], bm[4, 0], bm[5, 0], bm[6, 0], bm[
            7, 0], bm[8, 0]
        B1, B2, B3, B4, B5, B6, B7, B8, B9 = bm[0, 1], bm[1, 1], bm[2, 1], bm[3, 1], bm[4, 1], bm[5, 1], bm[6, 1], bm[
            7, 1], bm[8, 1]
        C1, C2, C3, C4, C5, C6, C7, C8, C9 = bm[0, 2], bm[1, 2], bm[2, 2], bm[3, 2], bm[4, 2], bm[5, 2], bm[6, 2], bm[
            7, 2], bm[8, 2]
        D1, D2, D3, D4, D5, D6, D7, D8, D9 = bm[0, 3], bm[1, 3], bm[2, 3], bm[3, 3], bm[4, 3], bm[5, 3], bm[6, 3], bm[
            7, 3], bm[8, 3]
        E1, E2, E3, E4, E5, E6, E7, E8, E9 = bm[0, 4], bm[1, 4], bm[2, 4], bm[3, 4], bm[4, 4], bm[5, 4], bm[6, 4], bm[
            7, 4], bm[8, 4]
        F1, F2, F3, F4, F5, F6, F7, F8, F9 = bm[0, 5], bm[1, 5], bm[2, 5], bm[3, 5], bm[4, 5], bm[5, 5], bm[6, 5], bm[
            7, 5], bm[8, 5]
        G1, G2, G3, G4, G5, G6, G7, G8, G9 = bm[0, 6], bm[1, 6], bm[2, 6], bm[3, 6], bm[4, 6], bm[5, 6], bm[6, 6], bm[
            7, 6], bm[8, 6]
        H1, H2, H3, H4, H5, H6, H7, H8, H9 = bm[0, 7], bm[1, 7], bm[2, 7], bm[3, 7], bm[4, 7], bm[5, 7], bm[6, 7], bm[
            7, 7], bm[8, 7]
        I1, I2, I3, I4, I5, I6, I7, I8, I9 = bm[0, 8], bm[1, 8], bm[2, 8], bm[3, 8], bm[4, 8], bm[5, 8], bm[6, 8], bm[
            7, 8], bm[8, 8]
        nm = zeros(9, 9)
        nm[0, 0] = a * A1 + d * B1 + g * C1
        nm[1, 0] = a * A2 + d * B2 + g * C2
        nm[2, 0] = a * A3 + d * B3 + g * C3
        nm[3, 0] = a * A4 + d * B4 + g * C4
        nm[4, 0] = a * A5 + d * B5 + g * C5
        nm[5, 0] = a * A6 + d * B6 + g * C6
        nm[6, 0] = a * A7 + d * B7 + g * C7
        nm[7, 0] = a * A8 + d * B8 + g * C8
        nm[8, 0] = a * A9 + d * B9 + g * C9

        nm[0, 1] = b * A1 + e * B1 + h * C1
        nm[1, 1] = b * A2 + e * B2 + h * C2
        nm[2, 1] = b * A3 + e * B3 + h * C3
        nm[3, 1] = b * A4 + e * B4 + h * C4
        nm[4, 1] = b * A5 + e * B5 + h * C5
        nm[5, 1] = b * A6 + e * B6 + h * C6
        nm[6, 1] = b * A7 + e * B7 + h * C7
        nm[7, 1] = b * A8 + e * B8 + h * C8
        nm[8, 1] = b * A9 + e * B9 + h * C9

        nm[0, 2] = c * A1 + f * B1 + k * C1
        nm[1, 2] = c * A2 + f * B2 + k * C2
        nm[2, 2] = c * A3 + f * B3 + k * C3
        nm[3, 2] = c * A4 + f * B4 + k * C4
        nm[4, 2] = c * A5 + f * B5 + k * C5
        nm[5, 2] = c * A6 + f * B6 + k * C6
        nm[6, 2] = c * A7 + f * B7 + k * C7
        nm[7, 2] = c * A8 + f * B8 + k * C8
        nm[8, 2] = c * A9 + f * B9 + k * C9

        nm[0, 3] = a * D1 + d * E1 + g * F1
        nm[1, 3] = a * D2 + d * E2 + g * F2
        nm[2, 3] = a * D3 + d * E3 + g * F3
        nm[3, 3] = a * D4 + d * E4 + g * F4
        nm[4, 3] = a * D5 + d * E5 + g * F5
        nm[5, 3] = a * D6 + d * E6 + g * F6
        nm[6, 3] = a * D7 + d * E7 + g * F7
        nm[7, 3] = a * D8 + d * E8 + g * F8
        nm[8, 3] = a * D9 + d * E9 + g * F9

        nm[0, 4] = b * D1 + e * E1 + h * F1
        nm[1, 4] = b * D2 + e * E2 + h * F2
        nm[2, 4] = b * D3 + e * E3 + h * F3
        nm[3, 4] = b * D4 + e * E4 + h * F4
        nm[4, 4] = b * D5 + e * E5 + h * F5
        nm[5, 4] = b * D6 + e * E6 + h * F6
        nm[6, 4] = b * D7 + e * E7 + h * F7
        nm[7, 4] = b * D8 + e * E8 + h * F8
        nm[8, 4] = b * D9 + e * E9 + h * F9

        nm[0, 5] = c * D1 + f * E1 + k * F1
        nm[1, 5] = c * D2 + f * E2 + k * F2
        nm[2, 5] = c * D3 + f * E3 + k * F3
        nm[3, 5] = c * D4 + f * E4 + k * F4
        nm[4, 5] = c * D5 + f * E5 + k * F5
        nm[5, 5] = c * D6 + f * E6 + k * F6
        nm[6, 5] = c * D7 + f * E7 + k * F7
        nm[7, 5] = c * D8 + f * E8 + k * F8
        nm[8, 5] = c * D9 + f * E9 + k * F9

        nm[0, 6] = a * G1 + d * H1 + g * I1
        nm[1, 6] = a * G2 + d * H2 + g * I2
        nm[2, 6] = a * G3 + d * H3 + g * I3
        nm[3, 6] = a * G4 + d * H4 + g * I4
        nm[4, 6] = a * G5 + d * H5 + g * I5
        nm[5, 6] = a * G6 + d * H6 + g * I6
        nm[6, 6] = a * G7 + d * H7 + g * I7
        nm[7, 6] = a * G8 + d * H8 + g * I8
        nm[8, 6] = a * G9 + d * H9 + g * I9

        nm[0, 7] = b * G1 + e * H1 + h * I1
        nm[1, 7] = b * G2 + e * H2 + h * I2
        nm[2, 7] = b * G3 + e * H3 + h * I3
        nm[3, 7] = b * G4 + e * H4 + h * I4
        nm[4, 7] = b * G5 + e * H5 + h * I5
        nm[5, 7] = b * G6 + e * H6 + h * I6
        nm[6, 7] = b * G7 + e * H7 + h * I7
        nm[7, 7] = b * G8 + e * H8 + h * I8
        nm[8, 7] = b * G9 + e * H9 + h * I9

        nm[0, 8] = c * G1 + f * H1 + k * I1
        nm[1, 8] = c * G2 + f * H2 + k * I2
        nm[2, 8] = c * G3 + f * H3 + k * I3
        nm[3, 8] = c * G4 + f * H4 + k * I4
        nm[4, 8] = c * G5 + f * H5 + k * I5
        nm[5, 8] = c * G6 + f * H6 + k * I6
        nm[6, 8] = c * G7 + f * H7 + k * I7
        nm[7, 8] = c * G8 + f * H8 + k * I8
        nm[8, 8] = c * G9 + f * H9 + k * I9
        return nm

    def getList_ss(self):
        # find the corresponding variable in the expression and return a list containing all the appeared elements
        lst = [theta, phi, xxx, xxy, xxz, xyx, xyy, xyz, xzx, xzy, xzz, yxx, yxy, yxz, yyx, yyy, yyz, yzx, yzy,
               yzz, zxx, zxy, zxz, zyx, zyy, zyz, zzx, zzy, zzz]
        new_lst_ss = []
        for e in lst:
            if str(e) in str(self.exprss):
                new_lst_ss.append(e)
        return new_lst_ss

    def getList_ss_eQ(self):
        lst = [theta, phi, xxxx, xxxy, xxxz, xyxx, xyxy, xyxz, xzxx, xzxy, xzxz, xxyx, xxyy, xxyz, xyyx, xyyy, xyyz,
               xzyx, xzyy, xzyz, xxzx, xxzy, xxzz, xyzx, xyzy, xyzz,
               xzzx, xzzy, xzzz, yxxx, yxxy, yxxz, yyxx, yyxy, yyxz, yzxx, yzxy, yzxz, yxyx, yxyy, yxyz, yyyx, yyyy,
               yyyz, yzyx, yzyy, yzyz, yxzx, yxzy, yxzz,
               yyzx, yyzy, yyzz, yzzx, yzzy, yzzz, zxxx, zxxy, zxxz, zyxx, zyxy, zyxz, zzxx, zzxy, zzxz, zxyx, zxyy,
               zxyz, zyyx, zyyy, zyyz, zzyx, zzyy, zzyz,
               zxzx, zxzy, zxzz, zyzx, zyzy, zyzz, zzzx, zzzy, zzzz]
        new_lst_ss = []
        for e in lst:
            if str(e) in str(self.exprss):
                new_lst_ss.append(e)
        return new_lst_ss

    def getList_ss_Md(self):
        # find the corresponding variable in the expression and return a list containing all the appeared elements
        lst = [theta, phi, xxx, xxy, xxz, xyx, xyy, xyz, xzx, xzy, xzz, yxx, yxy, yxz, yyx, yyy, yyz, yzx, yzy,
               yzz, zxx, zxy, zxz, zyx, zyy, zyz, zzx, zzy, zzz]
        new_lst_ss = []
        for e in lst:
            if str(e) in str(self.exprss):
                new_lst_ss.append(e)
        return new_lst_ss

    def getList_sp(self):
        # find the corresponding variable in the expression and return a list containing all the appeared elements
        lst = [theta, phi, xxx, xxy, xxz, xyx, xyy, xyz, xzx, xzy, xzz, yxx, yxy, yxz, yyx, yyy, yyz, yzx, yzy,
               yzz, zxx, zxy, zxz, zyx, zyy, zyz, zzx, zzy, zzz]
        new_lst_sp = []
        for e in lst:
            if str(e) in str(self.exprsp):
                new_lst_sp.append(e)
        return new_lst_sp

    def getList_sp_Md(self):
        # find the corresponding variable in the expression and return a list containing all the appeared elements
        lst = [theta, phi, xxx, xxy, xxz, xyx, xyy, xyz, xzx, xzy, xzz, yxx, yxy, yxz, yyx, yyy, yyz, yzx, yzy,
               yzz, zxx, zxy, zxz, zyx, zyy, zyz, zzx, zzy, zzz]
        new_lst_sp = []
        for e in lst:
            if str(e) in str(self.exprsp):
                new_lst_sp.append(e)
        return new_lst_sp

    def getList_sp_eQ(self):
        lst = [theta, phi, xxxx, xxxy, xxxz, xyxx, xyxy, xyxz, xzxx, xzxy, xzxz, xxyx, xxyy, xxyz, xyyx, xyyy, xyyz,
               xzyx, xzyy, xzyz, xxzx, xxzy, xxzz, xyzx, xyzy, xyzz,
               xzzx, xzzy, xzzz, yxxx, yxxy, yxxz, yyxx, yyxy, yyxz, yzxx, yzxy, yzxz, yxyx, yxyy, yxyz, yyyx, yyyy,
               yyyz, yzyx, yzyy, yzyz, yxzx, yxzy, yxzz,
               yyzx, yyzy, yyzz, yzzx, yzzy, yzzz, zxxx, zxxy, zxxz, zyxx, zyxy, zyxz, zzxx, zzxy, zzxz, zxyx, zxyy,
               zxyz, zyyx, zyyy, zyyz, zzyx, zzyy, zzyz,
               zxzx, zxzy, zxzz, zyzx, zyzy, zyzz, zzzx, zzzy, zzzz]
        new_lst_sp = []
        for e in lst:
            if str(e) in str(self.exprsp):
                new_lst_sp.append(e)
        return new_lst_sp

    def getList_pp(self):
        # find the corresponding variable in the expression and return a list containing all the appeared elements
        lst = [theta, phi, xxx, xxy, xxz, xyx, xyy, xyz, xzx, xzy, xzz, yxx, yxy, yxz, yyx, yyy, yyz, yzx, yzy,
               yzz, zxx, zxy, zxz, zyx, zyy, zyz, zzx, zzy, zzz]
        new_lst_pp = []
        for e in lst:
            if str(e) in str(self.exprpp):
                new_lst_pp.append(e)
        return new_lst_pp

    def getList_pp_Md(self):
        # find the corresponding variable in the expression and return a list containing all the appeared elements
        lst = [theta, phi, xxx, xxy, xxz, xyx, xyy, xyz, xzx, xzy, xzz, yxx, yxy, yxz, yyx, yyy, yyz, yzx, yzy,
               yzz, zxx, zxy, zxz, zyx, zyy, zyz, zzx, zzy, zzz]
        new_lst_pp = []
        for e in lst:
            if str(e) in str(self.exprpp):
                new_lst_pp.append(e)
        return new_lst_pp

    def getList_pp_eQ(self):
        # find the corresponding variable in the expression and return a list containing all the appeared elements
        lst = [theta, phi, xxxx, xxxy, xxxz, xyxx, xyxy, xyxz, xzxx, xzxy, xzxz, xxyx, xxyy, xxyz, xyyx, xyyy, xyyz,
               xzyx, xzyy, xzyz, xxzx, xxzy, xxzz, xyzx, xyzy, xyzz,
               xzzx, xzzy, xzzz, yxxx, yxxy, yxxz, yyxx, yyxy, yyxz, yzxx, yzxy, yzxz, yxyx, yxyy, yxyz, yyyx, yyyy,
               yyyz, yzyx, yzyy, yzyz, yxzx, yxzy, yxzz,
               yyzx, yyzy, yyzz, yzzx, yzzy, yzzz, zxxx, zxxy, zxxz, zyxx, zyxy, zyxz, zzxx, zzxy, zzxz, zxyx, zxyy,
               zxyz, zyyx, zyyy, zyyz, zzyx, zzyy, zzyz,
               zxzx, zxzy, zxzz, zyzx, zyzy, zyzz, zzzx, zzzy, zzzz]
        new_lst_pp = []
        for e in lst:
            if str(e) in str(self.exprpp):
                new_lst_pp.append(e)
        return new_lst_pp

    def getList_ps(self):
        # find the corresponding variable in the expression and return a list containing all the appeared elements
        lst = [theta, phi, xxx, xxy, xxz, xyx, xyy, xyz, xzx, xzy, xzz, yxx, yxy, yxz, yyx, yyy, yyz, yzx, yzy,
               yzz, zxx, zxy, zxz, zyx, zyy, zyz, zzx, zzy, zzz]
        new_lst_ps = []
        for e in lst:
            if str(e) in str(self.exprps):
                new_lst_ps.append(e)
        return new_lst_ps

    def getList_ps_Md(self):
        # find the corresponding variable in the expression and return a list containing all the appeared elements
        lst = [theta, phi, xxx, xxy, xxz, xyx, xyy, xyz, xzx, xzy, xzz, yxx, yxy, yxz, yyx, yyy, yyz, yzx, yzy,
               yzz, zxx, zxy, zxz, zyx, zyy, zyz, zzx, zzy, zzz]
        new_lst_ps = []
        for e in lst:
            if str(e) in str(self.exprps):
                new_lst_ps.append(e)
        return new_lst_ps

    def getList_ps_eQ(self):
        # find the corresponding variable in the expression and return a list containing all the appeared elements
        lst = [theta, phi, xxxx, xxxy, xxxz, xyxx, xyxy, xyxz, xzxx, xzxy, xzxz, xxyx, xxyy, xxyz, xyyx, xyyy, xyyz,
               xzyx, xzyy, xzyz, xxzx, xxzy, xxzz, xyzx, xyzy, xyzz,
               xzzx, xzzy, xzzz, yxxx, yxxy, yxxz, yyxx, yyxy, yyxz, yzxx, yzxy, yzxz, yxyx, yxyy, yxyz, yyyx, yyyy,
               yyyz, yzyx, yzyy, yzyz, yxzx, yxzy, yxzz,
               yyzx, yyzy, yyzz, yzzx, yzzy, yzzz, zxxx, zxxy, zxxz, zyxx, zyxy, zyxz, zzxx, zzxy, zzxz, zxyx, zxyy,
               zxyz, zyyx, zyyy, zyyz, zzyx, zzyy, zzyz,
               zxzx, zxzy, zxzz, zyzx, zyzy, zyzz, zzzx, zzzy, zzzz]
        new_lst_ps = []
        for e in lst:
            if str(e) in str(self.exprps):
                new_lst_ps.append(e)
        return new_lst_ps

    def charTable(self):
        self.chr_data = [
            ['C$_1$', 'E'],
            ['A', '+1']], \
            [['S$_2$','E','i','linear functions, rotations', 'quadratic functions', 'cubic functions'],
             ['A$_g$', '+1', '+1', 'R$_x$, R$_y$, R$_z$', 'x$^2$, y$^2$, z$^2$, xy, xz, yz','-'],
             ['A$_u$','+1','-1','x, y, z','-', 'x$^3$, y$^3$, z$^3$, x$^2$y, x$^2$z, y$^2$x, y$^2$z, z$^2$x, z$^2$y, xyz']],\
            [['C$_2$','E','C$_2$','linear functions, rotations', 'quadratic functions', 'cubic functions'],
             ['A', '+1', '+1', 'z,R$_z$', 'x$^2$,y$^2$,z$^2$,xy', 'z$^3$, xyz, y$^2$z, x$^2$z'],
             ['B','+1','-1','x, y, R$_x$, R$_z$','yz, xz', 'xz$^2$, yz$^2$, x$^2$y, xy$^2$, x$^3$, y$^3$']],\
            [['C$_3$','E','C$_3$','(C$_3$)$^2$','linear functions, rotations', 'quadratic functions', 'cubic functions'],
             ['A', '+1', '+1', '+1','z,R$_z$', 'x$^2$ + y$^2$,z$^2$', 'z$^3$, y(3x$^2$-y$^2$), x(x$^2$-3y$^2$), z(x$^2$+y$^2$)'],
             ['E', '+1', '+$\epsilon$', '+$\epsilon^*$','x+iy; R$_x$+iR$_y$', '(x$^2$-y$^2$,xy)(yz,xz)', '(xz$^2$,'
                                                                                                         'yz$^2$)['
                                                                                                         'xyz, '
                                                                                                         'z('
                                                                                                         'x$^2$-y$^2$'
                                                                                                         ')][x('
                                                                                                         'x$^2$+y$^2$'
                                                                                                         '), '
                                                                                                         'y('
                                                                                                         'x$^2$+y$^2$)]'],
             ['E', '+1', '+$\epsilon^*$', '+$\epsilon$', 'x-iy; R$_x$-iR$_y$', '(x$^2$-y$^2$,xy)(yz,xz)', '(xz$^2$,'
                                                                                                          'yz$^2$)['
                                                                                                          'xyz, '
                                                                                                          'z('
                                                                                                          'x$^2$-y$^2$'
                                                                                                          ')][x('
                                                                                                          'x$^2$+y$^2$'
                                                                                                          '), '
                                                                                                          'y('
                                                                                                          'x$^2$+y$^2$)]']
             ],\
            [['C$_{2h}$','E','C$_2$(z)','i','$\sigma_h$','linear functions, rotations', 'quadratic functions', 'cubic functions'],
             ['A$_g$', '+1', '+1', '+1', '+1', 'R$_z$', 'x$^2$, y$^2$, z$^2$,xy','-'],
             ['B$_g$', '+1', '-1','+1','-1','R$_x$,R$_y$','xz,yz','-'],
             ['A$_u$', '+1', '+1','-1','-1','z','-','z$^3$,xyz,x$^2$z,y$^2$z'],
             ['B$_u$', '+1', '-1','-1','+1','x,y','-','xz$^2$,yz$^2$,x$^2$y,xy$^2$,x$^3$,y$^3$']],\
            [['D$_2$','E','C$_2$(z)','C$_2$(y)','C$_2$(x)','linear functions, rotations', 'quadratic functions', 'cubic functions'],
             ['A', '+1', '+1', '+1', '+1', '-', 'x$^2$, y$^2$, z$^2$','xyz'],
             ['B$_1$', '+1', '+1', '-1', '-1', 'z, R$_z$', 'xy','z$^3$, y$^2$z, x$^2$z'],
             ['B$_2$', '+1', '-1', '+1', '-1', 'y, R$_y$', 'xz','y$^3$, yz$^2$, x$^2$y'],
             ['B$_3$', '+1', '-1', '-1', '+1', 'x, R$_x$', 'yz','x$^3$, xz$^2$, xy$^2$']],\
            [['C$_{2v}$','E','C$_2$(z)','$\sigma_v$(xz)','$\sigma_v$(yz)','linear functions, rotations', 'quadratic functions', 'cubic functions'],
             ['A$_1$', '+1', '+1', '+1', '+1', 'z', 'x$^2$, y$^2$, z$^2$','z$^3$,x$^2$z,y$^2$z'],
             ['A$_2$', '+1', '+1', '-1', '-1', 'R$_z$', 'xy','xyz'],
             ['B$_1$', '+1', '-1', '+1', '-1', 'x,R$_y$', 'xz','xz$^2$,x$^3$,xy$^2$'],
             ['B$_2$', '+1', '-1', '-1', '+1', 'y,R$_x$', 'yz','yz$^2$,y$^3$,x$^2$y']],\
            [['D$_{2h}$','E','C$_2$(z)','C$_2$(y)','C$_2$(x)','i','$\sigma$(xy)','$\sigma$(xz)','$\sigma$(yz)','linear functions, rotations', 'quadratic functions', 'cubic functions'],
             ['A$_g$', '+1', '+1', '+1', '+1', '+1', '+1', '+1', '+1', '-', 'x$^2$, y$^2$, z$^2$','-'],
             ['B$_{1g}$', '+1', '+1', '-1', '-1', '+1', '+1', '-1', '-1', 'R$_z$', 'xy', '-'],
             ['B$_{2g}$', '+1', '-1', '+1', '-1', '+1', '-1', '+1', '-1', 'R$_y$', 'xz','-'],
             ['B$_{3g}$', '+1', '-1', '-1', '+1', '+1', '-1', '-1', '+1', 'R$_x$', 'yz','-'],
             ['A$_u$', '+1', '+1', '+1', '+1', '-1', '-1', '-1', '-1', '-', '-','xyz'],
             ['B$_{1u}$', '+1', '+1', '-1', '-1', '-1', '-1', '+1', '+1', 'z', '-','z$^3$,y$^2$z,x$^2$z'],
             ['B$_{2u}$', '+1', '-1', '+1', '-1', '-1', '+1', '-1', '+1', 'y', '-','yz$^2$,y$^3$,x$^2$y'],
             ['B$_{3u}$', '+1', '-1', '-1', '+1', '-1', '+1', '+1', '-1', 'x', '-','xz$^2$,xy$^2$,x$^3$']],\
            [['C$_4$','E','C$_4$','C$_2$','(C$_4$)$^3$','linear functions, rotations', 'quadratic functions', 'cubic functions'],
             ['A', '+1', '+1', '+1','+1','z,R$_z$', 'x$^2$ + y$^2$,z$^2$', 'z$^3$, z(x$^2$+y$^2$)'],
             ['B', '+1', '-1', '+1','-1','-', 'x$^2$ - y$^2$,xy', 'xyz,z(x$^2$-y$^2$)'],
             ['E', '+1', '+i', '-1','-i','x+iy; R$_x$+iR$_y$', '(yz,xz)', '(xz$^2$,yz$^2$)(xy$^2$,x$^2$y)(x$^3$,y$^3$)'],
             ['E', '+1', '-i', '-1','+i','x-iy; R$_x$-iR$_y$', '(yz,xz)', '(xz$^2$,yz$^2$)(xy$^2$,x$^2$y)(x$^3$,y$^3$)']],\
            [['S$_4$','E','S$_4$','C$_2$','(S$_4$)$^3$','linear functions, rotations', 'quadratic functions', 'cubic functions'],
             ['A', '+1', '+1', '+1','+1','R$_z$', 'x$^2$ + y$^2$,z$^2$', 'xyz,z(x$^2$-y$^2$)'],
             ['B', '+1', '-1', '+1','-1','z', 'x$^2$ - y$^2$,xy', 'z$^3$,z(x$^2$+y$^2$)'],
             ['E', '+1', '+i', '-1','-i','x+iy; R$_x$+iR$_y$', '(xz,yz)', '(xz$^2$,yz$^2$)(xy$^2$,x$^2$y)(x$^3$,y$^3$)'],
             ['E', '+1', '-i', '-1','+i','x-iy; R$_x$-iR$_y$', '(xz,yz)', '(xz$^2$,yz$^2$)(xy$^2$,x$^2$y)(x$^3$,y$^3$)']],\
            [['C$_{4h}$','E','C$_4$(z)','C$_2$','(C$_4$)$^3$','i','(S$_4$)$^3$','$\sigma_h$','S$_4$','linear functions, rotations', 'quadratic functions', 'cubic functions'],
             ['A$_g$', '+1', '+1', '+1', '+1', '+1', '+1', '+1', '+1', 'R$_z$', 'x$^2$+y$^2$, z$^2$','-'],
             ['B$_g$', '+1', '-1', '+1', '-1', '+1', '-1', '+1', '-1', '-', 'xy,x$^2$-y$^2$', '-'],
             ['E$_g$', '+1', '+i', '-1', '-i', '+1', '+i', '-1', '-i', 'R$_x$ +iR$_y$', '(xz,yz)','-'],
             ['E$_g$', '+1', '-i', '-1', '+i', '+1', '-i', '-1', '+i', 'R$_x$ -iR$_y$', '(xz,yz)', '-'],
             ['A$_u$', '+1', '+1', '+1', '+1', '-1', '-1', '-1', '-1', 'z', '-','z$^3$,z(x$^2$+y$^2$)'],
             ['B$_u$', '+1', '-1', '+1', '-1', '-1', '+1', '-1', '+1', '-', '-','xyz, z(x$^2$-y$^2$)'],
             ['E$_u$', '+1', '+i', '-1', '-i', '-1', '-i', '+1', '+i', 'x+iy', '-','(xz$^2$,yz$^2$)(xy$^2$,x$^2$y)(x$^3$,y$^3$)'],
             ['E$_u$', '+1', '-i', '-1', '+i', '-1', '+i', '+1', '-i', 'x-iy', '-','(xz$^2$,yz$^2$)(xy$^2$,x$^2$y)(x$^3$,y$^3$)']],\
            [['D$_4$','E','2C$_4$(z)','C$_2$(z)','2C$^\prime$$_2$','2C$^{\prime\prime}$$_2$','linear functions, rotations', 'quadratic functions', 'cubic functions'],
             ['A$_1$', '+1', '+1', '+1', '+1','+1', '-', 'x$^2$+y$^2$, z$^2$', '-'],
             ['A$_2$', '+1', '+1', '+1', '-1', '-1','z,R$_z$', '-', 'z$^3$, z(x$^2$+y$^2$)'],
             ['B$_1$', '+1', '-1', '+1', '+1','-1', '-', 'x$^2$-y$^2$', 'xyz'],
             ['B$_2$', '+1', '-1', '+1', '-1','+1', '-', 'xy', 'z(x$^2$-y$^2$)'],
             ['E', '+2', '0', '-2', '0','0', '(x, y)(R$_x$,R$_y$)', '(xz,yz)', '(xz$^2$, yz$^2$)(xy$^2$,x$^2$y)(x$^3$,y$^3$)']],\
            [['C$_{4v}$','E','2C$_4$(z)','C$_2$','2$\sigma_v$','2$\sigma_d$','linear functions, rotations', 'quadratic functions', 'cubic functions'],
             ['A$_1$', '+1', '+1', '+1', '+1','+1', 'z', 'x$^2$+y$^2$, z$^2$', 'z$^3$, z(x$^2$+y$^2$)'],
             ['A$_2$', '+1', '+1', '+1', '-1', '-1','R$_z$', '-', '-'],
             ['B$_1$', '+1', '-1', '+1', '+1','-1', '-', 'x$^2$-y$^2$', 'z(x$^2$-y$^2$)'],
             ['B$_2$', '+1', '-1', '+1', '-1','+1', '-', 'xy', 'xyz'],
             ['E', '+2', '0', '-2', '0','0', '(x, y)(R$_x$,R$_y$)', '(xz,yz)', '(xz$^2$, yz$^2$)(xy$^2$,x$^2$y)(x$^3$,y$^3$)']],\
            [['D$_{2d}$','E','2S$_4$(z)','C$_2$(z)','2C$^\prime_2$','2$\sigma_d$','linear functions, rotations', 'quadratic functions', 'cubic functions'],
             ['A$_1$', '+1', '+1', '+1', '+1','+1', '-', 'x$^2$+y$^2$, z$^2$', 'xyz'],
             ['A$_2$', '+1', '+1', '+1', '-1', '-1', 'R$_z$', '-', 'z(x$^2$-y$^2$)'],
             ['B$_1$', '+1', '-1', '+1', '+1','-1', '-', 'x$^2$-y$^2$', '-'],
             ['B$_2$', '+1', '-1', '+1', '-1','+1', 'z', 'xy', 'z$^3$, z(x$^2$+y$^2$)'],
             ['E', '+2', '0', '-2', '0','0', '(x, y)(R$_x$,R$_y$)', '(xz,yz)', '(xz$^2$, yz$^2$)(xy$^2$,x$^2$y)(x$^3$,y$^3$)']],\
            [['D$_{4h}$','E','2C$_4$(z)','C$_2$','2C$^\prime$$_2$','2C$^{\prime\prime}$$_2$','i','2S$_4$','$\sigma_h$','2$\sigma_v$','2$\sigma_d$','linear functions, rotations', 'quadratic functions', 'cubic functions'],
             ['A$_{1g}$', '+1', '+1', '+1', '+1', '+1', '+1', '+1', '+1', '+1', '+1', '-', 'x$^2$+y$^2$, z$^2$','-'],
             ['A$_{2g}$', '+1', '+1', '+1', '-1', '-1', '+1', '+1', '+1', '-1', '-1', 'R$_z$', '-', '-'],
             ['B$_{1g}$', '+1', '-1', '+1', '+1', '-1', '+1', '-1', '+1', '+1', '-1', '-', 'x$^2$-y$^2$','-'],
             ['B$_{2g}$', '+1', '-1', '+1', '-1', '+1', '+1', '-1', '+1', '-1', '+1', '-', 'xy', '-'],
             ['E$_g$', '+2', '0', '-2', '0', '0', '+2', '0', '-2', '0', '0', '(R$_x$,R$_y$)', '(xy,yz)','-'],
             ['A$_{1u}$', '+1', '+1', '+1', '+1', '+1', '-1', '-1', '-1', '-1', '-1', '-', '-','-'],
             ['A$_{2u}$', '+1', '+1', '+1', '-1', '-1', '-1', '-1', '-1', '+1', '+1', 'z', '-','z$^3$,z(x$^2$+y$^2$)'],
             ['B$_{1u}$', '+1', '-1', '+1', '+1', '-1', '-1', '+1', '-1', '-1', '+1', '-', '-', 'xyz'],
             ['B$_{2u}$', '+1', '-1', '+1', '-1', '+1', '-1', '+1', '-1', '+1', '-1', '-', '-', 'z(x$^2$-y$^2$)'],
             ['E$_u$', '+2', '0', '-2', '0', '0', '-2', '0', '+2', '0', '0','(x,y)','-','(xz$^2$,yz$^2$)(xy$^2$,x$^2$y)(x$^3$,y$^3$)']],\
            [['C$_3$','E','C$_3$','(C$_3$)$^2$','linear functions, rotations', 'quadratic functions', 'cubic functions'],
             ['A', '+1', '+1', '+1','z,R$_z$', 'x$^2$ + y$^2$,z$^2$', 'z$^3$,y(3x$^2$-y$^2$),x(x$^2$-3y$^2$),z(x$^2$+y$^2$)'],
             ['E', '+1', '+$\epsilon$', '+$\epsilon^*$', 'x+iy; R$_x$+iR$_y$', '(x$^2$-y$^2$,xy)(yz,xz)', '(xz$^2$,'
                                                                                                          'yz$^2$)['
                                                                                                          'xyz, '
                                                                                                          'z('
                                                                                                          'x$^2$-y$^2$'
                                                                                                          ')][x('
                                                                                                          'x$^2$+y$^2$'
                                                                                                          '), '
                                                                                                          'y('
                                                                                                          'x$^2$+y$^2$)]'],
             ['E', '+1', '+$\epsilon^*$', '+$\epsilon$', 'x-iy; R$_x$-iR$_y$', '(x$^2$-y$^2$,xy)(yz,xz)', '(xz$^2$,'
                                                                                                          'yz$^2$)['
                                                                                                          'xyz, '
                                                                                                          'z('
                                                                                                          'x$^2$-y$^2$'
                                                                                                          ')][x('
                                                                                                          'x$^2$+y$^2$'
                                                                                                          '), '
                                                                                                          'y('
                                                                                                          'x$^2$+y$^2$)]']],\
            [['S$_6$','E','C$_3$(z)','(C$_3$)$^2$','i','(S$_6$)$^2$', 'S$_6$', 'linear functions, rotations', 'quadratic functions', 'cubic functions'],
             ['A$_{g}$', '+1', '+1', '+1', '+1', '+1', '+1', 'R$_2$', 'x$^2$+y$^2$,z$^2$', '-'],
             ['E$_g$', '+1', '+$\epsilon$', '+$\epsilon^*$', '+1', '+$\epsilon$', '+$\epsilon^*$', 'R$_x$+iR$_y$', '(x$^2$-y$^2$,xy)(xz,yz)','-'],
             ['E$_g$', '+1', '+$\epsilon^*$', '+$\epsilon$', '+1', '+$\epsilon^*$', '+$\epsilon$', 'R$_x$-iR$_y$', '(x$^2$-y$^2$,xy)(xz,yz)','-'],
             ['A$_{u}$', '+1', '+1', '+1', '-1', '-1', '-1', 'z', '-', 'z$^3$,y(3x$^2$-y$^2$),x(x$^2$-3y$^2$),z(x$^2$+y$^2$)'],
             ['E$_u$', '+1', '+$\epsilon$', '+$\epsilon^*$', '-1', '-$\epsilon$', '-$\epsilon^*$', 'x+iy', '-',
              '(xz$^2$,yz$^2$)[xyz,z(x$^2$-y$^2$)][x(x$^2$+y$^2$),y(x$^2$+y$^2$)]'],
             ['E$_u$', '+1', '+$\epsilon^*$', '+$\epsilon$', '-1', '-$\epsilon^*$', '-$\epsilon$', 'x-iy', '-',
              '(xz$^2$,yz$^2$)[xyz,z(x$^2$-y$^2$)][x(x$^2$+y$^2$),y(x$^2$+y$^2$)]']],\
            [['D$_3$','E','2C$_3$(z)','3C$^{\prime\prime}$$_v$','linear functions, rotations', 'quadratic functions', 'cubic functions'],
             ['A$_1$', '+1', '+1', '+1', '-','x$^2$+y$^2$, z$^2$', 'x(x$^2$-3y$^2$)'],
             ['A$_2$', '+1', '+1', '-1', 'z,R$_z$','-', 'z$^3$,y(3x$^2$-y$^2$),z(x$^2$+y$^2$)'],
             ['E', '+2', '-1', '0', '(x, y)(R$_x$,R$_y$)', '(x$^2$-y$^2$,xy)(xz,yz)', '(xz$^2$, yz$^2$)[xyz,z(x$^2$-y$^2$)][x(x$^2$+y$^2$),y(x$^2$+y$^2$)]']],\
            [['C$_{3v}$','E','2C$_3$(z)','3$\sigma_v$','linear functions, rotations', 'quadratic functions', 'cubic functions'],
             ['A$_1$', '+1', '+1', '+1', 'z','x$^2$+y$^2$, z$^2$', 'z$^3$,x(x$^2$-3y$^2$),z(x$^2$+y$^2$)'],
             ['A$_2$', '+1', '+1', '-1', 'R$_z$','-', 'y(3x$^2$-y$^2$)'],
             ['E', '+2', '-1', '0', '(x, y)(R$_x$,R$_y$)', '(x$^2$-y$^2$,xy)(xz,yz)', '(xz$^2$, yz$^2$)[xyz,z(x$^2$-y$^2$)][x(x$^2$+y$^2$),y(x$^2$+y$^2$)]']],\
            [['D$_{3d}$','E','2C$_3$','3C$^\prime$$_2$','i','2S$_6$','3$\sigma_d$','linear functions, rotations', 'quadratic functions', 'cubic functions'],
             ['A$_{1g}$', '+1', '+1', '+1', '+1', '+1', '+1', '-', 'x$^2$+y$^2$, z$^2$','-'],
             ['A$_{2g}$', '+1', '+1', '-1', '+1', '+1', '-1', 'R$_z$', '-', '-'],
             ['E$_g$', '+2', '-1', '0', '+2', '-1', '0', '(R$_x$,R$_y$)', '(x$^2$-y$^2$,xy)(xz,yz)','-'],
             ['A$_{1u}$', '+1', '+1', '+1', '-1', '-1', '-1', '-', '-','x(x$^2$-3$y^2$)'],
             ['A$_{2u}$', '+1', '+1', '-1', '-1', '-1', '+1', 'z', '-','y(3x$^2$-y$^2$), z$^3$,z(x$^2$+y$^2$)'],
             ['E$_u$', '+2', '-1', '0', '-2', '+1', '0','(x,y)','-','(xz$^2$,yz$^2$)[xyz,z(x$^2$-y$^2$)][x(x$^2$+y$^2$),y(x$^2$+y$^2$)']], \
            [['C$_6$','E','C$_6$','C$_3$','C$_2$','(C$_3$)$^2$','(C$_6$)$^5$','linear functions, rotations', 'quadratic functions', 'cubic functions'],
             ['A', '+1', '+1', '+1','+1', '+1','+1','z,R$_z$', 'x$^2$ + y$^2$,z$^2$', 'z$^3$,z(x$^2$+y$^2$)'],
             ['B', '+1', '-1', '+1','-1', '+1','-1','-', '-', 'y(3x$^2$-y$^2$),x(x$^2$-3y$^2$)'],
             ['E$_1$', '+1', '+$\epsilon$', '-$\epsilon^*$', '-1','-$\epsilon$', '+$\epsilon^*$','x+iy; R$_x$+iR$_y$', '(xz,yz)', '(xz$^2$,yz$^2$)[x(x$^2$+y$^2$),y(x$^2$+y$^2$)]'],
             ['E$_1$', '+1', '+$\epsilon^*$', '-$\epsilon$', '-1','-$\epsilon^*$', '+$\epsilon$','x-iy; R$_x$-iR$_y$', '(xz,yz)', '(xz$^2$,yz$^2$)[x(x$^2$+y$^2$),y(x$^2$+y$^2$)]'],
             ['E$_2$', '+1', '-$\epsilon^*$', '-$\epsilon$', '+1', '-$\epsilon^*$', '-$\epsilon$', '-','(x$^2$-y$^2$,xy)', '[xyz,z(x$^2$-y$^2$]'],
             ['E$_2$', '+1', '-$\epsilon$', '-$\epsilon^*$', '+1', '-$\epsilon$', '-$\epsilon^*$', '-','(x$^2$-y$^2$,xy)', '[xyz,z(x$^2$-y$^2$]']], \
            [['C$_{3h}$','E','C$_3$(z)','(C$_3$)$^2$','$\sigma_h$','S$_3$','(S$_3$)$^5$','linear functions, rotations', 'quadratic functions', 'cubic functions'],
             ['A$^\prime$','+1','+1','+1','+1','+1','+1','R$_z$','x$^2$+y$^2$,z$^2$','y(3x$^3$-y$^2$),x(x$^2$-3y$^2$)'],
             ['E$^\prime$', '+1', '+$\epsilon$', '+$\epsilon^*$', '+1', '+$\epsilon$', '+$\epsilon^*$', 'x+iy',
              '(x$^2$-y$^2$,xy)', '(xz$^2$,yz$^2$)[x(x$^2$+y$^2$),y(x$^2$+y$^2$)]'],
             ['E$^\prime$', '+1', '+$\epsilon^*$', '+$\epsilon$', '+1', '+$\epsilon^*$', '+$\epsilon$', 'x-iy',
              '(x$^2$-y$^2$,xy)', '(xz$^2$,yz$^2$)[x(x$^2$+y$^2$),y(x$^2$+y$^2$)]'],
             ['A$^{\prime\prime}$','+1','+1','+1','-1','-1','-1','z','-','zx$^3$,z(x$^2$+y$^2$)'],
             ['E$^{\prime\prime}$', '+1', '+$\epsilon$', '+$\epsilon^*$', '-1', '-$\epsilon$', '-$\epsilon^*$', 'R$_x$+iR$_y$',
              '(xz,yz)', '[xyz,z(x$^2$-y$^2$)]'],
             ['E$^{\prime\prime}$', '+1', '+$\epsilon^*$', '+$\epsilon$', '-1', '-$\epsilon^*$', '-$\epsilon$',
              'R$_x$-iR$_y$',
              '(xz,yz)', '[xyz,z(x$^2$-y$^2$)]'],
             ],\
            [['C$_{6h}$','E','C$_6$(z)','C$_3$','C$_2$','(C$_3$)$^2$','(C$_6$)$^5$','i','(S$_3$)$^5$','(S$_6$)$^5$','$\sigma_h$','S$_6$','S$_3$','linear functions, rotations', 'quadratic functions', 'cubic functions'],
             ['A$_g$', '+1', '+1', '+1', '+1', '+1', '+1', '+1', '+1', '+1', '+1', '+1', '+1', 'R$_z$', 'x$^2$+y$^2$, z$^2$','-'],
             ['B$_g$', '+1', '-1', '+1', '-1', '+1', '-1', '+1', '-1', '+1', '-1', '+1', '-1', '-', '-', '-'],
             ['E$_{1g}$', '+1', '+$\epsilon$', '-$\epsilon^*$', '-1', '-$\epsilon$', '+$\epsilon^*$', '+1',
              '+$\epsilon$', '-$\epsilon^*$', '-1','-$\epsilon$','+$\epsilon^*$', 'R$_x$ +iR$_y$', '(xz,yz)','-'],
             ['E$_{1g}$', '+1', '+$\epsilon^*$', '-$\epsilon$', '-1', '-$\epsilon^*$', '+$\epsilon$', '+1',
              '+$\epsilon^*$', '-$\epsilon$', '-1', '-$\epsilon^*$', '+$\epsilon$', 'R$_x$-iR$_y$', '(xz,yz)', '-'],
             ['E$_{2g}$', '+1', '-$\epsilon^*$', '-$\epsilon$', '+1', '-$\epsilon^*$', '-$\epsilon$', '+1',
              '-$\epsilon^*$', '-$\epsilon$', '+1', '-$\epsilon^*$', '-$\epsilon$', '-', '(x$^2$-y$^2$,xy)', '-'],
             ['E$_{2g}$', '+1', '-$\epsilon$', '-$\epsilon^*$', '+1', '-$\epsilon$', '-$\epsilon^*$', '+1',
              '-$\epsilon$', '-$\epsilon^*$', '+1', '-$\epsilon$', '+$\epsilon^*$', '-', '(x$^2$-y$^2$,xy)', '-'],
             ['A$_u$', '+1', '+1', '+1', '+1', '+1', '+1', '-1', '-1','-1', '-1', '-1', '-1', 'z', '-','z$^3$,z(x$^2$+y$^2$)'],
             ['B$_u$', '+1', '-1', '+1', '-1', '+1','-1','-1', '+1', '-1', '+1', '-1', '+1', '-', '-','y(3x$^2$-y$^2$),x(x$^2$-3y$^2$)'],
             ['E$_{1u}$', '+1', '-$\epsilon^*$', '-$\epsilon$', '+1', '-$\epsilon^*$', '-$\epsilon$', '-1',
              '+$\epsilon^*$', '+$\epsilon$', '-1', '+$\epsilon^*$', '+$\epsilon$', '-', '-','(xz$^2$,yz$^2$)[x(x$^2$+y$^2$),y(x$^2$+y$^2$)]'],
             ['E$_u$',  '+1', '-$\epsilon$', '-$\epsilon^*$', '+1', '-$\epsilon$', '-$\epsilon^*$', '-1',
              '+$\epsilon$', '+$\epsilon^*$', '-1', '+$\epsilon$', '-$\epsilon^*$', '-', '-','[(xyz,z(x$^2$-y$^2$)]']],\
            [['D$_6$','E','2C$_6$(z)','2C$_3$(z)','C$_2$(z)','3C$^{\prime}$$_2$','3C$^{\prime\prime}$$_2$','linear functions, rotations', 'quadratic functions', 'cubic functions'],
             ['A$_1$', '+1', '+1', '+1', '+1', '+1', '+1', '-','x$^2$+y$^2$, z$^2$', '-'],
             ['A$_2$', '+1', '+1', '+1', '+1', '-1', '-1', 'z,R$_z$','-', 'z$^3$,z(x$^2$+y$^2$)'],
             ['B$_1$', '+1', '-1', '+1', '-1', '+1', '-1', '-', '-', 'x(x$^2$-3y$^2$)'],
             ['B$_2$', '+1', '-1', '+1', '-1', '-1', '+1', '-', '-', 'y(3x$^2$-y$^2$)'],
             ['E$_1$', '+2', '+1','-1','-2','0', '0', '(x, y)(R$_x$,R$_y$)', '(xz,yz)', '(xz$^2$, yz$^2$)[x(x$^2$+y$^2$),y(x$^2$+y$^2$)]'],
             ['E$_2$', '+2', '-1','-1','+2','0', '0', '-', '(x$^2$-y$^2$,xy)', '[xyz,z(x$^2$-y$^2$)]']], \
            [['C$_{6v}$','E','2C$_6$(z)','2C$_3$(z)','C$_2$(z)','3$\sigma$$_v$','3$\sigma$$_d$','linear functions, rotations', 'quadratic functions', 'cubic functions'],
             ['A$_1$', '+1', '+1', '+1', '+1', '+1', '+1', 'z','x$^2$+y$^2$, z$^2$', 'z$^3$,z(x$^2$+y$^2$)'],
             ['A$_2$', '+1', '+1', '+1', '+1', '-1', '-1', 'R$_z$','-', '-'],
             ['B$_1$', '+1', '-1', '+1', '-1', '+1', '-1', '-', '-', 'x(x$^2$-3y$^2$)'],
             ['B$_2$', '+1', '-1', '+1', '-1', '-1', '+1', '-', '-', 'y(3x$^2$-y$^2$)'],
             ['E$_1$', '+2', '+1','-1','-2','0', '0', '(x, y)(R$_x$,R$_y$)', '(xz,yz)', '(xz$^2$, yz$^2$)[x(x$^2$+y$^2$),y(x$^2$+y$^2$)]'],
             ['E$_2$', '+2', '-1','-1','+2','0', '0', '-', '(x$^2$-y$^2$,xy)', '[xyz,z(x$^2$-y$^2$)]']], \
            [['D$_{3h}$','E','2C$_3$(z)','3C$^\prime$$2$','$\sigma$$_h$(xy)','2SC$_3$','3$\sigma$$_v$','linear functions, rotations', 'quadratic functions', 'cubic functions'],
             ['A$^\prime$$_1$', '+1', '+1', '+1', '+1', '+1', '+1', '-','x$^2$+y$^2$, z$^2$', 'x(x$^2$-3y$^2$)'],
             ['A$^\prime$$_2$', '+1', '+1', '-1', '+1', '+1', '-1', 'R$_z$','-', 'y(3x$^2$-y$^2$)'],
             ['E$^\prime$', '+2', '-1', '0', '+2', '-1', '0', '(x,y)', '(x$^2$-y$^2$,xy)', '(xz$^2$,yz$^2$)[x(x$^2$+y$^2$),y(x$^2$+y$^2$)]'],
             ['A$^{\prime\prime}$$_1$', '+1', '+1', '+1', '-1', '-1', '-1', '-', '-', '-'],
             ['A$^{\prime\prime}$$_2$', '+1', '+1','-1','-1','-1', '+1', 'z', '-', 'z$^3$,z(x$^2$+y$^2$)'],
             ['E$^{\prime\prime}$', '+2', '-1','0','-2','+1', '0', '(R$_x$,R$_y$)', '(xz,yz)', '[xyz,z(x$^2$-y$^2$)]']], \
            [['D$_{6h}$','E','2C$_6$(z)','2C$_3$','2C$_2$','3C$^\prime$$_2$','3C$^{\prime\prime}$$_2$','i','2S$_3$','2S$_6$','$\sigma_h$(xy)','3$\sigma_d$','3$\sigma_v$','linear functions, rotations', 'quadratic functions', 'cubic functions'],
             ['A$_{1g}$', '+1', '+1', '+1', '+1', '+1', '+1', '+1', '+1', '+1', '+1', '+1', '+1', '', 'x$^2$+y$^2$, z$^2$','-'],
             ['A$_{2g}$', '+1', '+1', '+1', '+1', '-1', '-1', '+1', '+1', '+1', '+1', '-1', '-1', 'R$_z$', '-', '-'],
             ['B$_{1g}$', '+1', '-1', '+1', '-1', '+1', '-1', '+1', '-1', '+1', '-1', '+1', '-1', '-', '-', '-'],
             ['B$_{2g}$', '+1', '-1', '+1', '-1', '-1', '+1', '+1', '-1', '+1', '-1', '-1', '+1', '-', '-', '-'],
             ['E$_{1g}$', '+2', '+1', '-1', '-2', '0', '0', '+2', '+1', '-1', '-2', '0', '0', '(R$_x$,R$_y$)', '(xz,yz)', '-'],
             ['E$_{2g}$', '+2', '-1', '-1', '+2', '0', '0', '+2', '-1', '-1', '+2', '0', '0', '-', '(x$^2$-y$^2$,xy)', '-'],
             ['A$_{1u}$', '+1', '+1', '+1', '+1', '+1', '+1', '-1', '-1', '-1', '-1', '-1', '-1', '-', '-', '-'],
             ['A$_{2u}$', '+1', '+1', '+1', '+1', '-1', '-1', '-1', '-1', '-1', '-1', '+1', '+1', 'z', '-', 'z$^3$,z(x$^2$+y$^2$)'],
             ['B$_{1u}$', '+1', '-1', '+1', '-1', '+1','-1','-1', '+1', '-1', '+1', '-1', '+1', '-', '-','x(x$^2$-3y$^2$)'],
             ['B$_{2u}$', '+1', '-1', '+1', '-1', '-1', '+1', '-1', '+1', '-1', '+1', '+1', '-1', '-', '-',
              'y(3x$^2$-y$^2$)'],
             ['E$_{1u}$', '+2', '+1', '-1', '-2', '0', '0', '-2', '-1', '+1', '+2', '0', '0', '(x,y)', '-', '(xz$^2$,yz$^2$)[x(x$^2$+y$^2$),y(x$^2$+y$^2$)]'],
             ['E$_{2u}$', '+2', '-1', '-1', '+2', '0', '0', '-2', '+1', '+1', '-2', '0', '0', '-', '-', '[xyz,z(x$^2$-y$^2$)]']
             ], \
            [['T','E','4C$_3$','4(C$_3$)$^2$','3C$_2$','linear functions, rotations', 'quadratic functions', 'cubic functions'],
            ['A','+1','+1','+1','+1','-','x$^2$+y$^2$+z$^2$','-'],
            ['E','+1','+$\epsilon$','+$\epsilon$$^*$','+1','-','(x$^2$-y$^2$,2z$^2$-x$^2$-y$^2$)','-'],
            ['E','+1','+$\epsilon$$^*$','+$\epsilon$','+1','-','(x$^2$-y$^2$,2z$^2$-x$^2$-y$^2$)','-'],
            ['T','+3','0','0','-1','(x,y,z)(R$_x$,R$_y$,R$_z$)','(xy,xz,yz)','(x$^3$,y$^3$,z$^3$)(xy$^2$,x$^2$z,yz$^2$)(xz$^2$,x$^2$y,y$^2$z)']],\
            [['T$_h$','E','4C$_3$','4(C$_3$)$^2$','3C$_2$','i','4(S$_6$)$^5$','4S$_6$','3$\sigma$$_h$','linear functions, rotations', 'quadratic functions', 'cubic functions'],
            ['A$_g$','+1','+1','+1','+1','+1','+1','+1','+1','-','x$^2$+y$^2$+z$^2$','-'],
            ['E$_g$','+1', '+$\epsilon$','+$\epsilon$$^*$', '+1','+1', '+$\epsilon$','+$\epsilon$$^*$', '+1','-', '(x$^2$-y$^2$,2z$^2$-x$^2$-y$^2$)', '-'],
            ['E$_g$','+1', '+$\epsilon$$^*$','+$\epsilon$', '+1','+1', '+$\epsilon$$^*$','+$\epsilon$', '+1','-', '(x$^2$-y$^2$,2z$^2$-x$^2$-y$^2$)', '-'],
            ['T$_g$','+3','0','0','-1','+3','0','0','-1','(R$_x$,R$_y$,R$_z$)','(xy,xz,yz)','-'],
            ['A$_u$','+1','+1','+1','+1','-1','-1','-1','-1','-','-','xyz'],
            ['E$_u$','+1', '+$\epsilon$','+$\epsilon$$^*$', '+1', '-1', '-$\epsilon$','-$\epsilon$$^*$', '-1','-','-','-'],
            ['E$_u$','+1', '+$\epsilon$$^*$','+$\epsilon$', '+1', '-1', '-$\epsilon$$^*$','-$\epsilon$', '-1','-','-','-'],
            ['T$_u$','+3','0','0','-1','-3','0','0','+1','(x,y,z)','-','(x$^3$,y$^3$,z$^3$)(xy$^2$,x$^2$z,yz$^2$)(xz$^2$,x$^2$y,y$^2$z)']], \
            [['O','E','8C$_3$','6C$\prime$$_2$','6C$_4$','3C$_2$=(C$_4$)$^2$','linear functions, rotations', 'quadratic functions', 'cubic functions'],
            ['A$_1$','+1','+1','+1','+1','+1','-','x$^2$+y$^2$+z$^2$','-'],
            ['A$_2$','+1','+1','-1','-1','+1','-','-','xyz'],
            ['E','+2','-1','0','0','+2','-','(x$^2$-y$^2$,2z$^2$-x$^2$-y$^2$)','-'],
            ['T$_1$','+3','0','-1','+1','-1','(x,y,z)(R$_x$,R$_y$,R$_z$)','-','(x$^3$,y$^3$,z$^3$)[x(z$^2$+y$^2$),y(z$^2$+x$^2$),z(x$^2$+y$^2$)]'],
            ['T$_2$','+3','0','+1','-1','-1','-','(xy,xz,yz)','[x(z$^2$-y$^2$),y(z$^2$-x$^2$),z(x$^2$-y$^2$)]']], \
            [['T$_d$','E','8C$_3$','3C$_2$','6S$_4$','6$\sigma$$_d$','linear functions, rotations', 'quadratic functions', 'cubic functions'],
            ['A$_1$','+1','+1','+1','+1','+1','-','x$^2$+y$^2$+z$^2$','xyz'],
            ['A$_2$','+1','+1','+1','-1','-1','-','-','-'],
            ['E','+2','-1','+2','0','0','-','(2z$^2$-x$^2$-y$^2$,x$^2$-y$^2$)','-'],
            ['T$_1$','+3','0','-1','+1','-1','(R$_x$,R$_y$,R$_z$)','-','[x(z$^2$-y$^2$),y(z$^2$-x$^2$),z(x$^2$-y$^2$)]'],
            ['T$_2$','+3','0','-1','-1','+1','(x,y,z)','(xy,xz,yz)','(x$^3$,y$^3$,z$^3$)[x(z$^2$+y$^2$),y(z$^2$+x$^2$),z(x$^2$+y$^2$)]']], \
            [['O$_h$','E','8C$_3$','6C$_2$','6C$_4$','3C$_2$=(C$_4$)$^2$','i','6S$_4$','8S$_6$','3$\sigma$$_h$','6$\sigma$$_d$','linear functions, rotations', 'quadratic functions', 'cubic functions'],
            ['A$_{1g}$','+1','+1','+1','+1','+1','+1','+1','+1','+1','+1','-','x$^2$+y$^2$+z$^2$',','],
            ['A$_{2g}$','+1','+1','-1','-1','+1','+1','-1','+1','+1','-1','-','-','-'],
            ['E$_g$','+2','-1','0','0','+2','+2','0','-1','+2','0','-','(2z$^2$-x$^2$-y$^2$,x$^2$-y$^2$)','-'],
            ['T$_{1g}$','+3','0','-1','+1','-1','+3','+1','0','-1','-1','(R$_x$,R$_y$,R$_z$)','-','-'],
            ['T$_{2g}$','+3','0','+1','-1','-1','+3','-1','0','-1','+1','-','(xz,yz,xy)','-'],
            ['A$_{1u}$','+1','+1','+1','+1','+1','-1','-1','-1','-1','-1','-','-','-'],
            ['A$_{2u}$','+1','+1','-1','-1','+1','-1','+1','-1','-1','+1','-','-','xyz'],
            ['E$_u$','+2','-1','0','0','+2','-2','0','+1','-2','0','-','-','-'],
            ['T$_{1u}$','+3','0','-1','+1','-1','-3','-1','0','+1','+1','(x,y,z)','-','(x$^3$,y$^3$,z$^3$)[x(z$^2$+y$^2$),y(z$^2$+x$^2$),z(x$^2$+y$^2$)]'],
            ['T$_{2u}$','+3','0','+1','-1','-1','-3','+1','0','+1','-1','-','-','[x(z$^2$-y$^2$),y(z$^2$-x$^2$),z(x$^2$-y$^2$)]']]

    def calculate(self):
        # self.file_menu.entryconfig("Export Polar Graph...", state="normal")
        # self.file_menu.entryconfig("Export Expression Latex...", state="normal")
        # self.file_menu.entryconfig("Export Expression Text...", state="normal")
        # self.file_menu.entryconfig("Export Table...", state="normal")
        itm = self.group_box_group.get(self.group_box_group.curselection())
        self.option_var = [itm]
        self.fr_button_dw_message = Frame(master=root)
        self.fr_button_dw_message.grid(row=4, column=0,)
        self.text_box = Text(self.fr_button_dw_message, height=1, width=215, bg='#D3D3D3')
        def parse(d):
            dictionary = {}
            # Removes curly braces and splits the pairs into a list
            pairs = d.strip('{}').split(', ')
            for i in pairs:
                pair = i.split(': ')
                # Other symbols from the key-value pair should be stripped.
                dictionary[pair[0].strip('\'\'\"\"')] = pair[1].strip('\'\'\"\"')
            return dictionary

        self.path_exp = 'ExpressAndLatex/' + str(self.input_matrix_c) + '/' + str(self.option_var_1[0]) + '/' + str(
            self.option_var[0]) + '/Expfile.txt'
        self.path = 'ExpressAndLatex/' + str(self.input_matrix_c) + '/' + str(self.option_var_1[0]) + '/' + str(
            self.option_var[0])
        if self.input_matrix_c == 'Electric Dipole':
            isExist = os.path.exists(self.path_exp)
            if not isExist:  # Create a new directory because it does not exist
                epin = Matrix([[-cos(theta), 0, sin(theta)]])
                esin = Matrix([[0, 1, 0]])
                rot = Matrix([[cos(phi), -sin(phi), 0], [sin(phi), cos(phi), 0], [0, 0, 1]])
                input_matrix = self.dic[self.option_var_1[0]][self.option_var[0]]

                # calculate the expression
                rs_matrix = simplify(self.trans(self.sTB(rot, self.trans(self.sTB(rot, self.bTS(input_matrix, rot.T))))))

                # PP
                pxp = epin * rs_matrix[0:3, 0:3] * epin.T
                pzp = epin * rs_matrix[6:9, 0:3] * epin.T
                self.exprpp = simplify((pxp * cos(theta)) ** 2 + (pzp * sin(theta)) ** 2)[0]

                # PS
                pys = epin * rs_matrix[3:6, 0:3] * epin.T
                self.exprps = simplify((pys ** 2)[0])

                # SP
                sxp = esin * rs_matrix[0:3, 0:3] * esin.T
                szp = esin * rs_matrix[6:9, 0:3] * esin.T
                self.exprsp = simplify((sxp * cos(theta)) ** 2 + (szp * sin(theta)) ** 2)[0]

                # SS
                sys = esin * rs_matrix[3:6, 0:3] * esin.T
                self.exprss = simplify((sys ** 2)[0])
            else:
                express_txt = open(self.path_exp, 'rt')
                lines = express_txt.read().split('\n')
                dict_exp_extract = {}
                i = 0
                for l in lines:
                    if l != '':
                        dict_exp_extract[i] = parse(l)
                        i += 1
                express_txt.close()
                self.exprss = parse_expr(dict_exp_extract[0]['SS'],evaluate=False)
                self.exprsp = parse_expr(dict_exp_extract[1]['SP'],evaluate=False)
                self.exprps = parse_expr(dict_exp_extract[2]['PS'],evaluate=False)
                self.exprpp = parse_expr(dict_exp_extract[3]['PP'],evaluate=False)

            # every change should clear the symbolList at first
            self.symbolList_pp = self.getList_pp()
            self.symbolList_ps = self.getList_ps()
            self.symbolList_ss = self.getList_ss()
            self.symbolList_sp = self.getList_sp()
            # self.symbolList = self.getList()
            # Electric dipole
            if phi in self.symbolList_pp:
                self.symbolList_pp.remove(phi)
            if phi in self.symbolList_ps:
                self.symbolList_ps.remove(phi)
            if phi in self.symbolList_ss:
                self.symbolList_ss.remove(phi)
            if phi in self.symbolList_sp:
                self.symbolList_sp.remove(phi)
        elif self.input_matrix_c == 'Electric Quadrupole':
            isExist = os.path.exists(self.path_exp)
            if not isExist:  # Create a new directory because it does not exist
                k = Matrix([[-sin(theta), 0, -cos(theta)]])
                rot = Matrix([[cos(phi), -sin(phi), 0], [sin(phi), cos(phi), 0], [0, 0, 1]])
                epin = Matrix([[-cos(theta), 0, sin(theta)]])
                esin = Matrix([[0, 1, 0]])

                input_matrix_quad = self.dic_qud[self.option_var_1[0]][self.option_var[0]]
                rs_matrix_quad = simplify(self.trans_quad_2Swap(self.trans_quad(self.bTS_quad(self.trans_quad_2Swap(
                    self.sTB_quad(rot, self.trans_quad(self.sTB_quad(rot, self.bTS_quad(input_matrix_quad, rot.T))))),
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

                # PP
                self.exprpp = simplify((pxp * cos(theta)) ** 2 + (pzp * sin(theta)) ** 2)

                # PS
                self.exprps = simplify((pys ** 2))

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
                # SP
                self.exprsp = simplify((sxp * cos(theta)) ** 2 + (szp * sin(theta)) ** 2)


                # SS
                self.exprss = simplify((sys ** 2))
            else:
                express_txt = open(self.path_exp, 'rt')
                lines = express_txt.read().split('\n')
                dict_exp_extract = {}
                i = 0
                for l in lines:
                    if l != '':
                        dict_exp_extract[i] = parse(l)
                        i += 1
                express_txt.close()
                ss_temp = dict_exp_extract[0]['SS']
                self.exprss = parse_expr(ss_temp, evaluate=False)
                sp_temp = dict_exp_extract[1]['SP']
                self.exprsp = parse_expr(sp_temp, evaluate=False)
                ps_temp = dict_exp_extract[2]['PS']
                self.exprps = parse_expr(ps_temp, evaluate=False)
                pp_temp = dict_exp_extract[3]['PP']
                self.exprpp = parse_expr(pp_temp, evaluate=False)

            # every change should clear the symbolList at first
            self.symbolList_pp = self.getList_pp_eQ()
            self.symbolList_ps = self.getList_ps_eQ()
            self.symbolList_ss = self.getList_ss_eQ()
            self.symbolList_sp = self.getList_sp_eQ()

            # remove variable phi since no need of it
            if phi in self.symbolList_pp:
                self.symbolList_pp.remove(phi)
            if phi in self.symbolList_ps:
                self.symbolList_ps.remove(phi)
            if phi in self.symbolList_ss:
                self.symbolList_ss.remove(phi)
            if phi in self.symbolList_sp:
                self.symbolList_sp.remove(phi)
        elif self.input_matrix_c == 'Magnetic Dipole':
            isExist = os.path.exists(self.path_exp)
            if not isExist:  # Create a new directory because it does not exist
                epin = Matrix([[-cos(theta), 0, sin(theta)]])
                esin = Matrix([[0, 1, 0]])
                rot = Matrix([[cos(phi), -sin(phi), 0], [sin(phi), cos(phi), 0], [0, 0, 1]])
                k = Matrix([[-sin(theta), 0, -cos(theta)]])
                input_matrix = self.dic_mag_dip[self.option_var_1[0]][self.option_var[0]]

                # calculate the expression
                rs_matrix_md = simplify(self.trans(self.sTB(rot, self.trans(self.sTB(rot, self.bTS(input_matrix, rot.T))))))

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

                # PP
                self.exprpp = simplify((Spx * cos(theta)) ** 2 + (Spz * sin(theta)) ** 2)

                # PS
                self.exprps = simplify((Spy ** 2))

                # SP
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

                self.exprsp = simplify((Ssx * cos(theta)) ** 2 + (Ssz * sin(theta)) ** 2)
                # SS
                self.exprss = simplify((Ssy ** 2))
            else:
                express_txt = open(self.path_exp, 'rt')
                lines = express_txt.read().split('\n')
                dict_exp_extract = {}
                i = 0
                for l in lines:
                    if l != '':
                        dict_exp_extract[i] = parse(l)
                        i += 1
                express_txt.close()
                self.exprss = parse_expr(dict_exp_extract[0]['SS'],evaluate=False)
                self.exprsp = parse_expr(dict_exp_extract[1]['SP'],evaluate=False)
                self.exprps = parse_expr(dict_exp_extract[2]['PS'],evaluate=False)
                self.exprpp = parse_expr(dict_exp_extract[3]['PP'],evaluate=False)

            # every change should clear the symbolList at first
            self.symbolList_pp = self.getList_pp_Md()
            self.symbolList_ps = self.getList_ps_Md()
            self.symbolList_ss = self.getList_ss_Md()
            self.symbolList_sp = self.getList_sp_Md()

            if phi in self.symbolList_pp:
                self.symbolList_pp.remove(phi)
            if phi in self.symbolList_ps:
                self.symbolList_ps.remove(phi)
            if phi in self.symbolList_ss:
                self.symbolList_ss.remove(phi)
            if phi in self.symbolList_sp:
                self.symbolList_sp.remove(phi)

        self.fr_input_up.destroy()
        # root.eval('tk::PlaceWindow . center')
        self.text_box.delete('1.0', 'end')
        message = str(self.input_matrix_c) + '  :  ' + str(self.option_var_1[0]) + ' - ' + str(self.option_var[0])
        self.text_box.insert('end', message)
        self.text_box.grid()
        self.paned = Frame(master=root)
        self.paned.grid(row=0, column=0, ipadx=0, ipady=0)
        self.notebook = ttk.Notebook(self.paned)
        self.notebook.grid(row=0, column=0)

        self.tab_1 = Frame(self.notebook)
        self.tab_2 = Frame(self.notebook)
        self.tab_3 = Frame(self.notebook)
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
        self.tab2_scrollable.grid(column=0, row=1, ipadx=600, ipady=100)
        self.tab2_scrollable.bind_arrow_keys(root)
        self.tab2_scrollable.bind_scroll_wheel(root)

        # Create a frame within the ScrolledFrame
        self.tab2_scrollable_inside = self.tab2_scrollable.display_widget(Frame)

        self.f_e, self.wx = plt.subplots(4, 1, figsize=(60, 4))
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

        isExist = os.path.exists(self.path_exp + '/latexfile.txt')
        if not isExist:
        # if dict_extract.get(0, {}).get('SS') is None:
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
        # if dict_extract.get(1, {}).get('SP') is None:
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
        # if dict_extract.get(2, {}).get('PS') is None:
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
        # if dict_extract.get(3, {}).get('PP') is None:
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
                    dict_extract[i] = parse(l)
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
        if self.option_var[0] == 'C1' or self.option_var[0] == 'C1 – I':
            title_text = 'Character table for point group C$_1$'
            self.charSelect = 0

        if self.option_var[0] == 'S2' or self.option_var[0] == 'S2 – I(Bar)':
            title_text = 'Character table for point group S$_2$'
            self.charSelect = 1

        if self.option_var[0] == 'C2' or self.option_var[0] == 'C2 – 2':
            title_text = 'Character table for point group C$_2$'
            self.charSelect = 2

        if self.option_var[0] == 'C1h' or self.option_var[0] == 'C1h – m':
            title_text = 'Character table for point group C$_{1h}$'
            self.charSelect = 3

        if self.option_var[0] == 'C2h' or self.option_var[0] == 'C2h – 2|m':
            title_text = 'Character table for point group C$_{2h}$'
            self.charSelect = 4

        if self.option_var[0] == 'D2' or self.option_var[0] == 'D2 – 222':
            title_text = 'Character table for point group D$_2$'
            self.charSelect = 5

        if self.option_var[0] == 'C2v' or self.option_var[0] == 'C2v – mm2':
            title_text = 'Character table for point group C$_{2v}$'
            self.charSelect = 6

        if self.option_var[0] == 'D2h' or self.option_var[0] == 'D2h – mmm':
            title_text = 'Character table for point group D$_{2h}$'
            self.charSelect = 7

        if self.option_var[0] == 'C4' or self.option_var[0] == 'C4 – 4':
            title_text = 'Character table for point group C$_4$'
            self.charSelect = 8

        if self.option_var[0] == 'S4' or self.option_var[0] == 'S4 – 4(Bar)':
            title_text = 'Character table for point group S$_4$'
            self.charSelect = 9

        if self.option_var[0] == 'D4h' or self.option_var[0] == 'D4h – 4|m':
            title_text = 'Character table for point group D$_{4h}$'
            self.charSelect = 10

        if self.option_var[0] == 'D4' or self.option_var[0] == 'D4 – 422':
            title_text = 'Character table for point group D$_4$'
            self.charSelect = 11

        if self.option_var[0] == 'C4v' or self.option_var[0] == 'C4v – 4mm':
            title_text = 'Character table for point group C$_{4v}$'
            self.charSelect = 12

        if self.option_var[0] == 'D2d' or self.option_var[0] == 'D2d – 4(Bar)2m':
            title_text = 'Character table for point group D$_{2d}$'
            self.charSelect = 13

        if self.option_var[0] == 'D4h' or self.option_var[0] == 'D4h – 4|mmm':
            title_text = 'Character table for point group D$_{4h}$'
            self.charSelect = 14

        if self.option_var[0] == 'C3' or self.option_var[0] == 'C3 – 3':
            title_text = 'Character table for point group C$_3$'
            self.charSelect = 15

        if self.option_var[0] == 'S6' or self.option_var[0] == 'S6 – 3(Bar)':
            title_text = 'Character table for point group S$_6$'
            self.charSelect = 16

        if self.option_var[0] == 'D3' or self.option_var[0] == 'D3 – 32':
            title_text = 'Character table for point group D$_3$'
            self.charSelect = 17

        if self.option_var[0] == 'C3v' or self.option_var[0] == 'C3v – 3m':
            title_text = 'Character table for point group C$_{3v}$'
            self.charSelect = 18

        if self.option_var[0] == 'D3d' or self.option_var[0] == 'D3d – 3(Bar)m':
            title_text = 'Character table for point group D$_{3d}$'
            self.charSelect = 19

        if self.option_var[0] == 'C6' or self.option_var[0] == 'C6 – 6':
            title_text = 'Character table for point group C$_{6}$'
            self.charSelect = 20

        if self.option_var[0] == 'C3h' or self.option_var[0] == 'C3h – 6(Bar)':
            title_text = 'Character table for point group C$_{3h}$'
            self.charSelect = 21

        if self.option_var[0] == 'C6h' or self.option_var[0] == 'C6h – 6|m':
            title_text = 'Character table for point group C$_{6h}$'
            self.charSelect = 22

        if self.option_var[0] == 'D6' or self.option_var[0] == 'D6 – 622':
            title_text = 'Character table for point group D$_6$'
            self.charSelect = 23

        if self.option_var[0] == 'C6v' or self.option_var[0] == 'C6v – 6mm':
            title_text = 'Character table for point group C$_{6v}$'
            self.charSelect = 24

        if self.option_var[0] == 'D3h' or self.option_var[0] == 'D3h – 6(Bar)m2':
            title_text = 'Character table for point group D$_{3h}$'
            self.charSelect = 25

        if self.option_var[0] == 'D6h' or self.option_var[0] == 'D6h – 6|mmm':
            title_text = 'Character table for point group D$_{6h}$'
            self.charSelect = 26

        if self.option_var[0] == 'T' or self.option_var[0] == 'T – 23':
            title_text = 'Character table for point group T'
            self.charSelect = 27

        if self.option_var[0] == 'Th' or self.option_var[0] == 'Th – m3':
            title_text = 'Character table for point group T$_h$'
            self.charSelect = 28

        if self.option_var[0] == 'O' or self.option_var[0] == 'O – 432':
            title_text = 'Character table for point group O'
            self.charSelect = 29

        if self.option_var[0] == 'Td' or self.option_var[0] == 'Td – 4(Bar)3m':
            title_text = 'Character table for point group T$_d$'
            self.charSelect = 30

        if self.option_var[0] == 'Oh' or self.option_var[0] == 'Oh – m3m':
            title_text = 'Character table for point group O$_h$'
            self.charSelect = 31

        cell_text = []
        for row in self.chr_data[self.charSelect]:
            cell_text.append([f'{x}' for x in row])
        self.f_char, self.ax_char = plt.subplots(figsize=(15, 4))  #figsize=(14, 4)
        self.canvs_char = FigureCanvasTkAgg(self.f_char, self.tab_3)
        # self.ax_char.figure(linewidth=2,tight_layout={'pad': 1})
        # Add a table at the bottom of the axes
        # self.f_char.patch.set_facecolor('#FAFAFA')
        the_table = self.ax_char.table(cellText=cell_text,
                              cellLoc='center',
                              rowLoc='center',
                              loc='center')

        if self.option_var[0] == 'C1' or self.option_var[0] == 'C1 – I':
            the_table.scale(2, 2)

        if self.option_var[0] == 'S2' or self.option_var[0] == 'S2 – I(Bar)':
            the_table.scale(2, 2.5)

        if self.option_var[0] == 'C2' or self.option_var[0] == 'C2 – 2':
            the_table.scale(2, 2.5)

        if self.option_var[0] == 'C1h' or self.option_var[0] == 'C1h – m':
            the_table.scale(2.5, 2.5)

        if self.option_var[0] == 'C2h' or self.option_var[0] == 'C2h – 2|m':
            the_table.scale(2.5, 2.5)

        if self.option_var[0] == 'D2' or self.option_var[0] == 'D2 – 222':
            the_table.scale(2.5, 2.5)

        if self.option_var[0] == 'C2v' or self.option_var[0] == 'C2v – mm2':
            the_table.scale(2.5, 2.5)

        if self.option_var[0] == 'D2h' or self.option_var[0] == 'D2h – mmm':
            the_table.scale(2.5, 2)

        if self.option_var[0] == 'C4' or self.option_var[0] == 'C4 – 4':
            the_table.scale(2.5, 2.5)

        if self.option_var[0] == 'S4' or self.option_var[0] == 'S4 – 4(Bar)':
            the_table.scale(2.5, 2.5)

        if self.option_var[0] == 'D4h' or self.option_var[0] == 'D4h – 4|m':
            the_table.scale(2.5, 2.5)

        if self.option_var[0] == 'D4' or self.option_var[0] == 'D4 – 422':
            the_table.scale(3, 1.6)

        if self.option_var[0] == 'C4v' or self.option_var[0] == 'C4v – 4mm':
            the_table.scale(2.5, 2.5)

        if self.option_var[0] == 'D2d' or self.option_var[0] == 'D2d – 4(Bar)2m':
            the_table.scale(2.5, 2.5)

        if self.option_var[0] == 'D4h' or self.option_var[0] == 'D4h – 4|mmm':
            the_table.scale(1.5, 0.65)

        if self.option_var[0] == 'C3' or self.option_var[0] == 'C3 – 3':
            the_table.scale(2.5, 2.3)

        if self.option_var[0] == 'S6' or self.option_var[0] == 'S6 – 3(Bar)':
            the_table.scale(2.9, 2.25)

        if self.option_var[0] == 'D3' or self.option_var[0] == 'D3 – 32':
            the_table.scale(2.5, 2.5)

        if self.option_var[0] == 'C3v' or self.option_var[0] == 'C3v – 3m':
            the_table.scale(2.5, 2.5)

        if self.option_var[0] == 'D3d' or self.option_var[0] == 'D3d – 3(Bar)m':
            the_table.scale(3, 2.5)

        if self.option_var[0] == 'C6' or self.option_var[0] == 'C6 – 6':
            the_table.scale(2.5, 2.5)

        if self.option_var[0] == 'C3h' or self.option_var[0] == 'C3h – 6(Bar)':
            the_table.scale(2.5, 2.5)

        if self.option_var[0] == 'C6h' or self.option_var[0] == 'C6h – 6|m':
            the_table.scale(2.8, 1.6)

        if self.option_var[0] == 'D6' or self.option_var[0] == 'D6 – 622':
            the_table.scale(2.5, 2.5)

        if self.option_var[0] == 'C6v' or self.option_var[0] == 'C6v – 6mm':
            the_table.scale(2.5, 2.5)

        if self.option_var[0] == 'D3h' or self.option_var[0] == 'D3h – 6(Bar)m2':
            the_table.scale(2.5, 2.5)

        if self.option_var[0] == 'D6h' or self.option_var[0] == 'D6h – 6|mmm':
            the_table.scale(3.5, 1.4)

        if self.option_var[0] == 'T' or self.option_var[0] == 'T – 23':
            the_table.scale(2.5, 2.5)

        if self.option_var[0] == 'Th' or self.option_var[0] == 'Th – m3':
            the_table.scale(3.5, 2)

        if self.option_var[0] == 'O' or self.option_var[0] == 'O – 432':
            the_table.scale(2.5, 2.5)

        if self.option_var[0] == 'Td' or self.option_var[0] == 'Td – 4(Bar)3m':
            the_table.scale(2.5, 2.5)

        if self.option_var[0] == 'Oh' or self.option_var[0] == 'Oh – m3m':
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

        self.fr_input_dw = ScrolledFrame(master=root)
        # root.eval('tk::PlaceWindow . center')
        self.fr_input_dw.grid(column=0, row=1, ipadx=600, ipady=80)
        self.fr_button_dw = Frame(master=root)
        root.eval('tk::PlaceWindow . center')
        self.fr_button_dw.grid(row=2, column=0, ipadx=760, ipady=20)

        self.fr_input_dw.bind_arrow_keys(root)
        self.fr_input_dw.bind_scroll_wheel(root)

        # Create a frame within the ScrolledFrame
        self.fr_input_dw_inside = self.fr_input_dw.display_widget(Frame)

        if len(self.symbolList_pp) > 10:
            num_rows = len(self.symbolList_pp)-5
        else:
            num_rows = len(self.symbolList_pp)+1
        num_cols = 10
        for row in range(num_rows):
            for column in range(num_cols):
                w = Label(self.fr_input_dw_inside,
                          width=15,
                          height=5,
                          borderwidth=0,
                          relief="groove",
                          anchor="center",
                          justify="center")

                w.grid(row=row,
                       column=column,
                       padx=4,
                       pady=4)
        # self.label_ss = ttk.LabelFrame(self.fr_input_dw, text='SS')
        # self.label_ss.grid(row=1, column=0, ipadx=673, ipady=200)

        # self.dw_canvas = Canvas(self.fr_input_dw, bg='coral')
        # self.dw_canvas.grid(row=1, column=0)
        # self.fr_input_dw.pack(expand=1)

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
            self.label = Label(self.fr_input_dw_inside, text=self.showSymbol(self.symbolList_ss[i]),
                               borderwidth=2, justify="left", font=('Arial', 18))
            self.label.place(x=191, y=34 + i * 40, width=40, height=40)

            inputStr = StringVar()
            SlideStr = IntVar()
            if i == 0:
                if chr(952) == self.showSymbol(self.symbolList_ss[0]):
                    self.Spin = Spinbox(self.fr_input_dw_inside, from_=-360, to=360, textvariable=SlideStr_theta, relief='groove',
                                        validate='key', validatecommand=range_validation,
                                        command=lambda: self.autoPlot())
                    self.Spin.bind('<Return>', lambda x: self.autoPlot())

                    self.entryList_ss.append(self.Spin)
                    # self.Spin.pack()
                    self.Spin.place(x=241, y=34, width=100, height=40)
                else:
                    self.Spin = Spinbox(self.fr_input_dw_inside, from_=-10, to=10, textvariable=SlideStr, relief='groove',
                                        validate='key', validatecommand=range_validation,
                                        command=lambda: self.autoPlot())
                    self.entryList_ss.append(self.Spin)
                    self.Spin.bind('<Return>', lambda x: self.autoPlot())
                    # self.Spin.pack()
                    self.Spin.place(x=241, y=34 + i * 40, width=100, height=40)
            else:
                self.Spin = Spinbox(self.fr_input_dw_inside, from_=-10, to=10, textvariable=SlideStr, relief='groove',
                                    validate='key', validatecommand=range_validation, command=lambda: self.autoPlot())
                self.entryList_ss.append(self.Spin)
                self.Spin.bind('<Return>', lambda x: self.autoPlot())
                # self.entry = Entry(self.fr_input_dw, textvariable=inputStr, relief='raised', bg='white')
                # self.Spin.pack()
                self.Spin.place(x=241, y=34 + i * 40, width=100, height=40)

            count = count + 1
            value = self.Spin.get()
            # assign values

            # self.entryList_ss.append(self.Spin)
            # self.plot()

        # loop over the symbolList and create labels and entries for each symbol within it
        # print(len(self.symbolList_sp))
        # count = 0
        self.label = Label(self.fr_input_dw_inside, text="SP", borderwidth=2, justify="left", font=('Arial', 18))
        self.label.place(x=self.label_position, y=4)
        self.label_position += self.label_gap
        for j in range(len(self.symbolList_sp)):

            # create labels
            self.label = Label(self.fr_input_dw_inside, text=self.showSymbol(self.symbolList_sp[j]),
                               borderwidth=2, justify="left", font=('Arial', 18))
            self.label.place(x=509, y=34 + j * 40, width=40, height=40)

            inputStr = StringVar()
            SlideStr = DoubleVar()

            if j == 0:
                if chr(952) == self.showSymbol(self.symbolList_sp[0]):
                    self.Spin = Spinbox(self.fr_input_dw_inside, from_=-360, to=360, textvariable=SlideStr_theta, relief='groove',
                                        validate='key', validatecommand=range_validation,
                                        command=lambda: self.autoPlot())
                    self.Spin.bind('<Return>', lambda x: self.autoPlot())

                    self.entryList_sp.append(self.Spin)
                    # self.Spin.pack()
                    self.Spin.place(x=559, y=34, width=100, height=40)
                else:
                    self.Spin = Spinbox(self.fr_input_dw_inside, from_=-10, to=10, textvariable=SlideStr, relief='groove',
                                        validate='key', validatecommand=range_validation,
                                        command=lambda: self.autoPlot())
                    self.entryList_sp.append(self.Spin)
                    self.Spin.bind('<Return>', lambda x: self.autoPlot())
                    # self.Spin.pack()
                    self.Spin.place(x=559, y=34 + j * 40, width=100, height=40)
            else:
                self.Spin = Spinbox(self.fr_input_dw_inside, from_=-10, to=10, textvariable=SlideStr, relief='groove',
                                    validate='key', validatecommand=range_validation, command=lambda: self.autoPlot())
                self.entryList_sp.append(self.Spin)
                self.Spin.bind('<Return>', lambda x: self.autoPlot())
                # self.entry = Entry(self.fr_input_dw, textvariable=inputStr, relief='raised', bg='white')
                # self.Spin.pack()
                self.Spin.place(x=559, y=34 + j * 40, width=100, height=40)

            count = count + 1
            value = self.Spin.get()
            # self.entryList_sp.append(self.Spin)

        # loop over the symbolList and create labels and entries for each symbol within it
        # print(len(self.symbolList_ps))
        count = 0
        self.label = Label(self.fr_input_dw_inside, text="PS", borderwidth=2, justify="left", font=('Arial', 18))
        self.label.place(x=self.label_position, y=4)
        self.label_position += self.label_gap
        for k in range(len(self.symbolList_ps)):
            # create labels
            self.label = Label(self.fr_input_dw_inside, text=self.showSymbol(self.symbolList_ps[k]),
                               borderwidth=2, justify="left", font=('Arial', 18))
            self.label.place(x=835, y=34 + k * 40, width=40, height=40)

            SlideStr = DoubleVar()

            if k == 0:
                if chr(952) == self.showSymbol(self.symbolList_ps[0]):
                    self.Spin = Spinbox(self.fr_input_dw_inside, from_=-360, to=360, textvariable=SlideStr_theta, relief='groove',
                                        validate='key', validatecommand=range_validation,
                                        command=lambda: self.autoPlot())
                    self.Spin.bind('<Return>', lambda x: self.autoPlot())

                    self.entryList_ps.append(self.Spin)
                    # self.Spin.pack()
                    self.Spin.place(x=885, y=34, width=100, height=40)
                else:
                    self.Spin = Spinbox(self.fr_input_dw_inside, from_=-10, to=10, textvariable=SlideStr, relief='groove',
                                        validate='key', validatecommand=range_validation,
                                        command=lambda: self.autoPlot())
                    self.entryList_ps.append(self.Spin)
                    self.Spin.bind('<Return>', lambda x: self.autoPlot())
                    # self.Spin.pack()
                    self.Spin.place(x=885, y=34 + k * 40, width=100, height=40)
            else:
                self.Spin = Spinbox(self.fr_input_dw_inside, from_=-10, to=10, textvariable=SlideStr, relief='groove',
                                    validate='key', validatecommand=range_validation, command=lambda: self.autoPlot())
                self.entryList_ps.append(self.Spin)
                self.Spin.bind('<Return>', lambda x: self.autoPlot())
                # self.entry = Entry(self.fr_input_dw, textvariable=inputStr, relief='raised', bg='white')
                # self.Spin.pack()
                self.Spin.place(x=885, y=34 + k * 40, width=100, height=40)

            count = count + 1
            # self.entryList_ps.append(self.Spin)

        # loop over the symbolList and create labels and entries for each symbol within it
        # print(len(self.symbolList_pp))
        count = 0
        self.label = Label(self.fr_input_dw_inside, text="PP", borderwidth=2, justify="left", font=('Arial', 18))
        self.label.place(x=self.label_position, y=4)
        self.label_position += self.label_gap
        for h in range(len(self.symbolList_pp)):
            # create labels

            self.label = Label(self.fr_input_dw_inside, text=self.showSymbol(self.symbolList_pp[h]),
                               borderwidth=2, justify="left", font=('Arial', 18))
            self.label.place(x=1153, y=34 + h * 40, width=40, height=40)

            inputStr = StringVar()
            SlideStr = DoubleVar()
            if h == 0:
                if chr(952) == self.showSymbol(self.symbolList_pp[0]):
                    self.Spin = Spinbox(self.fr_input_dw_inside, from_=-360, to=360, textvariable=SlideStr_theta, relief='groove',
                                        validate='key', validatecommand=range_validation,
                                        command=lambda: self.autoPlot())
                    self.Spin.bind('<Return>', lambda x: self.autoPlot())
                    self.entryList_pp.append(self.Spin)
                    # self.Spin.pack()
                    self.Spin.place(x=1203, y=34, width=100, height=40)
                else:
                    self.Spin = Spinbox(self.fr_input_dw_inside, from_=-10, to=10, textvariable=SlideStr, relief='groove',
                                        validate='key', validatecommand=range_validation,
                                        command=lambda: self.autoPlot())
                    self.entryList_pp.append(self.Spin)
                    self.Spin.bind('<Return>', lambda x: self.autoPlot())
                    # self.Spin.pack()
                    self.Spin.place(x=1203, y=34 + h * 40, width=100, height=40)

            else:
                self.Spin = Spinbox(self.fr_input_dw_inside, from_=-10, to=10, textvariable=SlideStr, relief='groove',
                                    validate='key', validatecommand=range_validation, command=lambda: self.autoPlot())
                self.entryList_pp.append(self.Spin)
                self.Spin.bind('<Return>', lambda x: self.autoPlot())
                # self.entry = Entry(self.fr_input_dw, textvariable=inputStr, relief='raised', bg='white')
                # self.Spin.pack()
                self.Spin.place(x=1203, y=34 + h * 40, width=100, height=40)

            count = count + 1
            value = self.Spin.get()

        self.button3 = ttk.Checkbutton(self.fr_button_dw, text='Quit', command=lambda: self._quit(), style="Toggle.TButton")
        # self.button3.pack()
        self.button3.place(x=1420, y=10)
        self.button4 = ttk.Button(self.fr_button_dw, text='Back', command=lambda: self._back())
        # self.button4.pack()
        self.button4.place(x=1344, y=10)
        self.button5 = ttk.Button(self.fr_button_dw, text='?')
        self.button5.place(x=5, y=10)
        myTip = Hovertip(self.button5, 'Switch through different tabs to check plot, equations and character table. '
                                       '\nExport the graph, expression (latex), and character table through Menu->File.', hover_delay=1000)

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

    def show_crystal_system(self):
        self.input_matrix_g = []
        itm_c = self.group_box.get(self.group_box.curselection())
        self.option_var_2 = [itm_c]

        self.group_box_group = Listbox(self.fr_input_up, width=16, justify="left", height=11, font=('Arial', 13),
                                       yscrollcommand='Vertical', selectmode=SINGLE, relief='sunken', exportselection=False)
        self.group_box_group.place(x=335, y=60)
        self.group_box_group.delete(0, END)
        self.input_matrix_c = self.option_var_2[0]

        self.crystal_box = Listbox(self.fr_input_up, width=16, justify="left", height=11, font=('Arial', 13),
                                   yscrollcommand='Vertical', selectmode=SINGLE, relief='sunken', exportselection=False)
        self.crystal_box.place(x=200, y=60)

        if self.input_matrix_c == 'Electric Dipole':
            for x in self.dic:
                self.crystal_box.insert(END, x)
        elif self.input_matrix_c == 'Electric Quadrupole':
            for x in self.dic_qud:
                self.crystal_box.insert(END, x)
        elif self.input_matrix_c == 'Magnetic Dipole':
            for x in self.dic_mag_dip:
                self.crystal_box.insert(END, x)
        # elif self.input_matrix_c == 'Magnetic Monopole':
        #     self.crystal_box.insert(1, 'Continue...')
        elif self.input_matrix_c == 'Coming Soon...':
            self.crystal_box.insert(1, 'Coming Soon...')

        self.cal_bt = ttk.Button(self.fr_input_up, text='Calculate', command=lambda: self.pop_up_warning(), width=10,
                                 style='Accent.TButton')

        self.crystal_box.bind('<Return>', lambda x: self.show_group())
        self.crystal_box.bind('<Double-Button-1>', lambda x: self.show_group())
        self.crystal_box.bind('<<ListboxSelect>>', lambda x: self.show_group())
        self.cal_bt.bind('<Double-1>', lambda: self.calculate())
        self.cal_bt.grid(row=0, column=0, padx=350, pady=260)

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
        # elif self.input_matrix_c == 'Magnetic Monopole':
        #     self.group_box_group.insert(1, 'Continue...')

        elif self.input_matrix_c == 'Coming Soon...':
            self.group_box_group.insert(1, 'Coming Soon...')

        # if self.input_matrix_c == 'Magnetic Monopole':
        #     self.cal_bt = ttk.Button(self.fr_input_up, text='Calculate', command=lambda: self.suprise(), width=12,
        #                              style='Accent.TButton')
        # else:
        self.cal_bt = ttk.Button(self.fr_input_up, text='Calculate', command=lambda: self.calculate(), width=10,
                                     style='Accent.TButton')

        self.group_box_group.bind('<Return>', lambda x: self.calculate())
        self.group_box_group.bind('<Double-Button-1>', lambda x: self.calculate())
        self.cal_bt.bind('<Double-1>', lambda: self.calculate())
        self.cal_bt.grid(row=0, column=0, padx=200, pady=250)

    def suprise(self):
        webview.create_window(title='Monopole Tutorials', url='https://youtu.be/dQw4w9WgXcQ', hidden=True)
        webview.start()


if __name__ == '__main__':
    # initialize the global variables
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

    # construct the main window
    try:
        root = Tk()
        # root.tk.call("source", "Theme/azure.tcl")
        sv_ttk.set_theme('light')
        # root.tk.call("set_theme", "light")
        root.title("SHG Simulation Tool v1")
        root.geometry('+450+200')  # window position (450 pixels from left, 200 ones from right)
        # create a substance
        window1 = polarplotGUI(master=root)
        root.eval('tk::PlaceWindow . center')
        # endless loop unless quit
        root.mainloop()
    except:
        import traceback
        traceback.print_exc()
        input("Press Enter to end...")