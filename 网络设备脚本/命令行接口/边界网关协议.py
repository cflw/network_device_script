from ..基础接口 import 边界网关协议
from . import 模式
class I进程配置(模式.I模式, 边界网关协议.I进程配置):
	def __init__(self, a, a自治系统号):
		模式.I模式.__init__(self, a)
		self.m自治系统号 = int(a自治系统号)
	def fg模式参数(self):
		"返回自治系统号"
		return (self.m自治系统号,)
	def fg自治系统号(self):
		return self.m自治系统号
class I地址族配置(模式.I模式, 边界网关协议.I地址族配置):
	def __init__(self, a, a参数):
		模式.I模式.__init__(self, a)
		self.m参数 = a参数
class I对等体配置(模式.I模式, 边界网关协议.I对等体配置):
	def __init__(self, a, a对等体):
		模式.I模式.__init__(self, a)
		self.m对等体 = a对等体
	def __str__(self):
		return str(self.m对等体)
