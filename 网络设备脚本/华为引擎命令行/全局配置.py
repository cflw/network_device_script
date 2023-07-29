from ..基础接口 import 操作
from ..命令行接口 import 命令
from ..华为命令行 import 全局配置 as 旧全局配置
class C系统视图ne(旧全局配置.C系统视图):
	"""适用于: 华为ne40e(v8.180)"""
	def fg进入命令(self):
		v命令 = 命令.C命令("system-view")
		if self.m设备.m自动提交 == 操作.E自动提交.e立即:
			v命令 += "immediately"
		return v命令
	def f事件_退出模式前(self):
		self.m设备.f自动提交(操作.E自动提交.e退出配置模式时)
class C系统视图ce(C系统视图ne):
	"""适用于:"""
	pass