import time
from ..基础接口 import 异常
from ..命令行接口 import 用户模式
class C执行模式v8(用户模式.I用户模式):	#深信服文档有写，进入到命令行的模式叫执行模式
	def f模式_全局配置(self):
		from . import 全局配置
		return 全局配置.C全局配置v8(self)
	def f模式_全局显示(self):
		from . import 全局显示
		return 全局显示.C全局显示v8(self)
	#动作
	def f登录(self, a用户名 = "", a密码 = ""):	#深信服命令行只有ssh
		self.m设备.f切换到当前连接()
		self.f记住登录(a用户名, a密码)
		self.m设备.f输入_回车()
		self.f切换到当前模式()
