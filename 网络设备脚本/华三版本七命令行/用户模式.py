from ..华三命令行 import 用户模式 as 旧用户模式
class C用户视图v7(旧用户模式.C用户视图):
	def f模式_全局配置(self):
		from . import 全局配置
		return 全局配置.C系统视图v7(self)
