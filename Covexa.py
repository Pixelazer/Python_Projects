
import pyttsx3
import webbrowser
# import pygame as pg

engine = pyttsx3.init()
running = True

chrome_path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path))

dialogues = {"a": "It is a new virus, tramsmitted to humans by bats.",
             "b": "Quarantine yourselves if having symptoms or if you are in a city with any reported cases.",
             "c": 'Covid-19 transmits through mucous droplets while sneezing or coughing.',
             'd': "Wuhan, Hubei Province, China",
             'e': "Symptoms of Coronavirus include cough, fever, chills, headache, tiredness, and trouble breathing.",
             'f': "Use alcohol-based hand sanitizer and rub thoroughly after coming in contact with any object which could be contaminated.",
             'g': "For regular updates on Covid-19 from the World Health Organization, Send 'hi' to +41 798931892 on WhatsApp"}

def speech_init(): # Initialises Speech Output
    engine.setProperty('rate', 150)
    engine.setProperty('volume' , 2)
    voices = engine.getPropertyvoices = engine.getProperty('voices')  
    engine.setProperty('voice', voices[0].id)
    
def speech_output(x):
    engine.say(x)
    engine.runAndWait()

def open_website(a): # Function To open Webbrowser
    c = webbrowser.get('Chrome')
    c.open_new_tab(a)



""" Main Code """
    
speech_init()

print("I am Covexa, your Coronavirus HelpBot")
x = "I am covexa, your coronavirus help bot"
speech_output(x)
x = "Ask me any question related to Coronavirus."
print(x)
speech_output(x)
print("To exit enter Z")  
userinp = input("Enter your question ").lower()

while running:
    
    if "corona" or "covid" in userinp:
        x = dialogues['a']
        speech_output(x)
        userinp=input("Enter your question ").lower()
        
    if "precaution" in userinp:
        x = dialogues['b']
        speech_output(x)
        a = "https://www.who.int"
        open_website(a)
        userinp=input("Enter your question ").lower()
        
    
    if "transmission" in userinp:
        x = dialogues['c']
        speech_output(x)
        userinp=input("Enter your question").lower()
    
    if "origin" and "corona" in userinp:
        x = dialogues['d']
        speech_output(x)
        userinp = input("Enter your question ").lower()
        
    if "symptoms" in userinp:
        x = dialogues['e']
        speech_output(x)
        userinp = input("Enter your question ").lower()
        
    if "updates" in userinp:
        b = "https://www.who.int"
        open_website(b)
        userinp = input("Enter your question ").lower()
    
    if "sanitizer" in userinp:
        x = dialogues['f']
        speech_output(x) 
        userinp = input("Enter your question ").lower()
        
    if "z" in userinp:
        running = False

x = "Hope you are well"
speech_output(x)
print("See you later")  
