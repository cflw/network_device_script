from ..基础接口 import 全局显示
from . import 模式
from . import 基本表信息
class C全局显示ev6(全局显示.I全局显示):
	"""适用于: 浪潮s5350(v6.x)"""
	def __init__(self, a设备):
		self.m设备 = a设备
	def f显示_时间(self):
		self.m设备.f切换模式(模式.C模式ev6.c系统管理_系统配置)
		w时间日期 = self.m设备.f网页_查找("/html/body/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[1]/td/table/tbody/tr[5]/td[2]/form/table/tbody/tr/td/table/tbody/tr[10]/td[3]/input")
		from . import 时间
		return 时间.f解析时间ev6(w时间日期.fg文本())
	#表
	def f显示_接口表(self):
		return 基本表信息.C接口表ev6(self.m设备)