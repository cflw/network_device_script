from ..基础接口 import 操作
from ..基础接口 import 生成树 as 北向生成树
from ..命令行接口 import 模式
from ..命令行接口 import 命令
from ..命令行接口 import 生成树 as 南向生成树
from . import 虚拟局域网
from .常量 import *
ca优先级 = {
	北向生成树.E优先级.e主: "primary",
	北向生成树.E优先级.e次: "secondary",
}
ca模式 = {
	北向生成树.E模式.e快速生成树: "rstp",
	北向生成树.E模式.e多生成树: "mstp",
}
class C多生成树(南向生成树.I多生成树配置):
	def __init__(self, a):
		南向生成树.I多生成树配置.__init__(self, a)
	def fg进入命令(self):
		return "stp region-configuration"
	#操作
	def fs开关(self, a操作 = 操作.E操作.e开启):
		v操作 = 操作.f解析操作(a操作)
		v命令 = 命令.C命令("stp enable")
		v命令.f前置肯定(操作.fi关操作(v操作), c不)
		self.fg上级模式().f执行当前模式命令(v命令)
	def fs实例映射(self, a实例, a虚拟局域网, a操作 = 操作.E操作.e添加):
		v命令 = f"instance {a实例} vlan {虚拟局域网.f生成虚拟局域网(a虚拟局域网)}"
		self.f执行当前模式命令(v命令)
	def fs实例优先级(self, a实例, a优先级, a操作 = 操作.E操作.e设置):
		if a优先级 in 北向生成树.E优先级:
			v优先级 = ca优先级[a优先级]
		else:
			v优先级 = int(a优先级)
		v命令 = f"stp instance {a实例} priority {v优先级}"
		self.fg上级模式().f执行当前模式命令(v命令)
	def fs域名(self, a名称, a操作 = 操作.E操作.e设置):
		v命令 = f"region-name {a名称}"
		self.f执行当前模式命令(v命令)
	def fs版本(self, a版本, a操作 = 操作.E操作.e设置):
		v命令 = f"revision-level {a版本}"
		self.f执行当前模式命令(v命令)