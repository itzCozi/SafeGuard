// This code is old and was kind of a template sadly i still have to finish it.

// Imports
#include <stdlib.h>
//#include <windows.h>

#include <filesystem>
#include <fstream>
#include <time.h> 
#include <list>
#include <iostream>
#include <algorithm>
#include <iterator>
#include <string>

// Global Variables
bool healthCheck = true;
time_t my_time = time(NULL);
std::string logPath = "data/logs.sg";

// Logs
std::string systemRestoreLog = "System restored"; 
printf("%s", ctime(&my_time));


// Colors
void setColorGreen() {
  std::system("Color 0A");
}

void setColorRed(){
  std::system("Color 04");
}


// Functions

// BROKEBN FUNCTION
int readFolderList() {
std::list<std::string> threatList;
std::string line;
  
std::ifstream myfile ("test.txt");
   if (myfile.is_open()){  
     for(line; getline(myfile, line);)
     {
     threatList.push_back(line);
     }
        myfile.close();
        return threatList;
     }
}

void checkWindowsUpdate() {
  std::string UpdateConfirm;
  std::string y;
  std::string n;
  
  system("Install-Module PSWindowsUpdate");
  system("Get-WindowsUpdate");
  
  std::cout << "Do you want to update windows10? (y/n)";
  std::cin >> UpdateConfirm;

  if (UpdateConfirm==y) {
    system("Install-WindowsUpdate");
    
  }
  
}

void fileChecker() {
  if (healthCheck==true) {
    system("DISM.exe /Online /Cleanup-image /Restorehealth");
    setColorGreen();
    
    std::cout << "System restored";// file log system restored
    

    system("sfc /scannow");
    setColorGreen();
    
    std::cout << "System scaned for integrity";// file log system restored
    std::ifstream logFile(logPath);
    //Creates an instance of ofstream and opens log
    std::ofstream Database_write (logPath, std::ios::app);
    Database_write << userRecord << "\n";

  }
}


// Main
int main() {
  // main scans system and asks the user if they want to start tron or quits.
  
  // Class Variables
  std::string startTron;
  std::string virusDetected = "! SYSTEM FLAGGED THREAT !";
  std::string allClear = "System scanned negitive for known threats.";
  bool threats;

  if (threats == false) {
    setColorGreen();

    std::cout << allClear;
  }
  

  
}