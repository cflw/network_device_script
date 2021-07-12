import cflw代码库py.cflw网络连接 as 连接
from ..命令行接口 import 设备 as 南向设备
from ..命令行接口 import 用户模式 as 用户模式
from .. import 中兴
from .常量 import *
class C设备(南向设备.I设备):
	def __init__(self, a连接, a型号, a版本):
		南向设备.I设备.__init__(self, a连接)
		self.m连接.fs编码("gb2312")
		self.m型号 = a型号
		self.m版本 = a版本
		self.fs自动换页("--More--")
	#输入输出
	def f输入_结束符(self):	#ctrl+c
		self.f输入(c结束符)
	def f执行显示命令(self, a命令, a自动换页 = True):
		v命令 = str(a命令)
		v输出 = 南向设备.I设备.f执行显示命令(self, a命令 = v命令, a自动换页 = a自动换页)
		v输出 = v输出.replace("\r\n", "\n")
		v输出 = 南向设备.f去头尾行(v输出)
		# if v输出.count("\n") < 10:	#输出行数太少,检测是否有异常
		# 	self.f检测命令异常(v输出)
		return v输出
	#动作
	def f退出(self):
		self.f执行命令("exit")
	#模式
	def f模式_用户(self):
		if self.m型号 == 中兴.E型号.zxr10_m6000:
			from . import 用户模式
			v模式 = 用户模式.C用户模式m6000(self)
		else:
			raise ValueError("不支持的型号")
		return v模式
