# A program that calculates the dimensions of a shape (Area, Perimeter, Volume) with user specifics.
# Made by Aryan Takalkar

# importing

import pyttsx3 as speech
from time import sleep

# Initializing class UI

class UI():
    def __init__(self):
        self.running = True
        self.speechEngine = speech.init()
        self.l = 0
        self.b = 0
        self.h = 0
        self.op = 0
        self.data = 0
        print("Welcome to Cal**2 \nThis program can calculate the area, perimeter, and volume of a shape.")
        self.speak("Welcome to Cal square.")
        sleep(0.10)
        self.speak("This program can calculate the area, perimeter, and volume of a rectangle, square, or cube.")

    def startup(self):
        self.speak("Enter the length of the shape.")
        self.l = int(input("Enter the length of the shape. \n"))
        self.speak("Enter the breadth of the shape.")
        self.b = int(input("Enter the breadth of the shape. \n"))
        self.speak("Enter the height of the shape")
        self.speak("If the shape is 2 dimensional enter 0")
        self.h = int(input("Enter the height of the shape. \n"))
        self.speak("Choose an option, and enter the number corresponding to the option.")
        self.op = int(input("Choose an option: \n 1 - Area \n 2 - Perimeter \n 3 - Volume \n 4 - Quit \n"))
        sleep(1)
        
    def run(self):
            self.startup()
            self.operations(self.op)

    def operations(self, opt):
        def area(length, breadth):
            calArea = length * breadth
            return(str(calArea))
        
        def perimeter(length, breadth):
            CalPerimeter = 2 * (length + breadth)
            return(CalPerimeter)
        
        def volume(length, breadth, height):
            CalVolume = length * breadth * height
            return(CalVolume)
        
        if opt == 1:
            self.data = str(area(self.l, self.b))
            print(self.data)
            self.speak("The area of the shape is")
            self.speak(self.data)
            sleep(3)
        elif opt == 2:
            self.data = str(perimeter(self.l, self.b))
            print(self.data)
            self.speak("The perimeter of the shape is")
            self.speak(self.data)            
            sleep(3)
        elif opt == 3:
            self.data = str(volume(self.l, self.b, self.h))
            print(self.data)
            self.speak("The volume of the shape is")
            self.speak(self.data)             
            sleep(3)
        else:
            print("Exiting program.")
            self.speak("Goodbye!")
            sleep(3)
            self.running = False
            
    def speech_init(self):
        self.speechEngine.setProperty("rate", 125)
        self.speechEngine.setProperty("volume", 0.8)
    
    def speak(self, msg):
        self.speechEngine.say(msg)
        self.speechEngine.runAndWait()
        
            
           
calc = UI()

while calc.running:
    calc.run()
print("Thank you for using this program. \nVer 1.2")

