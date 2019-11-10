from ..命令行接口 import 设备 as 南向设备
from ..命令行接口 import 命令
from ..命令行接口 import 用户模式
#===============================================================================
# nexus(v7.x)
#===============================================================================
class C设备nv7(南向设备.I设备):
	"""适用于: 思科nexus9000(v7.0), 浪潮cn8000系列(v7.3), 浪潮cn61108pcv(v7.0)"""
	def __init__(self, a连接, a型号, a版本):
		南向设备.I设备.__init__(self, a连接)
		self.m型号 = a型号
		self.m版本 = a版本
	#输入输出
	def f输入_结束符(self):
		self.f输入('\x1a')	#ctrl+z
	#模式
	def f模式_用户(self):
		from . import 用户模式
		if self.m版本 < 7.3:
			return 用户模式.C用户模式nv7_0(self)
		else:
			return 用户模式.C用户模式nv7_3(self)
	#命令
	def f执行显示命令(self, a命令, a自动换页 = True):
		v命令 = str(a命令)
		v输出 = 南向设备.I设备.f执行显示命令(self, v命令, a自动换页)
		return self.f处理显示结果(v输出)
	def f处理显示结果(self, a命令):
		v输出 = a命令.replace("\r\n", "\n")
		v输出 = 南向设备.f去头尾行(v输出)
		# if v输出.count("\n") < 10:
		# 	self.f检测命令异常(self, v输出)
		return v输出
	def f退出(self, a关闭 = False):
		self.f执行命令("exit")
