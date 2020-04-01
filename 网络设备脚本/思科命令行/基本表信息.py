import functools
import cflw代码库py.cflw字符串 as 字符串
import cflw代码库py.cflw网络地址 as 地址
import cflw代码库py.cflw工具_序列 as 序列
from ..基础接口 import 数据表
from ..基础接口 import 接口 as 北向接口
from ..基础接口 import 信息
from . import 接口 as 实现接口
#===============================================================================
# 物理地址表
#===============================================================================
class F物理地址表(数据表.I解析表格管线):
	"""show mac address-table
	适用于: 思科c3560(v15.0)"""
	c虚拟局域网 = 0
	c物理地址 = 8
	c类型 = 26
	c端口 = 38
	ca列 = 序列.C切片组(c虚拟局域网, c物理地址, c类型, c端口)
	c标题行0 = "Vlan    Mac Address       Type        Ports"
	c标题行1 = "----    -----------       --------    -----"
	def __init__(self):
		数据表.I解析表格管线.__init__(self)
		self.f添加字段(数据表.E字段.e本端虚拟局域网, F物理地址表.ca列.F切片(0), int)
		self.f添加字段(数据表.E字段.e对端物理地址, F物理地址表.ca列.F切片(1), 地址.S物理地址.fc字符串)
		self.f添加字段(数据表.E字段.e对端物理地址类型, F物理地址表.ca列.F切片(2), 信息.ca物理地址类型.get)
		self.f添加字段(数据表.E字段.e本端接口, F物理地址表.ca列.F切片(3), 实现接口.f创建接口缩写)
	f初始处理 = staticmethod(数据表.F去标题行(c标题行0, c标题行1))
	@staticmethod
	def fi有效行(a行):
		if "CPU" in a行:
			return False
		if not "." in a行:	#物理地址用.分隔
			return False
		return True
f物理地址表 = F物理地址表()
#===============================================================================
# 网络接口表4
#===============================================================================
def f解析网络地址4(a地址s):
	if "unassigned" in a地址s:
		return None
	else:
		return 地址.S网络地址4.fc地址前缀长度(a地址s, 32)
class F网络接口表4(数据表.I解析表格管线):
	"""show ip interface brief"""
	c接口 = 0	#Interface
	c地址 = 23	#IP-Address
	c好 = 39	#OK?
	c方法 = 43	#Method
	c状态 = 50	#Status
	c协议 = 72	#Protocol
	ca列 = 序列.C切片组(c接口, c地址, c好, c方法, c状态, c协议)
	c标题行0 = "Interface              IP-Address      OK? Method Status                Protocol"
	def __init__(self):
		数据表.I解析表格管线.__init__(self)
		self.f添加字段(数据表.E字段.e本端接口, F网络接口表4.ca列.F切片(0), 实现接口.f创建接口)
		self.f添加字段(数据表.E字段.e本端网络地址4, F网络接口表4.ca列.F切片(1), f解析网络地址4)
		self.f添加字段(数据表.E字段.e本端链路状态, F网络接口表4.ca列.F切片(4), 信息.f解析起宕状态)
		self.f添加字段(数据表.E字段.e本端协议状态, F网络接口表4.ca列.F切片(5), 信息.f解析起宕状态)
	f初始处理 = staticmethod(数据表.F去标题行(c标题行0))
	@staticmethod
	def fi有效行(a行):
		return "YES" in a行
f网络接口表4 = F网络接口表4()
#===============================================================================
# 网络接口表6
#===============================================================================
class C网络接口表6:	#需重写
	"""show ipv6 interface brief"""
	c接口开始 = 0
	c状态开始 = 23
	c地址开始 = 4
	def __init__(self, a):
		self.m字符串 = str(a)
	def __iter__(self):
		return self.fe行()
	def fe行(self):
		v项 = None
		for v行 in 字符串.fe分割(self.m字符串, "\n"):
			if "/" in v行:	#接口行包含斜杠
				if v项:
					yield v项
				v接口s, v状态s, v协议s  = 字符串.fe按字符分割(v行, "[", "/", "]")
				v接口 = 实现接口.f创建接口(v接口s)
				v状态 = "up" in v状态s
				v项 = 信息.S网络接口表项(a接口 = v接口, a地址 = [], a状态 = v状态)
			elif v项:	#地址行
				v地址s = v行.strip()
				if "unassigned" in v地址s:
					pass
				else:
					v地址 = 地址.S网络地址6.fc地址前缀长度(v地址s, 128)
					v项.m地址.append(v地址)
			else:
				raise RuntimeError("迷之错误")
		yield v项
