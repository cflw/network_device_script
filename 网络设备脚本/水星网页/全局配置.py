from ..基础接口 import 全局配置
class C全局配置(全局配置.I全局配置):
	def __init__(self, a设备):
		self.m设备 = a设备
	def f模式_静态路由(self):
		from . import 静态路由
		return 静态路由.C静态路由配置(self.m设备)