import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import subprocess
import psutil
import email.parser
import pyautogui
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import requests
import json 
from flask import Flask, render_template, request, jsonify
import pymsgbox  # pip install pymsgbox for message box UI
import tkinter as tk  # GUI library for Python
import pyaudio
import threading
from tkinter import simpledialog
from pytube import YouTube  # pip install pytube3 for downloading YouTube videos

# Initialize pyttsx3 engine for Text-to-Speech
engine = pyttsx3.init()

def speak(text):
    def speak_thread():
        try:
            engine.say(text)
            engine.runAndWait()
        except RuntimeError:
            pass  

    thread = threading.Thread(target=speak_thread)
    thread.start()

# Function to greet based on time
def wishMe():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am your assistant. How can I help you today?")

# Function to take voice input and convert to text
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query.lower()

# Function to send email using SMTP with GUI for email and password input
def sendEmail():
    root = tk.Tk()
    root.withdraw()
    email = simpledialog.askstring("Email Address", "Enter your email address:")
    password = simpledialog.askstring("Password", "Enter your email password:", show='*')
    if email and password:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        try:
            server.login(email, password)
            speak("Login successful. What should I say in the email?")
            content = takeCommand()
            if content:
                speak("Who is the recipient?")
                recipient = takeCommand()
                if recipient:
                    try:
                        with open('email_recipients.txt', 'r') as file:
                            recipients = file.readlines()
                        found = False
                        for rec in recipients:
                            if recipient.lower() in rec.lower():
                                to_email = rec.split(': ')[1].strip()
                                subject = "Subject"
                                email_text = f"Subject: {subject}\n{content}"
                                server.sendmail(email, to_email, email_text)
                                server.close()
                                speak("Email has been sent!")
                                found = True
                                break
                        if not found:
                            speak(f"Sorry, I couldn't find {recipient} in the recipient list.")
                    except Exception as e:
                        print(e)
                        speak("Sorry, I am not able to send this email")
                else:
                    speak("No recipient provided.")
            else:
                speak("No content provided for the email.")
        except smtplib.SMTPAuthenticationError:
            speak("Authentication failed. Please check your email and password.")
        except Exception as e:
            print(e)
            speak("Sorry, an error occurred while sending the email.")
    else:
        speak("No email or password entered. Please try again.")
    root.destroy()

# Function to add email recipients using GUI for recipient name and email input
def addEmailRecipient():
    root = tk.Tk()
    root.withdraw()
    recipient_name = simpledialog.askstring("Recipient Name", "Enter recipient's name:")
    recipient_email = simpledialog.askstring("Recipient Email", "Enter recipient's email:")
    if recipient_name and recipient_email:
        with open('email_recipients.txt', 'a') as file:
            file.write(f"{recipient_name}: {recipient_email}\n")
        speak(f"Added {recipient_name} with email {recipient_email} to the recipient list")
    else:
        speak("No data entered. Please try again.")
    root.destroy()

# Function to minimize all open windows
def minimizeWindows():
    pyautogui.hotkey('win', 'd')
    speak("Minimizing all windows")

# Function to maximize a specific window by application name
def maximizeWindow(app_name):
    try:
        app = [p for p in psutil.process_iter(attrs=['name']) if app_name.lower() in p.info['name'].lower()][0]
        app_pid = app.pid
        pyautogui.hotkey('win', 'up')  # Maximizes the window
        speak(f"Maximizing {app_name} window")
    except Exception as e:
        print(e)
        speak(f"Could not find {app_name} application")

# Function to open a new tab in the default web browser
def openNewTab():
    pyautogui.hotkey('ctrl', 't')
    speak("Opening new tab")

# Function to clear browsing data (cookies, cache, history) for the default web browser
def clearBrowserHistory():
    pyautogui.hotkey('ctrl', 'shift', 'delete')
    speak("Clearing browsing data")

# Function to retrieve and speak the public IP address of the system
def getIpAddress():
    ip = requests.get('https://api.ipify.org').text
    speak(f"Your IP address is {ip}")

# Function to generate a to-do list based on user input
def generateTodoList():
    speak("What tasks do you want to add to your to-do list?")
    tasks = takeCommand()
    if tasks != "None":
        with open('todo_list.txt', 'a') as file:
            file.write(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}: {tasks}\n")
        speak("To-do list updated")
    else:
        speak("No tasks detected")

# Function to retrieve news using a free API and speak headlines
def getNews():
    news_api_key = 'use your own API'  
    url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={news_api_key}'
    response = requests.get(url)
    news_data = json.loads(response.text)
    articles = news_data['articles'][:5]  # Fetching top 5 articles
    speak("Here are the top news headlines for today:")
    for article in articles:
        speak(article['title'])

# Function to open an application by its name
def openApp(app_name):
    try:
        subprocess.Popen(app_name)
        speak(f"Opening {app_name}")
    except Exception as e:
        print(e)
        speak(f"Could not find {app_name} application")

# Function to search Google Maps for a specific place
def searchGoogleMaps(place_query):
    url = f"https://www.google.com/maps/search/{place_query.replace(' ', '+')}"
    webbrowser.open(url)
    speak(f"Here is the location of {place_query} on Google Maps")

# Function to download a YouTube video using its URL
def downloadYouTube():
    speak("Please provide the URL of the YouTube video you want to download.")
    youtube_url = takeCommand()
    if youtube_url != "None":
        try:
            yt = YouTube(youtube_url)
            video = yt.streams.filter(progressive=True, file_extension='mp4').first()
            video.download()
            speak("Video downloaded successfully")
        except Exception as e:
            print(e)
            speak("Sorry, I couldn't download the video.")
    else:
        speak("No URL provided")

# Function to look up a word in the dictionary and speak its meaning
def dictionaryLookup(word):
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    response = requests.get(url)
    data = response.json()
    try:
        definition = data[0]['meanings'][0]['definitions'][0]['definition']
        speak(f"The definition of {word} is: {definition}")
    except Exception as e:
        print(e)
        speak(f"Sorry, I couldn't find the definition of {word}")

# Main function to execute commands based on user input
def process_command(command):
    if 'Wikipedia' in command:
        speak('Searching Wikipedia...')
        command = command.replace("wikipedia", "")
        results = wikipedia.summary(command, sentences=2)
        speak("According to Wikipedia")
        speak(results)

    elif 'open YouTube' in command:
        webbrowser.open("youtube.com")
        speak("Opening YouTube")

    elif 'open Google' in command:
        webbrowser.open("google.com")
        speak("Opening Google")

    elif 'stack overflow' in command:
        webbrowser.open("stackoverflow.com")
        speak("Opening Stack Overflow")

    elif 'play music' in command:
        speak("Playing music")
        # Add your music player logic here, for example, if using Spotify:
        # spotipy.play("song_name")

    elif 'the time' in command:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Sir, the time is {strTime}")

    elif 'open code' in command:
        codePath = "C:\\Users\\Sonwa\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(codePath)
        speak("Opening VS Code")

    elif 'email to' in command:
        sendEmail()

    elif 'address' in command:
        getIpAddress()

    elif 'todo list' in command:
        generateTodoList()

    elif 'news' in command:
        getNews()

    elif 'open discord' in command:
        openApp('discord')

    elif 'Google Map' in command:
        speak("What place do you want to search on Google Maps?")
        place_query = takeCommand()
        searchGoogleMaps(place_query)

    elif 'open email recipient editor' in command:
        addEmailRecipient()

    elif 'YouTube downloader' in command:
        downloadYouTube()

    elif 'open calculator' in command:
        subprocess.Popen('calc.exe')
        speak("Opening calculator")

    elif 'take screenshot' in command:
        pyautogui.screenshot('screenshot.png')
        speak("Screenshot taken")

    elif 'dictionary' in command:
        speak("What word do you want to look up?")
        word = takeCommand()
        dictionaryLookup(word)

    elif 'minimize' in command:
        app_name = command.split('minimize ', 1)[1].lower()
        minimizeWindows()

    elif 'maximize' in command:
        app_name = command.split('maximize ', 1)[1].lower()
        maximizeWindow(app_name)

    elif 'restart' in command:
        speak("Restarting your computer")
        os.system("shutdown /r /t 1")

    elif 'shutdown' in command:
        speak("Shutting down your computer")
        os.system("shutdown /s /t 1")

    elif 'lock' in command:
        speak("Locking the computer")
        os.system("rundll32.exe user32.dll,LockWorkStation")

    elif 'volume up' in command:
        pyautogui.press("volumeup")

    elif 'volume down' in command:
        pyautogui.press("volumedown")

    elif 'mute' in command:
        pyautogui.press("volumemute")

    elif 'brightness up' in command:
        pyautogui.press("brightnessup")

    elif 'brightness down' in command:
        pyautogui.press("brightnessdown")

    elif 'exit' in command or 'bye' in command:
        speak("Goodbye!")
        return False  # Exit the loop

    else:
        speak("Sorry, I didn't catch that. Can you please repeat?")

    return True

app = Flask(__name__)

# Define the route for the home page
@app.route('/')
def home():
    return render_template('index.html')  # Create a simple HTML page with a button to trigger the command

# Define the route for voice command
@app.route('/take_command', methods=['GET'])
def take_voice_input():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print(e)
        print("Say that again please...")
        return jsonify({"response": "Sorry, I couldn't hear you properly. Please try again."})

    # Process the voice command
    command_response = process_command(query)

    if command_response:
        return jsonify({"response": f"You said: {query}"})
    else:
        return jsonify({"response": "Goodbye!"})

if __name__ == '__main__':
    app.run(debug=True)