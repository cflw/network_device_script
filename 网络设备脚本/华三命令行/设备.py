import cflw代码库py.cflw网络连接 as 连接
from ..基础接口 import 异常
from ..命令行接口 import 设备 as 南向设备
from .. import 华三
from .常量 import *
ca错误文本与异常类 = [
	("% Unrecognized command found at '^' position.", 异常.X命令),
	("% Ambiguous command found at '^' position.", 异常.X命令)
]
class C设备(南向设备.I设备):
	def __init__(self, a连接, a型号, a版本):
		南向设备.I设备.__init__(self, a连接)
		self.fs自动换页("  ---- More ----")
		self.m连接.fs编码("gb2312")
		self.m型号 = a型号
		self.m版本 = a版本
	def f退出(self):
		self.f执行命令("quit")
	def f输入_结束符(self):
		self.f输入(c中断符 + c回车符)
		self.f输入(c结束符 + c回车符)
	def f模式_用户(self):
		from . import 用户模式
		return 用户模式.C用户视图(self)
	def f模式_启动(self):
		from . import 启动
		return 启动.C启动(self)
	def f执行显示命令(self, a命令, a自动换页 = True):
		v命令 = str(a命令)
		v输出 = 南向设备.I设备.f执行显示命令(self, v命令, a自动换页)
		return self.f处理显示结果(v输出)
	def f处理显示结果(self, a输出):
		v输出 = a输出.replace("\r", "")	#可能有多个\r,清掉
		v输出 = 南向设备.f去头尾行(v输出)
		return v输出
	def f显示_当前模式配置(self):
		v输出 = self.f执行显示命令("display this", a自动换页 = True)
		v输出 = 南向设备.f去头尾行(v输出)
		return v输出
