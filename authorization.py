import os
import base64
from Crypto.Cipher import AES
from cryptography.fernet import Fernet
from config import ConfConst

class Authorization:

	def __init__(self):
		self.const = ConfConst()
	def signIn(self):
		#print (self._crackPassword())
		return "signed on"
	def __crackPassword(self):
		fnet = Fernet(self.const.UNKEY)
		return fnet.decrypt(self.const.PASSWORD).decode()
