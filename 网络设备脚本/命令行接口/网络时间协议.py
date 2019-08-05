from ..基础接口 import 网络时间协议
from . import 模式
class I服务器配置(模式.I模式, 网络时间协议.I服务器配置):
	def __init__(self, a):
		模式.I模式.__init__(self, a)
class I客户端配置(模式.I模式, 网络时间协议.I客户端配置):
	def __init__(self, a):
		模式.I模式.__init__(self, a)
class I远端配置(模式.I模式, 网络时间协议.I远端配置):
	def __init__(self, a, a地址):
		模式.I模式.__init__(self, a)
		self.m地址 = a地址
	def fg地址(self):
		return self.m地址