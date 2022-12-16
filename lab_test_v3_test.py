# CPRG-216
# Project Class
# Student Name: Henry Chung
# Student ID: 000887335
# Group 6
# Reponsible for "Lab" Class
import pandas as pd

menuOptions = {
    1: 'Display laboratories list',
    2: 'Add laboratory',
    3: 'Back to the Main Menu',
}

def printMenu():
    print('\nLaboratories Menu:\n')
    for key in menuOptions.keys():
        print (key, '-', menuOptions[key])

class lab:
    """A class to create lab object
    Attributes:
        newLabname(str):string that enter the lab name
        newLabcost(int):integer that represent the cost of the lab
        newLabInfo(str):string that combine NewLabName + NewLabCost"""
    
    def __init__ (self, newLabname, newLabCost, newLabInfo):
        self.newlabname = newLabname
        self.newlabcost = newLabCost
        self.newlabinfo = newLabInfo
        
    def readLaboratoriesFile():
        labList = open('laboratories.txt', 'r')
        return labList

    def displayLabsList():
        list = lab.formatLabInfo()
        print(list)
    
    def enterLaboratoryInfo():
        newLabName = input('\nEnter Laboratory facility: ')
        newLabCost = int(input('\nEnter Laboratory cost: '))
        newLabInfo = str(newLabName)+'_'+str(newLabCost)
        return newLabInfo
    
    def formatLabInfo():
        newlab=open('laboratories.txt','r')
        newLabList = newlab.read()
        newLabList = newLabList.replace("_","\t")
        return newLabList
    
    def addLabToFile():
        list = lab.formatLabInfo()
        print (list)

        
        

while(True):
    printMenu()
    menuSelection = ''
    menuSelection = input('\nPlease select your options: ')
    menuSelection = menuSelection.strip()
    if menuSelection == "1":
        lab.displayLabsList()
    elif menuSelection == "2":
        lab.enterLaboratoryInfo()
    elif menuSelection == "3":
        loop = 0
    else:
        print('Invalid option. Please enter a number between 1 and 3.')
        