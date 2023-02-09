# Make a program to check the known directorys for folders which usally hold viruses (Windows/Temp, roaming/Peer2Profit, All other malawarebytes detections) PYTHON PORT FROM C++
# https://replit.com/@cozi08/NewProgram#SafeGuard.cpp
"""
TODO: Test checkDirectory function
TODO: Finish logs and add color
TODO: Review and refine code
TODO: Add lots of clears
TODO: Add direcory detected and undetected text logs instead of debuglogs
TODO: test all phases and make sure they work
TODO: Look at https://learn.microsoft.com/en-us/microsoft-365/security/intelligence/safety-scanner-download?view=o365-worldwide and maybe run it in phase_4
TODO: When done finish C++ version
"""

# Imports
import os
import subprocess
import sys
import time
import datetime
import shutil
import ctypes
from colorama import Fore, Style

# Global Variables
knownThreatFile = "C:/Users/coope/Python-SafeGuard/resources/threatList.sg"
sleep = time.sleep(3)
shortsleep = time.sleep(1)
now = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n\n")

# Triggers
debug = True
sickbay = False
systemRestore = True
diskCleanup = True
checkDirectorys = True

# Load threats into 'knownThreats' list
knownThreats = open("C:/Users/coope/Python-SafeGuard/resources/threatList.sg", "r")
data = knownThreats.read()
data_into_list = data.split("\n")
print(data_into_list)
knownThreats.close()


# Functions
def is_admin():
  try:
    return ctypes.windll.shell32.IsUserAnAdmin()
  except:
    return False


def clear():
  clr = os.system('cls' if os.name in ('nt', 'dos') else 'clear')
  return clr


def checkWindowsUpdate(sickbay):
  os.system("Install-Module PSWindowsUpdate")
  os.system("Get-WindowsUpdate")
  clear()
  shortsleep

  updateConfirmation = input("Do you want to update Windows10? (y/n) \n")

  if updateConfirmation == 'y' or sickbay == True:
    os.system("Install-WindowsUpdate")

    # Log
    with open("C:/Users/coope/Python-SafeGuard/resources/logs.txt", "w+") as f:
      shortsleep
      f.write("Windows10 updated - AT: " + now)
      if debug == True:
        print(Fore.GREEN + "Windows updated AT: " + now + Style.RESET_ALL)
        shortsleep

  if updateConfirmation == 'n':
    with open("C:/Users/coope/Python-SafeGuard/resources/logs.txt", "w+") as f:
      shortsleep
      f.write("Update skipped - AT: " + now)
    if debug == True:
      print(Fore.RED + "Update skipped" + now + Style.RESET_ALL)
      shortsleep

  else:
    print(Fore.RED + "Invaild Input!" + Style.RESET_ALL)
    shortsleep


def systemRestore(systemRestore, sickbay):
  if systemRestore == True or sickbay == True:
    os.system("DISM.exe /Online /Cleanup-image /Restorehealth")
    sleep
    os.system("sfc /scannow")

    # Log
    with open("C:/Users/coope/Python-SafeGuard/resources/logs.txt", "w+") as f:
      shortsleep
      f.write("System restored - AT: " + now)
      if debug == True:
        print(Fore.GREEN + "System restored - AT: " + now + Style.RESET_ALL)
        shortsleep

  else:
    # Log
    with open("C:/Users/coope/Python-SafeGuard/resources/logs.txt", "w+") as f:
      shortsleep
      f.write("System restore !SKIPPED! - AT:" + now)
      if debug == True:
        print(Fore.RED + "System restore !SKIPPED! - AT:" + now + Style.RESET_ALL)
        shortsleep


def diskCleanup(diskCleanup, sickbay):
  if diskCleanup == True or sickbay == True:
    
    diskCleanupYorN = input("Do you want to run disk cleanup? (y/n) \n")
    
    if diskCleanupYorN == 'y':
      os.system("c:\windows\SYSTEM32\cleanmgr.exe /cDrive")

      # Log
      with open("C:/Users/coope/Python-SafeGuard/resources/logs.txt", "w+") as f:
        shortsleep
        f.write("Disk cleanup - AT:" + now)
        if debug == True:
          print(Fore.BLUE + "Disk cleanup - AT:" + now + Style.RESET_ALL)
          shortsleep

    else:
      with open("C:/Users/coope/Python-SafeGuard/resources/logs.txt", "w+") as f:
        shortsleep
        f.write("Disk cleanup !SKIPPED! - AT:" + now)
        if debug == True:
          print(Fore.RED + "Disk cleanup !SKIPPED! - AT:" + now + Style.RESET_ALL)
          shortsleep
  else:
    print(Fore.RED+"Failed to run disk cleanup"+Style.RESET_ALL)
        
        
def startTron():
  os.startfile("D:/vscode/Workspace/Python-SafeGuard/resources/tronAdmin")

  # Log
  with open("C:/Users/coope/Python-SafeGuard/resources/logs.txt", "w+") as f:
    shortsleep
    f.write("Tron.bat activated - AT:" + now)
    if debug == True:
      print(Fore.RED + "Tron.bat activated - AT" + now + Style.RESET_ALL)
      shortsleep


def checkDirectorys():
  for iteam in data_into_list:

    if os.path.isdir(iteam) == True:
      # User notification
      print(Fore.RED+"Directory detected"+Style.RESET_ALL)
      shortsleep
      
      # Log directory detected
      with open("C:/Users/coope/Python-SafeGuard/resources/logs.txt", "w+") as f:
        shortsleep
        f.write("[" + iteam + "] Directory !DETECTED! - AT:" + now)
      if debug == True:
        print(Fore.RED + "[" + iteam + "] Directory !DETECTED! - AT:" + now + Style.RESET_ALL)
        shortsleep

      # Delete detected directory
      shutil.rmtree(iteam)

      # Log directory deleted
      with open("C:/Users/coope/Python-SafeGuard/resources/logs.txt", "w+") as f:
        shortsleep
        f.write("[" + iteam + "] Directory !DELETED! - AT:" + now)
      if debug == True:
        print(Fore.RED + "[" + iteam + "] Directory !DELETED! - AT:" + now + Style.RESET_ALL)
        shortsleep
      return True
    
    if os.path.isdir(iteam) == False:
      print(Fore.RED+"No directory detected"+Style.RESET_ALL)
      shortsleep
  

def PHASE_1():
  # This will run checkDirectory and systemRestore

  print(Fore.GREEN + "PHASE-1")

  # Log
  with open("C:/Users/coope/Python-SafeGuard/resources/logs.txt", "w+") as f:
    shortsleep
    f.write("SafeGuard PHASE-1 initalized - AT:" + now)
    if debug == True:
      print(Fore.BLUE + "SafeGuard PHASE-1 initalized - AT:" + now + Style.RESET_ALL)
      shortsleep

      #systemRestore(systemRestore == True, sickbay == False)
      sleep
      #If checkDirectorys() returns true then run PHASE_2
      if checkDirectorys():
        print("!THREAT-DETECTED! Start Phase-2? (y/n)")
        PHASE_2YorN = input("Your system scanned a malacious folder, do you want to take action? (y/n) \n")
        
        if PHASE_2YorN == 'y':
          PHASE_2()
        else:
          print("SafeGuard will now exit")
          sleep
          exit()
          

def PHASE_2():
  # This will run diskcleanup after that ask to run windowsUpdate and tron

  clear()
  print(Fore.YELLOW + "PHASE-2")

  # Log
  with open("C:/Users/coope/Python-SafeGuard/resources/logs.txt", "w+") as f:
    shortsleep
    f.write("SafeGuard PHASE-2 initalized - AT:" + now)
    if debug == True:
      print(Fore.BLUE + "SafeGuard PHASE-2 initalized - AT:" + now + Style.RESET_ALL)
      shortsleep

  print("Your system scanned a malacious folder, don't worry we have removed it for you\n"
        "althogh the program that made the folder may still be on your system.\n"
        "Do you want to prep your system for disinfection? \n")
  prepYorN = input("Do you want to run disk cleanup and windows update? (y/n) \n")  
  
  if prepYorN == 'y':
    diskCleanup(diskCleanup == True, sickbay == False)
    #systemRestore(systemRestore == True, sickbay == False)
  else:
    print("Prep skipped... QUITTING")
    quit()

  TronYorN = input("Do you want to remove threats? (y/n) \n")

  if TronYorN == 'y':
    print("\n\n Activating Tron Please wait... \n")
    shortsleep
    startTron()
    PHASE_3()

  if TronYorN == 'n':
    print("Tron skipped")
    shortsleep

  else:
    print(Fore.RED + "Invaild Input!" + Style.RESET_ALL)
    shortsleep


def PHASE_3():
  # This will run tron as admin and then when tron is done it run stinger

  clear()
  print(Fore.RED + "PHASE-3")

  # Log
  with open("C:/Users/coope/Python-SafeGuard/resources/logs.txt", "w+") as f:
    shortsleep
    f.write("SafeGuard PHASE-3 initalized - AT:" + now)
  if debug == True:
    print(Fore.BLUE + "SafeGuard PHASE-3 initalized - AT:" + now + Style.RESET_ALL)

  print("\n\n Activating Tron Please wait... \n")
  print("Click 'Yes' when asked to run as admin \n")
  shortsleep

  startTron()

  # Restart computer after tron is done
  with open("C:/Users/coope/Python-SafeGuard/resources/logs.txt", "w+") as f:
    shortsleep
    f.write("SafeGuard !THREAT-ACTION-FINISHED! - AT:" + now)
  if debug == True:
    print(Fore.BLUE + "SafeGuard !THREAT-ACTION-FINISHED! - AT:" + now + Style.RESET_ALL)
    shortsleep

  # Start stinger
  os.startfile("C:/Users/coope/Python-SafeGuard/resources/tron/resources/stage_0_prep/mcafee_stinger/stinger64.exe")


if is_admin():
  clear()
  shortsleep
  PHASE_1()
else:
  # Re-run the program with admin rights
  ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
