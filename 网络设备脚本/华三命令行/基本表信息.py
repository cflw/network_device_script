import cflw代码库py.cflw字符串 as 字符串
import cflw代码库py.cflw网络地址 as 地址
from ..基础接口 import 虚拟局域网
from ..基础接口 import 信息
from ..基础接口 import 数据表
from . import 接口 as 实现接口
from .常量 import *
#===============================================================================
# 接口表
#===============================================================================
ca链路类型 = {
	"A": 虚拟局域网.E链路类型.e接入,
	"T": 虚拟局域网.E链路类型.e中继,
	"H": 虚拟局域网.E链路类型.e混合,
}
class F接口表r4(数据表.I解析表格管线):
	"""display interface brief
	适用于: 路由器"""
	c接口 = 0
	c链路 = 21
	c协议 = 26
	c地址 = 35
	c描述 = 51
	ca列 = 数据表.C切割列(c接口, c链路, c协议, c地址, c描述)
	c标题行 = "Interface            Link Protocol Primary IP      Description"
	def __init__(self):
		数据表.I解析表格管线.__init__(self)
		self.f添加字段(数据表.E字段.e本端接口, F接口表r4.ca列[0], 实现接口.f创建接口缩写)
		self.f添加字段(数据表.E字段.e本端链路状态, F接口表r4.ca列[1], 信息.f解析起宕状态)
		self.f添加字段(数据表.E字段.e本端协议状态, F接口表r4.ca列[2], 信息.f解析起宕状态)
		self.f添加字段(数据表.E字段.e本端网络地址4, F接口表r4.ca列[3], 信息.f解析网络地址4)
		self.f添加字段(数据表.E字段.e本端描述, F接口表r4.ca列[4], str)
	f初始处理 = staticmethod(数据表.F去标题行(c标题行))
	fi有效行 = staticmethod(数据表.F有效长度(50))
f接口表r4 = F接口表r4()
class F接口表sv3(数据表.I解析表格管线):
	"""display brief interface
	适用于: 华为s3900系列(v3.10), 华三s3900系列(v3.10), 华三s7500系列(v3.10)"""
	c标题行0 = "Interface   Link     Speed  Duplex Type   PVID Description"
	c标题行1 = "---------------------------------------------------------------------------"
	c接口 = 0
	c链路 = 12
	c速率 = 21
	c双工 = 28
	c类型 = 35
	c虚拟局域网 = 42
	c描述 = 47
	ca列 = 数据表.C切割列(c接口, c链路, c速率, c双工, c类型, c虚拟局域网, c描述)
	def __init__(self):
		数据表.I解析表格管线.__init__(self)
		self.f添加字段(数据表.E字段.e本端接口, F接口表sv3.ca列[0], 实现接口.f创建接口缩写)
		self.f添加字段(数据表.E字段.e本端链路状态, F接口表sv3.ca列[1], 信息.f解析起宕状态)
		self.f添加字段(数据表.E字段.e本端速率, F接口表sv3.ca列[2], 信息.f解析速率)
		self.f添加字段(数据表.E字段.e本端双工模式, F接口表sv3.ca列[3], 信息.f解析双工模式)
		self.f添加字段(数据表.E字段.e本端链路类型, F接口表sv3.ca列[4], 信息.f解析链路类型)
		self.f添加字段(数据表.E字段.e本端虚拟局域网, F接口表sv3.ca列[5], 信息.f解析虚拟局域网)
		self.f添加字段(数据表.E字段.e本端描述, F接口表sv3.ca列[6], str)
	f初始处理 = staticmethod(数据表.F去标题行(c标题行0, c标题行1))
	fi有效行 = staticmethod(数据表.F有效长度(c虚拟局域网))
	fi结束 = staticmethod(数据表.fi空行)
f接口表sv3 = F接口表sv3()
class F接口表sv5(数据表.I解析表格管线):
	"""display interface brief
	适用于: 华三s3600v2(v5.20), 华三s5500(v5.20)"""
	c接口 = 0
	c链路 = 21
	c速率 = 26
	c双工 = 34
	c类型 = 41
	c虚拟局域网 = 46
	c描述 = 51
	ca列 = 数据表.C切割列(c接口, c链路, c速率, c双工, c类型, c虚拟局域网, c描述)
	c标题行 = "Interface            Link Speed   Duplex Type PVID Description"
	def __init__(self):
		数据表.I解析表格管线.__init__(self)
		self.f添加字段(数据表.E字段.e本端接口, F接口表sv5.ca列[0], 实现接口.f创建接口缩写)
		self.f添加字段(数据表.E字段.e本端链路状态, F接口表sv5.ca列[1], 信息.f解析起宕状态)
		self.f添加字段(数据表.E字段.e本端速率, F接口表sv5.ca列[2], 信息.f解析速率)
		self.f添加字段(数据表.E字段.e本端双工模式, F接口表sv5.ca列[3], lambda s: "F" in s)
		self.f添加字段(数据表.E字段.e本端链路类型, F接口表sv5.ca列[4], ca链路类型.get)
		self.f添加字段(数据表.E字段.e本端虚拟局域网, F接口表sv5.ca列[5], 信息.f解析虚拟局域网)
		self.f添加字段(数据表.E字段.e本端描述, F接口表sv5.ca列[6], str)
	f初始处理 = staticmethod(数据表.F去标题行(c标题行))
	fi有效行 = staticmethod(数据表.F有效长度(c虚拟局域网))
	fi结束 = staticmethod(数据表.fi空行)
f接口表sv5 = F接口表sv5()
#===============================================================================
# 网络接口表
#===============================================================================
class F网络接口表4(数据表.I解析表格管线):
	"""display ip interface brief
	适用于:msr36系列(v7.1.*)"""
	c接口 = 0
	c物理 = 25
	c协议 = 34
	c地址 = 43
	c描述 = 59
	ca列 = 数据表.C切割列(c接口, c物理, c协议, c地址, c描述)
	c标题行 = "Interface                Physical Protocol IP Address      Description"
	def __init__(self):
		数据表.I解析表格管线.__init__(self)
		self.f添加字段(数据表.E字段.e本端接口, F网络接口表4.ca列[0], 实现接口.f创建接口缩写)
		self.f添加字段(数据表.E字段.e本端链路状态, F网络接口表4.ca列[1], 信息.f解析起宕状态)
		self.f添加字段(数据表.E字段.e本端协议状态, F网络接口表4.ca列[2], 信息.f解析起宕状态)
		self.f添加字段(数据表.E字段.e本端网络地址4, F网络接口表4.ca列[3], 信息.f解析网络地址4)
		self.f添加字段(数据表.E字段.e本端描述, F网络接口表4.ca列[4], str)
	f初始处理 = staticmethod(数据表.F去标题行(c标题行))
	fi有效行 = staticmethod(数据表.F有效长度(50))
f网络接口表4 = F网络接口表4()
#===============================================================================
# 物理地址表
#===============================================================================
ca物理地址类型 = {
	"Learned": 信息.E物理地址类型.e动态,
	"Config static": 信息.E物理地址类型.e静态,
}
class F物理地址表s3v3(数据表.I解析表格管线):
	"""display mac-address
	适用于: 华三s3928(v3.10)"""
	c标题行 = "MAC ADDR        VLAN ID   STATE          PORT INDEX               AGING TIME(s)"
	c物理地址 = 0
	c虚拟局域网 = 16
	c状态 = 26
	c接口 = 41
	c老化 = 66
	ca列 = 数据表.C切割列(c物理地址, c虚拟局域网, c状态, c接口, c老化)
	def __init__(self):
		数据表.I解析表格管线.__init__(self)
		self.f添加字段(数据表.E字段.e对端物理地址, self.ca列[0], 地址.S物理地址.fc字符串)
		self.f添加字段(数据表.E字段.e本端虚拟局域网, self.ca列[1], 信息.f解析虚拟局域网)
		self.f添加字段(数据表.E字段.e对端物理地址类型, self.ca列[2], ca物理地址类型.get)
		self.f添加字段(数据表.E字段.e本端接口, self.ca列[3], 实现接口.f创建接口)
		# self.f添加字段(数据表.E字段.e本端描述, self.ca列[4], str)
	f初始处理 = staticmethod(数据表.F去标题行(c标题行))
	fi有效行 = staticmethod(数据表.F有效长度(c老化))
f物理地址表s3v3 = F物理地址表s3v3()
class F物理地址表s7v3(数据表.I解析多行表格管线):
	"""display mac-address
	适用于: 华三s7503(v3.10)"""
	c物理地址 = 0
	c虚拟局域网 = 16
	c状态 = 27
	c接口 = 44
	c老化 = 67
	ca列 = 数据表.C切割列(c物理地址, c虚拟局域网, c状态, c接口, c老化)
	c标题行0 = "MAC ADDR        VLAN ID    STATE            PORT INDEX             AGING TIME(s)"
	def __init__(self):
		数据表.I解析多行表格管线.__init__(self)
		self.m行0 = 数据表.C行()
		self.m行0.f添加字段(数据表.E字段.e对端物理地址, self.ca列[0], 地址.S物理地址.fc字符串)
		self.m行0.f添加字段(数据表.E字段.e本端虚拟局域网, self.ca列[1], int)
		self.m行0.f添加字段(数据表.E字段.e对端物理地址类型, self.ca列[2], ca物理地址类型.get)
		self.m行0.f添加字段(数据表.E字段.e本端接口, self.ca列[3], 实现接口.f创建接口)
		self.m行1 = 数据表.C行()	#只有接口列
		self.m行1.f添加字段(数据表.E字段.e对端物理地址, self.F上次结果(数据表.E字段.e对端物理地址))
		self.m行1.f添加字段(数据表.E字段.e本端虚拟局域网, self.F上次结果(数据表.E字段.e本端虚拟局域网))
		self.m行1.f添加字段(数据表.E字段.e对端物理地址类型, self.F上次结果(数据表.E字段.e对端物理地址类型))
		self.m行1.f添加字段(数据表.E字段.e本端接口, self.ca列[3], 实现接口.f创建接口)
	def f解析行(self, a行: str):
		if a行[4] == '-':	#是mac地址的分隔符号
			return self.m行0.f解析(a行)
		else:
			return self.m行1.f解析(a行)
	f初始处理 = staticmethod(数据表.F去标题行(c标题行0))
	fi有效行 = staticmethod(数据表.F有效长度(c老化))
f物理地址表s7v3 = F物理地址表s7v3()
#===============================================================================
# 地址解析表
#===============================================================================
ca地址解析协议类型 = {
	"S": 信息.E地址解析协议类型.e静态,
	"D": 信息.E地址解析协议类型.e动态,
}
class F地址解析表v5(数据表.I解析表格管线):
	"""display arp
	适用于: 华三s5500(v5.20)"""
	c标题行 = "IP Address       MAC Address     VLAN ID  Interface              Aging Type"
	c网络地址 = 0
	c物理地址 = 17
	c虚拟局域网 = 33
	c接口 = 42
	c寿命 = 65
	c类型 = 71
	ca列 = 数据表.C切割列(c网络地址, c物理地址, c虚拟局域网, c接口, c寿命, c类型)
	def __init__(self):
		数据表.I解析表格管线.__init__(self)
		self.f添加字段(数据表.E字段.e对端网络地址4, F地址解析表v5.ca列[0], 地址.S网络地址4.fc主机地址字符串)
		self.f添加字段(数据表.E字段.e对端物理地址, F地址解析表v5.ca列[1], 地址.S物理地址.fc字符串)
		self.f添加字段(数据表.E字段.e本端虚拟局域网, F地址解析表v5.ca列[2], 信息.f解析数字)
		self.f添加字段(数据表.E字段.e本端接口, F地址解析表v5.ca列[3], lambda x: 实现接口.f创建接口缩写(x) if x != c不适用 else None)
		self.f添加字段(数据表.E字段.e本端寿命, F地址解析表v5.ca列[4], lambda x: 信息.f解析数字(x) * 60)
		self.f添加字段(数据表.E字段.e本端地址解析协议类型, F地址解析表v5.ca列[5], ca地址解析协议类型.get)
	f初始处理 = staticmethod(数据表.F去标题行(c标题行))
	fi有效行 = staticmethod(数据表.F有效长度(c类型))
f地址解析表v5 = F地址解析表v5()
