from ..基础接口 import 设备模式
from . import 模式
t模式 = 模式.C模式_af8059
class C设备显示_af8059(设备模式.I设备显示):
	"""适用于: 深信服FW-2000-X210(af8.0.83)"""
	def __init__(self, a设备):
		self.m设备 = a设备
	def f显示_序列号(self):	#返回网关ID
		self.m设备.f切换模式(t模式.c系统_通用设置_授权管理)
		c路径 = "/html/body/div[1]/section/main/div/div/div/div/div/div/div/div[2]/div/div/div[2]/div[1]/div/div/div[1]/div[7]/span[2]"
		v元素 = self.m设备.f查找_直到(c路径)
		return v元素.fg文本()