from ..命令行接口 import 全局配置
from . import 接口
from ..基础接口 import 操作
class C全局配置(全局配置.I全局配置):
	"""适用于: s3956(v2.2.0B)"""
	def __init__(self, a):
		全局配置.I全局配置.__init__(self, a)
	#命令
	def fg进入命令(self):
		return "configure"
	#模式
	def f模式_接口(self, a接口, a操作 = 操作.E操作.e设置):
		v接口 = 接口.f创建接口(a接口)
		return 接口.C接口(self, v接口)
	#服务
	def f模式_网络终端(self):
		from . import 网络终端
		return 网络终端.C网络终端配置(self)
	def f模式_安全外壳(self):
		from . import 安全外壳
		return 安全外壳.C安全外壳配置(self)
