from sympy.parsing.sympy_parser import parse_expr
import os

def reference():
    reference = '[1] Li, Yilei et al. "Probing symmetry properties of few-layer MoS2 and h-BN by optical second-harmonic generation." Nano letters vol. 13,7 (2013): 3329-33. doi: 10.1021/n/401561г.' \
                '\n[2] Fiebig, Manfred et al. "Second-harmonic generation as a tool for studying electronic and magnetic structures of crystals: review."Journalof The Optical Societyof America B-optical Physics 22 (2005): 96-118.' \
                '\n[3] http://symmetry.jacobs-university.de/group.html.' \
                '\n[4] Gallego et al. "Automatic calculation of symmetry-adapted tensors in magnetic and non-magnetic materials: a new tool of the Bilbao Crystallographic Server" Acta Cryst. A (2019) 75, 438-447.' \
                '\n[5] Boyd, Robert W., Alexander L.Gaeta, and Enno Giese. "Nonlinear optics." Springer Handbook of Atomic, Molecular, and Optical Physics.Cham: Springer International Publishing, 2008.1097 - 1110.' \
                '\n[6] Torchinsky, D. H., et al. "Structural distortion-induced magnetoelastic locking in Sr 2 IrO 4 revealed through nonlinear optical harmonic generation." Physical review letters 114.9 (2015): 096404.' \
                '\n[7] Fichera, Bryan T., et al. "Second harmonic generation as a probe of broken mirror symmetry." Physical Review B 101.24 (2020): 241106.' \
                '\n[8] Fonseca, Jordan, et al. "Anomalous Second Harmonic Generation from Atomically Thin MnBi2Te4." Nano Letters (2022).' \
                '\n[9] Li, Yilei, et al. "Probing symmetry properties of few-layer MoS2 and h-BN by optical second-harmonic generation." Nano letters 13.7 (2013): 3329-3333.' \
                '\n[10] Germer, Thomas A., et al. "Depletion-electric-field-induced second-harmonic generation near oxidized GaAs (001) surfaces." Physical Review B 55.16 (1997): 10694.' \
                '\n[11] Luo, Xiangpeng, et al. "Ultrafast modulations and detection of a ferro-rotational charge density wave using time-resolved electric quadrupole second harmonic generation." Physical review letters 127.12 (2021): 126401.' \
                '\n[12] Jin, Wencan, et al. "Observation of a ferro-rotational order coupled with second-order nonlinear optical fields." Nature Physics 16.1 (2020): 42-46.' \
                '\n[13] Anisimov, A. N., N. A. Perekopaiko, and Aleksei Valerevich Petukhov. "Relationship between the anisotropy of reflected second harmonic radiation and the orientation of the crystal surface." -Soviet journal of quantum electronics 21.1 (1991): 82.' \
                '\n[14] Newnham, Robert E.Properties of materials: anisotropy, symmetry, structure.Oxford university press, 2005.'
    return reference

def disclaimer():
    disclaimer = open('Core/Misc/License.txt', 'rt')
    disclaimer = disclaimer.read()
    return disclaimer

def ack():
    acknowledge = 'This work was supported by NSF EPM Grant No. DMR-2129879 ' \
                  '\n\nWe would like to give a special thanks to: \nBrian Opatosky, Matt Galinger, J Isaac Garcia'
    return acknowledge


def showSymbol(symbol):
    if str(symbol) == 'theta':
        return chr(952)
    else:
        return symbol

def parse(d):
    dictionary = {}
    # Removes curly braces and splits the pairs into a list
    pairs = d.strip('{}').split(', ')
    for i in pairs:
        pair = i.split(': ')
        # Other symbols from the key-value pair should be stripped.
        dictionary[pair[0].strip('\'\'\"\"')] = pair[1].strip('\'\'\"\"')
    return dictionary