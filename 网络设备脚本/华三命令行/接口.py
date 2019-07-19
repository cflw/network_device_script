import cflw代码库py.cflw网络地址 as 地址
from ..基础接口 import 操作
from ..基础接口 import 协议
from ..基础接口 import 接口 as 北向接口
from ..命令行接口 import 命令
from ..命令行接口 import 地址 as 南向地址
from ..命令行接口 import 接口 as 南向接口
from .常量 import *
ca接口名称 = 北向接口.fc接口名称字典({
	北向接口.E类型.e虚拟局域网: "Vlan-interface",
	北向接口.E类型.e以太网: "Ethernet",
	北向接口.E类型.e千兆以太网: "GigabitEthernet",
	北向接口.E类型.e万兆以太网: "TenGigabitEthernet",
	北向接口.E类型.e四万兆以太网: "FortyGigabitEthernet",
	北向接口.E类型.e内部: "InLoopback",
	北向接口.E类型.e环回: "Loopback",
	北向接口.E类型.e空: "NULL",
	北向接口.E类型.e串行: "Serial",
	北向接口.E类型.e注册隧道: "Register-Tunnel",
})
f生成接口 = 北向接口.F生成接口(ca接口名称)
f创建接口 = 北向接口.F创建接口(ca接口名称, f生成接口)
ca接口缩写 = {
	北向接口.E类型.e百兆以太网: "Eth",
	北向接口.E类型.e吉以太网: "GE",
	北向接口.E类型.e万兆以太网: "XGE",
	北向接口.E类型.e四万兆以太网: "FGE",
	北向接口.E类型.e内部: "InLoop",
	北向接口.E类型.e环回: "Loop",
	北向接口.E类型.e空: "NULL",
	北向接口.E类型.e串行: "Ser",
	北向接口.E类型.e注册隧道: "REG",	#Register-Tunnel
}
f创建接口缩写 = 北向接口.F创建接口(ca接口缩写, f生成接口)
def f生成地址命令4(a地址, a肯定, a次):
	v地址 = 地址.S网络地址4.fc自动(a地址)
	v命令 = 命令.C命令("ip address")
	v命令 += (v地址.fg地址s(), v地址.fg掩码s())
	v命令.f前置否定(a肯定, c不)
	if a次:
		v命令 += "sub"
	return v命令
class C接口(南向接口.I接口配置):
	def __init__(self, a, a接口):
		南向接口.I接口配置.__init__(self, a, a接口)
	#三层
	@南向接口.A接口自动展开
	def fs网络地址4(self, a地址, a操作 = 操作.E操作.e设置):
		if a操作 == 操作.E操作.e设置:
			v命令 = f生成地址命令4(a地址, True, False)
		elif a操作 == 操作.E操作.e添加:
			v命令 = f生成地址命令4(a地址, True, True)
		elif a操作 == 操作.E操作.e删除:
			v命令 = f生成地址命令4(a地址, False, True)
		else:
			raise ValueError("无法解析的操作")
		self.f执行当前模式命令(v命令)
	@南向接口.A接口自动展开
	def fs描述(self, a描述 = "", a操作 = 操作.E操作.e设置):
		v操作 = 操作.f解析操作(a操作)
		v命令 = 命令.C命令("description")
		if 操作.fi加操作(v操作):
			v命令 += a描述
		else:
			v命令.f前面添加(c不)
		self.f执行当前模式命令(v命令)
	def fe网络地址4(self):
		v输出 = self.f显示_当前模式配置()
		for v in v输出.split("\n"):
			v地址 = 南向地址.f解析地址4(v)
			if v地址:
				yield v地址
