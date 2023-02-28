# SHG Simulation Package
![GitHub release version](https://img.shields.io/github/v/release/CharlieGPA40/SHG-Simulation-Package?color=%2350C878&include_prereleases)
![License](https://img.shields.io/github/license/CharlieGPA40/SHG-Simulation-Package)
![GitHub Size](https://img.shields.io/github/repo-size/CharlieGPA40/SHG-Simulation-Package)

The purpose of this package is to assist the Condensed Matter Physics community work efficiently with Rotational-Anisotropic Second-Harmonic Generation (RA-SHG):
1. Easier confirmation of RA-SHG experimental results with an all-in-one package.
2. Quick visualization of the symmetries of quantum materials.
3. Simulation of the nonlinear optical response for the electric dipole (ED), electric quadrupole (EQ), and magnetic dipole (MD) radiation sources.
	
Note: This pacakge is for academic research and educational purposes.

## Requirements
1. Latex is required. Install Latex on your computer before run the program.
2. We tested the program on python version 3.9-3.11 on both M1 Mac and Intel Mac.
3. All the required packages are listed in `requirements.txt`.

## Setup
### Setup Enviroment
#### Use default virtual enviroment. Go to `SHG-Simulation/`:
```bash
source venv/bin/activate
```

Note: the venv packed with python 3.11

#### Create new virtual enviroment based on your python version:
First, create a python virtural enviroment:
```bash
python -m venv name
```
Second, activate the enviroment:
```bash
source name/bin/activate
```
Install required packages:
```bash
pip install -r requirements.txt
```
for linux user only, install idle library:
```bash
sudo apt install idle3
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

## Running
1. Run from the python code `SHG Simulation.py`. (faster)
2. Run from application in `dict/SHG Simulation/SHG Simlation.exec`.

## Expression and Latex
1. All the expressions can be found under `SHG-Simulation/ExpressAndLatex/`.
2. The calculation geometry is under `SHG-Simulation/Image/Model1.png`.

## About us 
Our group focuses on studying novel phases of matter in low-dimensional quantum systems. We exploit a variety of experimental techniques, such as femtosecond laser-based nonlinear optical spectroscopy and synchrotron-based photoemission spectroscopy/microscopy, to investigate the electronic and magnetic structure at the surface and interface.

## Contact
This project is contributed by:
* Chunli Tang (Auburn Univeristy – Electrical and Computer Engineering: chunli.tang@auburn.edu)
* Hussam Mustafa (Auburn Univeristy – Physics Department: hnm0037@auburn.edu)
Advisor:
* [Dr. Masoud Mahjouri-Samani](http://wp.auburn.edu/Mahjouri/) (Auburn Univeristy – Electrical and Computer Engineering: mzm0185@auburn.edu)
* [Dr. Wencan Jin](http://wp.auburn.edu/JinLab/) (Auburn Univeristy – Physics Department: wjin@auburn.edu)
