from ..基础接口 import 全局显示
from . import 模式
class C全局显示_af8059(全局显示.I全局显示):
	"""适用于: 深信服FW-2000-X210(af8.0.83)"""
	def __init__(self, a设备):
		self.m设备 = a设备
	def f模式_设备(self):
		from . import 设备模式
		return 设备模式.C设备显示_af8059(self.m设备)
