# SHG Simulation Package
![GitHub release version](https://img.shields.io/github/v/release/CharlieGPA40/SHG-Simulation-Package?color=%2350C878&include_prereleases)
![License](https://img.shields.io/github/license/CharlieGPA40/SHG-Simulation-Package)
![GitHub Size](https://img.shields.io/github/repo-size/CharlieGPA40/SHG-Simulation-Package)

The purpose of this package is to assist the Condensed Matter Physics community work efficiently with Rotational-Anisotropic Second-Harmonic Generation (RA-SHG):
1. Easier confirmation of RA-SHG experimental results with an all-in-one package.
2. Quick visualization of the symmetries of quantum materials.
3. Simulation of the nonlinear optical response for the electric dipole (ED), electric quadrupole (EQ), and magnetic dipole (MD) radiation sources.

Check our poster: [Link](https://jinlab.auburn.edu/research/software/)
	
Note: This package is for academic and educational research (WITHOUT WARRANTIES, our software does not collect any data from users).

## Requirements
1. This package is compatible with Python 3.7 or newer. 
2. Latex is required on all platforms:
   1. Windows users need to install Latex before running the program
   2. Mac and Linux users can install the package by simply running `StartGui.py` or install before running.
2. We tested the program on Python version 3.9-3.11 on M1 Mac (macOS 13.4.1), Intel Mac (macOS 12.6.7), Windows (win 10 & 11), and Linux (Ubuntu 22.04 LST) Machines.

## Setup
#### Create a new virtual environment based on your Python version:
First, create a Python virtual environment:
```bash
sudo apt install python3.xx-venv
python3 -m venv name
```
Second, activate the environment:
```bash
source name/bin/activate
```

linux common issue (tested on Ubuntu):
1. Latex
```bash
sudo apt install texlive-latex-extra
```
2. Latex extra package
```bash
sudo apt install cm-super
```
3. Matplotlib missing file
```bash
sudo apt install dvipng
```
4. install idle library:
```bash
sudo apt install idle3
```
Note: Linux users can run `StartGui.py` to install all the required packages.
## Running
1. Run from the Python IDE using code `StartGui.py`.

## Expression and Latex
1. All the expressions can be found under `SHG-Simulation/ExpressAndLatex/`.

## Update Notes
New Features in Version 0.5.0 include:

    *   New feature of Orientation selection
    *   An initialization file to install all the required packages 
    *   Combining the running files into one file
    *   Improving the calculation model and updating Logo
    *   Relocating all the calculation functions into separate folders
    *   Improving the symbolic format calculation by using Cython package symengine
    *   Small modifications to improve user interface and enhance user experience

Version 0.0.1

    *   Thanks for supporting us and we released our first beta for users to test
    *   General Rotational Anisotropy - Second Harmonic Generation simulation on four different channels

    
## About us
Our group focuses on studying novel phases of matter in low-dimensional quantum systems. We exploit a variety of experimental techniques, such as femtosecond laser-based nonlinear optical spectroscopy and synchrotron-based photoemission spectroscopy/microscopy, to investigate the electronic and magnetic structure at the surface and interface.

## Contact
This project is contributed by:
* Chunli Tang (Auburn University – Electrical and Computer Engineering: chunli.tang@auburn.edu)
* Hussam Mustafa (Auburn University – Physics Department: hnm0037@auburn.edu)

Advisor:
* [Dr. Masoud Mahjouri-Samani](http://wp.auburn.edu/Mahjouri/) (Auburn University – Electrical and Computer Engineering: mzm0185@auburn.edu)
* [Dr. Wencan Jin](http://wp.auburn.edu/JinLab/) (Auburn University – Physics Department: wjin@auburn.edu)

Join our SHG Simulation Software Google group: shg-simulation-package@googlegroup.com
