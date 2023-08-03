# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 09:50:12 2021

@author: Dean
"""
import os
import sys 
import yaml
import textwrap
from yaml.loader import SafeLoader
from datetime import date #imports date to allow for accurate updated year info
from datetime import time 
import datetime
#import colorama
#from colorama import Fore,Back,Style
path = os.path.abspath(__file__)
def openEntry(data): # - Displays information from a dict
        rate = data['rate']
        date = data['date']
        time = data['time']
        sig = data['signature']
        desc = data['desc']
        
        os.system('clear')
        print('='*30)
        print(f"""    {date} || {time}""")
        print('='*30)
        print('\n'.join(textwrap.wrap(desc,30))+"\n")
        print(f"""{sig},\n-Dean""")


def modifyEntry(entry): #Replace a file's contents
    # TODO: Gotta update this
    print("This will modify the text of: ", entry)
    if os.path.exists(getFileName(entry)): # if file exists, delete it, and replace with new one
        os.remove(getFileName(entry)) #delete
        content = input("How was your day today?: ")
        rate = input('What would you rate today? 1-5: ')
        writeNewFile(content,entry,rate)
        print("Entry for "+ entry + " successfully updated!")

def writeNewFile(data):#Creates new file

    f = open(f"{data['date']}.yml", "w")
    f.write(yaml.dump(data))
    f.close()
    print('File has been created!')
    openEntry(data)

def addToEntry(entry): #Adds a supplied text to an existing text document below the last entry
    # TODO: Needs to be updated
    file = open(getFileName(entry))
    line = file.read()
    line = line
    file.close()
    
    addition = input("What else happened this day?")
    line = line +'\n'+ addition
    file = open(getFileName(entry), 'w')
    file.write(line)
    file.close()
    print("Entry for "+entry + " successfully updated!")
    print(line)

def getRateDisplay(filename):
    # TODO: this can be updated
    ln = str(filename) #ln = NEW:'2021-10-20.3.txt' OLD:'2001-09-11.txt'
    rate = ln[11]
    try:
        
        if rate == '1':
            print(">:(")
            return
        elif rate == '2':
            print(":(")
            return
        elif rate =='3':
            print(':|')
        elif rate == '4':
            print(':)')
        elif rate == '5':
            print(':D')
        elif int(rate) > 5:
            print("Wow, whats a high number!")
        elif int(rate) > 0:
            print("Seems like you had a rough day")
        else:
                print("I don't know how you felt this day")
    except ValueError:
        print("No Valid Rating for this day")
def getFileName(date):
    for filename in os.listdir():#for every file in the current path,
        if filename.startswith(str(date)):#if it starts with todays_date
            return filename #Ex:2021-10-20.3.txt

def dailyEntry(path): #Entry for the current date
    todays_date = str(date.today()) 
    print(f'listing every file: {os.listdir()}')
    for filename in os.listdir():#for every file in the current path,

        print(f'Mathing files:{filename} = = {todays_date}.yml . . .')

        if filename.startswith(todays_date):#if it starts with todays_date
            print(f"{filename} was FOUND. Attempting to open...")
            searchEntry(todays_date) #display contents
            return
    else:    
        print("You have not made an entry today!")
        content = input("How was your day today?: ")
        rate = input('What would you rate today? 1-5: ')
        writeNewFile(content,todays_date,rate)
        print("Entry for today successfully updated!")

        ########
        data = {
        'rate': 0,
        'desc':'',
        'date': '', # YYYY-MM-DD
        'signature': '',
        'time': ''
        }
        
        today = str(date.today())
        rn = str(datetime.datetime.now())

        data['rate'] = str(input('Rate: '))
        data['desc'] = input('Description: ')
        data['date'] = today
        data['sig'] = input('Signature: ')

        print('Creating...')
        writeNewFile(data)


def searchEntry(date):
    try:
        with open(f"{date}.yml") as f:
            data = yaml.load(f, Loader=SafeLoader)
            print('Found! Attempting to open...')
            openEntry(data)
            return
    except:
         print(f'{date} was not found!!')
         entryInfo(date)

def entryInfo(datetoday):
    data = {
        'rate': 0,
        'desc':'',
        'date': '', # YYYY-MM-DD
        'signature': '',
        'time': ''
    }
    
    today = str(date.today())
    rn = str(datetime.datetime.now())

    data['rate'] = str(input('Rate: '))
    data['desc'] = input('Description: ')
    data['date'] = str(datetoday)
    data['signature'] = input('Signature: ')

    print('Creating...')
    writeNewFile(data)
  
    
def main(): #main function, hold;s menu

     #Records the current file path
    os.system('cls')
    
    directory = 'entries'
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(parent_dir,directory)
    os.chdir(path) #changes the current directory to the entries folder to access the text documents (for organization)
    #Displays menu
    print ("V1.1.2 Current path:\033[0;33;40m",path,'\033[0;37;40m')
    print (30 * '-')
    print ("\033[0;37;40m    D A I L Y - J O U R N A L")
    print (30 * '-')
    print ("1. Today's Entry")
    print ("2. Entry Search by Date")
    print ("3. List all entries")
    print ("4. EXIT")
    print (30 * '-')

    # Get input for menu selection
    choice = input('Enter your choice [1-4] : ')
    choice = int(choice)
     
    #menu choices
    if choice == 1:
        os.system('cls')
        dailyEntry(path)
        input("Press any key to continue...")
        os.system('cls')
        main()#back to menu
           
    elif choice == 2:
            os.system('cls')
            date = input("Enter the date to look for: (YYYY.MM.DD)... ")
            searchEntry(date) # Successful


            """
            overwrite = input('What would you like to modify? (ov/add/r/close)').lower()
            if overwrite == 'ov':#if the user wants to overwrite the data
                modifyEntry(date)
            if overwrite == 'add':#if the user would like to add to their existing entry
               addToEntry(date) 
            if overwrite == 'r':
               rate = input("What would you rate this day?")
               os.rename(getFileName(date),str(date+'.'+rate+".txt"))
               print("File successfuly updated rate!")
            else:
                print('File unchanged.')
            """
            
            
            input("Press any key to continue...")
            main()
    elif choice == 3:
            os.system('cls')
            
            rootdir = os.getcwd() #uses os.walk to "walk" from the root directory to the entries folder
            for subdir, dirs, files in os.walk(rootdir):
                for file in files:
                    if file.endswith(".yml"): 
                        print (file[:-4])
            input("Press any key to continue...")
            main()
    elif choice == 4:
                sys.exit("Program Completed successfully")            
    else:    #default 
            print ("Invalid number. Try again...")
            main()

main()
