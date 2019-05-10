import cflw代码库py.cflw网络地址 as 地址
from ..基础接口 import 接口 as 北向接口
from ..基础接口 import 操作
from ..命令行接口 import 命令
from ..基础接口 import 协议
from ..命令行接口 import 接口 as 南向接口
from .常量 import *
#中兴常见接口
ca接口名称 = 接口.fc接口名称字典({
	北向接口.E接口.e空: "null",
	北向接口.E接口.e百兆以太网: "fei_",
	北向接口.E接口.e千兆以太网: "gei_",
})
f创建接口 = 接口.F创建接口(ca接口名称)
#zxr10 m6000接口
ca接口名称m6000 = 接口.fc接口名称字典({
	北向接口.E接口.e空: "null",
	北向接口.E接口.e千兆以太网: "gei-",
	北向接口.E接口.e万兆以太网: "xgei-",
	北向接口.E接口.e四万兆以太网: "xlgei-",
	北向接口.E接口.e十万兆以太网: "cgei-",
	北向接口.E接口.qx: "qx",
	北向接口.E接口.qx以太网: "qx_eth-",
	北向接口.E接口.e管理: "mgmt_eth",
	北向接口.E接口.e环回: "loopback",
})
f创建接口m6000 = 接口.F创建接口(ca接口名称m6000)
#===============================================================================
# 接口模式
#===============================================================================
class C接口m6000(南向接口.I接口配置):
	def __init__(self, a, a接口):
		南向接口.I接口配置.__init__(self, a, a接口)
	#显示
	def f显示_当前模式配置(self):
		v命令 = 命令.C命令("show running-config-interface")
		v命令 += self.fg模式参数()
		return self.m设备.f执行命令(v命令)
	#操作
	def fs开关(self, a操作 = 操作.E操作.e设置):
		v命令 = 命令.f生成开关命令("shutdown", c不, a操作)
		self.f执行当前模式命令(v命令)
	def fs描述(self, a描述 = "", a操作 = 操作.E操作.e设置):
		v命令 = 命令.C命令("description")
		if a操作 == 操作.E操作.e删除:
			v命令.f前面添加(c不)
		else:
			v命令 += a描述
		self.f执行当前模式命令(v命令)
	def fs网络地址4(self, a地址, a操作 = 操作.E操作.e设置):
		v地址 = 地址.S网络地址4.fc自动(a地址)
		v命令 = 命令.C命令("ip address %s %s" % (v地址.fg地址s(), v地址.fg掩码s()))
		if a操作 == 操作.E操作.e添加:
			v命令 += "secondary"
		elif a操作 == 操作.E操作.e删除:
			v命令.f前面添加(c不)
		self.f执行当前模式命令(v命令)