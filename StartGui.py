import platform
import os
from Core import Mac_GUI, Window_GUI
import sys

if sys.version_info[:2] < (3, 7):
    print("SymEngine requires Python 3.7 or newer. "
          "Python %d.%d detected" % sys.version_info[:2])
    sys.exit(-1)


if platform.system() == 'Windows':
    OS = 'Windows'
if platform.system() == 'Linux':
    OS = 'Linux'
elif platform.system() == 'Darwin':
    OS = 'Darwin'

os.system('pip install -r requirements.txt')

if OS == 'Windows':
    Window_GUI.run()
elif OS == 'Darwin':
    Mac_GUI.run()
else:  # Linux
    Window_GUI.run()
    os.system('sudo apt install idle3')
    os.system('sudo apt install texlive-latex-extra')
    os.system('sudo apt install cm-super')
    os.system('sudo apt install dvipng')