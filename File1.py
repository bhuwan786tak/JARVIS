import webbrowser

import pyttsx3
import speech_recognition
import requests
import bs4
from bs4 import BeautifulSoup
import datetime
import os
import pyautogui
import keyboard
import random
from plyer import notification
from pygame import mixer
import speedtest
import plyer
import requests

for i in range(3):
    a = input("Enter password to open Jarvis")
    pw_file = open("password.txt", "r")
    pw = pw_file.read()
    pw_file.close()
    if(a==pw):
        print("Welcome sir ! Please speak wake up to launch me")
        break
    elif(i ==2 and a!=pw):
        exit()

    elif(a!=pw):
        print("Try Again")


from INTRO import play_gif
play_gif




engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 170)


def speak(audio: object) -> object:
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source, 0, 4)

    try:
        print("Understanding...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again please")
        return "None"
    return query


def alarm(query):
    timehere = open("Alarmtext.txt", "a")
    timehere.write(query)
    timehere.close()
    os.startfile("Alarm.py")
if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if "wake up" in query:
            from Greetme import greetMe

            greetMe()

            while True:
                query = takeCommand().lower()
                if "go to sleep" in query:
                    speak("OK sir, You can call me anytime again")
                    break

########################JARVIS : the trilogy 2.0###########################################

                elif "change password" in query:
                    speak("what's the new password")
                    new_pw = input("Enter the new password\n")
                    new_password = open("password.txt", "w")
                    new_password.write(new_pw)
                    speak("Done Sir")
                    speak("Your new password is{new_pw}")

                elif "schedule my day" in query:
                    tasks = [] #Empty list
                    speak("DO you want to clear old tasks (Please speak YES or NO)")
                    query = takeCommand().lower()
                    if "yes" in query:
                        file = open("tasks.txt", "w")
                        file.write(f"")
                        file.close()
                        no_task = int(input("Enter the no. of tasks : "))
                        i = 0
                        for i in range(no_task):
                            tasks.append(input("Enter the task : " ))
                            file = open("tasks.txt", "a")
                            file.write(f"{i}. {tasks[i]}\n")
                            file.close()

                    elif "no" in query:
                        i = 0
                        no_task = int(input("Enter the no. of tasks : "))
                        for i in range(no_task):
                            tasks.append(input("Enter the task : " ))
                            file = open("tasks.txt", "a")
                            file.write(f"{i}. {tasks[i]}\n")
                            file.close()

                elif "show my schedule" in query:
                    file = open("tasks.txt", "r")
                    content = file.read()
                    file.close()
                    # mixer.init()
                    # mixer.music.load("notification.mp3")
                    # mixer.music.play()

                    notification.notify(
                        title = "My schedule : ",
                        message = content,
                        timeout = 15
                    )
            # Command for open any app

                elif "open" in query:
                    query = query.replace("open", "")
                    query = query.replace("jarvis", "")
                    pyautogui.press("super")
                    pyautogui.typewrite(query)
                    pyautogui.sleep(1)
                    pyautogui.press("enter")

            # Command for checking Internet Speed

                elif "internet speed" in query:
                    wifi = speedtest.Speedtest()
                    upload_net = wifi.upload()//1048576  #megabyte = 1024*1024 bytes
                    download_net = wifi.download()//1048576
                    print("wifi Upload Speed is" , upload_net)
                    print("Wifi download speed is", download_net)
                    speak(f"Wifi download speed is: {download_net}")
                    speak(f"Wifi upload speed is: {upload_net}")


            # Command for IPL Score

                elif "ipl score" in query:
                    from plyer import notification  # pip install plyer
                    import requests  # pip install requests
                    from bs4 import BeautifulSoup  # pip install bs4

                    url = "https://www.cricbuzz.com/"
                    page = requests.get(url)
                    soup = BeautifulSoup(page.text, "html.parser")
                    team1 = soup.find_all(class_="cb-ovr-flo cb-hmscg-tm-nm")[1].get_text()
                    team2 = soup.find_all(class_="cb-ovr-flo cb-hmscg-tm-nm")[2].get_text()
                    team1_score = soup.find_all(class_="cb-ovr-flo")[8].get_text()
                    team2_score = soup.find_all(class_="cb-ovr-flo")[10].get_text()

                    a = print(f"{team1} : {team1_score}")
                    b = print(f"{team2} : {team2_score}")

                    notification.notify(
                        title="IPL SCORE :- ",
                        message=f"{team1} : {team1_score}\n {team2} : {team2_score}",
                        timeout=15
                    )



############################################################################################


                # Basic commands (Greetings)

                elif 'hello' in query:
                    speak("Hello Sir, How are you ?")
                elif "I am Fine" in query:
                    speak("That's great Sir")
                elif 'how are you' in query:
                    speak("Perfect Sir, Thank you for asking")
                elif 'Thankyou' in query:
                    speak("Your Welcome, Sir")
                elif 'Hi Jarvis' in query:
                    speak("Hello, Sir")
                elif 'thankyou' in query:
                    speak("Your Welcome, Sir")

                # Commands for Playlist

                elif "tired" in query:
                    speak("Playing your favourite songs, Sir")
                    a = (1,2,3)
                    b = random.choice(a)
                    if b == 1:
                        webbrowser.open("https://www.youtube.com/watch?v=-0lql0pSSwQ")

                # Commands dor play,pause,mute,volume up and volume down

                elif " pause" in query:
                    pyautogui.press("k")
                    speak("Video paused")
                elif "play" in query:
                    pyautogui.press("k")
                    speak("Video played")
                elif "mute" in query:
                    pyautogui.press("m")
                    speak("Video Muted")
                elif "volume up" in query:
                    from Keyboard import volumeup
                    speak("Turning volume up, Sir")
                    volumeup()
                elif "volume down" in query:
                    from Keyboard import volumedown
                    speak("Turning volume down, Sir")
                    volumedown()



                # Commands for opening and closing apps

                elif "open" in query:
                    from DictionaryOfApps import openappweb
                    openappweb(query)
                elif "close" in query:
                    from DictionaryOfApps import closeappweb
                    closeappweb(query)

                # commands for searching on Google, YouTube, Wiki

                elif "google" in query:
                    from SearchNow import searchGoogle
                    searchGoogle(query)
                elif "youtube" in query:
                    from SearchNow import searchYoutube
                    searchYoutube(query)
                elif "wikipedia" in query:
                    from SearchNow import searchWikipedia
                    searchWikipedia(query)


                # Commands for News

                elif "news" in query:
                    from NewsRead import latestnews
                    latestnews()

                # Commands for Calculation

                elif "calculate" in query:
                    from Calculatenumbers import WolfRamAlpha
                    from Calculatenumbers import Calc
                    query = query.replace("calculate", "")
                    query = query.replace("jarvis", "")
                    Calc(query)


                # Commands for Sending Message on Whatsapp

                elif "Whatsapp" in query:
                    from Whatsapp import sendMessage
                    sendMessage()


                # Commands for Temperature or Weather

                elif "temperature" in query:
                    search = "temperature"
                    url = f"https://www.google.com/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text, "html.parser")
                    temp = data.find("div", class_="BNeawe").text
                    speak(f"current{search} is {temp}")
                elif "weather" in query:
                    search = "temperature"
                    url = f"https://www.google.com/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text, "html.parser")
                    temp = data.find("div", class_="BNeawe").text
                    speak(f"current{search} is {temp}")


                elif "set an alarm" in query:
                    print("input time example: 10 and 10 and 10")
                    speak("Set the time")
                    a = input("Please tell the time:  ")
                    alarm(a)
                    speak("Done, Sir")

                # Command for Time

                elif "the time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")
                    speak(f"Sir, the time is{strTime}")

                # Command to exit code and stop

                elif "Finally Sleep" in query:
                    speak("Going to sleep, sir")
                    exit()

                # Command to remember

                elif "remember that" in query:
                    rememberMessage = query.replace("remember that", "")
                    rememberMessage = query.replace("jarvis", "")
                    speak("You told me " + rememberMessage)
                    remember = open("Remember.txt", "w")
                    remember.write(rememberMessage)
                    remember.close()

                elif "what do you remember" in query:
                    remember = open("Remember.txt", "r")
                    speak("You told me " + remember.read())


                # Command for Shut Down

                elif "shutdown system" in query:
                    speak("Are you sure you want to shut down your system? ")
                    shutdown = input("Do you want to shutdown your computer? (yes/no)")
                    if shutdown == "yes":
                        os.system("shutdown /s /t 1")

                    elif shutdown == "no":
                        break




