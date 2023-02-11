# Imports
try:
  import os
  import requests
  import time
  import datetime
  from colorama import Fore, Style
except:
  print("Error: Missing required modules. Please install the following modules: os, requests, time, datetime, colorama")


class Files():
  appUserFile = str("C:/Users/" + os.getlogin() + "/Python-SafeGuard/SafeGuard.app");
  appUserFileFolder = str("C:/Users/" + os.getlogin() + "/Python-SafeGuard");
  
  pythondiscreteFile = str("C:/Users/" + os.getlogin() + "/Python-SafeGuard/resources/SafeGuard-Python-Discrete.py");
  pythondiscreteFileFolder = str("C:/Users/" + os.getlogin() + "/Python-SafeGuard/resources");
  
  tronAdmin =  str("C:/Users/" + os.getlogin() + "/Python-SafeGuard/resources/tronAdmin");
  tronAdminFolder = str("C:/Users/" + os.getlogin() + "/Python-SafeGuard/resources");
  
  tronPath = str("C:/Users/" + os.getlogin() + "/Python-SafeGuard/resources/tron");
  tronPathFolder = str("C:/Users/" + os.getlogin() + "/Python-SafeGuard/resources");
  
  appFile = str("C:/Users/" + os.getlogin() + "/Python-SafeGuard/resources/SafeGuard.cmd");
  appUserFileFolder = str("C:/Users/" + os.getlogin() + "/Python-SafeGuard/resources");
  
  pythonFile = str("C:/Users/" + os.getlogin() + "/Python-SafeGuard/resources/SafeGuard-Python.py");
  pythonFileFolder = str("C:/Users/" + os.getlogin() + "/Python-SafeGuard/resources");
  
  logFile = str("C:/Users/" + os.getlogin() + "/Python-SafeGuard/resources/logs.txt");
  logFileFolder = str("C:/Users/" + os.getlogin() + "/Python-SafeGuard/resources");
  
  knownThreatFile = str("C:/Users/" + os.getlogin() + "/Python-SafeGuard/resources/threatList.sg");
  knownThreatFileFolder = str("C:/Users/" + os.getlogin() + "/Python-SafeGuard/resources");
 
  
sleep = time.sleep(3)
now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n\n"
debug = True

def clear():
  clr = os.system('cls' if os.name in ('nt', 'dos') else 'clear')
  return clr

def CUSTOMinstall(URL, Destination, NewName, FileExt=""):

  # Download and write to file
  file_content = requests.get(URL)
  open(Destination + '/' + NewName + FileExt, "wb").write(file_content.content)
  with open(Files.logFile, "a") as f:
    f.write("Downloaded file to: " + Destination + " - AT: " + now)
  if debug:
    print(Fore.GREEN + "Downloaded file to: " + Destination + Style.RESET_ALL)


def preRun():
  # Developers cover your eyes!
  if not os.path.exists(Files.tronPath):
    CUSTOMinstall("http://www.bmrf.org/repos/tron/Tron%20v12.0.5%20(2023-02-02).exe" ,Files.tronPathFolder, "Tron v12.0.5 (2023-02-02)", ".exe")
    with open(Files.logFile, "a") as f:
      f.write("Program file [" + Files.tronPath + "] !REDOWNLOADED! - AT: " + now)
    if debug:
      print(Fore.RED + "Program file [" + Files.tronPath + "] !MISSING! - AT: " + now + Style.RESET_ALL)

  if not os.path.exists(Files.pythonFile):
    CUSTOMinstall("https://itzcozi.github.io/SafeGuard/data/safeguard-files/SafeGuard-Python%20.py" ,Files.pythonFileFolder, "SafeGuard-Python", ".py")
    with open(Files.logFile, "a") as f:
      f.write("Program file [" + Files.pythonFile + "] !REDOWNLOADED! - AT: " + now)
    if debug:
      print(Fore.RED + "Program file [" + Files.pythonFile + "] !MISSING! - AT: " + now + Style.RESET_ALL)

  if not os.path.exists(Files.knownThreatFile):
    CUSTOMinstall("https://itzcozi.github.io/SafeGuard/data/safeguard-files/threatList%20.sg" ,Files.knownThreatFileFolder, "threatList", ".sg")
    with open(Files.logFile, "a") as f:
      f.write("Program file [" + Files.knownThreatFile + "] !REDOWNLOADED! - AT: " + now)
    if debug:
      print(Fore.RED + "Program file [" + Files.knownThreatFile + "] !MISSING! - AT: " + now + Style.RESET_ALL)

  if not os.path.exists(Files.logFile):
    CUSTOMinstall("https://itzcozi.github.io/SafeGuard/data/safeguard-files/logs.txt" ,Files.logFileFolder, "logs", ".txt")
    with open(Files.logFile, "a") as f:
      f.write("Program file [" + Files.logFile + "] !REDOWNLOADED! - AT: " + now)
    if debug:
      print(Fore.RED + "Program file [" + Files.logFile + "] !MISSING! - AT: " + now + Style.RESET_ALL)
  
  else:
    with open(Files.logFile, "a") as f:
      f.write("All files !ACCOUNTED! - AT: " + now)
    if debug:
      print(Fore.GREEN+"All files accounted for."+Style.RESET_ALL)
      clear()
