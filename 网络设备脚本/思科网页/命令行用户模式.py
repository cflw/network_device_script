import time
from ..思科命令行 import 用户模式
from ..基础接口 import 异常
class C用户模式(用户模式.C用户模式):
	"""适用于: 思科c7200"""
	def __init__(self, a):
		用户模式.C用户模式.__init__(self, a)
	#模式
	def f模式_全局配置(self):
		from . import 命令行全局配置
		return 命令行全局配置.C全局配置(self)
	#连接
	def f连接_网络终端(self, a地址, **a参数):
		raise 异常.X操作("网页端没有连接命令")
	def f连接_安全外壳(self, a地址, **a参数):
		raise 异常.X操作("网页端没有连接命令")
	def f连接_集群(self, a名称):
		raise 异常.X操作("网页端没有连接命令")
	#动作
	def f登录(self):
		time.sleep(0.5)
		self.m设备.f输入_结束符()
