from tkinter import *
from gtts import gTTS
import os
from playsound import playsound
from translate import Translator

root = Tk()
root.geometry("600x500")
root.configure(bg = 'ghost white')
root.title("TEXT TO SPEECH CONVERTER")

Label(root , text = 'TEXT TO SPEECH CONVERTER' , font = "arial 20 bold", bg='white smoke').pack()


Msg = StringVar()
Label(root,text ="Enter Text", font = 'arial 15 bold', bg ='white smoke').place(x=20,y=60)

entry_field = Entry(root , textvariable = Msg ,width ='50')
entry_field.place(x=20 , y=100)

english_lang = 'en'
spanish_lang = 'es-ES'
french_lang = 'fr-FR'

def text_to_speech_english():   
    Message = entry_field.get()
    speech = gTTS(text = Message , lang = english_lang)
    speech.save('Sarthak.mp3')
    playsound('Sarthak.mp3')

def text_to_speech_spanish():
    Message = entry_field.get()
    translator = Translator(to_lang="spanish")
    translated_msg = translator.translate(Message)
    speech = gTTS(text = translated_msg, lang = spanish_lang) 
    speech.save('spanish.mp3')
    playsound('spanish.mp3')

def text_to_speech_french():
    Message = entry_field.get()
    translator = Translator(to_lang="french")
    translated_msg = translator.translate(Message)
    speech = gTTS(text = translated_msg, lang = french_lang) 
    speech.save('french.mp3')
    playsound('french.mp3')

def Exit():
    root.destroy()

def Reset():
    Msg.set("")
    os.remove('Sarthak.mp3')
    os.remove('spanish.mp3')
    os.remove('french.mp3')

Button(root, text = 'PLAY IN ENGLISH ', font = 'arial 15 bold' , command = text_to_speech_english ,width = '20').place(x=25,y=140)
Button(root, text = 'PLAY IN SPANISH ', font = 'arial 15 bold' , command = text_to_speech_spanish ,width = '20').place(x=25,y=200)
Button(root, text = 'PLAY IN FRENCH ', font = 'arial 15 bold' , command = text_to_speech_french ,width = '20').place(x=25,y=260)
Button(root, font = 'arial 15 bold',text = 'EXIT', width = '10' , command = Exit, bg = 'OrangeRed1').place(x=25 , y = 320)
Button(root, font = 'arial 15 bold',text = 'RESET', width = '10' , command = Reset).place(x=25, y = 380)

root.mainloop()

