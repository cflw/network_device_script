from ..华为命令行 import 全局显示 as 旧全局显示
class C全局显示ne(旧全局显示.C全局显示):
	"""适用于: 华为ne40e(v8.180)"""
	def f显示_时间(self):
		from . import 时间
		v命令 = "display clock"
		v输出 = self.m设备.f执行显示命令(v命令)
		return 时间.f解析时间(v输出)
class C全局显示ce(C全局显示ne):
	"""适用于:"""
	pass