from ..基础接口 import 设备模式 as 北向设备模式
from . import 模式
class C设备显示_p(北向设备模式.I设备显示):
	"""适用于: 山石SG-6000-P1242(v5.5)"""
	t模式 = 模式.C模式_sg6000p1242
	def __init__(self, a设备):
		self.m设备 = a设备
	def f显示_序列号(self):
		c序列号路径 = "/html/body/div[4]/div/div[2]/div/div/div/div/div/div/span/div/table[1]/tbody/tr/td[2]/div"
		self.m设备.f切换模式(self.t模式.c系统_系统信息)
		w序列号 = self.m设备.f查找_直到(c序列号路径)
		return w序列号.fg文本()
class C设备显示_a(北向设备模式.I设备显示):
	"""适用于: 山石SG-6000-A5100(v5.5)"""
	t模式 = 模式.C模式_sg6000a5100
	def __init__(self, a设备):
		self.m设备 = a设备
	def f显示_序列号(self):
		c序列号路径 = "/html/body/div[3]/div[2]/div[2]/div/span/div/div[1]/div[2]/span/div/div/div/span/div/table[1]/tbody/tr/td[2]/div[1]"
		self.m设备.f切换模式(self.t模式.c系统_系统信息)
		w序列号 = self.m设备.f查找_直到(c序列号路径)
		return w序列号.fg文本()
