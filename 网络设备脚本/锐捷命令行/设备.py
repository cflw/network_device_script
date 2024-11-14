import cflw代码库py.cflw网络连接 as 连接
from ..命令行接口 import 设备 as 南向设备
from ..思科命令行.常量 import *
class C设备(南向设备.I设备):
	"""适用于: s5750(v11.4)"""
	def __init__(self, a连接, a型号, a版本):
		南向设备.I设备.__init__(self)
		if a连接.c连接特性 & 连接.E连接特性.e命令行:
			self.m连接 = a连接
			self.m连接.fs编码("gb2312")
		else:
			raise TypeError("a连接 必须是 I连接 类型")
		self.m型号 = a型号
		self.m版本 = a版本
		self.fs自动换页("--More--")
	def f输入_结束符(self):	#ctrl+c
		self.f输入(c结束符)
	def f处理显示结果(self, a输出):
		v输出 = a输出.replace("\r\n", "\n")
		v输出 = 南向设备.f去头尾行(v输出)
		return v输出
	#动作
	def f退出(self):
		self.f执行命令("exit")
	#模式
	def f模式_用户(self):
		from . import 用户模式
		v模式 = 用户模式.C用户模式(self)
		return v模式
	def f模式_启动(self):
		from . import 启动
		if self.m版本 < 10.4:
			return 启动.C启动v10(self)
		elif self.m版本 < 11:
			return 启动.C启动v1042(self)
		elif self.m版本 < 12:
			return 启动.C启动v11(self)
		else:
			return NotImplementedError("不支持的版本")
