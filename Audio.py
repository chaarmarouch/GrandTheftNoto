from gtts import gTTS
import os

def enrollUser(userID):
	tts = gTTS(text = 'Welcome ' + userID, lang='en')
	tts.save(userID + ".mp3")

def createNeg():
	tts = gTTS(text = 'Unauthorized User', lang='en')
	tts.save("0000.mp3") 

def positive(userID):
	os.system(userID + ".mp3")
	
def negative():
	os.system("0000.mp3")