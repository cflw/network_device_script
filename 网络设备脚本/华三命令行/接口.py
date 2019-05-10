import cflw代码库py.cflw网络地址 as 地址
from ..基础接口 import 操作
from ..基础接口 import 协议
from ..基础接口 import 北向接口
from ..命令行接口 import 命令
from ..命令行接口 import 地址 as 南向地址
from ..命令行接口 import 接口 as 南向接口
from . import 常量 import *
ca接口名称 = 接口.fc接口名称字典({
	北向接口.E接口.e虚拟局域网: "Vlan-interface",
})
f创建接口 = 接口.F创建接口(ca接口名称)
ca接口缩写 = {
	"Eth": 北向接口.E接口.e百兆以太网,
	"GE": 北向接口.E接口.e吉以太网,
	"XGE": 北向接口.E接口.e万兆以太网,
	"FGE": 北向接口.E接口.e四万兆以太网,
	"InLoop": 北向接口.E接口.e内部,
	"Loop": 北向接口.E接口.e环回,
	"NULL": 北向接口.E接口.e空,
	"Ser": 北向接口.E接口.e串行,
	"REG": 北向接口.E接口.e注册隧道,	#Register-Tunnel
}
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
	def fs网络地址4(self, a地址):
		v命令 = f生成地址命令4(a地址, True, False)
		self.f执行当前模式命令(v命令)
	def f添加网络地址4(self, a地址):
		v命令 = f生成地址命令4(a地址, True, True)
		self.f执行当前模式命令(v命令)
	def f删除网络地址4(self, a地址 = None):
		v命令 = f生成地址命令4(a地址, False, True)
		self.f执行当前模式命令(v命令)
	def fe网络地址4(self):
		v输出 = self.f显示_当前模式配置()
		for v in v输出.split("\n"):
			v地址 = 南向地址.f解析地址4(v)
			if v地址:
				yield v地址
	
