from Audio import *
import time

def audioTest(userID):
	enrollUser(userID)
	createNeg()
	negative()
	time.sleep(2)
	positive(userID)
	