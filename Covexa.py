'''
Covexa 1.4
[alpha]
'''

import pyttsx3
import webbrowser
# import pygame as pg

engine = pyttsx3.init()
running = True

# Registering chrome
chrome_path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))

# Dictionary of Covexa's responses
dialogues = {"a": "It is a new virus, tramsmitted to humans by bats.",
             "b": "Quarantine yourself if having symptoms or if you are in a city with any reported cases.",
             "c": 'Covid-19 transmits through mucous droplets that are sprayed into the air while sneezing or coughing.',
             'd': "Coronavirus originated in Wuhan, Hubei Province, China.",
             'e': "Symptoms of Coronavirus include cough, fever, chills, headache, tiredness, and trouble breathing.",
             'f': "Use alcohol-based hand sanitizer and rub thoroughly after coming in contact with any object which could be contaminated.",
             'g': "For regular updates on Covid-19 from the World Health Organization, Send 'hi' to + 4 1, 7 9 8, 9 3 1, 8 9 2 on WhatsApp.",
             'h': "Symptoms include coughing, sneezing, difficulty breathing, and pneumonia.",
             'z': "Hope you are well. Goodbye",
             '?': "I don't konw the answer to that question."}

# Initialises Speech Output
def speech_init(): 
    engine.setProperty('rate', 150)
    engine.setProperty('volume' , 2)
    voices = engine.getPropertyvoices = engine.getProperty('voices')  
    engine.setProperty('voice', voices[0].id)
    
def speech_output(x):
    engine.say(x)
    engine.runAndWait()

def open_website(a):
    c = webbrowser.get('Chrome')
    c.open_new_tab(a)



""" Main Code """
    
speech_init()

# Startup
print("I am Covexa, your Coronavirus HelpBot")
x = "I am covexa, your coronavirus help bot"
speech_output(x)
x = "Ask me any questions you have related to Coronavirus."
print(x)
speech_output(x)
print("To exit enter Z")  
userinp = input("Enter your question ").lower()

# Function that will run Covexa until user exits
while running:   
    if "corona" or "covid-19" or 'covid 19' in userinp:
        x = dialogues['a']
        speech_output(x)
        x = dialogues['h']
        speech_output(x)
        userinp=input("Enter your question ").lower()
        
    if "precaution" in userinp:
        x = dialogues['b']
        speech_output(x)
        a = "https://www.who.int"
        open_website(a)
        userinp=input("Enter your question ").lower()
        
    if "symptoms" in userinp:
        x = dialogues['h']
    
    if "transmission" in userinp:
        x = dialogues['c']
        speech_output(x)
        userinp=input("Enter your question").lower()
    
    if "origin" in userinp:
        x = dialogues['d']
        speech_output(x)
        userinp = input("Enter your question ").lower()
        
    if "symptoms" in userinp:
        x = dialogues['e']
        speech_output(x)
        userinp = input("Enter your question ").lower()
        
    if "updates" in userinp:
        x = dialogues['g']
        speech_output(x)
        b = "https://who.sprinklr.com/"
        open_website(b)
        userinp = input("Enter your question ").lower()
    
    if "sanitizer" in userinp:
        x = dialogues['f']
        speech_output(x) 
        userinp = input("Enter your question ").lower()
        
    if "z" in userinp:
        running = False

    if '' in userinp:
        x = dialogues["?"]
        speech_output(x)

# Covexa will say this after exiting the while loop
x = dialogues['z']
speech_output(x)
print("Have a good day!")  
