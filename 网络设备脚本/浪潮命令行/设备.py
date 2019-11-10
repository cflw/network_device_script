from .. import 浪潮
from ..命令行接口 import 设备 as 南向设备
from ..命令行接口 import 命令
from ..命令行接口 import 用户模式
#===============================================================================
# s系列(v3.x)
#===============================================================================
class C设备sv3_50(南向设备.I设备):
	"""适用于: s6550(v3.50)"""
	def __init__(self, a连接, a型号, a版本):
		南向设备.I设备.__init__(self, a连接)
		self.m型号 = a型号
		self.m版本 = a版本
		self.fs自动换页("--More--")
	#输入输出
	def f输入_结束符(self):
		self.f输入('\x1a')	#ctrl+z
	#模式
	def f模式_用户(self):
		from . import 用户模式
		return 用户模式.C用户模式sv3(self)
	#命令
	def f执行命令(self, a命令):
		v输出 = 南向设备.I设备.f执行命令(self, a命令)
		return v输出
	def f执行用户命令(self, a命令):
		#退到用户模式执行
		self.ma模式[0].f切换到当前模式()
		return self.f执行命令(a命令)
	def f执行显示命令(self, a命令, a自动换页 = True):
		#退到用户模式执行
		self.ma模式[0].f切换到当前模式()
		v输出 = 南向设备.I设备.f执行显示命令(self, a命令, a自动换页)
		return self.m处理显示结果(v输出)
	def f处理显示结果(self, a输出):
		v输出 = a输出.replace("\r\n", "\n")
		v输出 = 南向设备.f去头尾行(v输出)
		return v输出
	def f退出(self, a关闭 = False):
		self.f执行命令("exit")
class C设备sv3_60(C设备sv3_50):
	"""适用于: s6550(v3.60)"""
	def __init__(self, a连接, a型号, a版本):
		C设备sv3_50.__init__(self, a连接, a型号, a版本)
	def f执行显示命令(self, a命令, a自动换页 = True):
		v输出 = 南向设备.I设备.f执行显示命令(self, a命令, a自动换页)
		v输出 = v输出.replace("\r\n", "\n")
		v输出 = 南向设备.f去头尾行(v输出)
		return v输出