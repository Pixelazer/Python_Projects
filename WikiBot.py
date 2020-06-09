# WikiBot
# 
# Made by Aryan Takalkar

import speech_recognition as speech
import wikipedia
import pyttsx3

engine = pyttsx3.init()


running = True

def speech_init(): 
    engine.setProperty('rate', 175)
    engine.setProperty('volume' , 2)
    voices = engine.getPropertyvoices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    
def speech_output(x):
    engine.say(x)
    engine.runAndWait()
    
def start_listening():
    global command
    try:
        r = speech.Recognizer() 
        with speech.Microphone() as source:
            r.adjust_for_ambient_noise(source) 
            speech_output("Say something")
            audio = r.listen(source)
        command = r.recognize_google(audio)
        speech_output("You said: " + command) 
    except speech.UnknownValueError:
        speech_output("Sorry, I didn't get that. Try again.")
        start_listening()
    return str(command)

### Main Code ###

speech_init()

speech_output("I am Wikibot. I can give you information on just about anything, as long as it's in a Wikipedia article.")
userinp = start_listening()

while running:

    y = wikipedia.summary(userinp, sentences = 5)
    try: 
        speech_output(y)
        userinp = start_listening()
    except wikipedia.DisambiguationError:
        speech_output("Sorry, I didn't get that. Try again.")
        userinp = start_listening()

