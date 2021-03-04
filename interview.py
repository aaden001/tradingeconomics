# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 00:47:17 2021

@author: adeni
"""
#imports
import tradingeconomics as te
import sys   #for command line arguements
import re #for splitting user inputs


def check_valid_input(get_sytem_arguments):
    count = 1 # track how many times wrong input is taken in
    pattern = re.compile(r"(.\\interview.py)\s([\w]*)\s([\w]*)\s([\w]*)")    
    while len(get_sytem_arguments) < 4:
        count = count +1
        
        print("You need to enter input in this format.\n\n"+
              ".\interview.py BYcontry namecountry1 countryname2 \n"+"\n or\n"
              ".\interview.py BYcontry namecountry1 countryname2 ")
        getInput = input("\n Waiting for input. \n")
        
        m = pattern.match(getInput)
        if m != None:
            final = [m.group(0),m.group(1),m.group(2),m.group(3)]
            return final
        else:
            print("Wrong input Please try again\n\n")
        if count > 5: #gives user only 5 trials
            break;
    else:
        #get arguemnet var
        return final
def buildqueryStrings():
    print("same time")
def download_data_byCountry(inputVals):
    print("https://brains.tradingeconomics.com/v2/search/wb,fred,comtrade?q=nigeria&pp=50&p=0&_=1557934352427&stance=2.")
if __name__ == "__main__":
    print(check_valid_input(sys.argv))
    print("hellow")