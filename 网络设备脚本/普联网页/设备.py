import time
from ..网页接口 import 设备 as 网页设备
class C设备(网页设备.I设备):
	"""适用于: wdr5620"""
	def __init__(self, a连接, a型号, a版本):
		网页设备.I设备.__init__(self, a连接)
		self.m型号 = a型号
		self.m版本 = a版本
		self.ma模式 = []
	def f模式_用户(self):
		from . import 用户模式
		return 用户模式.C用户模式(self)
	#模式
	def f切换模式(self, aa模式: tuple):
		if self.ma模式 == aa模式:
			return
		time.sleep(0.2)
		for v模式 in aa模式:
			v元素 = self.f网页_查找(f"//*[@id='{v模式}']")
			v元素.f点击()
			time.sleep(0.2)
		self.ma模式 == aa模式