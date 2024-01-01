import cflw代码库py.cflw网络地址 as 地址
from ..基础接口 import 操作
from ..基础接口 import 接口 as 北向接口
from ..命令行接口 import 命令
from ..命令行接口 import 模式
from ..命令行接口 import 接口 as 南向接口
ca接口名称_nv7 = {
	北向接口.E类型.e虚拟局域网: "Vlan",
	北向接口.E类型.e聚合: "port-channel",
	北向接口.E类型.e以太网: "Ethernet",
	北向接口.E类型.e管理: "mgmt",
}
ca接口缩写_nv7 = {
	北向接口.E类型.e以太网: "Eth",
	北向接口.E类型.e快速以太网: "Fa",
	北向接口.E类型.e吉以太网: "Gi",
	北向接口.E类型.e聚合: "Po",
	北向接口.E类型.e管理: "mgmt",
	北向接口.E类型.e虚拟局域网: "Vlan",
	北向接口.E类型.e堆叠: "sup-eth",	#全名应该是supervisor ethernet,不确定接口干嘛用的,只在mac地址表出现
}
f生成接口_nv7, f创建接口_nv7 = 北向接口.F接口工厂(ca接口名称_nv7)
f生成接口缩写_nv7, f创建接口缩写_nv7 = 北向接口.F接口工厂(ca接口缩写_nv7)
class I接口配置(南向接口.I接口配置):
	def __init__(self, a, a接口):
		南向接口.I接口配置.__init__(self, a, a接口)
class C接口_nv7(I接口配置):
	def fs网络地址4(self, a地址, a操作 = 操作.E操作.e设置):
		raise NotImplementedError()
	def fs默认网关4(self, a地址, a操作 = 操作.E操作.e设置):
		raise NotImplementedError()