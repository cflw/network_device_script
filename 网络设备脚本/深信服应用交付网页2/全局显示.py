from ..基础接口 import 全局显示
from . import 模式
class C全局显示_ad705(全局显示.I全局显示):
	"""适用于: ad 7.0.8"""
	def __init__(self, a设备):
		self.m设备 = a设备
	def f模式_设备(self):
		from . import 设备模式
		return 设备模式.C设备显示_ad705(self.m设备)
	def f显示_路由表4(self):
		from . import 静态路由
		v静态路由 = 静态路由.C静态路由_ad705(self.m设备)
		return v静态路由.f显示_路由表()