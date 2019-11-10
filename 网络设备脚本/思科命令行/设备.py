import cflw代码库py.cflw网络连接 as 连接
from ..命令行接口 import 设备 as 南向设备
from ..基础接口 import 异常 as 异常
from ..命令行接口 import 命令
from ..命令行接口 import 用户模式
from .常量 import *
ca错误文本与异常类 = [
	("% Invalid input detected at '^' marker.", 异常.X命令),	#语法错误
	("% Ambiguous command:", 异常.X命令),	#无法识别的命令
	("% Duplicate sequence number", 异常.X执行),	#重复的acl规则序号
	("% Multiple ports are allowed on named ACLs only", 异常.X执行),	#多端口号只允许在命名acl使用
]
class C设备(南向设备.I设备):
	def __init__(self, a连接, a型号, a版本):
		南向设备.I设备.__init__(self, a连接)
		self.m连接.fs编码("ascii")
		self.fs自动换页("--More--")
		self.m型号 = a型号
		self.m版本 = a版本
	def f退出(self):
		self.f执行命令("exit")
	def f输入_结束符(self):	#ctrl+c
		self.f输入(c结束符)
	def f模式_用户(self):
		from . import 用户模式 as 实现用户模式
		v模式 = 实现用户模式.C用户模式(self)
		# self.fs顶级模式(v模式)
		return v模式
	def f执行命令(self, a命令):
		v输出 = 南向设备.I设备.f执行命令(self, a命令)
		self.f检测命令异常(v输出)
		return v输出
	def f执行用户命令(self, a命令):
		v命令 = 命令.C命令(a命令)
		if not isinstance(self.fg当前模式(), 用户模式.I用户模式):	#在配置模式，命令前要加个do
			v命令.f前面添加(c做)
		v输出 = self.f执行命令(v命令)
		v输出 = v输出.replace("\r\n", "\n")
		return v输出
	def f执行显示命令(self, a命令, a自动换页 = True):
		v命令 = 命令.C命令(a命令)
		if not isinstance(self.fg当前模式(), 用户模式.I用户模式):	#在配置模式，命令前要加个do
			v命令.f前面添加(c做)
		v输出 = 南向设备.I设备.f执行显示命令(self, a命令 = v命令, a自动换页 = a自动换页)
		return self.f处理显示结果(v输出)
	def f处理显示结果(self, a输出):
		v输出 = a输出.replace("\r\n", "\n")
		v输出 = 南向设备.f去头尾行(v输出)
		if v输出.count("\n") < 10:	#输出行数太少,检测是否有异常
			self.f检测命令异常(v输出)
		return v输出
	def f检测命令异常(self, a输出):
		if not self.m检测异常:
			return
		def f返回异常(ax):
			if type(ax) == type:
				v异常 = ax(a输出)
			else:
				v异常 = ax
			if self.m检测异常:
				raise v异常
			return v异常
		for v文本, vt异常 in ca错误文本与异常类:
			if v文本 in a输出:
				return f返回异常(vt异常)
		return None
	#助手
	def f助手_访问控制列表(self):
		from . import 访问控制列表 as 访问控制列表
		return 访问控制列表.C助手
	def f助手_密码(self, a强密码 = True):
		from . import 密码 as 密码
		if a强密码:
			return 密码.C强密码助手()
		else:
			return 密码.C弱密码助手()
