import platform
import os
import sys
from distutils.spawn import find_executable

if sys.version_info[:2] < (3, 7):
    print("Requires Python 3.7 or newer. "
          "Python %d.%d detected" % sys.version_info[:2])
    sys.exit(-1)

if platform.system() == 'Windows':
    OS = 'Windows'
elif platform.system() == 'Linux':
    OS = 'Linux'
elif platform.system() == 'Darwin':
    OS = 'Darwin'

os.system('pip install -r requirements.txt')
os.system('pip install latex')

from Core import Mac_GUI, Window_GUI

if OS == 'Windows':
    Window_GUI.run()
elif OS == 'Darwin':
    if find_executable('latex'):
        print('latex installed')
    else:
        os.system('/bin / bash - c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"')
        os.system('brew install mactex')
    Mac_GUI.run()
else:  # Linux
    Window_GUI.run()
    os.system('sudo apt install idle3')
    os.system('sudo apt install texlive-latex-extra')
    os.system('sudo apt install cm-super')
    os.system('sudo apt install dvipng')