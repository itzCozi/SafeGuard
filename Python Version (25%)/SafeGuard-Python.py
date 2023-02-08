# Make a program to check the known directorys for folders which usally hold viruses (Windows/Temp, roaming/Peer2Profit, All other malawarebytes detections) PYTHON PORT FROM C++
# https://replit.com/@cozi08/NewProgram#SafeGuard.cpp
"""
TODO: Add logs to all functions with date and time
TODO: Remeber to add fileChecker function from c++ code
TODO: Look at https://learn.microsoft.com/en-us/microsoft-365/security/intelligence/safety-scanner-download?view=o365-worldwide and maybe run it in phase_4
TODO: When done finish C++ version
"""

# Imports
import os
import subprocess
import sys
import datetime
import shutil
from colorama import Fore, Style

# Global Variables
knownsThreatFile = "data/knownThreats.sg"
now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n\n"

# Triggers
debug = True
sickbay = False
systemRestore = True
diskCleanup = True

# Load threats into 'knownThreats' list
knownThreats = open("resources/knownThreats.txt", "r")
data = knownsThreatFile.read()
data_into_list = data.split("\n")
print(data_into_list)
knownsThreatFile.close()


# Functions
def clear():
  clr = os.system('cls' if os.name in ('nt', 'dos') else 'clear')
  return clr


def checkWindowsUpdate(sickbay):
  os.system("Install-Module PSWindowsUpdate")
  os.system("Get-WindowsUpdate")

  updateConfirmation = input("Do you want to update Windows10? (y/n) \n")

  if updateConfirmation == 'y' or sickbay == True:
    os.system("Install-WindowsUpdate")

    # Log
    with open("resources/logs.sg") as f:
      f.write("Windows10 updated - AT: " + now)
      if debug == True:
        print(Fore.BLUE + "Windows updated AT: " + now + Style.RESET_ALL)

  if updateConfirmation == 'n':
    print("Update skipped")

  else:
    print(Fore.RED + "Invaild Input!"+ Style.RESET_ALL)


def systemRestore(systemRestore, sickbay):
  if systemRestore == True or sickbay == True:
    os.system("DISM.exe /Online /Cleanup-image /Restorehealth")
    os.system("sfc /scannow")

    # Log
    with open("resources/logs.sg") as f:
      f.write("System restored - AT: " + now)
      if debug == True:
        print(Fore.BLUE + "System restored - AT: " + now + Style.RESET_ALL)
  
  else:
    # Log
    with open("resources/logs.sg") as f:
      f.write("System restore !SKIPPED! - AT:" + now)
      if debug == True:
        print(Fore.BLUE + "System restore !SKIPPED! - AT:" + now + Style.RESET_ALL)


def diskCleanup(diskCleanup, sickbay):
  if diskCleanup == True or sickbay == True:
    os.system("c:\windows\SYSTEM32\cleanmgr.exe /cDrive")

    # Log
    with open("resources/logs.sg") as f:
      f.write("Disk cleanup - AT:" + now)
      if debug == True:
        print(Fore.BLUE + "Disk cleanup - AT:" + now + Style.RESET_ALL)

  else:
    # Log
    with open("resources/logs.sg") as f:
      f.write("Disk cleanup !SKIPPED! - AT:" + now)
      if debug == True:
        print(Fore.BLUE + "Disk cleanup !SKIPPED! - AT:" + now + Style.RESET_ALL)


def startTron():
  subprocess.call([r'resources/tron.bat'])

  # Log
  with open("resources/logs.sg") as f:
    f.write("Tron.bat activated - AT:" + now)
    if debug == True:
      print(Fore.BLUE + "Tron.bat activated - AT" + now + Style.RESET_ALL)


def checkDirectorys():
  for iteam in data_into_list:
    
    if iteam.path.isdir() == False:
      return False
      
    if iteam.path.isdir() == True:

      # Log directory detected
      with open("resources/logs.sg") as f:
        f.write("[" + iteam + "] Directory detected - AT:" + now)
      if debug == True:
        print(Fore.BLUE + "[" + iteam + "] Directory detected - AT:" + now + Style.RESET_ALL)
      
      # Delete detected directory
      shutil.rmtree(iteam)

       # Log directory deleted
      with open("resources/logs.sg") as f:
        f.write("[" + iteam + "] Directory deleted - AT:" + now)
      if debug == True:
        print(Fore.BLUE + "[" + iteam + "] Directory deleted - AT:" + now + Style.RESET_ALL)
      
      return True


def PHASE_1():
  # This will run checkDirectory and systemRestore

  # Log
  with open("resources/logs.sg") as f:
    f.write("SafeGuard initalized - AT:" + now)
    if debug == True:
      print(Fore.BLUE + "SafeGuard initalized - AT:" + now + Style.RESET_ALL)

      systemRestore(systemRestore == True, sickbay == False)
      if checkDirectorys(checkDirectorys == True, sickbay == False) == True:
        print("!THREAT-DETECTED! Starting Phase-2")
        PHASE_2()

def PHASE_2():
  # This will run diskcleanup after that ask to run windowsUpdate and  tron

  print("PHASE-2")

  diskCleanup(diskCleanup == True, sickbay == True)
  checkWindowsUpdate(sickbay == True)