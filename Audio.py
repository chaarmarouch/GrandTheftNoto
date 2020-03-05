from gtts import gTTS
import os

def enrollUser(userID):
	tts = gTTS(text = 'Welcome ' + userID, lang='en')
	tts.save(userID + ".mp3")

def createNeg():
	tts = gTTS(text = 'Unauthorized User', lang='en')
	tts.save("0000.mp3") 

def positive(userID):
	path = userID + '.mp3'
	os.system("play 'path'")
	
def negative():
	os.system("play '0000.mp3'")