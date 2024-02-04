from ..基础接口 import 全局显示
from . import 模式
class C全局显示_p(全局显示.I全局显示):
	"""适用于: 山石SG-6000-P1242(v5.5)"""
	t模式 = 模式.C模式_sg6000p1242
	def __init__(self, a设备):
		self.m设备 = a设备
	def f模式_设备(self):
		from . import 设备模式
		return 设备模式.C设备显示_p(self.m设备)
class C全局显示_a(全局显示.I全局显示):
	"""适用于: 山石SG-6000-A5100(v5.5)"""
	t模式 = 模式.C模式_sg6000a5100
	def __init__(self, a设备):
		self.m设备 = a设备
	def f模式_设备(self):
		from . import 设备模式
		return 设备模式.C设备显示_a(self.m设备)
