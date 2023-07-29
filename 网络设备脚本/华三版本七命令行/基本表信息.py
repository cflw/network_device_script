import cflw代码库py.cflw字符串 as 字符串
import cflw代码库py.cflw网络地址 as 地址
from ..基础接口 import 信息
from ..基础接口 import 数据表
from . import 接口 as 实现接口
#===============================================================================
# 接口详细
#===============================================================================
class F接口详细v7(数据表.I解析列表管线):
	"""display interface
	适用于: 华三s3100v3(v7.1.*), 华三s6900(v7.1.070), 紫光s7800xp(v7.1.*)"""
	c管理状态 = "Current state"
	c协议状态 = "Line protocol state"
	c物理地址 = "hardware address"
	c描述 = "Description"
	c带宽 = "Bandwidth"
	c最大传输单元 = "Maximum transmission unit"
	c网络地址4 = r"Internet address: (\d+\.\d+\.\d+\.\d+\/\d+)\s"
	c虚拟局域网 = "PVID"
	c链路类型 = "Port link-type"
	c接收率正则 = r"Last 300 seconds input:\s+(\d+) packets/sec (\d+) bytes/sec (.+?)%"
	c发送率正则 = r"Last 300 seconds output:\s+(\d+) packets/sec (\d+) bytes/sec (.+?)%"
	c接收数正则 = r"Input \(total\):  (\d+) packets, (\d+) bytes"
	c发送数正则 = r"Output \(total\): (\d+) packets, (\d+) bytes"
	c接收错误数正则 = r"Input:\s+(\d+) input errors, (\d+) runts, (\d+) giants, (.+?) throttles"
	c发送错误数正则 = r"Output:\s+(\d+) output errors, (.+?) underruns, (.+?) buffer failures"
	def __init__(self):
		数据表.I解析列表管线.__init__(self)
		self.f添加字段(数据表.E字段.e本端接口, lambda s: s[:s.find('\n')], str)
		self.f添加字段(数据表.E字段.e本端管理状态, 数据表.F列表字段(self.c管理状态), 信息.f解析起宕状态)
		self.f添加字段(数据表.E字段.e本端协议状态, 数据表.F列表字段(self.c协议状态), 信息.f解析起宕状态)
		self.f添加字段(数据表.E字段.e本端物理地址, 数据表.F列表字段(self.c物理地址), 地址.S物理地址.fc字符串)
		self.f添加字段(数据表.E字段.e本端描述, 数据表.F列表字段(self.c描述), str)
		self.f添加字段(数据表.E字段.e本端带宽, 数据表.F列表字段(self.c带宽, a结束 = ' '), lambda x: int(x) * 1000)
		self.f添加字段(数据表.E字段.e本端最大传输单元, 数据表.F列表字段(self.c最大传输单元), int)
		self.f添加字段(数据表.E字段.e本端网络地址4, 数据表.F正则字段(self.c网络地址4, 1), 地址.S网络地址4.fc地址前缀长度字符串)
		self.f添加字段(数据表.E字段.e本端虚拟局域网, 数据表.F列表字段(self.c虚拟局域网), int)
		self.f添加字段(数据表.E字段.e本端链路类型, 数据表.F列表字段(self.c链路类型), 信息.f解析链路类型)
		self.f添加字段(数据表.E字段.e本端每秒接收包数, 数据表.F正则字段(self.c接收率正则, 1), int)
		self.f添加字段(数据表.E字段.e本端每秒接收比特数, 数据表.F正则字段(self.c接收率正则, 2), 信息.f字节到比特)
		self.f添加字段(数据表.E字段.e本端接收包数, 数据表.F正则字段(self.c接收数正则, 1), int)
		self.f添加字段(数据表.E字段.e本端接收字节数, 数据表.F正则字段(self.c接收数正则, 2), int)
		self.f添加字段(数据表.E字段.e本端接收错误数, 数据表.F正则字段(self.c接收错误数正则, 1), int)
		self.f添加字段(数据表.E字段.e本端每秒发送包数, 数据表.F正则字段(self.c发送率正则, 1), int)
		self.f添加字段(数据表.E字段.e本端每秒发送比特数, 数据表.F正则字段(self.c发送率正则, 2), 信息.f字节到比特)
		self.f添加字段(数据表.E字段.e本端发送包数, 数据表.F正则字段(self.c发送数正则, 1), int)
		self.f添加字段(数据表.E字段.e本端发送字节数, 数据表.F正则字段(self.c发送数正则, 2), int)
		self.f添加字段(数据表.E字段.e本端发送错误数, 数据表.F正则字段(self.c发送错误数正则, 1), int)
	@staticmethod
	def f下一记录(a文本: str, a开始位置: int)->int:
		"""第1行接口,第2行接口状态.从接口状态往上找"""
		v状态位置0 = a文本.find("Current state:", a开始位置)	#当前记录的状态位置
		v状态位置1 = a文本.find("Current state:", v状态位置0 + 1)	#下一记录的状态位置
		if v状态位置1 < 0:
			return -1
		v接口位置1 = 字符串.f找当前行(a文本, v状态位置1 - 2).start	#下一记录的接口位置
		return v接口位置1
	fi有效记录 = staticmethod(数据表.F有效行数(8))
f接口详细v7 = F接口详细v7()
#===============================================================================
# 网络接口表
#===============================================================================
class F网络接口表4v7(数据表.I解析表格管线):
	"""display ip interface brief
	适用于: 华三s6900(v7.1.070)"""
	c标题行 = "Interface           Physical Protocol IP address      VPN instance Description "
	c接口 = 0
	c物理 = 20
	c协议 = 29
	c地址 = 38
	c实例 = 54
	c描述 = 67
	ca列 = 数据表.C切割列(c接口, c物理, c协议, c地址, c实例, c描述)
	def __init__(self):
		数据表.I解析表格管线.__init__(self)
		self.f添加字段(数据表.E字段.e本端接口, F网络接口表4v7.ca列[0], 实现接口.f创建接口缩写v7)
		self.f添加字段(数据表.E字段.e本端链路状态, F网络接口表4v7.ca列[1], 信息.f解析起宕状态)
		self.f添加字段(数据表.E字段.e本端协议状态, F网络接口表4v7.ca列[2], 信息.f解析起宕状态)
		self.f添加字段(数据表.E字段.e本端网络地址4, F网络接口表4v7.ca列[3], 信息.f解析网络地址4)
		self.f添加字段(数据表.E字段.e本端描述, F网络接口表4v7.ca列[5], str)
	f初始处理 = staticmethod(数据表.F去标题行(c标题行))
	fi有效行 = staticmethod(数据表.F有效长度(c描述))
f网络接口表4v7 = F网络接口表4v7()
class F网络接口表4s5v7(数据表.I解析表格管线):
	"""display ip interface brief
	适用于: 华三s5820v2(v7.1.075)"""
	c接口 = 0
	c物理 = 25
	c协议 = 34
	c地址 = 43
	c描述 = 59
	ca列 = 数据表.C切割列(c接口, c物理, c协议, c地址, c描述)
	c标题行0 = "Interface                Physical Protocol IP Address      Description "
	def __init__(self):
		数据表.I解析表格管线.__init__(self)
		self.f添加字段(数据表.E字段.e本端接口, self.ca列[0], 实现接口.f创建接口缩写v7)
		self.f添加字段(数据表.E字段.e本端链路状态, self.ca列[1], 信息.f解析起宕状态)
		self.f添加字段(数据表.E字段.e本端协议状态, self.ca列[2], 信息.f解析起宕状态)
		self.f添加字段(数据表.E字段.e本端网络地址4, self.ca列[3], 信息.f解析网络地址4)
		self.f添加字段(数据表.E字段.e本端描述, self.ca列[4], str)
	f初始处理 = staticmethod(数据表.F去标题行(c标题行0))
	fi有效行 = staticmethod(数据表.F有效长度(c描述))
	fi结束 = staticmethod(数据表.fi空行)
f网络接口表4s5v7 = F网络接口表4s5v7()
class F网络接口表4s7v7(数据表.I解析表格管线):
	"""display ip interface brief
	适用于: 紫光s8600x(v7.1.070), 紫光s7800xp(v7.1.*)"""
	c接口 = 0
	c物理 = 20
	c协议 = 29
	c地址 = 38
	c实例 = 57
	c描述 = 70
	ca列 = 数据表.C切割列(c接口, c物理, c协议, c地址, c实例, c描述)
	c标题行0 = "Interface           Physical Protocol IP address/Mask    VPN instance Description"
	def __init__(self):
		数据表.I解析表格管线.__init__(self)
		self.f添加字段(数据表.E字段.e本端接口, self.ca列[0], 实现接口.f创建接口缩写v7)
		self.f添加字段(数据表.E字段.e本端链路状态, self.ca列[1], 信息.f解析起宕状态)
		self.f添加字段(数据表.E字段.e本端协议状态, self.ca列[2], 信息.f解析起宕状态)
		self.f添加字段(数据表.E字段.e本端网络地址4, self.ca列[3], 信息.f解析网络地址4)
		self.f添加字段(数据表.E字段.e本端虚拟路由转发, self.ca列[4], lambda x: x if x != "--" else None)
		self.f添加字段(数据表.E字段.e本端描述, self.ca列[5], str)
	f初始处理 = staticmethod(数据表.F去标题行(c标题行0))
	fi有效行 = staticmethod(数据表.F有效长度(c描述))
	fi结束 = staticmethod(数据表.fi空行)
f网络接口表4s7v7 = F网络接口表4s7v7()
#===============================================================================
# 接口表
#===============================================================================
class F接口表s5v7(数据表.I解析表格管线):
	"""display interface brief
	适用于: 华三s5820v2(v7.1.075)"""
	c接口 = 0
	c链路 = 21
	c速率 = 26
	c双工 = 35
	c类型 = 41
	c虚拟局域网 = 46
	c描述 = 51
	ca列 = 数据表.C切割列(c接口, c链路, c速率, c双工, c类型, c虚拟局域网, c描述)
	c标题行0 = "Interface            Link Speed   Duplex Type PVID Description     "
	def __init__(self):
		数据表.I解析表格管线.__init__(self)
		self.f添加字段(数据表.E字段.e本端接口, self.ca列[0], 实现接口.f创建接口缩写v7)
		self.f添加字段(数据表.E字段.e本端链路状态, self.ca列[1], 信息.f解析起宕状态)
		self.f添加字段(数据表.E字段.e本端速率, self.ca列[2], 信息.f解析速率)
		self.f添加字段(数据表.E字段.e本端双工模式, self.ca列[3], 信息.f解析双工模式)
		self.f添加字段(数据表.E字段.e本端链路类型, self.ca列[4], 信息.f解析链路类型)
		self.f添加字段(数据表.E字段.e本端虚拟局域网, self.ca列[5], 信息.f解析虚拟局域网)
		self.f添加字段(数据表.E字段.e本端描述, self.ca列[6], str)
	f初始处理 = staticmethod(数据表.F去标题行(c标题行0))
	fi有效行 = staticmethod(数据表.F有效长度(c描述))
	fi结束 = staticmethod(数据表.fi空行)
f接口表s5v7 = F接口表s5v7()
class F接口表s5v7(数据表.I解析表格管线):
	"""display interface brief,只看二层接口
	适用于: 紫光s8600x(v7.1.070), 紫光s7800xp(v7.1.*)"""
	c接口 = 0
	c链路 = 21
	c速率 = 26
	c双工 = 36
	c类型 = 43
	c虚拟局域网 = 48
	c描述 = 53
	ca列 = 数据表.C切割列(c接口, c链路, c速率, c双工, c类型, c虚拟局域网, c描述)
	c标题行0 = "Interface            Link Speed     Duplex Type PVID Description              "
	def __init__(self):
		数据表.I解析表格管线.__init__(self)
		self.f添加字段(数据表.E字段.e本端接口, self.ca列[0], 实现接口.f创建接口缩写v7)
		self.f添加字段(数据表.E字段.e本端链路状态, self.ca列[1], 信息.f解析起宕状态)
		self.f添加字段(数据表.E字段.e本端速率, self.ca列[2], 信息.f解析速率)
		self.f添加字段(数据表.E字段.e本端双工模式, self.ca列[3], 信息.f解析双工模式缩写)
		self.f添加字段(数据表.E字段.e本端链路类型, self.ca列[4], 信息.f解析链路类型缩写)
		self.f添加字段(数据表.E字段.e本端虚拟局域网, self.ca列[5], 信息.f解析虚拟局域网)
		self.f添加字段(数据表.E字段.e本端描述, self.ca列[6], str)
	f初始处理 = staticmethod(数据表.F去标题行(c标题行0))
	fi有效行 = staticmethod(数据表.F有效长度(c描述))
	fi结束 = staticmethod(数据表.fi空行)
f接口表s7v7 = F接口表s5v7()
#===============================================================================
# 物理地址表
#===============================================================================
class F物理地址表(数据表.I解析表格管线):
	"""display mac-address
	适用于: 华三s5820v2(v7.1.075), 华三s6900(v7.1.070), 紫光s8600x(v7.1.070), 紫光s7800xp(v7.1.*)"""
	c地址 = 0
	c虚拟局域网 = 17
	c状态 = 28
	c端口 = 45
	c老化 = 70
	ca列 = 数据表.C切割列(c地址, c虚拟局域网, c状态, c端口, c老化)
	c标题行0 = "MAC Address      VLAN ID    State            Port/Nickname            Aging"
	def __init__(self):
		数据表.I解析表格管线.__init__(self)
		self.f添加字段(数据表.E字段.e对端物理地址, self.ca列[0], 地址.S物理地址.fc字符串)
		self.f添加字段(数据表.E字段.e本端虚拟局域网, self.ca列[1], 信息.f解析虚拟局域网)
		self.f添加字段(数据表.E字段.e本端接口, self.ca列[3], 实现接口.f创建接口缩写v7)
	f初始处理 = staticmethod(数据表.F去标题行(c标题行0))
	fi有效行 = staticmethod(数据表.F有效长度(c老化))
	fi结束 = staticmethod(数据表.fi空行)
f物理地址表 = F物理地址表()
#===============================================================================
# 地址解析表
#===============================================================================
ca地址解析协议类型 = {
	"S": 信息.E地址解析协议类型.e静态,
	"D": 信息.E地址解析协议类型.e动态,
}
class F地址解析表s5v7(数据表.I解析表格管线):
	"""display arp
	适用于: 华三s5820v2(v7.1.075)"""
	c网络地址 = 0
	c物理地址 = 17
	c虚拟局域网 = 32
	c接口 = 42
	c寿命 = 67
	c类型 = 73
	ca列 = 数据表.C切割列(c网络地址, c物理地址, c虚拟局域网, c接口, c寿命, c类型)
	c标题行0 = "IP address       MAC address    SVLAN/VSI Interface/Link ID        Aging Type  "
	def __init__(self):
		数据表.I解析表格管线.__init__(self)
		self.f添加字段(数据表.E字段.e对端网络地址4, self.ca列[0], 地址.S网络地址4.fc主机地址字符串)
		self.f添加字段(数据表.E字段.e对端物理地址, self.ca列[1], 地址.S物理地址.fc字符串)
		self.f添加字段(数据表.E字段.e本端虚拟局域网, self.ca列[2], 信息.f解析虚拟局域网)
		self.f添加字段(数据表.E字段.e本端接口, self.ca列[3], 实现接口.f创建接口缩写v7)
		self.f添加字段(数据表.E字段.e本端寿命, self.ca列[4], int)
		self.f添加字段(数据表.E字段.e本端地址解析协议类型, self.ca列[5], ca地址解析协议类型.get)
	f初始处理 = staticmethod(数据表.F去标题行(c标题行0))
	fi有效行 = staticmethod(数据表.F有效长度(c类型))
f地址解析表s5v7 = F地址解析表s5v7()
class F地址解析表s6v7(数据表.I解析表格管线):
	"""display arp
	适用于: 华三s6900(v7.1.070)"""
	c网络地址 = 0
	c物理地址 = 16
	c虚拟局域网 = 31
	c接口 = 42
	c寿命 = 67
	c类型 = 73
	ca列 = 数据表.C切割列(c网络地址, c物理地址, c虚拟局域网, c接口, c寿命, c类型)
	c标题行0 = "IP address      MAC address    VLAN/VSI   Interface/Link ID        Aging Type "
	def __init__(self):
		数据表.I解析表格管线.__init__(self)
		self.f添加字段(数据表.E字段.e对端网络地址4, self.ca列[0], 地址.S网络地址4.fc主机地址字符串)
		self.f添加字段(数据表.E字段.e对端物理地址, self.ca列[1], 地址.S物理地址.fc字符串)
		self.f添加字段(数据表.E字段.e本端虚拟局域网, self.ca列[2], 信息.f解析虚拟局域网)
		self.f添加字段(数据表.E字段.e本端接口, self.ca列[3], 实现接口.f创建接口缩写v7)
		self.f添加字段(数据表.E字段.e本端寿命, self.ca列[4], int)
		self.f添加字段(数据表.E字段.e本端地址解析协议类型, self.ca列[5], ca地址解析协议类型.get)
	f初始处理 = staticmethod(数据表.F去标题行(c标题行0))
	fi有效行 = staticmethod(数据表.F有效长度(c类型))
f地址解析表s6v7 = F地址解析表s6v7()
class F地址解析表s7v7(数据表.I解析表格管线):
	"""display arp
	适用于: 紫光s8600x(v7.1.070), 紫光s7800xp(v7.1.*)"""
	c网络地址 = 0
	c物理地址 = 16
	c虚拟局域网 = 31
	c接口 = 45
	c寿命 = 70
	c类型 = 76
	ca列 = 数据表.C切割列(c网络地址, c物理地址, c虚拟局域网, c接口, c寿命, c类型)
	c标题行0 = "IP address      MAC address    VLAN/VSI name Interface                Aging Type"
	def __init__(self):
		数据表.I解析表格管线.__init__(self)
		self.f添加字段(数据表.E字段.e对端网络地址4, self.ca列[0], 地址.S网络地址4.fc主机地址字符串)
		self.f添加字段(数据表.E字段.e对端物理地址, self.ca列[1], 地址.S物理地址.fc字符串)
		self.f添加字段(数据表.E字段.e本端虚拟局域网, self.ca列[2], 信息.f解析虚拟局域网)
		self.f添加字段(数据表.E字段.e本端接口, self.ca列[3], 实现接口.f创建接口缩写v7)
		self.f添加字段(数据表.E字段.e本端寿命, self.ca列[4], int)
		self.f添加字段(数据表.E字段.e本端地址解析协议类型, self.ca列[5], ca地址解析协议类型.get)
	f初始处理 = staticmethod(数据表.F去标题行(c标题行0))
	fi有效行 = staticmethod(数据表.F有效长度(c类型))
f地址解析表s7v7 = F地址解析表s7v7()
class F地址解析表rv7(数据表.I解析表格管线):
	"""display arp
	适用于: 华三msr3640(v7.1.070)"""
	c网络地址 = 0
	c物理地址 = 16
	c虚拟局域网 = 31
	c接口 = 40
	c寿命 = 65
	c类型 = 71
	ca列 = 数据表.C切割列(c网络地址, c物理地址, c虚拟局域网, c接口, c寿命, c类型)
	c标题行0 = "IP address      MAC address    VLAN     Interface                Aging Type "
	def __init__(self):
		数据表.I解析表格管线.__init__(self)
		self.f添加字段(数据表.E字段.e对端网络地址4, self.ca列[0], 地址.S网络地址4.fc主机地址字符串)
		self.f添加字段(数据表.E字段.e对端物理地址, self.ca列[1], 地址.S物理地址.fc字符串)
		self.f添加字段(数据表.E字段.e本端虚拟局域网, self.ca列[2], 信息.f解析虚拟局域网)
		self.f添加字段(数据表.E字段.e本端接口, self.ca列[3], 实现接口.f创建接口缩写v7)
		self.f添加字段(数据表.E字段.e本端寿命, self.ca列[4], int)
		self.f添加字段(数据表.E字段.e本端地址解析协议类型, self.ca列[5], ca地址解析协议类型.get)
	f初始处理 = staticmethod(数据表.F去标题行(c标题行0))
	fi有效行 = staticmethod(数据表.F有效长度(c类型))
f地址解析表rv7 = F地址解析表rv7()