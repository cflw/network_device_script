from ..命令行接口 import 设备
from ..网络设备 import 通用_实用 as 通用实用
class C设备(设备.I设备):
	"""适用于: mps4120(v6.6.4.1.3)"""
	def __init__(self, a连接, a型号, a版本):
		设备.I设备.__init__(self)
		if a连接.c连接特性 & 0x0001:
			self.m连接 = a连接
			self.m连接.fs编码("gb2312")
		else:
			raise TypeError("a连接 必须是 I连接 类型")
		self.m型号 = a型号
		self.m版本 = a版本
		self.fs自动换页("---MORE---")
	def f输入_结束符(self):	#ctrl+c
		self.f输入(c结束符)
	def f执行显示命令(self, a命令, a自动换页 = True):
		v命令 = str(a命令)
		v输出 = 设备.I设备.f执行显示命令(self, a命令 = v命令, a自动换页 = a自动换页)
		v输出 = v输出.replace("\r\n", "\n")
		v输出 = 通用实用.f去头尾行(v输出)
		# if v输出.count("\n") < 10:	#输出行数太少,检测是否有异常
		# 	self.f检测命令异常(v输出)
		return v输出
	#动作
	def f退出(self):
		self.f执行命令("exit")
	#模式
	def f模式_用户(self):
		from . import 用户模式
		v模式 = 用户模式.C用户模式(self)
		return v模式
