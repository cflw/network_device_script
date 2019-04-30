from . import 模式
from ..基础接口 import 接口配置
class I接口配置模式基础(模式.I模式):	#所有接口配置模式接口的基类
	c模式名 = "接口配置模式"
	def __init__(self, a设备, a接口):
		I模式.__init__(self, a设备)
		if not (isinstance(a接口, S接口) or type(a接口) == str):
			raise TypeError("a接口 必须是一个 S接口 对象")
		self.m接口 = a接口
	def __eq__(self, a):
		if not isinstance(a, I接口配置模式基础):
			return False
		return self.m接口 == a.m接口
	#通用方法
	def fg模式参数(self):	#在这里确定不同厂商的接口名称
		return (self.m接口,)
	def fg进入命令(self):
		return C命令("interface") + self.fg模式参数()
	def fg接口(self):
		return self.m接口
class I接口配置模式(I接口配置模式基础, 接口配置.I接口配置模式):
	def __init__(self, a, a接口):
		I接口配置模式基础.__init__(self, a, a接口)
