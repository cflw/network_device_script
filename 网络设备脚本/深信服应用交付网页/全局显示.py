from ..基础接口 import 全局显示
class C全局显示_ad70(全局显示.I全局显示):
	"""适用于: ad 7.0.3"""
	def __init__(self, a设备):
		self.m设备 = a设备
	def f模式_设备(self):
		from . import 设备模式
		return 设备模式.C设备显示_ad70(self.m设备)
