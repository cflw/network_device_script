from ..基础接口 import 全局配置
from . import 模式
class C全局配置_ev6(全局配置.I全局配置):
	"""适用于: 浪潮s5350(v6.x)"""
	def __init__(self, a设备):
		self.m设备 = a设备
	def f模式_时间(self):
		from . import 时间
		return 时间.C时间_ev6(self.m设备)
	def fs设备名(self, a名称):
		self.m设备.f切换模式(模式.C模式_ev6.c系统管理_系统配置)
		w设备名 = self.m设备.f查找("/html/body/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[1]/td/table/tbody/tr[5]/td[2]/form/table/tbody/tr/td/table/tbody/tr[6]/td[3]/input")
		w设备名.f输入(a名称)
		w应用 = self.m设备.f查找("/html/body/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[1]/td/table/tbody/tr[5]/td[2]/form/table/tbody/tr/td/table/tbody/tr[8]/td[6]/input")
		w应用.f点击()