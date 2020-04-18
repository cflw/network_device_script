from ..基础接口 import 全局配置	
from . import 模式
class I全局配置(全局配置.I全局配置, 模式.I模式):
	#设置
	def f设置_系统名(self, a名称):
		self.m设备.f设置(".1.3.6.1.2.1.1.5.0", a名称)
	def fs设备名(self, a名称):
		self.f设置_系统名(a名称)