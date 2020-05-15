from __future__ import print_function
from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume
from playsound import playsound
import schedule
import time
import os

# How frequently to make an announcement in minutes
runTime = 15
# List to hold announcements
announcementsPaths = []
# Holds the next announcement to be played
next = 0

def main():
    print("=======================================================")
    print("DO NOT CLOSE THIS WINDOW UNDER ANY CIRCUMSTANCES")
    print("THESE PSAs ARE REQUIRED. NO EXCEPTIONS.")
    print("(C) 2020 Kevin Salvatorelli")
    print("=======================================================")
    print("")

    print("Adding files to use as announcements")
    for file in os.listdir(os.path.dirname(os.path.abspath(__file__))):
        if file.endswith(".mp3"):
            print("Adding File: " + os.path.join(os.path.dirname(os.path.abspath(__file__)), file))
            announcementsPaths.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), file))

    print("Running Initial Annoucement")
    makeAnnouncement()

    print("Scheduling Tasks to be ran every " + str(runTime) + " minutes")
    schedule.every(runTime).minutes.do(makeAnnouncement)


    print("Starting task queue")
    while True:
        schedule.run_pending()
        time.sleep(1)



def makeAnnouncement():
    global next
    playSound(announcementsPaths[next])
    if next + 1 < len(announcementsPaths):
        next = next + 1
    else:
        next = 0

def playSound(audioFile):

    print("Playing " + audioFile)

    sessions = AudioUtilities.GetAllSessions()

    # Decrease all app
    for session in sessions:
        volume = session._ctl.QueryInterface(ISimpleAudioVolume)
        volume.SetMasterVolume(0.1, None)

    time.sleep(3)
    # Play the audio
    playsound(audioFile)
    # Make sure Python is full volume
    for session in sessions:
        if session.Process and session.Process.name() == "Python.exe":
            volume = session._ctl.QueryInterface(ISimpleAudioVolume)
            volume.SetMasterVolume(1.0, None)

    time.sleep(3)

    # Set all app back to full
    for session in sessions:
        volume = session._ctl.QueryInterface(ISimpleAudioVolume)
        volume.SetMasterVolume(1.0, None)

if __name__ == "__main__":
    main()