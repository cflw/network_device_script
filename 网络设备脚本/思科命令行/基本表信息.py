import pandas	#pandas
import cflw代码库py.cflw字符串 as 字符串
import cflw代码库py.cflw网络地址 as 地址
from ..基础接口 import 数据表
from ..基础接口 import 接口 as 北向接口
from ..基础接口 import 信息
from . import 接口 as 实现接口
#===============================================================================
# 接口详细
#===============================================================================
class F接口详细(数据表.I解析列表管线):
	"""show interface
	适用于: 思科c7200(v15.*)"""
	c接口状态正则 = r"is (.+?), line protocol is (.+?)\s"
	c物理地址正则 = r"Hardware is (.+?), address is (.+?)\s"
	c网络地址4正则 = r"Internet address is (.+?)\s"
	c指标1正则 = r"MTU (\d+) bytes, BW (\d+) Kbit/sec, DLY (\d+) usec,"
	c指标2正则 = r"reliability (\d+)/255, txload (\d+)/255, rxload (\d+)/255"
	c接收率正则 = r"5 minute input rate (\d+) bits/sec, (\d+) packets/sec"
	c发送率正则 = r"5 minute output rate (\d+) bits/sec, (\d+) packets/sec"
	c接收数正则 = r"(\d+) packets input, (\d+) bytes, (\d+) no buffer"
	c接收错误数正则 = r"(\d+) input errors, (\d+) CRC, (\d+) frame, (\d+) overrun, (\d+) ignored"
	c发送数正则 = r"(\d+) packets output, (\d+) bytes, (\d+) underruns"
	c发送错误数正则 = r"(\d+) output errors, (\d+) collisions, (\d+) interface resets"
	def __init__(self):
		数据表.I解析列表管线.__init__(self)
		self.f添加字段(数据表.E字段.e本端接口, 数据表.F正则字段(北向接口.c接口正则, 0), 实现接口.f创建接口)
		self.f添加字段(数据表.E字段.e本端管理状态, 数据表.F正则字段(self.c接口状态正则, 1), 信息.f解析起宕状态)
		self.f添加字段(数据表.E字段.e本端协议状态, 数据表.F正则字段(self.c接口状态正则, 2), 信息.f解析起宕状态)
		self.f添加字段(数据表.E字段.e本端物理地址, 数据表.F正则字段(self.c物理地址正则, 2), 地址.S物理地址.fc字符串)
		self.f添加字段(数据表.E字段.e本端网络地址4, 数据表.F正则字段(self.c网络地址4正则, 1), 地址.S网络地址4.fc地址前缀长度字符串)
		self.f添加字段(数据表.E字段.e本端最大传输单元, 数据表.F正则字段(self.c指标1正则, 1), int)
		self.f添加字段(数据表.E字段.e本端带宽, 数据表.F正则字段(self.c指标1正则, 2), lambda x: int(x) * 1000)
		self.f添加字段(数据表.E字段.e本端每秒接收比特数, 数据表.F正则字段(self.c接收率正则, 1), int)
		self.f添加字段(数据表.E字段.e本端每秒接收包数, 数据表.F正则字段(self.c接收率正则, 2), int)
		self.f添加字段(数据表.E字段.e本端接收包数, 数据表.F正则字段(self.c接收数正则, 1), int)
		self.f添加字段(数据表.E字段.e本端接收字节数, 数据表.F正则字段(self.c接收数正则, 2), int)
		self.f添加字段(数据表.E字段.e本端接收错误数, 数据表.F正则字段(self.c接收错误数正则, 1), int)
		self.f添加字段(数据表.E字段.e本端每秒发送比特数, 数据表.F正则字段(self.c发送率正则, 1), int)
		self.f添加字段(数据表.E字段.e本端每秒发送包数, 数据表.F正则字段(self.c发送率正则, 2), int)
		self.f添加字段(数据表.E字段.e本端发送包数, 数据表.F正则字段(self.c发送数正则, 1), int)
		self.f添加字段(数据表.E字段.e本端发送字节数, 数据表.F正则字段(self.c发送数正则, 2), int)
		self.f添加字段(数据表.E字段.e本端发送错误数, 数据表.F正则字段(self.c发送错误数正则, 1), int)
	f下一记录 = staticmethod(数据表.F下一记录行("line protocol is"))
f接口详细 = F接口详细()
#===============================================================================
# 接口表
#===============================================================================
class F接口状态表_v11(数据表.I解析表格管线):
	"""show interface status
	适用于: 浪潮s6650(v11.12.*)"""
	c接口 = 0	#Port
	c名称 = 13	#Name
	c连接状态 = 32	#Status
	c虚拟局域网 = 45	#Vlan
	c双工 = 56	#Duplex
	c速率 = 63	#Speed
	c类型 = 70	#Type
	ca列 = 数据表.C切割列(c接口, c名称, c连接状态, c虚拟局域网, c双工, c速率, c类型)
	c标题行0 = "Port         Name               Status       Vlan       Duplex  Speed Type"
	def __init__(self):
		数据表.I解析表格管线.__init__(self)
		self.f添加字段(数据表.E字段.e本端接口, self.ca列[0], 实现接口.f创建接口缩写)
		self.f添加字段(数据表.E字段.e本端名称, self.ca列[1], str)
		self.f添加字段(数据表.E字段.e本端链路状态, self.ca列[2], lambda x: x == "connected")
		self.f添加字段(数据表.E字段.e本端虚拟局域网, self.ca列[3], lambda x: int(x) if x.isdigit() else 0)
		self.f添加字段(数据表.E字段.e本端双工模式, self.ca列[4], 信息.f解析双工模式)
		self.f添加字段(数据表.E字段.e本端速率, self.ca列[5], 信息.f解析速率)
	f初始处理 = staticmethod(数据表.F去标题行(c标题行0))
	@staticmethod
	def fi有效行(a行):
		return (not "Port" in a行) and (len(a行) > 70)
f接口状态表_v11 = F接口状态表_v11()
class F接口状态表_v12(F接口状态表_v11):
	"""show interface status
	适用于: 浪潮s5960(v12.2)"""
	c接口 = 0	#Port
	c名称 = 10	#Name
	c连接状态 = 29	#Status
	c虚拟局域网 = 42	#Vlan
	c双工 = 53	#Duplex
	c速率 = 60	#Speed
	c类型 = 67	#Type
	ca列 = 数据表.C切割列(c接口, c名称, c连接状态, c虚拟局域网, c双工, c速率, c类型)
	c标题行0 = "Port      Name               Status       Vlan       Duplex  Speed Type"
	f初始处理 = staticmethod(数据表.F去标题行(c标题行0))
f接口状态表_v12 = F接口状态表_v12()
#===============================================================================
# 网络接口表4
#===============================================================================
class F网络接口表4(数据表.I解析表格管线):
	"""show ip interface brief
	适用于: 思科c7200(v15.*), 思科csr1000v(v16.9.1)
		浪潮s6650(v11.12.*)"""
	c接口 = 0	#Interface
	c地址 = 23	#IP-Address
	c好 = 39	#OK?
	c方法 = 43	#Method
	c状态 = 50	#Status
	c协议 = 72	#Protocol
	ca列 = 数据表.C切割列(c接口, c地址, c好, c方法, c状态, c协议)
	c标题行0 = "Interface              IP-Address      OK? Method Status                Protocol"
	def __init__(self):
		数据表.I解析表格管线.__init__(self)
		self.f添加字段(数据表.E字段.e本端接口, self.ca列[0], 实现接口.f创建接口)
		self.f添加字段(数据表.E字段.e本端网络地址4, self.ca列[1], 信息.f解析网络地址4)
		self.f添加字段(数据表.E字段.e本端管理状态, self.ca列[4], 信息.F解析管理状态(a宕 = "administratively"))
		self.f添加字段(数据表.E字段.e本端链路状态, self.ca列[4], 信息.f解析起宕状态)
		self.f添加字段(数据表.E字段.e本端协议状态, self.ca列[5], 信息.f解析起宕状态)
	f初始处理 = staticmethod(数据表.F去标题行(c标题行0))
	@staticmethod
	def fi有效行(a行):
		return "YES" in a行
f网络接口表4 = F网络接口表4()
#===============================================================================
# 网络接口表6
#===============================================================================
class F网络接口表6:
	"""show ipv6 interface brief
	适用于: 思科c7200(v15.*)"""
	c接口开始 = 0
	c状态开始 = 23
	c地址开始 = 4
	def __init__(self):
		pass
	def __call__(self, a):
		self.m字符串 = str(a)
		return pandas.DataFrame(self.fe行())
	def fe行(self):
		v项 = None
		for v行 in 字符串.fe分割(self.m字符串, "\n"):
			if "/" in v行:	#接口行包含斜杠
				if v项:
					yield v项
				v接口s, v状态s, v协议s  = 字符串.fe按字符分割(v行, "[", "/", "]")
				v项 = {
					数据表.E字段.e本端接口: 实现接口.f创建接口(v接口s),
					数据表.E字段.e本端网络地址6: [],
					数据表.E字段.e本端链路状态: 信息.f解析起宕状态(v状态s),
					数据表.E字段.e本端协议状态: 信息.f解析起宕状态(v协议s),
				}
			elif v项:	#地址行
				v地址s = v行.strip()
				if "unassigned" in v地址s:
					pass
				else:
					v地址 = 地址.S网络地址6.fc地址前缀长度(v地址s, 128)
					v项[数据表.E字段.e本端网络地址6].append(v地址)
			else:
				raise RuntimeError("迷之错误")
		yield v项
f网络接口表6 = F网络接口表6()
#===============================================================================
# 地址解析表
#===============================================================================
class F地址解析表(数据表.I解析表格管线):
	"""show arp 或 show ip arp
	适用于: 思科c2960(v12.2),
		浪潮s5960(v12.2), 浪潮s6650(v11.12.*)"""
	c协议 = 0
	c网络地址 = 10
	c寿命 = 27
	c物理地址 = 38
	c类型 = 54
	c接口 = 61
	ca列 = 数据表.C切割列(c协议, c网络地址, c寿命, c物理地址, c类型, c接口)
	c标题行0 = "Protocol  Address          Age (min)  Hardware Addr   Type   Interface"
	def __init__(self):
		数据表.I解析表格管线.__init__(self)
		self.f添加字段(数据表.E字段.e对端网络地址4, self.ca列[1], 地址.S网络地址4.fc主机地址字符串)
		self.f添加字段(数据表.E字段.e本端寿命, self.ca列[2], lambda x: 信息.f解析数字(x) * 60)
		self.f添加字段(数据表.E字段.e对端物理地址, self.ca列[3], 地址.S物理地址.fc字符串)
		self.f添加字段(数据表.E字段.e本端接口, self.ca列[5], 实现接口.f创建接口)
	f初始处理 = staticmethod(数据表.F去标题行(c标题行0))
	def fi有效行(self, a行: str) -> bool:
		return a行 != self.c标题行0
f地址解析表 = F地址解析表()
#===============================================================================
# 物理地址表
#===============================================================================
class F物理地址表(数据表.I解析表格管线):
	"""show mac address-table
	适用于: 思科c2960(v12.2), 思科c3560(v15.0),
		浪潮s6650(v11.12.*)"""
	c虚拟局域网 = 0
	c物理地址 = 8
	c类型 = 26
	c端口 = 38
	ca列 = 数据表.C切割列(c虚拟局域网, c物理地址, c类型, c端口)
	c标题行0 = "Vlan    Mac Address       Type        Ports"
	c标题行1 = "----    -----------       --------    -----"
	def __init__(self):
		数据表.I解析表格管线.__init__(self)
		self.f添加字段(数据表.E字段.e本端虚拟局域网, self.ca列[0], int)
		self.f添加字段(数据表.E字段.e对端物理地址, self.ca列[1], 地址.S物理地址.fc字符串)
		self.f添加字段(数据表.E字段.e对端物理地址类型, self.ca列[2], 信息.f解析物理地址类型)
		self.f添加字段(数据表.E字段.e本端接口, self.ca列[3], 实现接口.f创建接口缩写)
	f初始处理 = staticmethod(数据表.F去标题行(c标题行0, c标题行1))
	@staticmethod
	def fi有效行(a行):
		if "CPU" in a行:
			return False
		if not "." in a行:	#物理地址用.分隔
			return False
		return True
f物理地址表 = F物理地址表()