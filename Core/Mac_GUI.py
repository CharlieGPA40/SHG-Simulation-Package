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
from Core.CharTable import characterTable
from Core.Dict import SetUpDict
from Core.function import TensorMath as tm
from Core.function import rotation as rt
from timeit import default_timer as clock


# ************************************** #
# construct a class used to generate the polar plot
def run():
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
            self.root.protocol("WM_DELETE_WINDOW", self.close)
            au_logo = Image.open("Image/vect.png")
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
            wb_label.bind("<Button-1>", lambda e: callback("http://wp.auburn.edu/JinLab/"))
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
                          '\n\nWe would like to give a special thanks to: \nBrian Opatosky, Matt Galinger, J Isaac Garcia'
            Ack_box.insert(END, acknowledge)
            Ack_box.config(state='disabled')


            ref_box = Text(self.tab_3, height=10, width=80, relief='sunken')
            ref_box.grid(column=0, row=10)
            reference = '[1] Li, Yilei et al. "Probing symmetry properties of few-layer MoS2 and h-BN by optical second-harmonic generation." Nano letters vol. 13,7 (2013): 3329-33. doi: 10.1021/n/401561г.' \
                        '\n[2] Fiebig, Manfred et al. "Second-harmonic generation as a tool for studying electronic and magnetic structures of crystals: review."Journalof The Optical Societyof America B-optical Physics 22 (2005): 96-118.' \
                        '\n[3] http://symmetry.jacobs-university.de/group.html.' \
                        '\n[4] Gallego et al. "Automatic calculation of symmetry-adapted tensors in magnetic and non-magnetic materials: a new tool of the Bilbao Crystallographic Server" Acta Cryst. A (2019) 75, 438-447.' \
                        '\n[5] Boyd, Robert W. Nonlinear optics. Academic press, 2020.' \
                        '\n[6] Torchinsky, D. H., et al. "Structural distortion-induced magnetoelastic locking in Sr 2 IrO 4 revealed through nonlinear optical harmonic generation." Physical review letters 114.9 (2015): 096404.' \
                        '\n[7] Fichera, Bryan T., et al. "Second harmonic generation as a probe of broken mirror symmetry." Physical Review B 101.24 (2020): 241106.' \
                        '\n[8] Fonseca, Jordan, et al. "Anomalous Second Harmonic Generation from Atomically Thin MnBi2Te4." Nano Letters (2022).' \
                        '\n[9] Li, Yilei, et al. "Probing symmetry properties of few-layer MoS2 and h-BN by optical second-harmonic generation." Nano letters 13.7 (2013): 3329-3333.' \
                        '\n[10] Germer, Thomas A., et al. "Depletion-electric-field-induced second-harmonic generation near oxidized GaAs (001) surfaces." Physical Review B 55.16 (1997): 10694.' \
                        '\n[11] Luo, Xiangpeng, et al. "Ultrafast modulations and detection of a ferro-rotational charge density wave using time-resolved electric quadrupole second harmonic generation." Physical review letters 127.12 (2021): 126401.' \
                        '\n[12] Jin, Wencan, et al. "Observation of a ferro-rotational order coupled with second-order nonlinear optical fields." Nature Physics 16.1 (2020): 42-46.' \
                        '\n[13] Anisimov, A. N., N. A. Perekopaiko, and Aleksei Valerevich Petukhov. "Relationship between the anisotropy of reflected second harmonic radiation and the orientation of the crystal surface." -Soviet journal of quantum electronics 21.1 (1991): 82.'

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
            self.chr_data = characterTable.charTable(self)
            self.dic, self.dic_qud, self.dic_mag_dip = SetUpDict.setupdict(self)
            # Only work for windows
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
            menu_bar.add_cascade(label='Help', menu=Help)
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

        def beta_back(self):
            self.fr_input_up.destroy()
            self.fr_input_up = Frame(master=root, bg='#F2F3F4')
            self.createWidget()

        def createWidget(self):
            self.list_init()
            self.view_init()
            # set up a navigation toolbar
            self.option_var = []
            self.option_var_1 = []
            self.option_var_2 = []
            self.option_var_3 = []
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
                                           yscrollcommand='Vertical', selectmode=SINGLE, relief='sunken',
                                           exportselection=False)
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
                                          yscrollcommand='Vertical', selectmode=SINGLE, relief='sunken',
                                          exportselection=False)
            self.crystal_system.place(x=200, y=60)

            self.nex_bt = ttk.Button(self.fr_input_up, text='Calculate', command=lambda: self.pop_up_warning(), width=10,
                                     style='Accent.TButton')
            self.nex_bt.bind('<Return>', lambda: self.show_crystal_system())
            self.nex_bt.grid(row=0, column=0, padx=355, pady=260)
            self.myBtn = ttk.Button(self.fr_input_up, text='?')
            self.myBtn.place(y=260, x=312)
            myTip = Hovertip(self.myBtn, 'Please select all the elements to do the calculation. '
                                         '\nThe calculation model can be found at menu->Model->Calculation Model',
                             hover_delay=1000)
            self.nex_bt['state'] = DISABLED
            self.sample_rot_label = ttk.Label(self.fr_input_up, text='Sample Rotation:', background='#F2F3F4',
                                              font=('Arial bold', 15))
            self.sample_rot_label.place(x=470, y=32)
            self.sample_rot = Listbox(self.fr_input_up, width=16, justify="left", height=11, font=('Arial', 13),
                                      yscrollcommand='Vertical', selectmode=SINGLE, relief='sunken',
                                      exportselection=False)
            self.sample_rot.place(x=472, y=60)

            self.nex_bt.grid(row=0, column=0, padx=490, pady=260)
            self.myBtn.place(y=260, x=447)
            self.beta_back_bt = ttk.Button(self.fr_input_up, text='Back', command=lambda: self.beta_back(),
                                           width=5, )
            self.beta_back_bt.place(y=260, x=367)
            # self._beta_init()

        def view_init(self):
            self.fr_input_up = Frame(master=root, bg='#F2F3F4')
            self.fr_input_up.grid(row=1, column=0, ipadx=320, ipady=152, sticky='NW')
            self.fr_input_up.grid_propagate(False)

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
            # print('Opt #1 {}'.format(self.option_var_1))
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
            self.cal_bt_dis.grid(row=0, column=0, padx=490, pady=250)
            self.cal_bt_dis['state'] = DISABLED

        def SampleRotation(self):
            if self.input_matrix_g == 'Triclinic':
                self.sample_rot.delete(0, END)
                self.sample_rot.insert(1, '(001)')
            elif self.input_matrix_g == 'Monoclinic':
                self.sample_rot.delete(0, END)
                self.sample_rot.insert(1, '[010]')
                self.sample_rot.insert(2, '[001]')
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
            self.cal_bt_dis.grid(row=0, column=0, padx=490, pady=260)
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

        def showSymbol(self, symbol):
            if str(symbol) == 'theta':
                return chr(952)
            else:
                return symbol

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
                if chr(952) == self.showSymbol(self.symbolList_ss[0]):
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
                if chr(952) == self.showSymbol(self.symbolList_sp[0]):
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
                # print(self.valueList_ps)
                if chr(952) == self.showSymbol(self.symbolList_ps[0]):
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
                if chr(952) == self.showSymbol(self.symbolList_pp[0]):
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
                self.newWindow.maxsize()
                self.opened = True
            else:
                self.newWindow.destroy()

            itm_rot = self.sample_rot.get(self.sample_rot.curselection())
            self.option_var_3 = [itm_rot]
            itm = self.group_box_group.get(self.group_box_group.curselection())
            self.option_var = [itm]
            self.fr_button_dw_message = Frame(self.newWindow)
            self.fr_button_dw_message.grid(row=4, column=0,)
            self.text_box = Text(self.fr_button_dw_message, height=1, width=214, bg='#D3D3D3')
            def parse(d):
                dictionary = {}
                # Removes curly braces and splits the pairs into a list
                pairs = d.strip('{}').split(', ')
                for i in pairs:
                    pair = i.split(': ')
                    # Other symbols from the key-value pair should be stripped.
                    dictionary[pair[0].strip('\'\'\"\"')] = pair[1].strip('\'\'\"\"')
                return dictionary

            # self.fr_input_up.destroy()
            self.path_exp = 'Core/ExpressAndLatex/' + str(self.input_matrix_c) + '/' + str(self.option_var_1[0]) + '/' + str(
                self.option_var[0]) + '/' + str(
                self.option_var_3[0]) + '/Expfile.txt'

            self.path = 'Core/ExpressAndLatex/' + str(self.input_matrix_c) + '/' + str(self.option_var_1[0]) + '/' + str(
                self.option_var[0]) + '/' + str(
                self.option_var_3[0])

            epin = Matrix([[-cos(theta), 0, sin(theta)]])
            esin = Matrix([[0, 1, 0]])
            rot = Matrix([[cos(phi), -sin(phi), 0], [sin(phi), cos(phi), 0], [0, 0, 1]])
            k = Matrix([[-sin(theta), 0, -cos(theta)]])
            if self.input_matrix_c == 'Electric Dipole':
                rank = 3
                isExist = os.path.exists(self.path_exp)
                if not isExist:  # Create a new directory because it does not exist
                    input_matrix = self.dic[self.option_var_1[0]][self.option_var[0]]

                    input_matrix = rt.rotationCal(rank, self.option_var_3[0], input_matrix, self.Rank3Matrix())

                    rs_matrix = simplify(tm.trans(tm.sTB(rot, tm.trans(tm.sTB(rot, tm.bTS(input_matrix, rot.T))))))
                    # PP
                    rs_matrix = simplify(rs_matrix)
                    pxp = epin * rs_matrix[0:3, 0:3] * epin.T
                    pzp = epin * rs_matrix[6:9, 0:3] * epin.T
                    # pxp = se.sympify(pxp)
                    # pzp = se.sympify(pzp)
                    self.exprpp = simplify((pxp * cos(theta))** 2 + (pzp * sin(theta))** 2)[0]
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
                            dict_exp_extract[i] = parse(l)
                            i += 1
                    express_txt.close()
                    # sympy
                    self.exprss = parse_expr(dict_exp_extract[0]['SS'],evaluate=False)
                    self.exprsp = parse_expr(dict_exp_extract[1]['SP'],evaluate=False)
                    self.exprps = parse_expr(dict_exp_extract[2]['PS'],evaluate=False)
                    self.exprpp = parse_expr(dict_exp_extract[3]['PP'],evaluate=False)

                self.symbolList_pp = self.getList(self.exprpp)
                self.symbolList_ps = self.getList(self.exprps)
                self.symbolList_ss = self.getList(self.exprss)
                self.symbolList_sp = self.getList(self.exprsp)
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
                if isExist == False:  # Create a new directory because it does not exist
                    rank = 4
                    # Using sympy
                    # k = Matrix([[-sin(theta), 0, -cos(theta)]])
                    input_matrix_quad = self.dic_qud[self.option_var_1[0]][self.option_var[0]]

                    input_matrix_quad = rt.rotationCal(rank, self.option_var_3[0], input_matrix_quad, self.Rank4Matrix())
                    rs_matrix_quad = simplify(tm.trans_quad_2Swap(tm.trans_quad(tm.bTS_quad(tm.trans_quad_2Swap(
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
                    self.exprpp = simplify((pxp * cos(theta)) ** 2 + (pzp * sin(theta)) ** 2)
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
                    # Sympy
                    self.exprsp = simplify((sxp * cos(theta)) ** 2 + (szp * sin(theta)) ** 2)
                    self.exprss = simplify((sys ** 2))
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
                            dict_exp_extract[i] = parse(l)
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
                self.symbolList_pp = self.getList(self.exprpp)
                self.symbolList_ps = self.getList(self.exprps)
                self.symbolList_ss = self.getList(self.exprss)
                self.symbolList_sp = self.getList(self.exprsp)

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
                rank = 3
                if not isExist:  # Create a new directory because it does not exist
                    input_matrix = self.dic_mag_dip[self.option_var_1[0]][self.option_var[0]]
                    input_matrix = rt.rotationCal(rank, self.option_var_3[0], input_matrix, self.Rank3Matrix())
                    # calculate the expression
                    rs_matrix_md = simplify(tm.trans(tm.sTB(rot, tm.trans(tm.sTB(rot, tm.bTS(input_matrix, rot.T))))))

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

                    self.exprpp = simplify((Spx * cos(theta)) ** 2 + (Spz * sin(theta)) ** 2)
                    self.exprps = simplify((Spy ** 2))
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
                    # # SS
                    self.exprss = simplify((Ssy ** 2))
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
                            dict_exp_extract[i] = parse(l)
                            i += 1
                    express_txt.close()

                    # sympy
                    self.exprss = parse_expr(dict_exp_extract[0]['SS'],evaluate=False)
                    self.exprsp = parse_expr(dict_exp_extract[1]['SP'],evaluate=False)
                    self.exprps = parse_expr(dict_exp_extract[2]['PS'],evaluate=False)
                    self.exprpp = parse_expr(dict_exp_extract[3]['PP'],evaluate=False)

                # every change should clear the symbolList at first
                self.symbolList_pp = self.getList(self.exprpp)
                self.symbolList_ps = self.getList(self.exprps)
                self.symbolList_ss = self.getList(self.exprss)
                self.symbolList_sp = self.getList(self.exprsp)

                if phi in self.symbolList_pp:
                    self.symbolList_pp.remove(phi)
                if phi in self.symbolList_ps:
                    self.symbolList_ps.remove(phi)
                if phi in self.symbolList_ss:
                    self.symbolList_ss.remove(phi)
                if phi in self.symbolList_sp:
                    self.symbolList_sp.remove(phi)

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

            self.path = 'Core/ExpressAndLatex/' + str(self.input_matrix_c) + '/' + str(self.option_var_1[0]) + '/' + str(self.option_var[0]) + '/' + str(self.option_var_3[0]) + '/'
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
                        dict_extract[i] = parse(l)
                        i += 1
                latex_txt.close()

                print('THis is {}'.format(dict_extract))
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

            if self.option_var[0] == 'C4h' or self.option_var[0] == 'C4h – 4|m':
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

            if self.option_var[0] == 'Iso':
                title_text = 'Character table for point group Iso'
                self.charSelect = 32

            cell_text = []
            for row in self.chr_data[self.charSelect]:
                cell_text.append([f'{x}' for x in row])
            self.f_char, self.ax_char = plt.subplots(figsize=(15, 4))
            self.canvs_char = FigureCanvasTkAgg(self.f_char, self.tab_3)
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

            if self.option_var[0] == 'C4h' or self.option_var[0] == 'C4h – 4|m':
                the_table.scale(2.5, 2.5)

            if self.option_var[0] == 'D4' or self.option_var[0] == 'D4 – 422':
                the_table.scale(3, 1.6)

            if self.option_var[0] == 'C4v' or self.option_var[0] == 'C4v – 4mm':
                the_table.scale(2.5, 2.5)

            if self.option_var[0] == 'D2d' or self.option_var[0] == 'D2d – 4(Bar)2m':
                the_table.scale(2.5, 2.5)

            if self.option_var[0] == 'D4h' or self.option_var[0] == 'D4h – 4|mmm':
                the_table.scale(2.5, 1.25)

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
            num_cols = 10
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
                        self.Spin.place(x=1203, y=34 + h * 40, width=100, height=40)

                else:
                    self.Spin = Spinbox(self.fr_input_dw_inside, from_=-10, to=10, textvariable=SlideStr, relief='groove',
                                        validate='key', validatecommand=range_validation, command=lambda: self.autoPlot())
                    self.entryList_pp.append(self.Spin)
                    self.Spin.bind('<Return>', lambda x: self.autoPlot())
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

        def buffer(self):
            self.cal_bt_dis['state'] = ACTIVE


    # if __name__ == '__main__':

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
        sv_ttk.set_theme('light')
        root.title("SHG Simulation Tool v1")
        root.maxsize(250, 152)
        window1 = polarplotGUI(master=root)
        root.eval('tk::PlaceWindow . center')
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
run()
