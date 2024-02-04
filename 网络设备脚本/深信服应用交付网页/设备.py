import time
import cflw代码库py.cflw字符串 as 字符串
from ..网页接口 import 设备
from . import 模式
class C设备_ad70(设备.I设备):
	"""适用于: ad 7.0.3"""
	def __init__(self, a连接, a型号, a版本):
		设备.I设备.__init__(self, a连接)
		self.m型号 = a型号
		self.m版本 = a版本
		self.m当前模式 = 模式.C模式_ad70.c主页
		v链接 = self.fg地址()
		self.m主机 = 字符串.f提取字符串之间(v链接, "//", "/")
	def f切换模式(self, aa模式: tuple):
		if self.m当前模式 == aa模式:
			return
		for v序号, v名称, v路径 in aa模式:
			v地址 = self.fg模式地址(v路径)
			self.fs地址(v地址)
		self.m当前模式 = aa模式
	def fg模式地址(self, a模式: str):
		return f"https://{self.m主机}{a模式}"
	def f模式_用户(self):
		from . import 用户模式
		return 用户模式.C用户模式_ad70(self)
