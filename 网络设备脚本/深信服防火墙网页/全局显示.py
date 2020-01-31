from ..基础接口 import 全局显示
from . import 模式
class C全局显示(全局显示.I全局显示):
	"""适用于:v8.0.7~8.0.13"""
	def __init__(self, a设备):
		self.m设备 = a设备
	def f显示_中央处理器利用率(self):
		self.m设备.f切换模式(模式.C模式af8.c运行状态_总览)
		w资源利用率 = self.m设备.f查找('//*[@id="ext-comp-1049"]')
		w处理器利用率 = w资源利用率.f查找("ul/li[1]")
		from . import 系统信息
		return 系统信息.f解析利用率(w处理器利用率.fg文本())
	def f显示_内存利用率(self):
		self.m设备.f切换模式(模式.C模式af8.c运行状态_总览)
		w资源利用率 = self.m设备.f查找('//*[@id="ext-comp-1049"]')
		w内存利用率 = w资源利用率.f查找("ul/li[2]")
		from . import 系统信息
		return 系统信息.f解析利用率(w内存利用率.fg文本())
	def f显示_路由表4(self):
		from . import 路由表信息
		v查看路由 = 路由表信息.C查看路由(self.m设备)
		return v查看路由.f显示_路由表()