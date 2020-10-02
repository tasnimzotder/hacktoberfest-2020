#A Fortune Teller Using Python Programming
'''
Documentation:
1) Functionality = ask User for his Questions, Gives Answer to User through ansList( this is a list containing number of Answers.)
                    using pyttsx3 that makes it feel more advance :)
2) Global Variable = ansList (type: List, content: answers for user's question)
3) Author = prathmesh-Chaudhari05 (gitHub A/C)
'''

import random
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

ansLst = ["FINE :)","...","NOT NOW","Definately YES","Definately NO","I cant answer it now.","Hope You come later.","Without a doubt"]

def Fortune():  #main Code
    input("Ask a Question -> ")
    res = random.choice(ansLst)     #selects random answer from ansList
    engine.say(res)
    print(res)
    engine.runAndWait()
    Ask()


def Ask():  #function to ask next question from user
    ask = input("Want Ask Again [Y/N] : ")
    if ask == "Y":
        Fortune()
    elif ask == "N":
        exitmsg = "Thank You For Coming "+name
        engine.say(exitmsg)
        engine.say('Come Again :)')
        engine.runAndWait()
        exit()
    else:
        print("Cant Recognize")
        Ask()


print('Welcome to Fortune Teller :).')
name = input("Enter You Name -> ")
Fortune()