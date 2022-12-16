# CPRG-216
# Project Class
# Student Name: Henry Chung
# Student Number: 000887335
# Group 6
# Reponsible Class: Laboratories

def printMenu(): # menu function
    print('\nLaboratories Menu:\n')
    print('1 - Display laboratories list')
    print('2 - Add laboratory')
    print('3 - Back to the Main Menu')
    

def writeListOfLabsToFile(): # function to write the data into file
    contentFile = ['Facility_Cost', 'Facility1_800', 'Facility2_1200', 'Facility3_500', 'Facility4_50']
    createFile = open('laboratories.txt', 'w+')
    for item in contentFile:
        createFile.write(item + '\n')

class labInfo:
    """A class to create lab object
    Attributes:
        newLabname(str):string that enter the lab name
        newLabcost(int):integer that represent the cost of the lab
        newLabInfo(str):string that combine NewLabName + NewLabCost"""
    
    # Constructor:
    def __init__ (self,newLabname,newLabcost, newLabInfo): 
        self.newLabname = newLabname
        self.newLabcost = newLabcost
        self.newLabInfo = newLabInfo

    # Methods:
    def readLaboratoriesFile(): # Function of reading the laboratories file
        labList = open('laboratories.txt', 'r')
        dataList = labList.read()
        dataList = dataList.replace('Facility', 'Lab')
        dataList = dataList.replace('_','\t')
        return dataList

    def displayLabsList(): # Display the name of all list
        list = labInfo.readLaboratoriesFile()
        print('\n')
        print(list)
    
    def enterLaboratoryInfo(): #input new lab name and new lab cost
        newLabName = input('\nEnter Laboratory Name: ')
        newLabCost = int(input('\nEnter Laboratory cost: '))
        newLabInfo = str(newLabName)+'_'+str(newLabCost)
        return newLabInfo

    def formatLabInfo(): # format the output into a correct format
        formatLabInfo = labInfo.enterLaboratoryInfo()
        outputLabInfo = formatLabInfo.replace("Lab", "Facility")
        return outputLabInfo

    def addLabToFile(): # add the formatted info to the file
        file_object = open('laboratories.txt', "a+")
        file_object.seek(0)
        file_object.write(labInfo.formatLabInfo())
        file_object.write("\n")

writeListOfLabsToFile() #write info to laboratories.txt for editing
while(True):
    printMenu()
    labchoice = int(input('\nPlease select your options:\n'))
    if labchoice == 1:
        labInfo.displayLabsList()
    elif labchoice == 2:
        labInfo.addLabToFile()
    elif labchoice == 3:
        loop = 0
    else:
        print('\nInvalid option. Please enter a number between 1 and 3.')
        