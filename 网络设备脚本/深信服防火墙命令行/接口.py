import cflw代码库py.cflw网络地址 as 地址
from ..基础接口 import 操作
from ..基础接口 import 接口 as 北向接口
from ..命令行接口 import 命令
from ..命令行接口 import 模式
from ..命令行接口 import 接口 as 南向接口
#接口名称
ca接口名称 = 北向接口.ca接口名称 | {
	北向接口.E类型.e以太网: "eth",
	北向接口.E类型.e虚拟局域网: "veth.",
	北向接口.E类型.e聚合: "aggr.",
}
f生成接口, f创建接口 = 北向接口.F接口工厂(ca接口名称)
class C接口配置v8(南向接口.I接口配置):
	def __init__(self, a, a接口):
		南向接口.I接口配置.__init__(self, a, a接口)
	def fg进入命令(self):
		"""命令: interface 接口"""
		v命令 = f"interface {self.m接口}"
		return v命令
	#配置
	def fs开关(self, a开关):
		"""命令: [no] shutdown"""
		v操作 = 操作.f解析操作(a开关)
		if 操作.fi开操作(v操作):
			v命令 = "no shutdown"
		else:
			v命令 = "shutdown"
		self.f执行当前模式命令(v命令)
	def fs描述(self, a描述: str, a操作 = 操作.E操作.e设置):
		"""命令: [no] description 描述"""
		v命令 = f"description {a描述}"
		self.f执行当前模式命令(v命令)
	def fs区域(self, a区域, a操作 = 操作.E操作.e设置):
		"""命令: zone 区域"""
		v命令 = f"zone {a区域}"
		self.f执行当前模式命令(v命令)
	def fs管理(self, a管理方式, a操作 = 操作.E操作.e开启):
		"""命令: manage 管理方式 开关"""
	def fs网络地址4(self, a地址, a操作 = 操作.E操作.e设置):
		"""命令: ip address 地址"""
		v地址 = 地址.S网络地址4.fc自动(a地址)
		v命令 = f"ip address {v地址.ft字符串()}"
		self.f执行当前模式命令(v命令)
	def fs网络地址6(self, a地址, a操作 = 操作.E操作.e添加):
		"""命令: ipv6 address 地址"""
		v地址 = 地址.S网络地址6.fc自动(a地址)
		v命令 = f"ip address {v地址.ft字符串()}"
		self.f执行当前模式命令(v命令)
	def fs广域网(self, a开关):
		"""命令: wan 开关"""
		v操作 = 操作.f解析操作(a开关)
		if 操作.fi开操作(v操作):
			v命令 = "wan enable"
		else:
			v命令 = "wan disable"
		self.f执行当前模式命令(v命令)
