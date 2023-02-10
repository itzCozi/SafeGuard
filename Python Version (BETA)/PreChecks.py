class Files():
  appUserFile = pythonFile = "C:/Users/" + os.getlogin() + "/Python-SafeGuard/SafeGuard.app.ink",
  pythondiscreteFile = "C:/Users/" + os.getlogin() + "/Python-SafeGuard/resources/SafeGuard-Python-Discrete .py",
  tronAdmin =  "C:/Users/" + os.getlogin() + "/Python-SafeGuard/resources/tronAdmin.ink",
  tronPath = pythonFile = "C:/Users/" + os.getlogin() + "/Python-SafeGuard/resources/tron",
  appFile = pythonFile = "C:/Users/" + os.getlogin() + "/Python-SafeGuard/resources/SafeGuard.cmd",
  pythonFile = "C:/Users/" + os.getlogin() + "/Python-SafeGuard/resources/SafeGuard-Python .py",
  logFile = "C:/Users/" + os.getlogin() + "/Python-SafeGuard/resources/logs.txt",
  knownThreatFile = "C:/Users/" + os.getlogin() + "/Python-SafeGuard/resources/threatList .sg",

sleep = time.sleep(3)
now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n\n"

def CUSTOMinstall(URL, Destination, NewName, FileExt=""):

  # Download and write to file
  file_content = requests.get(URL)
  open(Destination + '/' + NewName + FileExt, "wb").write(file_content.content)
  with open(logFile, "a") as f:
    f.write("Downloaded file to: " + Destination + " - AT: " + now)
  if debug:
    print(Fore.GREEN + "Downloaded file to: " + Destination + Style.RESET_ALL)


def preRun():
  # Developers cover your eyes!
  if not os.path.exists(Files.appUserFile):
    CUSTOMinstall("https://itzcozi.github.io/SafeGuard/data/safeguard-files/SafeGuard.app.lnk" ,Files.appUserFile, "SafeGuard.app", ".ink")
    with open(logFile, "a") as f:
      f.write("Program file [" + Files.appUserFile + "] !REDOWNLOADED! - AT: " + now)
    if debug:
      print(Fore.RED + "Program file [" + Files.appUserFile + "] !MISSING! - AT: " + now + Style.RESET_ALL)

  if not os.path.exists(Files.pythondiscreteFile):
    CUSTOMinstall("https://itzcozi.github.io/SafeGuard/data/safeguard-files/SafeGuard-Python-Discrete.lnk" ,Files.pythondiscreteFile, "SafeGuard-Python-Discrete", ".ink")
    with open(logFile, "a") as f:
      f.write("Program file [" + Files.pythondiscreteFile + "] !REDOWNLOADED! - AT: " + now)
    if debug:
      print(Fore.RED + "Program file [" + Files.pythondiscreteFile + "] !MISSING! - AT: " + now + Style.RESET_ALL)

  if not os.path.exists(Files.tronAdmin):
    CUSTOMinstall("https://itzcozi.github.io/SafeGuard/data/safeguard-files/tronAdmin.lnk" ,Files.tronAdmin, "tronAdmin", ".ink")
    with open(logFile, "a") as f:
      f.write("Program file [" + Files.tronAdmin + "] !REDOWNLOADED! - AT: " + now)
    if debug:
      print(Fore.RED + "Program file [" + Files.tronAdmin + "] !MISSING! - AT: " + now + Style.RESET_ALL)

  if not os.path.exists(Files.tronPath):
    CUSTOMinstall("http://www.bmrf.org/repos/tron/Tron%20v12.0.5%20(2023-02-02).exe" ,Files.tronPath, "Tron v12.0.5 (2023-02-02)", ".exe")
    with open(logFile, "a") as f:
      f.write("Program file [" + Files.tronPath + "] !REDOWNLOADED! - AT: " + now)
    if debug:
      print(Fore.RED + "Program file [" + Files.tronPath + "] !MISSING! - AT: " + now + Style.RESET_ALL)

  if not os.path.exists(Files.pythonFile):
    CUSTOMinstall("https://itzcozi.github.io/SafeGuard/data/safeguard-files/SafeGuard-Python%20.py" ,Files.pythonFile, "SafeGuard-Python", ".py")
    with open(logFile, "a") as f:
      f.write("Program file [" + Files.pythonFile + "] !REDOWNLOADED! - AT: " + now)
    if debug:
      print(Fore.RED + "Program file [" + Files.pythonFile + "] !MISSING! - AT: " + now + Style.RESET_ALL)

  if not os.path.exists(Files.knownThreatFile):
    CUSTOMinstall("https://itzcozi.github.io/SafeGuard/data/safeguard-files/threatList%20.sg" ,Files.appFile, "threatList", ".sg")
    with open(logFile, "a") as f:
      f.write("Program file [" + Files.knownThreatFile + "] !REDOWNLOADED! - AT: " + now)
    if debug:
      print(Fore.RED + "Program file [" + Files.knownThreatFile + "] !MISSING! - AT: " + now + Style.RESET_ALL)

  if not os.path.exists(Files.logFile):
    CUSTOMinstall("https://itzcozi.github.io/SafeGuard/data/safeguard-files/logs.txt" ,Files.knownThreatFile, "logs", ".txt")
    with open(logFile, "a") as f:
      f.write("Program file [" + Files.logFile + "] !REDOWNLOADED! - AT: " + now)
    if debug:
      print(Fore.RED + "Program file [" + Files.logFile + "] !MISSING! - AT: " + now + Style.RESET_ALL)
  
  else:
    with open(logFile, "a") as f:
      f.write("All files !ACCOUNTED! - AT: " + now)
    if debug:
      print(Fore.GREEN+"All files accounted for."+Style.RESET_ALL)
      clear()
