from ..命令行接口 import 设备 as 南向设备
from ..命令行接口 import 命令
from ..命令行接口 import 用户模式
from .常量 import *
ca错误文本与异常类 = []
class C设备v8(南向设备.I设备):	#适用于8.0.35以上版本
	def __init__(self, a连接, a型号, a版本):
		南向设备.I设备.__init__(self, a连接)
		self.m连接.fs编码("utf-8")
		self.fs自动换页("--More--")
		self.m型号 = a型号
		self.m版本 = a版本
	def f退出(self):
		self.f执行命令("exit")
	def f输入_结束符(self):	#ctrl+c
		self.f输入(c结束符)
	def f模式_用户(self):
		from . import 用户模式 as 实现用户模式
		v模式 = 实现用户模式.C执行模式v8(self)
		# self.fs顶级模式(v模式)
		return v模式
	def f执行命令(self, a命令):
		v输出 = 南向设备.I设备.f执行命令(self, a命令)
		return v输出
	def f执行用户命令(self, a命令):
		v命令 = 命令.C命令(a命令)
		if not isinstance(self.fg当前模式(), 用户模式.I用户模式):	#在配置模式，命令前要加个do
			v命令.f前面添加(c做)
		v输出 = self.f执行命令(v命令)
		v输出 = v输出.replace("\r\n", "\n")
		return v输出
	def f处理显示命令(self, a命令):
		v命令 = 命令.C命令(a命令)
		if not isinstance(self.fg当前模式(), 用户模式.I用户模式):	#在配置模式，命令前要加个do
			v命令.f前面添加(c做)
		return str(v命令)
	def f处理显示结果(self, a输出):
		v输出 = a输出.replace("\r\n", "\n")
		v输出 = 南向设备.f去头尾行(v输出)
		return v输出
