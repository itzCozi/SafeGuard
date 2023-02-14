# Imports
try:
  import os
  import requests
  import hashlib
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

  prechecksFile = str("C:/Users/" + os.getlogin() + "/Python-SafeGuard/resources/PreChecks.py");
  prechecksFolder = str("C:/Users/" + os.getlogin() + "/Python-SafeGuard/resources");

  tronAdmin = str("C:/Users/" + os.getlogin() + "/Python-SafeGuard/resources/tronAdmin")
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


def hashFileLOCAL(file):
  BUF_SIZE = os.path.getsize(file)

  sha256 = hashlib.sha256()

  with open(file, 'rb') as f:
    while True:
      data = f.read(BUF_SIZE)

      if not data:
        break

      sha256.update(data)

  return sha256.hexdigest()


def hashFileURL(url):
  newFile = str("C:/Users/" + os.getlogin() + "/Python-SafeGuard/newFile")
  
  with open (newFile, "w") as f:
    f.write(requests.get(url).text)
    f.close()

  BUF_SIZE = os.path.getsize(newFile)
  sha256 = hashlib.sha256()

  with open(newFile, 'rb') as f:
    while True:
      data = f.read(BUF_SIZE)

      if not data:
        break

      sha256.update(data)
  
  f.close()
  os.remove(newFile)
  
  return sha256.hexdigest()


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
    CUSTOMinstall("http://www.bmrf.org/repos/tron/Tron%20v12.0.5%20(2023-02-02).exe", Files.tronPathFolder, "Tron v12.0.5 (2023-02-02)", ".exe")
    os.startfile(Files.tronPathFolder + "/Tron v12.0.5 (2023-02-02).exe")
    with open(Files.logFile, "a") as f:
      f.write("Program file [" + Files.tronPath + "] !REDOWNLOADED! - AT: " + now)
    if debug:
      print(Fore.RED + "Program file [" + Files.tronPath + "] !MISSING! - AT: " + now + Style.RESET_ALL)

  if not os.path.exists(Files.pythonFile):
    CUSTOMinstall("https://itzcozi.github.io/SafeGuard/data/safeguard-files/SafeGuard-Python%20.py", Files.pythonFileFolder, "SafeGuard-Python", ".py")
    with open(Files.logFile, "a") as f:
      f.write("Program file [" + Files.pythonFile + "] !REDOWNLOADED! - AT: " + now)
    if debug:
      print(Fore.RED + "Program file [" + Files.pythonFile + "] !MISSING! - AT: " + now + Style.RESET_ALL)

  if not os.path.exists(Files.knownThreatFile):
    CUSTOMinstall("https://itzcozi.github.io/SafeGuard/data/safeguard-files/threatList%20.sg", Files.knownThreatFileFolder, "threatList", ".sg")
    with open(Files.logFile, "a") as f:
      f.write("Program file [" + Files.knownThreatFile + "] !REDOWNLOADED! - AT: " + now)
    if debug:
      print(Fore.RED + "Program file [" + Files.knownThreatFile + "] !MISSING! - AT: " + now + Style.RESET_ALL)

  if not os.path.exists(Files.logFile):
    CUSTOMinstall("https://itzcozi.github.io/SafeGuard/data/safeguard-files/logs.txt", Files.logFileFolder, "logs", ".txt")
    with open(Files.logFile, "a") as f:
      f.write("Program file [" + Files.logFile + "] !REDOWNLOADED! - AT: " + now)
    if debug:
      print(Fore.RED + "Program file [" + Files.logFile + "] !MISSING! - AT: " + now + Style.RESET_ALL)

  else:
    with open(Files.logFile, "a") as f:
      f.write("All files !ACCOUNTED! - AT: " + now)
    if debug:
      print(Fore.GREEN + "All files accounted for." + Style.RESET_ALL)
      clear()


def autoUpdate():
# Compares the hashes of the main file and the file on the website. And if they are not the same replace the 
# main python files code with the newly downloaded file. If they are the same delete new file and print("SafeGuard is up to date")
  webFile = hashFileURL('https://itzcozi.github.io/SafeGuard/data/safeguard-files/SafeGuard-Python.py')
  localFile = hashFileLOCAL(Files.pythonFile)
  
  precheckFile = hashFileLOCAL(Files.prechecksFile)
  precheckwebFile = hashFileURL('https://itzcozi.github.io/SafeGuard/data/safeguard-files/PreChecks.py')
  
  print(hashFileURL('https://itzcozi.github.io/SafeGuard/data/safeguard-files/SafeGuard-Python.py'))
  print(hashFileLOCAL(Files.pythonFile))
  print(hashFileLOCAL(Files.prechecksFile))
  print(hashFileURL('https://itzcozi.github.io/SafeGuard/data/safeguard-files/PreChecks.py'))
  
  if webFile != localFile:
    # Logs
    with open (Files.logFile, "a") as f:
      f.write("SafeGuard-Python.py !OUTDATED! - AT: " + now)
    if debug:
      print(Fore.RED + "SafeGuard-Python.py !OUTDATED! - AT: " + now + Style.RESET_ALL)
      
    with open (Files.logFile, "a") as f:
      f.write("Updating SafeGuard-Python.py - AT: " + now)
    if debug:
      print(Fore.GREEN + "Updating SafeGuard-Python.py - AT: " + now + Style.RESET_ALL)
    
    # Update file
    with open (Files.pythonFile, "w") as f:
      f.truncate(0)
      f.write(requests.get('https://itzcozi.github.io/SafeGuard/data/safeguard-files/SafeGuard-Python.py').text)
      f.close()
    
    # Logs
    with open (Files.logFile, "a") as f:
      f.write("SafeGuard-Python.py !UPDATED! - AT: " + now)
    if debug:
      print(Fore.GREEN + "SafeGuard-Python.py !UPDATED! - AT: " + now + Style.RESET_ALL)
      
  if precheckwebFile != precheckFile:
    # Logs
    with open (Files.logFile, "a") as f:
      f.write("PreChecks.py !OUTDATED! - AT: " + now)
    if debug:
      print(Fore.RED + "PreChecks.py !OUTDATED! - AT: " + now + Style.RESET_ALL)
      
    with open (Files.logFile, "a") as f:
      f.write("Updating PreChecks.py - AT: " + now)
    if debug:
      print(Fore.GREEN + "Updating PreChecks.py - AT: " + now + Style.RESET_ALL)
    
    # Update file
    with open(Files.prechecksFile, "w") as f:
      f.truncate(0)
      f.write(requests.get('https://itzcozi.github.io/SafeGuard/data/safeguard-files/PreChecks.py').text)
      f.close()
    
    # Logs
    with open (Files.logFile, "a") as f:
      f.write("PreChecks.py !UPDATED! - AT: " + now)
    if debug:
      print(Fore.GREEN + "PreChecks.py !UPDATED! - AT: " + now + Style.RESET_ALL)
      
  else:
    print(Fore.GREEN + "SafeGuard is up to date" + Style.RESET_ALL)
    with open(Files.logFile, "a") as f:
      f.write("SafeGuard !UP-TO-DATE! - AT: " + now)
    if debug:
      print(Fore.GREEN + "SafeGuard !UP-TO-DATE! - AT: " + now + Style.RESET_ALL)
      clear()
  
