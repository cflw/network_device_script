import cflw代码库py.cflw网络地址 as 地址
from ..基础接口 import 操作
from ..基础接口 import 接口 as 北向接口
from ..命令行接口 import 命令
from ..命令行接口 import 模式
from ..命令行接口 import 接口 as 南向接口
#e580(v6.x)
ca接口名称ev6 = {
	北向接口.E类型.e以太网: "eth-",
	北向接口.E类型.e聚合: "agg",
	北向接口.E类型.e空: "null",
	北向接口.E类型.e虚拟局域网: "vlan",
}
class F生成接口ev6(北向接口.F生成接口):
	def f分隔符(self):
		return "-"
	def f生成范围(self, a范围):
		return f"{a范围.start} - {a范围.stop - 1}"
f生成接口ev6 = F生成接口ev6(ca接口名称ev6)
f创建接口ev6 = 北向接口.F创建接口(ca接口名称ev6, f生成接口ev6)
#接口
class C管理ev6(模式.C同级模式, 南向接口.I接口配置):
	"""适用于: 盛科e580(v6.x), 浪潮cn61108pcvh(v6.x), 浪潮s5350(v6.x)"""
	def __init__(self, a, a接口):
		南向接口.I接口配置.__init__(self, a, a接口)
	def fs网络地址4(self, a地址, a操作 = 操作.E操作.e设置):
		v地址 = 地址.S网络地址4.fc自动(a地址)
		v命令 = 命令.C命令("management ip address")
		v命令 += str(v地址)
		self.f执行当前模式命令(v命令)
	def fs默认网关4(self, a地址, a操作 = 操作.E操作.e设置):
		v地址 = 地址.S网络地址4.fc自动(a地址)
		v命令 = 命令.C命令("management route add gateway")
		v命令 += v地址.fg地址s()
		self.f执行当前模式命令(v命令)
class C接口ev6(南向接口.I接口配置):
	def __init__(self, a, a接口):
		南向接口.I接口配置.__init__(self, a, a接口)
	def fs描述(self, a描述 = "", a操作 = 操作.E操作.e设置):
		v命令 = 命令.C命令("description")
		v命令 += a描述
		self.f执行当前模式命令(v命令)
	def fs网络地址4(self, a地址, a操作 = 操作.E操作.e设置):
		v地址 = 地址.S网络地址4.fc自动(a地址)
		v命令 = 命令.C命令("ip address")
		v命令 += str(v地址)
		self.f执行当前模式命令(v命令)