from gtts import gTTS
import os

"""fh = open("test.txt", "r")
my_Text = fh.read().replace("\n", " ") """
# if you want read text from a file which is located in your current directory or computer uncomment the above statement

my_Text = "Hi, There This is Kirankumar Gonti From Hyderabad, please Hire me"

language = "en" #Change the language if you want other.

output = gTTS(text = my_Text, lang = language, slow = False)

output.save("My_audio.mp3")

"""fh.close()"""
# uncomment the above line if you want to read a text from a file

os.output("start My_audio.mp3")