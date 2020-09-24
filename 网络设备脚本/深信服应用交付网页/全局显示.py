from ..基础接口 import 全局显示
from . import 模式
class C全局显示ad70(全局显示.I全局显示):
	"""适用于: ad 7.0.3"""
	def __init__(self, a设备):
		self.m设备 = a设备
	def f显示_序列号(self):
		from . import 系统信息
		v序列号页 = 系统信息.C序列号页(self.m设备)
		return v序列号页.fg网关序号()
class C全局显示ad705(全局显示.I全局显示):
	"""适用于: ad 7.0.8"""
	def __init__(self, a设备):
		self.m设备 = a设备
	def f显示_路由表4(self):
		from . import 静态路由
		v静态路由 = 静态路由.C静态路由ad705(self.m设备)
		return v静态路由.f显示_路由表()