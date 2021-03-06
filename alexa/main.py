import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('rate')
#speed of the speech delivery
engine.setProperty('rate',140)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print("listening......")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'md' in command:
                command = command.replace('md','')
    except:
        pass
    return command

def run_md():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is' + time)

    elif 'search' in command:
        person = command.replace("search","")
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)

    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk("Sorry I didnt understand")
while True:
    run_md()