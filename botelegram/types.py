# -*- coding: utf-8 -*-
from botelegram.exceptions import LimitError
import json
import datetime

class User():
	"""
	Types User Parameters
	"""
	id = None
	first_name = None
	last_name = None
	username = None
	ok = None
	error_code = None
	error_message = None
	
	def __init__(self, json):
		self.ok = json['ok']
		if self.ok == False:
			self.error_code = json['error_code']
			self.error_message = json['description']
		else:
			self.id = json['result']['id']
			if "first_name" in json['result']:
				self.first_name = str(json['result']['first_name'])
			if "username" in json['result']:
				self.username = str(json['result']['username'])
			if "last_name" in json['result']:
				self.last_name = str(json['result']['last_name'])



class Message():
	message_id = None
	botFrom = None
	date = None
	chat = None
	forward_from = None
	forward_date = None
	reply_to_message = None
	text = None
	audio = None
	document = None
	photos = None
	sticker = None
	video = None
	contact = None
	location = None
	new_chat_participant = None
	left_chat_participant = None
	new_chat_title = None
	new_chat_photo = None
	delete_chat_photo = None
	group_chat_created = None
	error_code = None
	error_message = None
	ok = None
	

	def __init__(self, json):
		self.ok = json['ok']
		if self.ok == False:
			self.error_code = json['error_code']
			self.error_message = json['description']
		else:
			self.message_id = json['result']['message_id']
			self.botFrom = User({'ok':'True','result':json['result']['from']})
			self.date = datetime.datetime.fromtimestamp(int(json["result"]['date'])).strftime('%Y-%m-%d %H:%M:%S')
			self.chat = User({'ok':'True','result':json['result']['chat']})
			if "text" in json['result']:
				self.text = str(json['result']['text'])

			if "forward_date" in json['result']:
				self.forward_date = datetime.datetime.fromtimestamp(int(json['result']['forward_date'])).strftime('%Y-%m-%d %H:%M:%S')
				self.forward_from = User({'ok':'True','result':json['result']['forward_from']})

	def photo(self):
		return photos[3]

	def photo_tiny(self):
		return photos[0]

	def photo_small(self):
		return photos[1]
		
	def photo_medium(self):
		return photos[2]

	def photo_large(self):
		return photos[3]

class PhotoSize():
	file_id = None
	width = None
	height = None
	file_size = None

	def __init__(self, json):
		self.file_id = str(json['file_id'])
		self.width = json['width']
		self.height = json['height']
		self.file_size = json['file_size']

				
class Audio():

	file_id = None
	duration = None
	mime_type = None
	file_size = None

	def __init__(self, json):
		self.file_id = str(json['file_id'])
		self.duration = json['duration']
		self.mime_type = json['mime_type']
		self.file_size = json['file_size']

class Document():
	
	file_id = None
	thumb = None
	file_name = None
	mime_type = None
	file_size = None

	def __init__(self, json):
		self.file_id = json['file_id']
		if "thumb" in json:
			self.thumb = json['thumb']
		self.file_name = str(json['file_name'])
		self.mime_type = json['mime_type']
		self.file_size = json['file_size']

class Sticker():

	file_id = None
	width = None
	height = None
	thumb = None
	file_size = None
	
	def __init__(self, json):
		self.file_id = str(json['file_id'])
		self.width = json['width']
		self.height = json['height']
		if "thumb" in json:
			self.thumb = json['thumb']
		self.file_size = json['file_size']

class Video():

	file_id = None
	width = None
	height = None
	duration = None
	thumb = None
	mime_type = None
	file_size = None
	caption = None

	def __init__(self, json):
		self.file_id = str(json['file_id'])
		self.width = json['width']
		self.height = json['height']
		self.duration = json['duration']
		if "thumb" in json:
			self.thumb = json['thumb']
		if "mime_type" in json:
			self.thumb = json['mime_type']
		if "caption" in json:
			self.thumb = json['caption']
		self.file_size = json['file_size']

class Contact():

	phone_number = None
	first_name = None
	last_name = None
	user_id = None

	def __init__(self, json):
		self.phone_number = json['phone_number']
		self.first_name = json['first_name']
		self.last_name = json['last_name']
		self.user_id = json['user_id']

class Location():

	longitude = None
	latitude = None

	def __init__(self, json):
		self.longitude = json['longitude']
		self.latitude = json['latitude']

class UserProfilePhotos():

	total_count = None
	photos = None
	ok = None
	error_code = None
	error_message = None
	__photosArray = None
	def __init__(self, json):
		self.ok = json['ok']
		if self.ok == False:
			self.error_code = json['error_code']
			self.error_message = json['description']
		
		else:
			self.total_count = json['result']['total_count']
			if self.total_count>0:
				self.photos = []
				self.__photosArray = []
				for photo in json['result']['photos']:
					for photoValues in photo:
						self.__photosArray.append(PhotoSize(photoValues))
					self.photos.append(self.__photosArray)
				
			

class ReplyKeyboardMarkup():

	keyboard = None
	resize_keyboard = None
	one_time_keyboard = None
	selective = None

	def __init__(self, json):
		self.keyboard = json['keyboard']
		self.resize_keyboard = json['resize_keyboard']
		self.one_time_keyboard = json['one_time_keyboard']
		self.selective = json['selective']

class ReplyKeyboardHide():
	
	hide_keyboard = None
	selective = None
	
	def __init__(self, json):
		self.hide_keyboard = json['hide_keyboard']
		self.selective = json['selective']

class ForceReply(object):

	orce_reply = None
	selective = None

	def __init__(self, json):
		self.orce_reply = json['orce_reply']
		self.selective = json['selective']

class Update():

	update_id = None
	message = None
	def __init__(self,json):
		self.update_id = json["update_id"]
		self.message = Message({'ok':'True','result':json["message"]})
		if "document" in json["message"]:
			self.message.document =  Document(json['message']['document'])
		if "audio" in json["message"]:
			self.message.audio = Audio(json['message']['audio'])
		if "sticker" in json["message"]:
			self.message.sticker = Sticker(json['message']['sticker'])
		if "video" in json["message"]:
			self.message.video = Video(json['message']['video'])
		if "photo" in json['message']:
			self.message.photos = []
			for photoData in json['message']['photo']:
				self.message.photos.append(PhotoSize(photoData))
					
					
			

class UpdateResult():

	update_list = list()
	ok = None
	error_code = None
	error_message = None

	def __init__(self, json):
		self.ok = json['ok']
		if self.ok == False:
			self.error_code = json['error_code']
			self.error_message = json['description']
		else:
			self.ok = True
			if json["result"]!=[]:
				for update in json["result"]:
					self.update_list.append(Update(update))

class Action():
	upload_photo = "upload_photo"
	typing = "typing"
	record_video = "record_video"
	record_audio = "record_audio"
	upload_audio = "upload_audio"
	upload_document = "upload_document"
	find_location = "find_location"
