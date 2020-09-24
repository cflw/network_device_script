import cflw代码库py.cflw网络地址 as 地址
from ..基础接口 import 操作
from ..基础接口 import 接口 as 北向接口
from ..命令行接口 import 命令
from ..命令行接口 import 模式
from ..命令行接口 import 接口 as 南向接口
ca接口名称nv7 = {
	北向接口.E类型.e虚拟局域网: "Vlan",
	北向接口.E类型.e聚合: "port-channel",
	北向接口.E类型.e以太网: "Ethernet",
	北向接口.E类型.e管理: "mgmt",
}
ca接口缩写nv7 = {
	北向接口.E类型.e以太网: "Eth",
	北向接口.E类型.e快速以太网: "Fa",
	北向接口.E类型.e吉以太网: "Gi",
	北向接口.E类型.e聚合: "Po",
	北向接口.E类型.e管理: "mgmt",
	北向接口.E类型.e虚拟局域网: "Vlan",
}
f生成接口nv7 = 北向接口.F生成接口(ca接口名称nv7)
f创建接口nv7 = 北向接口.F创建接口(ca接口名称nv7, f生成接口nv7)
f创建接口缩写nv7 = 北向接口.F创建接口(ca接口缩写nv7, f生成接口nv7)
class C接口nv7(南向接口.I接口配置):
	def __init__(self, a, a接口):
		南向接口.I接口配置.__init__(self, a, a接口)
	def fs网络地址4(self, a地址, a操作 = 操作.E操作.e设置):
		raise NotImplementedError()
	def fs默认网关4(self, a地址, a操作 = 操作.E操作.e设置):
		raise NotImplementedError()