import speech_recognition as sr 
import pyttsx3
import datetime as dt 
import pywhatkit as pk 
import wikipedia as wk 

listener = sr.Recognizer()
speaker=pyttsx3.init()
rate=speaker.getProperty("rate")
speaker.setProperty("rate",155)

voice=speaker.getProperty("voices")
speaker.setProperty("voice",voice[1].id)

def speak(text):
    speaker.say('yes sir,'+ text)
    speaker.runAndWait()

def speak_ex(text):
    speaker.say(text)
    speaker.runAndWait()
name="Heidi"
speak_ex('i am your '+name+',Tell me sir,')

def take_command():
    command=' '
    try:
        with sr.Microphone() as source:
            print('Listening......')
            voice=listener.listen(source)
            command=listener.recognize_google(voice)
            command=command.lower()
            if name in command:
                command=command.replace(name+'','')
                
            
    except:
        print("Please check your microphone sir")
    return command
while True:
    user_command=take_command()
    if 'close' in user_command:
        print('Bye sir see you next time')
        speak('bye sir see you next time')
        break
    elif 'time' in user_command:
        cur_time=dt.datetime.now().strftime("%I:%M %P")
        print(cur_time)
        speak(cur_time)
    elif 'play' in user_command:
        user_command=user_command.replace('place',' ')
        print('playing...'+user_command)
        speak('playing...'+user_command+'enjoy boss')
        pk.playonyt(user_command)
        break 
    elif 'search for' in user_command or 'google' in user_command:
        user_command=user_command.replace('search for','')
        user_command=user_command.replace('google','')
    elif 'what is' in user_command:
        user_command=user_command.replace('what is','')
        speak("searching for"+user_command)
        pk.search(user_command)
        
    elif 'who is' in user_command:
        user_command=user_command.replace('who is','')
        speak('searching for'+user_command)
        pk.search(user_command)
        
    elif 'who are you' in user_command:
        user_command=user_command.replace('who are you','')
        speak("I am heidi your personal assistant sir")
    elif 'how many' in user_command:
        user_command=user_command.replace('how many','')
        speak('searching for'+user_command)
        pk.search(user_command)
    else:
        speak_ex('Please say again sir')
