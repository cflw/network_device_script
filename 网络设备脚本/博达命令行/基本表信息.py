import re
import cflw代码库py.cflw网络地址 as 地址
import cflw代码库py.cflw字符串 as 字符串
from ..基础接口 import 信息
from ..基础接口 import 数据表
from . import 接口 as 实现接口
#===============================================================================
# 接口表
#===============================================================================
class F接口表(数据表.I解析表格管线):
	"""show interface brief
	适用于: 博达s3956(v2.2.0B)"""
	c标题行 = "Port   Description    Status    Vlan        Duplex   Speed    Type"
	c接口 = 0
	c描述 = 7
	c状态 = 22
	c虚拟局域网 = 32
	c双工 = 44
	c速率 = 53
	c类型 = 62
	ca列 = 数据表.C切割列(c接口, c描述, c状态, c虚拟局域网, c双工, c速率, c类型)
	def __init__(self):
		数据表.I解析表格管线.__init__(self)
		self.f添加字段(数据表.E字段.e本端接口, F接口表.ca列[0], 实现接口.f创建接口缩写)
		self.f添加字段(数据表.E字段.e本端描述, F接口表.ca列[1], str)
		self.f添加字段(数据表.E字段.e本端链路状态, F接口表.ca列[2], 信息.f解析起宕状态)
		self.f添加字段(数据表.E字段.e本端虚拟局域网, F接口表.ca列[3], 信息.f解析虚拟局域网)
		self.f添加字段(数据表.E字段.e本端双工模式, F接口表.ca列[4], 信息.f解析双工模式)
		self.f添加字段(数据表.E字段.e本端速率, F接口表.ca列[5], 信息.f解析速率)
		# self.f添加字段(数据表.E字段.e本端类型, F接口表.ca列[6], str)
	f初始处理 = staticmethod(数据表.F去标题行(c标题行))
	@staticmethod
	def fi有效行(a行: str):
		if len(a行) < F接口表.c双工:
			return False	#过短
		if a行[F接口表.c描述-1] != " ":
			return False
		if a行[F接口表.c状态-1] != " ":
			return False
		if a行[F接口表.c虚拟局域网-1] != " ":
			return False
		return True
f接口表 = F接口表()
#===============================================================================
# 网络接口表
#===============================================================================
class F网络接口表4(数据表.I解析表格管线):
	"""show ip interface brief
	适用于: 博达s3956(v2.2.0B)"""
	c标题行 = "Interface                  IP-Address      Method Protocol-Status"
	c接口 = 0
	c地址 = 27
	c方法 = 43
	c协议状态 = 50
	ca列 = 数据表.C切割列(c接口, c地址, c方法, c协议状态)
	def __init__(self):
		数据表.I解析表格管线.__init__(self)
		self.f添加字段(数据表.E字段.e本端接口, F网络接口表4.ca列[0], 实现接口.f创建接口)
		self.f添加字段(数据表.E字段.e本端网络地址4, F网络接口表4.ca列[1], 信息.f解析网络地址4)
		self.f添加字段(数据表.E字段.e本端协议状态, F网络接口表4.ca列[3], 信息.f解析起宕状态)
	f初始处理 = staticmethod(数据表.F去标题行(c标题行))
	fi有效行 = staticmethod(数据表.F有效长度(c协议状态))
f网络接口表4 = F网络接口表4()
#===============================================================================
# 物理地址表
#===============================================================================
class F物理地址表(数据表.I解析表格管线):
	"""show mac address-table
	适用于: 博达s3956(v2.2.0B)"""
	c标题行0 = "Vlan    Mac Address       Type       Ports"
	c标题行1 = "----    -----------       ----       -----"
	c虚拟局域网 = 0
	c物理地址 = 8
	c类型 = 26
	c端口 = 37
	ca列 = 数据表.C切割列(c虚拟局域网, c物理地址, c类型, c端口)
	def __init__(self):
		数据表.I解析表格管线.__init__(self)
		self.f添加字段(数据表.E字段.e本端虚拟局域网, F物理地址表.ca列[0], 信息.f解析虚拟局域网)
		self.f添加字段(数据表.E字段.e对端物理地址, F物理地址表.ca列[1], 地址.S物理地址.fc字符串)
		self.f添加字段(数据表.E字段.e对端物理地址类型, F物理地址表.ca列[2], 信息.f解析物理地址类型)
		self.f添加字段(数据表.E字段.e本端接口, F物理地址表.ca列[3], 实现接口.f创建接口缩写)
	f初始处理 = staticmethod(数据表.F去标题行(c标题行0, c标题行1))
	fi有效行 = staticmethod(数据表.F有效长度(41))
f物理地址表 = F物理地址表()
#===============================================================================
# 地址解析表
#===============================================================================
class F地址解析表(数据表.I解析表格管线):
	"""show arp
	适用于: 博达s3956(v2.2.0B)"""
	c标题行 = "Protocol  Address         Age(min)  Hardware  Address  Type   Interface"
	c协议 = 0
	c网络地址 = 10
	c寿命 = 26
	c物理地址 = 36
	c类型 = 55
	c接口 = 62
	ca列 = 数据表.C切割列(c协议, c网络地址, c寿命, c物理地址, c类型, c接口)
	c虚拟局域网正则 = re.compile(r"v(\d+)")
	c接口正则 = re.compile(r"\((.+)\)")
	def __init__(self):
		数据表.I解析表格管线.__init__(self)
		self.f添加字段(数据表.E字段.e对端网络地址4, F地址解析表.ca列[1], 地址.S网络地址4.fc主机地址字符串)
		self.f添加字段(数据表.E字段.e本端寿命, F地址解析表.ca列[2], lambda x: int(x) * 60)
		self.f添加字段(数据表.E字段.e对端物理地址, F地址解析表.ca列[3], 地址.S物理地址.fc字符串)
		self.f添加字段(数据表.E字段.e本端虚拟局域网, F地址解析表.ca列[5], lambda x: int(F地址解析表.c虚拟局域网正则.search(x)[1]))
		self.f添加字段(数据表.E字段.e本端接口, F地址解析表.ca列[5], lambda x: 实现接口.f创建接口缩写(F地址解析表.c接口正则.search(x)[1]))
	f初始处理 = staticmethod(数据表.F去标题行(c标题行))
	@staticmethod
	def fi有效行(a行: str):
		if len(a行) < 66:
			return False	#过短
		if "-" in a行:
			return False	#没有寿命,本机地址,跳过
		if a行[F地址解析表.c网络地址-1] != " ":
			return False
		if a行[F地址解析表.c寿命-1] != " ":
			return False
		if a行[F地址解析表.c物理地址-1] != " ":
			return False
		return True
f地址解析表 = F地址解析表()