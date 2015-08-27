# -*- coding: utf-8 -*-
import unittest
import sys
sys.path.append('../')
import botelegram

class Test_Botelegram(unittest.TestCase):

	def test_assertTrue(self):
		bot = botelegram.TBot()
		bot.set_token("api_token")
		ret=bot.sendLocation(114093395,42.2,32.1)
		self.assertTrue(ret.ok)

if __name__ == '__main__':
	unittest.main()
