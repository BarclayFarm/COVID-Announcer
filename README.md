# COVID-Announcer
COVID-Announcer is a Python script that I wrote for my swim club to allow us to make automated announcements about the SARS-CoV-2/COVID-19 virus during the 2020 pandemic.  

## License
This software is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International license.  
THIS SOFTWARE IS PROVIDED WITH NO WARRANTY OF ANY KIND. USE AT YOUR OWN RISK.  
This software is free to use for anyone, but it may not be resold.  

## How to Use
This software is for Windows. It may work on other platforms but is untested.  
* Download Python 3.8
* During the Python 3.8 installation, select custom install. Be sure to install for all users and add to system path.
* Download the ZIP for COVID-Announcer from GitHub.
* Extract the files to wherever you like.
* Press the Windows key and the letter R at the same time.
* Enter shell:startup into the "Run" window that opens and hit enter.
* In the folder that opens, add a shortcut to run.bat wherever you extracted COVID-Announcer.
* Open a Command Prompt or Powershell Window as Administrator and enter `pip install pycaw schedule playsound`   
Next time you login, COVID-Announcer will run when you login.  

## Add or Remove Announcements
To add or remove an announcment, simply add or remove a MP3 file from the folder containing run.bat and main.py.  
I recommend adding a number before the file name (as seen in the included files) in order to specifiy the order that the messages will be played.
