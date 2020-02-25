from gtts import gTTS
import os

class Audio:
	
	def positive(userID):
		engine = pyttsx.init()
		saystring = 'Welcome ' + userID
		engine.say(saystring)
		
	def negative():
		engine = pyttsx.init()
		engine.say('Unauthorized user')