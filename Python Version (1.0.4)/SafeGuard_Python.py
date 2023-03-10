# Make a program to check the known directorys for folders which usally hold viruses (Windows/Temp, roaming/Peer2Profit, All other malawarebytes detections) PYTHON PORT FROM C++
"""
TODO: Look into adding a file shredder instead of just deleting the file (https://dev.to/geofspot/how-to-shred-a-file-in-python-545f)
TODO: Ask about C++ problem on stackoverflow (https://stackoverflow.com/a/20372880)
TODO: Fix C++ problem
"""

# Imports
try:
  import os
  import requests
  import sys
  import time
  import glob
  import datetime
  import shutil
  import ctypes
  import subprocess as sp
  from colorama import Fore, Style
except:
  print("Error: Missing required modules. Please install the following modules: os, requests, time, datetime, colorama, shutil, ctypes")

# File Imports
try:
  from PreChecks import preRun
  from PreChecks import autoUpdate
except:
  print("Error: SafeGuard PreChecks.py is missing. Please install PreChecks.")


# Pre run message
if ctypes.windll.shell32.IsUserAnAdmin():
  pass
else:
  print("SafeGuard Version-1.0.3 Anti-virus protection \nThis window will close momentarily...")


# Global Variables
class Files():
  appUserFile = str("C:/Users/" + os.getlogin() + "/Python-SafeGuard/SafeGuard.app")
  pythondiscreteFile = str("C:/Users/" + os.getlogin() + "/Python-SafeGuard/resources/SafeGuard-Python-Discrete.py")
  tronAdmin = str("C:/Users/" + os.getlogin() + "/Python-SafeGuard/resources/tronAdmin")
  tronPath = str("C:/Users/" + os.getlogin() + "/Python-SafeGuard/resources/tron")
  appFile = str("C:/Users/" + os.getlogin() + "/Python-SafeGuard/resources/SafeGuard.cmd")
  pythonFile = str("C:/Users/" + os.getlogin() + "/Python-SafeGuard/resources/SafeGuard-Python.py")
  logFile = str("C:/Users/" + os.getlogin() + "/Python-SafeGuard/resources/logs.txt")
  knownThreatFile = str("C:/Users/" + os.getlogin() + "/Python-SafeGuard/resources/threatList.sg")


sleep = time.sleep(3)
now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n\n"

# Triggers
debug = True
sickbay = False
systemRestore = True
diskCleanup = True

preRun()
autoUpdate()

# Load threats into 'knownThreats' list
knownThreats = open(Files.knownThreatFile)
data = knownThreats.read()
data_into_list = data.split("\n")
with open(Files.logFile, "a") as f:
  if os.path.getsize(Files.knownThreatFile) == 0:
    f.write("!THREAT-LIST-EMPTY! No directorys scanned. - AT: " + now)
    print("!THREAT-LIST-EMPTY! No directorys scanned.")
    knownThreats.close()
  if debug:
    print("!THREATS-LOADED! ")
    print(data_into_list)
    knownThreats.close()
  else:
    f.write("!THREATS-LOADED! " + now)
    knownThreats.close()


# Functions
def is_admin():
  try:
    return ctypes.windll.shell32.IsUserAnAdmin()
  except:
    return False


def URLinstall(URL, Destination, NewName, FileExt=""):
  FileExt = URL[-4:]

  # Download and write to file
  file_content = requests.get(URL)
  open(Destination + '/' + NewName + FileExt, "wb").write(file_content.content)
  with open(Files.logFile, "a") as f:
    f.write("Downloaded file to: " + Destination + " - AT: " + now)
  if debug:
    print(Fore.BLUE + "Downloaded file to: " + Destination + Style.RESET_ALL)


def CUSTOMinstall(URL, Destination, NewName, FileExt=""):
  # Download and write to file
  file_content = requests.get(URL)
  open(Destination + '/' + NewName + FileExt, "wb").write(file_content.content)
  with open(Files.logFile, "a") as f:
    f.write("Downloaded file to: " + Destination + " - AT: " + now)
  if debug:
    print(Fore.BLUE + "Downloaded file to: " + Destination + Style.RESET_ALL)


def clear():
  clr = os.system('cls' if os.name in ('nt', 'dos') else 'clear')
  return clr


def checkWindowsUpdate(sickbay):
  os.system("Install-Module PSWindowsUpdate")
  os.system("Get-WindowsUpdate")
  clear()

  updateConfirmation = input(
    "Are you sure you want to update Windows10? (y/n) \n")

  if updateConfirmation == 'y' or sickbay is True:
    os.system("Install-WindowsUpdate")

    # Log
    with open(Files.logFile, "a") as f:
      f.write("Windows10 updated - AT: " + now)
    if debug:
      print(Fore.BLUE + "Windows updated AT: " + now + Style.RESET_ALL)

  if updateConfirmation == 'n':
    with open(Files.logFile, "a") as f:
      f.write("Update skipped - AT: " + now)
    if debug:
      print(Fore.BLUE + "Update skipped" + now + Style.RESET_ALL)

  else:
    print(Fore.RED + "Invaild Input!" + Style.RESET_ALL)


def systemRestore(systemRestore, sickbay):
  if systemRestore is True or sickbay is True:
    os.system("DISM.exe /Online /Cleanup-image /Restorehealth")
    time.sleep(3)
    os.system("sfc /scannow")

    # Log
    with open(Files.logFile, "a") as f:
      f.write("System restored - AT: " + now)
    if debug:
      print(Fore.GREEN + "System restored - AT: " + now + Style.RESET_ALL)

  else:
    # Log
    with open(Files.logFile, "a") as f:
      f.write("System restore !SKIPPED! - AT:" + now)
    if debug:
      print(Fore.RED + "System restore !SKIPPED! - AT:" + now + Style.RESET_ALL)


def diskCleanup(diskCleanup, sickbay):
  if diskCleanup is True or sickbay is True:

    print(shutil.disk_usage("C:/"))

    diskCleanupYorN = input("Do you want to run disk cleanup? (y/n) \n")

    if diskCleanupYorN == 'y':
      os.system("c:\windows\SYSTEM32\cleanmgr.exe /cDrive")

      # Log
      with open(Files.logFile, "a") as f:
        f.write("Disk cleanup - AT:" + now)
      if debug:
        print(Fore.GREEN + "Disk cleanup - AT:" + now + Style.RESET_ALL)

    else:
      with open(Files.logFile, "a") as f:
        f.write("Disk cleanup !SKIPPED! - AT:" + now)
      if debug:
        print(Fore.RED + "Disk cleanup !SKIPPED! - AT:" + now + Style.RESET_ALL)
  else:
    print(Fore.BLUE + "Failed to run disk cleanup" + Style.RESET_ALL)


def installRUNSafetyScanner():
  CUSTOMinstall("https://go.microsoft.com/fwlink/?LinkId=212732", str("C:/Users/" + os.getlogin() + "/Downloads"), "SafetyScanner", ".exe")
  os.startfile(str("C:/Users/" + os.getlogin() + "/Downloads/SafetyScanner.exe"))


def shred(file):
  sp.call(f'shred -zvu -n 10 {file}', shell = True)

  # Log
  with open(Files.logFile, "a") as f:
    f.write("File shreder activated - AT:" + now)
  if debug:
    print(Fore.BLUE + "File shreder activated - AT" + now + Style.RESET_ALL)


def startTron():
  os.startfile(Files.tronAdmin)

  # Log
  with open(Files.logFile, "a") as f:
    f.write("Tron.bat activated - AT:" + now)
  if debug:
    print(Fore.BLUE + "Tron.bat activated - AT" + now + Style.RESET_ALL)


def checkDirectorys():
  for iteam in data_into_list:

    if os.path.isdir(iteam) is True:
      # User notification
      print(Fore.RED + "Directory detected" + Style.RESET_ALL)

      # Log directory detected
      with open(Files.logFile, "a") as f:
        f.write("[" + iteam + "] Directory !DETECTED! - AT:" + now)
      if debug:
        print(Fore.RED + "[" + iteam + "] Directory !DETECTED! - AT:" + now + Style.RESET_ALL)

      # Delete detected directory
      shutil.rmtree(iteam)

      # Log directory deleted
      with open(Files.logFile, "a") as f:
        f.write("[" + iteam + "] Directory !DELETED! - AT:" + now)
      if debug:
        print(Fore.RED + "[" + iteam + "] Directory !DELETED! - AT:" + now + Style.RESET_ALL)

      return True

    if os.path.isdir(iteam) is False:
      print(Fore.RED + "No directory detected" + Style.RESET_ALL)


def PHASE_1():
  # This will run checkDirectory and systemRestore

  print(Fore.GREEN + "PHASE-1")

  # Log
  with open(Files.logFile, "a") as f:
    f.write("SafeGuard PHASE-1 initalized - AT:" + now)
  if debug:
    print(Fore.BLUE + "SafeGuard PHASE-1 initalized - AT:" + now + Style.RESET_ALL)

  # If checkDirectorys() returns true then run PHASE_2
  if checkDirectorys():
    print(Fore.RED + Style.BRIGHT + "!RUNNING-EMMERGENCY-PROCEDURE!" + Style.RESET_ALL)
    systemRestore(systemRestore is True, sickbay is False)
    clear()

    print("!THREAT-DETECTED! Start Phase-2?")
    PHASE_2YorN = input("Your system scanned a malacious folder, do you want to take action? (y/n) \n")

    if PHASE_2YorN == 'y':
      PHASE_2()
    else:
      print("SafeGuard will now exit")
      time.sleep(3)
      sys.exit()

  else:
    print("SafeGuard will now exit")
    time.sleep(3)
    sys.exit()


def PHASE_2():
  # This will run diskcleanup after that ask to run windowsUpdate and tron

  clear()
  print(Fore.YELLOW + "PHASE-2")

  # Log
  with open(Files.logFile, "a") as f:
    f.write("SafeGuard PHASE-2 initalized - AT:" + now)
  if debug:
    print(Fore.BLUE + "SafeGuard PHASE-2 initalized - AT:" + now + Style.RESET_ALL)

  print(
    "Your system scanned a malacious folder, don't worry we have removed it for you\n"
    "althogh the program that made the folder may still be on your system.\n"
    "Do you want to prep your system for disinfection? \n")
  prepYorN = input("Do you want to run disk cleanup and windows update? (y/n) \n")

  if prepYorN == 'y':
    diskCleanup(diskCleanup is True, sickbay is False)
    systemRestore(systemRestore is True, sickbay is False)
  else:
    print("Prep skipped... QUITTING")
    sys.exit()

  SafteyscanYorN = input("Do you want to remove threats? (y/n) \n")

  if SafteyscanYorN == 'y':
    print("\n\n Activating SafteyScan Please wait... \n")
    installRUNSafetyScanner()
    input("Press enter to continue... \n")
    PHASE_3()

  if SafteyscanYorN == 'n':
    print(Fore.RED + "SafteyScan skipped" + Style.RESET_ALL)

    # Log
    with open(Files.logFile, "a") as f:
      f.write("!SCAN-SKIPPED! - AT:" + now)
    if debug:
      print(Fore.RED + "!SCAN-SKIPPED! - AT:" + now + Style.RESET_ALL)

  else:
    print(Fore.RED + "Invaild Input!" + Style.RESET_ALL)


def PHASE_3():
  # This will run tron as admin and then when tron is done it run stinger

  clear()
  print(Fore.RED + "PHASE-3")

  # Log
  with open(Files.logFile, "a") as f:
    f.write("SafeGuard PHASE-3 initalized - AT:" + now)
  if debug:
    print(Fore.BLUE + "SafeGuard PHASE-3 initalized - AT:" + now + Style.RESET_ALL)

  attemptUpdate = input("Would you like to update your PC? (y/n)")

  if attemptUpdate == "y":
    checkWindowsUpdate(sickbay is True)
  else:
    print(Fore.BLUE + "Update Skipped" + Style.RESET_ALL)

  time.sleep(3)
  clear()

  print("\n\n Activating Tron Please wait... \n")
  print("Click 'Yes' when asked to run as admin \n")
  time.sleep(5)

  startTron()

  # Log finished
  with open(Files.logFile, "a") as f:
    f.write("SafeGuard !THREAT-ACTION-FINISHED! - AT:" + now)
  if debug:
    print(Fore.BLUE + "SafeGuard !THREAT-ACTION-FINISHED! - AT:" + now + Style.RESET_ALL)

  # Start stinger
  StingerYorN = input("Do you want to run stinger it will help keep your device protected in the future? (y/n) \n")

  if StingerYorN == 'y':
    URLinstall("https://downloadcenter.trellix.com/products/mcafee-avert/Stinger/stinger64.exe", "Downloads", "Stinger")
    os.startfile(str("C:/Users/" + os.getlogin() +"/Python-SafeGuard/resources/tron/resources/Stinger.exe"))
  else:
    print(Fore.RED + "Stinger skipped" + Style.RESET_ALL)


# Check if program running as admin
if is_admin():
  clear()
  PHASE_1()
else:
  # Run the program with admin perms
  ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
