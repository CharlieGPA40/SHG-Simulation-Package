from sympy.parsing.sympy_parser import parse_expr
import os

def reference():
    reference = open('Core/Misc/References.txt', 'rt')
    reference = reference.read()
    return reference

def disclaimer():
    disclaimer = open('Core/Misc/License.txt', 'rt')
    disclaimer = disclaimer.read()
    return disclaimer

def ack():
    acknowledge = open('Core/Misc/Acknowledge.txt', 'rt')
    acknowledge = acknowledge.read()
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

def current_version():
    version = open('Current Version.txt', 'rt')
    version = version.read()
    return version
