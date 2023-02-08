# Make a program to check the known directorys for folders which usally hold viruses (Windows/Temp, roaming/Peer2Profit, All other malawarebytes detections) PYTHON PORT FROM C++
# https://replit.com/@cozi08/NewProgram#SafeGuard.cpp

"""
TODO: Add logs to all functions with date and time
TODO: Remeber to add fileChecker function from c++ code
TODO: When done finish C++ version
"""


# Imports
import os
import sys
import datetime
import time
from colorama import Fore, Style


# Global Variables
healthCheck = True
knownsThreatFile = "data/knownThreats.sg"
now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n\n"



# Load threats into 'knownThreats' list
knownThreats = open("data/topics.txt", "r")
data = knownsThreatFile.read()
data_into_list = data.split("\n")
print(data_into_list)
knownsThreatFile.close()



# Functions
def clear():
  clr = os.system('cls' if os.name in ('nt', 'dos') else 'clear')
  return clr



def checkWindowsUpdate():
  os.system("Install-Module PSWindowsUpdate")
  os.system("Get-WindowsUpdate")

  updateConfirmation = input("Do you want to update Windows10? (y/n) \n")

  if updateConfirmation=='y':
    os.system("Install-WindowsUpdate")

  if updateConfirmation=='n':
    print("Update skipped")