from ..基础接口 import 操作
from ..基础接口 import 全局配置
from ..基础接口 import 接口 as 北向接口
from . import 接口 as 实现接口
class C全局配置(全局配置.I全局配置):
	"""适用于: wdr5620"""
	def __init__(self, a设备):
		self.m设备 = a设备
	def f模式_接口(self, a接口, a操作 = 操作.E操作.e设置):
		v接口 = 实现接口.f创建接口(a接口)
		if v接口.m类型 == 北向接口.E类型.e无线电:
			from . import 无线局域网 as 实现无线局域网
			return 实现无线局域网.C无线电接口配置(self.m设备)
	def f模式_无线局域网(self):	#暂时
		from . import 无线局域网 as 实现无线局域网
		return 实现无线局域网.C无线电接口配置(self.m设备)
