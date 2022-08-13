from ..基础接口 import 区域
from ..基础接口 import 操作
from ..命令行接口 import 模式
from ..命令行接口 import 命令
from ..深信服防火墙命令行.常量 import *
from . import 接口 as 实现接口
ca类型 = {
	区域.E类型.e二层: "switch",
	区域.E类型.e三层: "route",
	区域.E类型.e虚拟: "virtual",
}
class C区域配置v8(区域.I区域配置, 模式.I模式):
	def __init__(self, a, a名称: str):
		模式.I模式.__init__(self, a)
		self.m名称 = a名称
	def fg进入命令(self):
		"""命令: zone 名称"""
		return f"zone {self.m名称}"
	def fg删除命令(self):
		"""命令: no zone 名称"""
		return f"no zone {self.m名称}"
	def fs类型(self, a类型, a操作 = 操作.E操作.e设置):
		"""命令: forward-type 类型"""
		if 操作.fi关操作(a操作):
			return	#区域类型不能删除,跳过
		v命令 = 命令.C命令("forward-type")
		v命令 += ca类型[a类型]
		self.f执行当前模式命令(v命令)
	def fs接口(self, a接口, a操作 = 操作.E操作.e添加):
		"""命令: [no] interface 接口"""
		v命令 = 命令.C命令("interface")
		v接口 = 实现接口.f创建接口(a接口)
		v命令 += v接口
		v命令.f前置肯定(操作.fi减操作(a操作), c不)
		self.f执行当前模式命令(v命令)