from ..基础接口 import 操作
from ..基础接口 import 协议
from ..基础接口 import 接口 as 北向接口
from ..命令行接口 import 全局配置
class C全局配置v8(全局配置.I全局配置):
	def __init__(self, a):
		全局配置.I全局配置.__init__(self, a)
	def fg进入命令(self):
		return "config"
	#模式
	def f模式_接口(self, a接口, a操作 = 操作.E操作.e设置):
		from . import 接口 as 实现接口
		v接口 = 实现接口.f创建接口(a接口)
		v模式 = 实现接口.C接口配置v8(self, v接口)
		return v模式
	def f模式_区域(self, a名称, a操作 = 操作.E操作.e设置):
		from . import 区域 as 实现区域
		v模式 = 实现区域.C区域配置v8(self, a名称)
		if 操作.fi减操作(a操作):
			v命令 = v模式.fg删除命令()
			self.f执行当前模式命令(v命令)
		return v模式