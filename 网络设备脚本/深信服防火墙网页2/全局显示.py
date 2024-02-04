from ..基础接口 import 全局显示
from . import 模式
class C全局显示af8035(全局显示.I全局显示):
	"""适用于:v8.0.35~"""
	def __init__(self, a设备):
		self.m设备 = a设备
	def f显示_中央处理器利用率(self):
		self.m设备.f切换模式(模式.C模式_af8035.c首页)
		c路径 = "/html/body/div[2]/div/div/div[2]/div/div[2]/div[2]/div[1]/div/div/div/div/div/div/div/div/div[2]/div/div/div/div/div/div/div/div/div/div/div[6]/div[2]/div/div/div/div/div[1]/div/div[2]/div/div/div/div[1]/div/div[2]/div/span[1]/span"
		w利用率 = self.m设备.f查找(c路径)
		from . import 系统信息
		return 系统信息.f解析利用率af8035(w利用率.fg文本())
	def f显示_内存利用率(self):
		self.m设备.f切换模式(模式.C模式_af8035.c首页)
		c路径 = "/html/body/div[2]/div/div/div[2]/div/div[2]/div[2]/div[1]/div/div/div/div/div/div/div/div/div[2]/div/div/div/div/div/div/div/div/div/div/div[6]/div[2]/div/div/div/div/div[1]/div/div[2]/div/div/div/div[2]/div/div[2]/div/span[1]/span"
		w利用率 = self.m设备.f查找(c路径)
		from . import 系统信息
		return 系统信息.f解析利用率af8035(w利用率.fg文本())
	def f显示_路由表4(self):
		from . import 路由表信息
		v查看路由 = 路由表信息.C查看路由af8035(self.m设备)
		return v查看路由.f显示_路由表()
