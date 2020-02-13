import Audio
import Switch
import Notification

class Authorize:

	def auth(userID, img):
		if (userUD == 'Unknown'):
			Switch.open()
			Audio.negative()
			Notification.notif(img)
		else:
			Switch.close()
			Audio.positive(userID)
			