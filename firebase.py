from google.cloud import storage
from image import convert
from pyfcm import FCMNotification
#from oauth2client.service_account import ServiceAccountCredentials
import os
# Enable Storage

def sendToStorage(image):

	convert(image)

	storage_client = storage.Client()
	print "get bucket"
	bucket = storage_client.get_bucket('enter-project-id-here')
	print "set blob"
	blob = bucket.blob('fejs')
	print "upload blob"
	blob.upload_from_filename('face.jpg')
	print "after upload"
	sendNotification('fejs')

def sendNotification(string):

	push_service = FCMNotification(api_key="enter-key-here")

# OR initialize with proxies

#proxy_dict = {
#          "http"  : "http://127.0.0.1",
#          "https" : "http://127.0.0.1",
#        }
#push_service = FCMNotification(api_key="<api-key>", proxy_dict=proxy_dict)

# Your api-key can be gotten from:  https://console.firebase.google.com/project/<project-name>/settings/cloudmessaging

	registration_ids = ["enter-ids-here-separated-with-commas"]
	message_title = "Nowe zdjecie"
	message_body = string
	result = push_service.notify_multiple_devices(registration_ids=registration_ids, message_title=message_title, message_body=message_body)

# Send to multiple devices by passing a list of ids.
#	registration_ids = ["<device registration_id 1>", "<device registration_id 2>", ...]
#	message_title = "Uber update"
#	message_body = "Hope you're having fun this weekend, don't forget to check today's news"
#	result = push_service.notify_multiple_devices(registration_ids=registration_ids, message_title=message_title, message_body=message_body)

	print result
