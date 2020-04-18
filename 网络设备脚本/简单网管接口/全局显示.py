from ..基础接口 import 全局显示
from . import 模式
from . import 标识
from . import 基本表信息
class I全局显示(全局显示.I全局显示, 模式.I模式):
	#系统
	def f获取_系统描述(self):
		return self.m设备.f获取(标识.c系统描述0)
	def f获取_系统名(self):
		return self.m设备.f获取(标识.c系统名称0)
	def f显示_设备名(self):
		return self.f获取_系统名()
	#网络
	def f显示_接口表(self):
		return 基本表信息.f接口表(self.m设备)
	def f显示_网络接口表4(self):
		return 基本表信息.f网络接口表4(self.m设备)