import cflw代码库py.cflw网络连接 as 连接
from ..基础接口 import 异常
from ..基础接口 import 操作
from ..命令行接口 import 设备 as 南向设备
from ..命令行接口 import 命令
from ..命令行接口 import 用户模式
from .. import 华为
from .常量 import *
ca错误文本与异常类 = [
	("Error: Wrong parameter found at '^' position.", 异常.X命令),
	("Error:Too many parameters found at '^' position.", 异常.X命令)
]
class C设备(南向设备.I设备):
	def __init__(self, a连接, a型号, a版本):
		南向设备.I设备.__init__(self, a连接)
		self.m连接.fs编码("gb2312")
		self.m型号 = a型号
		self.m版本 = a版本
		self.fs自动换页("  ---- More ----")
		if a型号 & 华为.E型号.c云:
			self.fs自动提交(操作.E自动提交.e退出配置模式时)
	def f退出(self):
		self.f执行命令("quit")
	def f提交(self):
		self.f执行命令("commit")
	def f输入_结束符(self):
		self.f输入(c结束符 + "\r")
	def f模式_用户(self):
		from . import 用户模式 as 实现
		return 实现.C用户视图(self)
	def f执行命令(self, a命令):
		v输出 = 南向设备.I设备.f执行命令(self, a命令)
		self.f检测命令异常(v输出)
		return v输出
	def f执行显示命令(self, a命令, a自动换页 = False):
		v输出 = 南向设备.I设备.f执行显示命令(self, a命令, a自动换页)
		return self.f处理显示结果(v输出)
	def f处理显示结果(self, a输出):
		v输出 = 南向设备.f去头尾行(a输出)
		if v输出.count("\n") < 10:
			self.f检测命令异常(v输出)
		return v输出
	def f显示_当前模式配置(self):
		self.fg当前模式().f切换到当前模式()
		v输出 = self.f执行显示命令("display this", a自动换页 = True)
		return v输出
	#助手
	def f助手_访问控制列表(self):
		return 访问控制列表.C助手()
	def f助手_服务质量策略(self, a策略名称, a分类名称, a行为名称, ai自动绑定 = True):
		from . import 服务质量
		return 服务质量.C助手(a策略名称, a分类名称, a行为名称, ai自动绑定)
	#其它
	f检测命令异常 = 命令.F检测命令异常(ca错误文本与异常类)
