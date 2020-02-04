from ..基础接口 import 全局显示
from . import 模式
class C全局显示(全局显示.I全局显示):
	"""适用于: SG-6000-P1242(v5.5)"""
	def __init__(self, a设备):
		self.m设备 = a设备
	def f显示_序列号(self):
		self.m设备.f切换模式(模式.C模式sg6000.c系统_系统信息)
		w序列号 = self.m设备.f查找_直到("/html/body/div[4]/div/div[2]/div/div/div/div/div/div/span/div/table[1]/tbody/tr/td[2]/div")
		return w序列号.fg文本()