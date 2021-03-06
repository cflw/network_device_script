import time
import cflw代码库py.cflw字符串 as 字符串
import cflw代码库py.cflw网络地址 as 地址
from ..基础接口 import 信息
from ..基础接口 import 数据表
from ..思科命令行 import 接口 as 思科接口
from ..思科命令行 import 基本表信息 as 思科基本表信息
#===============================================================================
# 接口表
#===============================================================================
def f解析速率(a: str):
	if "Unknown" in a:
		return None
	elif a[-1] == 'M':
		return int(a[:-1])
	elif a[-1] == 'G':
		return int(a[:-1]) * 1000
	raise ValueError()
def f解析双工(a: str):
	if "Unknown" in a:
		return None
	return "Full" in a
class F接口表(数据表.I解析表格管线):
	"""show interface status
	适用于: 锐捷s5750(v11.4)"""
	c接口 = 0
	c状态 = 41
	c虚拟局域网 = 51
	c双工 = 58
	c速率 = 67
	c类型 = 77	#铜还是光纤
	ca列 = 数据表.C切割列(c接口, c状态, c虚拟局域网, c双工, c速率, c类型)
	c标题行0 = "Interface                                Status    Vlan   Duplex   Speed     Type  "
	c标题行1 = "---------------------------------------- --------  ----   -------  --------- ------"
	def __init__(self):
		数据表.I解析表格管线.__init__(self)
		self.f添加字段(数据表.E字段.e本端接口, F接口表.ca列[0], 思科接口.f创建接口)
		self.f添加字段(数据表.E字段.e本端链路状态, F接口表.ca列[1], 信息.f解析起宕状态)
		self.f添加字段(数据表.E字段.e本端虚拟局域网, F接口表.ca列[2], int)
		self.f添加字段(数据表.E字段.e本端双工模式, F接口表.ca列[3], f解析双工)
		self.f添加字段(数据表.E字段.e本端速率, F接口表.ca列[4], f解析速率)
	f初始处理 = staticmethod(数据表.F去标题行(c标题行0, c标题行1))
	fi有效行 = staticmethod(数据表.F有效长度(80))
f接口表 = F接口表()
class F交换接口表(数据表.I解析表格管线):
	"""show interface switchport
	适用于: 锐捷s5750(v11.4)"""
	c接口 = 0
	c交换 = 33	#是否交换口
	c模式 = 44	#链路类型
	c接入 = 54	#接入口的vlan
	c本征 = 61	#中继口的vlan
	c保护 = 68	#意义不明的列
	c虚拟局域网 = 78	#意义不明的列
	c列表 = 83	#意义不明的列
	ca列 = 数据表.C切割列(c接口, c交换, c模式, c接入, c本征, c保护, c虚拟局域网, c列表)
	c标题行0 = "Interface                        Switchport Mode      Access Native Protected VLAN lists"
	c标题行1 = "-------------------------------- ---------- --------- ------ ------ --------- ----------------------"
	def __init__(self):
		数据表.I解析表格管线.__init__(self)
		self.f添加字段(数据表.E字段.e本端接口, F交换接口表.ca列[0], 思科接口.f创建接口)
		self.f添加字段(数据表.E字段.e本端链路类型, F交换接口表.ca列[2], 信息.f解析链路类型)
		self.f添加字段(数据表.E字段.e本端虚拟局域网, F交换接口表.f取虚拟局域网, int)
	f初始处理 = staticmethod(数据表.F去标题行(c标题行0, c标题行1))
	@staticmethod
	def f取虚拟局域网(a行: str):	#判断模式列
		if "ACCESS" in a行[F交换接口表.ca列[2]]:
			return a行[F交换接口表.ca列[3]]
		if "TRUNK" in a行[F交换接口表.ca列[2]]:
			return a行[F交换接口表.ca列[4]]
		raise RuntimeError()	#未知错误
	fi有效行 = staticmethod(数据表.F有效长度(80))
f交换接口表 = F交换接口表()
#===============================================================================
# 网络接口表
#===============================================================================
class F网络接口表4(数据表.I解析表格管线):
	"""show ip interface brief
	适用于: 锐捷s5750(v11.4)"""
	c接口 = 0
	c地址0 = 41
	c地址1 = 62
	c状态 = 83
	c协议 = 106
	ca列 = 数据表.C切割列(c接口, c地址0, c地址1, c状态, c协议)
	c标题行0 = "Interface                                IP-Address(Pri)      IP-Address(Sec)      Status                 Protocol "
	def __init__(self):
		数据表.I解析表格管线.__init__(self)
		self.f添加字段(数据表.E字段.e本端接口, F网络接口表4.ca列[0], 思科接口.f创建接口)
		self.f添加字段(数据表.E字段.e本端网络地址4, F网络接口表4.ca列[1], 地址.S网络地址4.fc自动)
		self.f添加字段(数据表.E字段.e本端链路状态, F网络接口表4.ca列[3], 信息.f解析起宕状态)
		self.f添加字段(数据表.E字段.e本端协议状态, F网络接口表4.ca列[4], 信息.f解析起宕状态)
	fi有效行 = staticmethod(数据表.F有效长度(110))
	f初始处理 = staticmethod(数据表.F去标题行(c标题行0))
f网络接口表4 = F网络接口表4()
#===============================================================================
# 物理地址表
#===============================================================================
class F物理地址表(数据表.I解析表格管线):
	"""show mac-address-table
	适用于: 锐捷s5750(v11.4)"""
	c虚拟局域网 = 0
	c物理地址 = 12
	c类型 = 33
	c接口 = 42
	c时间 = 73
	ca列 = 数据表.C切割列(c虚拟局域网, c物理地址, c类型, c接口, c时间)
	c标题行0 = "Vlan        MAC Address          Type     Interface                      Time"
	c标题行1 = "----------  -------------------- -------- ------------------------------ --------------------"
	c时间格式 = "%Y-%m-%d %H:%M:%S"
	def __init__(self):
		数据表.I解析表格管线.__init__(self)
		self.f添加字段(数据表.E字段.e本端虚拟局域网, F物理地址表.ca列[0], int)
		self.f添加字段(数据表.E字段.e对端物理地址, F物理地址表.ca列[1], 地址.S物理地址.fc字符串)
		self.f添加字段(数据表.E字段.e对端物理地址类型, F物理地址表.ca列[2], 信息.f解析物理地址类型)
		self.f添加字段(数据表.E字段.e本端接口, F物理地址表.ca列[3], 思科接口.f创建接口)
	f初始处理 = staticmethod(数据表.F去标题行(c标题行0, c标题行1))
	fi有效行 = staticmethod(数据表.F有效长度(90))
f物理地址表 = F物理地址表()
#===============================================================================
# 地址解析表
#===============================================================================
class F地址解析表4(数据表.I解析表格管线):
	"""show arp
	适用于: 锐捷s5750(v11.4)"""
	c协议 = 0
	c地址 = 10
	c寿命 = 27
	c硬件 = 37
	c类型 = 53
	c接口 = 60
	ca列 = 数据表.C切割列(c协议, c地址, c寿命, c硬件, c类型, c接口)
	c标题行0 = "Protocol  Address          Age(min)  Hardware        Type   Interface               "
	def __init__(self):
		数据表.I解析表格管线.__init__(self)
		self.f添加字段(数据表.E字段.e对端网络地址4, F地址解析表4.ca列[1], 地址.S网络地址4.fc主机地址字符串)
		self.f添加字段(数据表.E字段.e对端寿命, F地址解析表4.ca列[2], lambda a: int(a) * 60)
		self.f添加字段(数据表.E字段.e对端物理地址, F地址解析表4.ca列[3], 地址.S物理地址.fc字符串)
		self.f添加字段(数据表.E字段.e本端接口, F地址解析表4.ca列[5], 思科接口.f创建接口)
	@staticmethod
	def fi有效行(a行: str):
		if len(a行) < 80:
			return False
		if "-" in a行:
			return False
		return True
	f初始处理 = staticmethod(数据表.F去标题行(c标题行0))
f地址解析表4 = F地址解析表4()