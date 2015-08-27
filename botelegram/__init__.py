import os
import json
import requests
from distutils.version import LooseVersion
from botelegram.version import __version__
from botelegram.types import (
	User,
	Message,
	PhotoSize,
	Audio,
	Document,
	Sticker,
	Video,
	Contact,
	Location,
	UserProfilePhotos,
	ReplyKeyboardMarkup,
	ReplyKeyboardHide,
	ForceReply,
	Update,
	UpdateResult,)

from botelegram.exceptions import (
	TokenError,
	OfsetError,
	LimitError,
	TimeOutError,
	ChatIdError,
	TextError,
	ReplyMarkupError,
	DisableWebPagePreviewError,
	ReplyMarkupError,
	FromChatIdError,
	MessageIdError,
	CaptionError,
	FileLocationError,
	RequestsConnectionError,
	ActionError,
	LatitudeError,
	LongitudeError,
	VideoError,
	StickerError,
	DocumentError,
	AudioError,
	PhotoError,
	LatitudeBettwenError,
	LongitudeBettwenError,
	UnauthorizedAccessError,
	UnknownError,
)


""" Telegram Bot Api Main Class """
class TBot:

	__url = "https://api.telegram.org/bot"

	def __init__(self, token=None):
		"""
		:param token: bot API token as string
		:return: TBot object.
		"""
		self.__token = token
		self.__bot_id = None
	
	def set_token(self,token):
		"""
		Set function for token after initialization
		:param token: bot API token as string
		"""
		self.__token = token

	def get_token(self):
		"""
		get function for token
		:return token: bot API token as string
		"""
		return self.__token

	def set_bot_id(self,bot_id):
		"""
		Set function for Bot Id
		:param bot_id: Bot ID as integer
		"""
		self.__bot_id = int(bot_id)

	def get_bot_id(self):
		"""
		get function for Bot ID
		:return bot_id: bot ID as integer
		"""
		return self.__bot_id

	"""
	Starting external functions
	
	"""
	def getMe(self):
		if self.__token==None:
			raise TokenError()
		else:
			req = self._get( '/getMe')
			reqUser = User(req)
			return reqUser


	def getUpdate(self):
		if self.__token==None:
			raise TokenError()
		else:
			req = self._get( '/getUpdates')
			reqUpdate = UpdateResult(req)
			return reqUpdate

	def sendMessage(self, chat_id, text, disable_web_page_preview=None, reply_to_message_id=None, reply_markup=None):
		if self.__token==None:
			raise TokenError()
		else:
			req = self._post('/sendMessage',{'chat_id':chat_id,'text':text})
			reqMessage = Message(req)
			return reqMessage

	def forwardMessage(self, chat_id, from_chat_id, message_id):
		if self.__token==None:
			raise TokenError()
		else:
			req = self._post('/forwardMessage',{'chat_id':chat_id ,'from_chat_id':from_chat_id,'message_id':message_id})
			reqForwardMessage = Message(req)
			return reqForwardMessage


	def sendPhoto(self, chat_id, photo, caption=None, reply_to_message_id=None, reply_markup=None):
		if os.path.isfile(photo)==False:
			raise PhotoError
		if self.__token==None:
			raise TokenError()
		else:
			req = self._post('/sendPhoto', {'chat_id':chat_id},{'photo':(photo,open(photo))})
			reqMessage = Message(req)
			reqMessage.photos = []
			for photoData in req['result']['photo']:
				reqMessage.photos.append(PhotoSize(photoData))
			return reqMessage

	def sendAudio(self, chat_id, audio, caption=None, reply_to_message_id=None, reply_markup=None):
		if os.path.isfile(audio)==False:
			raise AudioError		
		if self.__token==None:
			raise TokenError()	
		else:
			req = self._post('/sendAudio', {'chat_id':chat_id},{'audio':(audio,open(audio))})	
			reqMessage = Message(req)
			reqMessage.audio = Audio(req['result']['audio'])
			return reqMessage

	def sendLocation(self, chat_id, latitude, longitude, eply_to_message_id=None, reply_markup=None):
		if self.__token==None:
			raise TokenError()	
		else:
			
			req = self._post('/sendLocation', {'chat_id': chat_id,'latitude':latitude,'longitude':longitude})
			reqMessage = Message(req)
			reqMessage.location = Location(req['result']['location'])
			return reqMessage

	def sendDocument(self,chat_id, document, caption=None, reply_to_message_id=None, reply_markup=None):
		if os.path.isfile(document)==False:
			raise DocumentError
		if self.__token==None:
			raise TokenError()	
		else:

			req = self._post('/sendDocument', {'chat_id':chat_id},{'document':(document,open(document))})	
			reqMessage = Message(req)
			reqMessage.document = Document(req['result']['document'])
			return reqMessage

			

	def sendChatAction(self,chat_id, action, caption=None, reply_to_message_id=None, reply_markup=None):
		if self.__token==None:
			raise TokenError()	
		else:
			req = self._post('/sendChatAction', {'chat_id':chat_id,'action':action})	
			return req["ok"]			

	def getUserProfilePhotos(self,user_id, caption=None, reply_to_message_id=None, reply_markup=None):
		if self.__token==None:
			raise TokenError()	
		else:
			req = self._get('/getUserProfilePhotos', {'user_id':user_id})
			reqUserProfilePhotos = UserProfilePhotos(req)
			return reqUserProfilePhotos

            
	def sendVideo(self,chat_id, video,reply_to_message_id=None, reply_markup=None):
		if os.path.isfile(video)==False:
			raise VideoError
		if self.__token==None:
			raise TokenError()
		else:
			req = self._post('/sendVideo', {'chat_id':chat_id},{'video':(video,open(video))})
			reqMessage = Message(req)
			reqMessage.video = Video(req['result']['video'])
			return reqMessage
			
	def sendSticker(self,chat_id, sticker,reply_to_message_id=None, reply_markup=None):
		if os.path.isfile(sticker)==False:
			raise StickerError
		if self.__token==None:
			raise TokenError()
		else:
			req = self._post('/sendSticker', {'chat_id':chat_id},{'sticker':(sticker,open(sticker))})							
			reqMessage = Message(req)
			reqMessage.sticker = Sticker(req['result']['sticker'])
			return reqMessage

	def _post(self, function_name,post_data,post_files=None):
		try:
			if post_files==None:
				req = requests.post(self.__url + self.__token + function_name, data=post_data)
			else:
				req = requests.post(self.__url + self.__token + function_name, data=post_data,files=post_files)
		
		except requests.exceptions.RequestException, e:
			raise RequestException
		except requests.exceptions.ConnectionError, e:
			raise RequestsConnectionError
		except requests.exceptions.HTTPError, e:
			raise RequestsHTTPError
		except requests.exceptions.URLRequired, e:
			raise RequestsURLRequiredError
		except requests.exceptions.TooManyRedirects, e:
			raise RequestsTooManyRedirectsError
		except requests.exceptions.ConnectTimeout, e:
			raise RequestsConnectTimeoutError
		except requests.exceptions.ReadTimeout, e:
			raise RequestsReadTimeoutError
		except requests.exceptions.Timeout, e:
			raise RequestsTimeoutError

		if req.status_code==401:
			raise UnauthorizedAccessError
		if req.status_code==403:
			raise OfsetError()
		if req.status_code != requests.codes.ok:
			raise UnknownError()
		else:
			return req.json()
			#return Message(req.json())

	def _get(self, function_name,get_data = None):
		try:
			if get_data==None:
				req = requests.get(self.__url + self.__token + function_name)
			else:
				req = requests.get(self.__url + self.__token + function_name, data=get_data)
		
		except requests.exceptions.RequestException, e:
			raise RequestException
		except requests.exceptions.ConnectionError, e:
			raise RequestsConnectionError
		except requests.exceptions.HTTPError, e:
			raise RequestsHTTPError
		except requests.exceptions.URLRequired, e:
			raise RequestsURLRequiredError
		except requests.exceptions.TooManyRedirects, e:
			raise RequestsTooManyRedirectsError
		except requests.exceptions.ConnectTimeout, e:
			raise RequestsConnectTimeoutError
		except requests.exceptions.ReadTimeout, e:
			raise RequestsReadTimeoutError
		except requests.exceptions.Timeout, e:
			raise RequestsTimeoutError

		if req.status_code==401:
			raise UnauthorizedAccessError
		if req.status_code==403:
			raise OfsetError()
		if req.status_code != requests.codes.ok:
			raise UnknownError()
		else:
			return req.json()