from . import 模式
from ..基础接口 import 用户模式
class I用户模式(模式.I模式, 用户模式.I用户模式):
	c模式名 = "用户模式"
	def __init__(self, a):
		模式.I模式.__init__(self, a)
		self.m登录用户名 = ""
		self.m登录密码 = ""
		self.m提权级别 = 0
		self.m提权密码 = ""
	#模式
	def fg进入命令(self):	#用户模式不需要进入命令
		return ""
	def fg提交命令(self):	#用户模式不需要提交命令
		return ""
	def fg退出命令(self):	#用户模式不需要命令
		return ""
	#动作
	def f导出配置(self, a目录 = "", a文件名 = ""):
		import pathlib
		if not a文件名:
			raise ValueError("文件名不能为空")
		v全局显示 = self.f模式_全局显示()
		v输出 = v全局显示.f显示_当前配置()
		v路径 = pathlib.PurePath(a目录) / a文件名
		v文件 = open(str(v路径), "w")
		v文件.write(v输出)
	#其它
	def f记住登录(self, a用户名 = None, a密码 = None):
		if a用户名:
			self.m登录用户名 = str(a用户名)
		if a密码:
			self.m登录密码 = str(a密码)
	def f记住提权(self, a级别 = None, a密码 = None):
		if a级别:
			self.m提权级别 = a级别
		if a密码:
			self.m提权密码 = a密码