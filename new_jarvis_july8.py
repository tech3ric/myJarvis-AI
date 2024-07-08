"""This program was developed and written by Graeme.
   This was for an example tutorial for YouTube"""

"""NOTE - you will need a microphone plugged into your computer"""

"""Libraries - for notes on how to install see video 4 in this series"""
import pyttsx3, ollama
import speech_recognition as sr #don't forget to 'pip install' this library
import time # this is part of python - you should not need to install this
from ollama_test import call_ollama
from datetime import datetime
import pywhatkit
import wikipedia
import pyjokes
from random import choice

#recognizer_instance.recognize_whisper


"""variables"""
r = sr.Recognizer()
wake_word ="tony"  # setting up our 'wake' words

source = sr.Microphone() #setting up which mic we are using


def Speak(text):
    rate = 100 #Sets the default rate of speech
    engine = pyttsx3.init() #Initialises the speech engine
    voices = engine.getProperty('voices') #sets the properties for speech
    engine.setProperty('voice', voices[1].id) #Gender and type of voice
    engine.setProperty('rate', rate+50) #Adjusts the rate of speech
    engine.say(text) #tells Python to speak variable 'text'
    engine.runAndWait() #waits for speech to finish and then continues with program

def take_user_input():
     with sr.Microphone() as source:
            print("Listening for your command...")
            r.pause_threshold = 1
            audio = r.listen(source)
            try:
                command = r.recognize_google(audio)
                command = command.lower()
                print("You said: " + command)
                print(type(command))
                command = command.replace("hey", "")
                command = command.replace("hi", "")
                if wake_word in command and "tony" != command:
                    print("wake word in command")

                    check_command(command)
                else:
                    print("wake word NOT in command or not enough info")


            except sr.UnknownValueError:
                print("I'm sorry, I didn't understand that.")
            except sr.RequestError as e:
                Speak("Sorry, I couldn't reach the Google servers. Check your internet connection.")
            

     
def check_command(input):

    input = input.replace("tony", "")
    print(f"Print from check_command function: {input}")
    
    if 'play' in input:
        Speak("playing")
        print("Playing")

    elif 'time' in input or 'what is the time?' in input:
        time = datetime.now().strftime('%I:%M %p')
        print(time)
        Speak('Current time is ' + time)

    # elif "who is" in input or 'who the heck is' in input:
    #     answer = call_ollama(input)
    #     Speak(answer)



    elif 'tell me a joke' in input or 'tell a joke' in input:
        joke = pyjokes.get_joke()
        print(joke)
        Speak(joke)
    
    else:
        answer = call_ollama(input)
        Speak(answer)

# response = ollama.chat(model='llama3', messages=[{'role': 'user','content': 'Why is the sky blue?',},])
# print(response['message']['content'])


while True:
    take_user_input()