# -*- coding: utf-8 -*-
import unittest
import sys
sys.path.append('../')
import botelegram
from botelegram.types import Action

class Test_Botelegram(unittest.TestCase):

	def test_assertTrue(self):
		bot = botelegram.TBot()
		bot.set_token("api_token")
		ret=bot.sendChatAction(114093395,Action.upload_photo)
		self.assertTrue(ret)

if __name__ == '__main__':
	unittest.main()

