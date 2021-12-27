from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from tkinter import *
import pygame
import pyttsx3
import time

#Getting la Musica ready
pygame.init()
pygame.mixer.init()

#Stopping Music Playback

def musicStop():
	pygame.mixer.music.stop()


# Function for clearing entries
def clearAll() :

	
	negativeField.delete(0, END)
	neutralField.delete(0, END)
	positiveField.delete(0, END)
	overallField.delete(0, END)

	
	textArea.delete(1.0, END)
	
# function to print sentiments
# of the sentence.
def detect_sentiment():

	# get the whole input content from text box
	sentence = textArea.get("1.0", "end")

	# Create a SentimentIntensityAnalyzer object
	analyzer_object = SentimentIntensityAnalyzer()
	sentiment_dict = analyzer_object.polarity_scores(sentence)

	string = str(sentiment_dict['neg']*100) + "% Negative" #We multiply by 100 to get the value out of 100% since +1=100%pov and -1=100%neg
	negativeField.insert(10, string)
	
	string = str(sentiment_dict['neu']*100) + "% Neutral"
	neutralField.insert(10, string)

	string = str(sentiment_dict['pos']*100) +"% Positive"
	positiveField.insert(10, string)
	
	# decide sentiment as positive, negative and neutral
	if sentiment_dict['compound'] >= 0.05 :
		string = "Positive"

	elif sentiment_dict['compound'] <= - 0.05 :
		string = "Negative"
	

	else :
		string = "Neutral"

	overallField.insert(10, string)
		
def textToSpeech():
	#COS WHY TF NOT
    engine = pyttsx3.init()
    time.sleep(3)
    engine.say("YOOOOOOOOOOOOO WELCOME.")
    engine.runAndWait()
    time.sleep(3)
    engine.say("I hope that you'll like this. I did this all by myself.")
    engine.runAndWait()
    time.sleep(3)
    engine.say("LETS FUCKING GOOOOOOOOOOOOOOOOOOO.")
    engine.runAndWait()

def laMusica():#DA MUSIC
	pygame.mixer.music.load("Attack on Titan S3 OST tk 0N ttn WMId.mp3")
	pygame.mixer.music.play()
	pygame.mixer.music.set_volume(0.6)

# GUI Main Code
if __name__ == "__main__" :
	

	gui = Tk()
	gui.config(background = "light blue")
	gui.title("Sentiment Detector")
	gui.geometry("425x425")
	enterText = Label(gui, text = "Enter Your Sentence",
									bg = "light blue")
	textArea = Text(gui, height = 5, width = 25, font = "lucida 13")


	check = Button(gui, text = "Check Sentiment", fg = "Black",
						bg = "Red", command = detect_sentiment)

	negative = Label(gui, text = "Sentence was rated as: ",
										bg = "light green")

	neutral = Label(gui, text = "Sentence was rated as: ",
									bg = "light green")

	positive = Label(gui, text = "Sentence was rated as: ",
										bg = "light green")

	overall = Label(gui, text = "Sentence Overall Rated As: ",
										bg = "light green")





	negativeField = Entry(gui)

	neutralField = Entry(gui)

	positiveField = Entry(gui)

	overallField = Entry(gui)

	#Stop music
	Mute = Button(gui, text="Mute", fg="Black",
					bg="Red", command= musicStop)

	#clear stuff
	Clear = Button(gui, text = "Clear", fg = "Black",
					bg = "Red", command = clearAll)
	
	#exit
	Exit = Button(gui, text = "Exit", fg = "Black",
						bg = "Red", command = exit)


	#Placement.
	enterText.grid(row = 0, column = 2)
	
	textArea.grid(row = 1, column = 2, padx = 10, sticky = W)
	
	check.grid(row = 2, column = 2)
	
	negative.grid(row = 3, column = 2)
	
	neutral.grid(row = 5, column = 2)
	
	positive.grid(row = 7, column = 2)
	
	overall.grid(row = 9, column = 2)
	
	negativeField.grid(row = 4, column = 2)

	neutralField.grid(row = 6, column = 2)
					
	positiveField.grid(row = 8, column = 2)
	
	overallField.grid(row = 10, column = 2)
	
	Mute.grid(row = 0, column = 1)

	Clear.grid(row = 11, column= 2)
	
	Exit.grid(row = 12, column = 2)

	# The loops
	laMusica()
	textToSpeech()
	gui.mainloop()
	
