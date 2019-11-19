import time
import cflw代码库py.cflw字符串 as 字符串
from ..网页接口 import 设备 as 网页设备
class C设备ev6(网页设备.I设备):
	"""适用于: 盛科e580(v6.x), 浪潮cn61108pcvh(v6.x), 浪潮s5350(v6.x)"""
	def __init__(self, a连接, a型号, a版本):
		网页设备.I设备.__init__(self, a连接)
		self.m型号 = a型号
		self.m版本 = a版本
		self.m主机 = None	#登录后赋值
		self.m会话 = None	#登录后赋值
		self.m当前模式 = None
	def f模式_用户(self):
		from . import 用户模式
		return 用户模式.C用户模式ev6(self)
	def f解析登录后地址(self):
		"""登录后调用
		解析"http://x.x.x.x/web_index.cgi?sessionId=1573646679&lang=cn" """
		v链接 = self.f网页_g地址()
		self.m主机 = 字符串.f提取字符串之间(v链接, "//", "/")
		self.m会话 = 字符串.f提取字符串之间(v链接, "sessionId=", "&")
	#模式
	def f切换模式(self, a模式):
		if self.m当前模式 == a模式:
			return
		v地址 = self.fg模式地址(a模式)
		self.f网页_s地址(v地址)
		self.m当前模式 = a模式
	def fg模式地址(self, a模式):
		return f"http://{self.m主机}/{a模式}?sessionId={self.m会话}&lang=cn"