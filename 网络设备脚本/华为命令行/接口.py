import hashlib
import struct
from ..基础接口 import 操作
from ..基础接口 import 协议
from ..基础接口 import 接口 as 北向接口
from ..命令行接口 import 命令
from ..命令行接口 import 接口 as 南向接口
from .常量 import *
from . import 实用 as 华为实用
ca接口名称 = 北向接口.fc接口名称字典({
	北向接口.E接口.e环回: "LoopBack",
	北向接口.E接口.e内部: "InLoopBack",
	北向接口.E接口.e虚拟局域网: "Vlanif",
})
f创建接口 = 北向接口.F创建接口(ca接口名称)
#===============================================================================
# 接口
#===============================================================================
class C接口视图(南向接口.I接口配置):
	def __init__(self, a, a接口):
		南向接口.I接口配置.__init__(self, a, a接口)
	#模式
	def f模式_虚拟局域网(self):
		from . import 虚拟局域网 as 实现虚网
		return 实现虚网.C接口配置(self.fg上级模式(), self.m接口)
	def f模式_开放最短路径优先(self, a进程号 = 1, a版本 = 协议.E协议.e开放最短路径优先):
		return self.fg上级模式().f模式_开放最短路径优先(a进程号 = a进程号, a版本 = a版本, a接口 = self.m接口)
	#接口操作
	@南向接口.A接口自动展开
	def fs开关(self, a操作 = 操作.E操作.e设置):
		v命令 = 命令.f生成开关命令("shutdown", c不, a操作)
		self.f执行当前模式命令(v命令)
	@南向接口.A接口自动展开
	def fs网络地址4(self, a地址, a操作 = 操作.E操作.e设置):
		v命令 = 命令.C命令("ip address")
		v命令 += 华为实用.f生成地址和前缀长度4(a地址)
		if a操作 == 操作.E操作.e设置:
			pass
		elif a操作 == 操作.E操作.e添加:
			v命令 += c次
		elif a操作 == 操作.E操作.e删除:
			v命令.f前面添加(c不)
		self.f执行当前模式命令(v命令)
class C端口组(C接口视图):	#需要重写!
	def __init__(self, a, a接口: 北向接口.S接口):
		C接口视图.__init__(self, a, a接口)
		#计算哈希
		v范围 = a接口.m序号[2]
		v字节 = struct.pack("iiiii", a接口.m名称, a接口.m序号[0], a接口.m序号[1], v范围.start, v范围.stop)
		v校验 = hashlib.md5()
		v校验.update(v字节)
		self.m哈希 = v校验.hexdigest()
	def fg模式参数(self):	#在这里确定不同厂商的接口名称
		return self.m哈希
	def fg进入命令(self):
		return 'port-group ' + self.fg模式参数()
	def f切换到当前模式(self):
		C接口视图.f切换到当前模式(self)