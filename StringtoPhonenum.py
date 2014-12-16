'''Converts string to phone number format.
eg. 435 4f3 sdwJ -> 435 433 7395
'''

from sys import version_info
import sys

def two():
    sys.stdout.write('2')

def three():
    sys.stdout.write('3')

def four():
    sys.stdout.write('4')

def five():
    sys.stdout.write('5')

def six():
    sys.stdout.write('6')

def seven():
    sys.stdout.write('7')

def eight():
    sys.stdout.write('8')

def nine():
    sys.stdout.write('9')

#converts string to number
def getNumber(string): 
#Uses a Dictonary for quick O(1) conversion.
    options = {'A' : two,
               'B' : two,
               'C' : two,
               'D' : three,
               'E' : three,
               'F' : three,
               'G' : four,
               'H' : four,
               'I' : four,
               'J' : five,
               'K' : five,
               'L' : five,
               'M' : six,
               'N' : six,
               'P' : seven,
               'Q' : seven,
               'R' : seven,
               'S' : seven,
               'T' : eight,
               'U' : eight,
               'V' : eight,
               'W' : nine,
               'X' : nine,
               'Y' : nine
        }
#Iterates once through given string and does required conversions.
    charList = list(string)
    for index in charList:
        if(index.isdigit() or index == '-'):
            sys.stdout.write(index)
        else:
            options[index]()
        
#Tests that Python major version > 2
#This is important in that the way input is done.
py3 = version_info[0] > 2 

if py3:
    response = input("Enter a string: ")
    response = response.upper()
    getNumber(response)
else:
    response = raw_input("Enter a string: ")
    response = response.upper()
    getNumber(response)
