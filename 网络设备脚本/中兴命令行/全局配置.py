from ..命令行接口 import 全局配置
from ..基础接口 import 操作
#===============================================================================
# 模式
#===============================================================================
class C全局配置m6000(全局配置.I全局配置):
	def __init__(self, a):
		全局配置.I全局配置.__init__(self, a)
	#命令
	def fg进入命令(self):
		return "configure terminal"
	#模式
	def f模式_接口(self, a接口, a操作 = 操作.E操作.e设置):
		from . import 接口
		v接口 = 接口.f创建接口m6000(a接口)
		return 接口.C接口m6000(self, v接口)
	#数据结构
	def f模式_访问控制列表(self, a名称, a类型 = None, a操作 = 操作.E操作.e设置):
		from ..基础接口 import 访问控制列表 as 北向列表
		from ..命令行接口 import 访问控制列表 as 南向列表
		from . import 访问控制列表 as 实现列表
		if a类型 in (北向列表.E类型.e标准4, 北向列表.E类型.e扩展4):
			v模式 = 实现列表.C扩展4_m6000(self, a名称)
		else:
			raise ValueError("未知的访问控制列表类型")
		return v模式