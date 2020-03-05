import pyttsx3
import os

class Audio:
	
	def positive(userID):
		engine = pyttsx3.init()
		saystring = 'Welcome ' + userID
		engine.say(saystring)
		
	def negative():
		engine = pyttsx3.init()
		engine.say('Unauthorized user')