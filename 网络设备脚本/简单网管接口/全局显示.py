from ..基础接口 import 全局显示
from . import 模式
class I全局显示(全局显示.I全局显示, 模式.I模式):
	def f获取_系统描述(self):
		return self.m连接.f获取(".1.3.6.1.2.1.1.1.0")
	def f获取_系统名(self):
		return self.m连接.f获取(".1.3.6.1.2.1.1.5.0")
	def f显示_设备名(self):
		return self.f获取_系统名()
