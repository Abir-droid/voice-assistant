import os
import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import requests
from newsapi import NewsApiClient
import subprocess
from pygetwindow import getWindowsWithTitle
from pywinauto import Application
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

# Initialize the speech recognizer and synthesizer
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Set the speaking rate (adjust the value as needed)
engine.setProperty('rate', 190)

# Initialize the News API client with your API key
news_api = NewsApiClient(api_key='Your Api key')  # Replace with your News API key


# Define a function to speak a text
def speak(text):
    engine.say(text)
    engine.runAndWait()


# Initialize a global variable for articles
articles = []


# Define a function to get the voice command from the user
def get_command():
    # Use the microphone as the audio source
    with sr.Microphone(sample_rate=44100, chunk_size=1024) as source:
        recognizer.energy_threshold = 4000
        # Listen for the user's voice and store it in an audio object
        print("Listening...")
        audio = recognizer.listen(source)
        # Try to recognize the speech and return the text
        try:
            print("Recognizing...")
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text.lower()
        # If the speech is not recognized, return None
        except:
            print("Sorry, I did not understand that.")
            return None


# Add a function to control the system volume
def set_system_volume(volume_level):
    try:
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(
            IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        current_volume = volume.GetMasterVolumeLevelScalar()
        if 0.0 <= volume_level <= 1.0:
            volume.SetMasterVolumeLevelScalar(volume_level, None)
            speak(f"Volume set to {int(volume_level * 100)}%")
        else:
            speak("Volume level should be between 0 and 1.")
    except Exception as e:
        speak("Sorry, I encountered an error while adjusting the volume.")
        print(f"Error: {e}")


def turn_on_wifi():
    try:
        subprocess.run("netsh interface set interface 'Wi-Fi' admin=enabled", shell=True)
        speak("Wi-Fi is now turned on.")
    except Exception as e:
        speak("Sorry, I encountered an error while turning on Wi-Fi.")
        print(f"Error: {e}")


def turn_off_wifi():
    try:
        # Create a PowerShell command to disable Wi-Fi
        powershell_cmd = 'Disable-NetAdapter -Name "Wi-Fi"'

        # Run PowerShell with administrator privileges and pipe 'Y' to confirm
        os.system(f'echo Y | powershell -Command "{powershell_cmd}"')

        print("Wi-Fi is now turned off.")
    except Exception as e:
        print(f"Failed to turn off Wi-Fi. Check your command and permissions.")
        print(f"Error: {e}")


# Define a function to list music files in the specified directory
def list_music_files(directory):
    music_files = [f for f in os.listdir(directory) if f.endswith((".mp3", ".wav", ".flac"))]
    if music_files:
        for i, music in enumerate(music_files):
            print(f"{i + 1}. {music}")
            speak(music)
    else:
        speak("No music files found in the directory.")


# Define a function to open a specific music file by its title or position
def open_music(title, directory):
    music_files = [f for f in os.listdir(directory) if f.endswith((".mp3", ".wav", ".flac"))]
    if title.isdigit():  # Check if the input is a number
        title = int(title)
        if 1 <= title <= len(music_files):
            music = music_files[title - 1]
            music_path = os.path.join(directory, music)
            os.system(f'start "" "{music_path}"')
            speak(f"Playing {music}.")
        else:
            speak("Invalid music number. Please specify a valid music number.")
    else:
        # Split the command into words and identify position keywords
        keywords = title.split()
        numeric_position = None

        for keyword in keywords:
            if keyword in ["first", "1st"]:
                numeric_position = 1
            elif keyword in ["second", "2nd"]:
                numeric_position = 2
            elif keyword in ["third", "3rd"]:
                numeric_position = 3
                # Add more position keywords as needed

        if numeric_position is not None:
            if 1 <= numeric_position <= len(music_files):
                music = music_files[numeric_position - 1]
                music_path = os.path.join(directory, music)
                os.system(f'start "" "{music_path}"')
                speak(f"Playing {music}.")
            else:
                speak("Invalid music position. Please specify a valid position keyword.")
        else:
            found = False
            for music in music_files:
                if title.lower() in music.lower():
                    music_path = os.path.join(directory, music)
                    os.system(f'start "" "{music_path}"')
                    speak(f"Opening {music}.")
                    found = True
                    break

            if not found:
                speak(f"Sorry, I could not find a music with the title or number: {title}")


# Define a function to list video files in the specified directory
def list_video_files(directory):
    video_files = [f for f in os.listdir(directory) if f.endswith((".mp4", ".avi", ".mkv"))]
    if video_files:
        for i, video in enumerate(video_files):
            print(f"{i + 1}. {video}")
            speak(video)
    else:
        speak("No video files found in the directory.")


# open the video with title or number
def open_video(title, directory):
    video_files = [f for f in os.listdir(directory) if f.endswith((".mp4", ".avi", ".mkv"))]
    if title.isdigit():
        title = int(title)  # Convert the title to an integer
        if 1 <= title <= len(video_files):
            video = video_files[title - 1]
            video_path = os.path.join(directory, video)
            os.system(f'start "" "{video_path}"')
            speak(f"Opening {video}.")
        else:
            speak("Invalid video number. Please specify a valid video number.")
    else:
        # Split the command into words and identify position keywords
        keywords = title.split()
        numeric_position = None

        for keyword in keywords:
            if keyword in ["first", "1st"]:
                numeric_position = 1
            elif keyword in ["second", "2nd"]:
                numeric_position = 2
            # Add more position keywords as needed

        if numeric_position is not None:
            if 1 <= numeric_position <= len(video_files):
                video = video_files[numeric_position - 1]
                video_path = os.path.join(directory, video)
                os.system(f'start "" "{video_path}"')
                speak(f"Opening {video}.")
            else:
                speak("Invalid video position. Please specify a valid position keyword.")
        else:
            found = False
            for video in video_files:
                if title.lower() in video.lower():
                    video_path = os.path.join(directory, video)
                    os.system(f'start "" "{video_path}"')
                    speak(f"Opening {video}.")
                    found = True
                    break

            if not found:
                speak(f"Sorry, I could not find a video with the title or number: {title}")


# Define a function to execute the voice command
def execute_command(command):
    global articles  # Access the global articles variable
    if command.startswith("open"):
        # Get the app name from the command
        app_name = command.replace("open", "", 1).strip()
        try:
            # Use PowerShell to find the AppId based on the app name
            cmd = f'powershell "(Get-StartApps | Where-Object {{ $_.Name -eq \'{app_name}\' }}).AppId"'
            app_id = os.popen(cmd).read().strip()

            if app_id:
                # Try to open the UWP app using the AppId
                os.system(f'start shell:AppsFolder\{app_id}')
                speak(f"Opening {app_name}")
                return  # Return from the function after successfully opening the app
            else:
                speak(f"Sorry, I could not find the app: {app_name}")
        except Exception as e:
            speak(f"Sorry, I encountered an error while trying to open {app_name}.")
            print(f"Error: {e}")

    if "volume up to" in command:
        try:
            volume_level = float(command.split("volume up to")[1].strip()) / 100.0
            set_system_volume(volume_level)
        except ValueError:
            speak("Invalid volume level. Please specify a valid number.")
    elif "volume down to" in command:
        try:
            volume_level = float(command.split("volume down to")[1].strip()) / 100.0
            set_system_volume(volume_level)
        except ValueError:
            speak("Invalid volume level. Please specify a valid number.")
            # Add the functionality to turn on/off Wi-Fi
    elif "turn on wireless fidelity" in command:
        turn_on_wifi()
    elif "turn off wireless fidelity" in command:
        turn_off_wifi()
    elif "videos" in command:
        list_video_files("C:\\Users\\aksar\\Videos")
    elif command.startswith("play video"):
        video_title = command.replace("play video", "", 1).strip()
        open_video(video_title, "C:\\Users\\aksar\\Videos")
    # Add the option to play a video by specifying its position
    elif command.startswith("play the"):
        video_position = command.replace("play the", "", 1).strip()
        open_video(video_position, "C:\\Users\\aksar\\Videos")
    elif "musics" in command:
        list_music_files("C:\\Users\\aksar\\Music")
    elif command.startswith("play music"):
        music_title = command.replace("play music", "", 1).strip()
        open_music(music_title, "C:\\Users\\aksar\\Music")
    # Add the option to play a music by specifying its position
    elif command.startswith("play"):
        music_position = command.replace("play", "", 1).strip()
        open_music(music_position, "C:\\Users\\aksar\\Music")
    elif command.startswith("search for"):
        # Extract the search query
        search_query = command.replace("search for", "", 1).strip()
        if search_query:
            search_url = f"https://www.google.com/search?q={search_query}"
            webbrowser.open(search_url)
            speak(f"Here are the search results for {search_query}.")
    elif "list apps" in command:
        cmd1 = f'powershell "Get-StartApps"'
        result = subprocess.run(cmd1, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
        if result.returncode == 0:
            output = result.stdout
            speak("Here is all your listed apps")
            print(output)
    elif "google" in command:
        # Perform a direct Google search
        search_url = "https://www.google.com"
        webbrowser.open(search_url)
        speak("Here is Google. You can search for anything you want.")
    elif "time" in command:
        # Get the current time of Bangladesh
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The current time in Bangladesh is {current_time}.")
    elif "date" in command:
        # Get the current date in Bangladesh
        current_date = datetime.date.today().strftime("%Y-%m-%d")
        speak(f"The current date in Bangladesh is {current_date}.")
    elif command == "exit":
        speak("Goodbye!")
        return "exit"  # Signal to exit the loop
    elif "news" in command:
        news = news_api.get_top_headlines(country='us')
        articles = news['articles']
        if articles:
            speak("Here are the top 5 latest international news topics:")
            for i, article in enumerate(articles[:5]):
                topic = f"{i + 1}. {article['title']}"
                print(topic)  # Print the topic
                speak(topic)
            speak("To read more about a topic, say 'tell me about topic' followed by the topic number.")
        else:
            speak("Sorry, I couldn't fetch the latest news at the moment.")
    elif "tell me about topic" in command:
        # Prompt the user to enter a number via console input
        try:
            article_number = int(input("Enter the number of the topic you want to read: "))
            if 1 <= article_number <= 5:
                article_url = articles[article_number - 1]['url']
                webbrowser.open(article_url)
            else:
                speak("Invalid article number. Please enter a number from 1 to 5.")
        except ValueError:
            speak("Invalid input. Please enter a number from 1 to 5.")
    # Add weather functionality
    elif "weather in" in command:
        city = command.split("weather in ")[-1]k
        weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=Yours_Api&units=metric"
        response = requests.get(weather_url)
        data = response.json()
        if data["cod"] == 200:
            weather_description = data["weather"][0]["description"]
            temperature = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            weather_info = f"The weather in {city} is {weather_description}, the temperature is {temperature}°C, and the humidity is {humidity}%."
            speak(weather_info)
            print(weather_info)
        else:
            speak(f"Sorry, I couldn't fetch the weather data for {city}.")
    else:
        speak("Sorry, that is not a valid command.")


# Initial greeting
speak("Hello, I am your voice assistant. What can I do for you?")

# Continuous loop for voice commands
while True:
    # Get the command
    command = get_command()

    # If the command is not None, execute it
    if command:
        exit_signal = execute_command(command)
        if exit_signal == "exit":
            break  # Exit the loop if the "exit" command is given
        else:
            speak("Anything else?")
