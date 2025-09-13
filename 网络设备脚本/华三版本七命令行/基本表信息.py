import cflw代码库py.cflw字符串 as 字符串
import cflw代码库py.cflw网络地址 as 地址
from ..基础接口 import 信息
from ..基础接口 import 数据表
from . import 接口 as 实现接口
#===============================================================================
# 接口详细
#===============================================================================
class F接口详细_v7(数据表.I解析列表管线):
	"""display interface
	适用于: 华三s3100v3(v7.1.*), 华三s6900(v7.1.070), 
		紫光s7800xp(v7.1.*), 紫光s5200(v7.1.*)"""
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
		v接口位置1 = 字符串.f找当前行切片(a文本, v状态位置1 - 2).start	#下一记录的接口位置
		return v接口位置1
	fi有效记录 = staticmethod(数据表.F有效行数(8))
f接口详细_v7 = F接口详细_v7()
#===============================================================================
# 网络接口表4
#===============================================================================
class F网络接口表4_v7(数据表.I解析表格管线):
	"""display ip interface brief
	适用于: 华三s5560x(v7.1.070), 华三s6520x(v7.1.070), 华三s6900(v7.1.070), 华三s9850(v7.1.070)
		紫光s5200(v7.1.*), 紫光s5600(v7.1.070 r7734p05)"""
	ca标题字段 = ("Interface", "Physical", "Protocol", "IP address", "VPN instance", "Description")
	def __init__(self):
		数据表.I解析表格管线.__init__(self)
		self.m自动切割列 = 数据表.C自动切割列()
		self.f添加字段(数据表.E字段.e本端接口, self.m自动切割列[0], 实现接口.f创建接口缩写v7)
		self.f添加字段(数据表.E字段.e本端链路状态, self.m自动切割列[1], 信息.f解析起宕状态)
		self.f添加字段(数据表.E字段.e本端协议状态, self.m自动切割列[2], 信息.f解析起宕状态)
		self.f添加字段(数据表.E字段.e本端网络地址4, self.m自动切割列[3], 信息.f解析网络地址4)
		self.f添加字段(数据表.E字段.e本端虚拟路由转发, self.m自动切割列[4], lambda x: x if x != "--" else None)
		self.f添加字段(数据表.E字段.e本端描述, self.m自动切割列[5], str)
	f初始处理 = 数据表.C自动切割列.F初始处理(*ca标题字段)
	fi有效行 = 数据表.C自动切割列.Fi有效行()
	fi结束 = staticmethod(数据表.fi空行)
f网络接口表4_v7 = F网络接口表4_v7()
class F网络接口表4_sv7(数据表.I解析表格管线):
	"""display ip interface brief
	适用于: 华三s5820v2(v7.1.075), 华三S9810(V7.1.*)"""
	ca标题字段 = ("Interface", "Physical", "Protocol", "IP Address", "Description")
	def __init__(self):
		数据表.I解析表格管线.__init__(self)
		self.m自动切割列 = 数据表.C自动切割列()
		self.f添加字段(数据表.E字段.e本端接口, self.m自动切割列[0], 实现接口.f创建接口缩写v7)
		self.f添加字段(数据表.E字段.e本端链路状态, self.m自动切割列[1], 信息.f解析起宕状态)
		self.f添加字段(数据表.E字段.e本端协议状态, self.m自动切割列[2], 信息.f解析起宕状态)
		self.f添加字段(数据表.E字段.e本端网络地址4, self.m自动切割列[3], 信息.f解析网络地址4)
		self.f添加字段(数据表.E字段.e本端描述, self.m自动切割列[4], str)
	f初始处理 = 数据表.C自动切割列.F初始处理(*ca标题字段)
	fi有效行 = 数据表.C自动切割列.Fi有效行()
	fi结束 = staticmethod(数据表.fi空行)
f网络接口表4_sv7 = F网络接口表4_sv7()
#===============================================================================
# 网络接口表6
#===============================================================================
class F网络接口表6_s9v7(数据表.I解析表格管线):
	"""display ipv6 interface brief
	适用于: 华三S9810(V7.1.*), 紫光s8600(v7.1.070)"""
	c标题行0 = "Interface                                 Physical Protocol IPv6 Address"
	c数据行0 = "M-GigabitEthernet1/0/0/0                  down     down     Unassigned"
	ca列 = 数据表.f自动分列(c标题行0, c数据行0)
	c接口, c物理, c协议, c地址 = ca列.fe列位置()
	def __init__(self):
		数据表.I解析表格管线.__init__(self)
		self.f添加字段(数据表.E字段.e本端接口, self.ca列[0], 实现接口.f创建接口v7)
		self.f添加字段(数据表.E字段.e本端链路状态, self.ca列[1], 信息.f解析起宕状态)
		self.f添加字段(数据表.E字段.e本端协议状态, self.ca列[2], 信息.f解析起宕状态)
		self.f添加字段(数据表.E字段.e本端网络地址4, self.ca列[3], 信息.f解析网络地址6)
	f初始处理 = staticmethod(数据表.F去标题行(c标题行0))
	fi有效行 = staticmethod(数据表.F有效长度(c地址))
	fi结束 = staticmethod(数据表.fi空行)
f网络接口表6_s9v7 = F网络接口表6_s9v7()
#===============================================================================
# 接口表
#===============================================================================
class F接口表_v7(数据表.I解析表格管线):
	"""display interface brief,只看二层接口
	适用于: 华三s5560x(v7.1.070), 华三s5820v2(v7.1.075), 华三s6520x(v7.1.070), 华三s6900(v7.1.070), 
		华三S9810(V7.1.*), 华三s9850(v7.1.070)
		紫光s5200(v7.1.*), 紫光s5600(v7.1.070), 紫光s7800xp(v7.1.*), 紫光s8600x(v7.1.070)"""
	ca标题字段 = "Interface", "Link", "Speed", "Duplex", "Type", "PVID", "Description"
	def __init__(self):
		数据表.I解析表格管线.__init__(self)
		self.m自动切割列 = 数据表.C自动切割列()
		self.f添加字段(数据表.E字段.e本端接口, self.m自动切割列[0], 实现接口.f创建接口缩写v7)
		self.f添加字段(数据表.E字段.e本端链路状态, self.m自动切割列[1], 信息.f解析起宕状态)
		self.f添加字段(数据表.E字段.e本端速率, self.m自动切割列[2], 信息.f解析速率)
		self.f添加字段(数据表.E字段.e本端双工模式, self.m自动切割列[3], 信息.f解析双工模式缩写)
		self.f添加字段(数据表.E字段.e本端链路类型, self.m自动切割列[4], 信息.f解析链路类型缩写)
		self.f添加字段(数据表.E字段.e本端虚拟局域网, self.m自动切割列[5], 信息.f解析虚拟局域网)
		self.f添加字段(数据表.E字段.e本端描述, self.m自动切割列[6], str)
	f初始处理 = 数据表.C自动切割列.F初始处理(*ca标题字段)
	fi有效行 = 数据表.C自动切割列.Fi有效行()
	fi结束 = staticmethod(数据表.fi空行)
f接口表_v7 = F接口表_v7()
#===============================================================================
# 物理地址表
#===============================================================================
class F物理地址表_v7(数据表.I解析表格管线):
	"""display mac-address
	适用于: 华三s5560x(v7.1.070), 华三s5820v2(v7.1.075), 
		华三s6900(v7.1.070), 华三s9810(v7.1.*), 华三s9850(v7.1.070)
		紫光s5200(v7.1.*), 紫光s5600(v7.1.070), 紫光s8600x(v7.1.070), 紫光s7800xp(v7.1.*)"""
	ca标题字段 = ("MAC Address", "VLAN ID", "State", "Port", "Aging")
	def __init__(self):
		数据表.I解析表格管线.__init__(self)
		self.m自动切割列 = 数据表.C自动切割列()
		self.f添加字段(数据表.E字段.e对端物理地址, self.m自动切割列[0], 地址.S物理地址.fc字符串)
		self.f添加字段(数据表.E字段.e本端虚拟局域网, self.m自动切割列[1], 信息.f解析虚拟局域网)
		self.f添加字段(数据表.E字段.e本端接口, self.m自动切割列[3], 实现接口.f创建接口缩写v7)
	f初始处理 = 数据表.C自动切割列.F初始处理(*ca标题字段)
	fi有效行 = 数据表.C自动切割列.Fi有效行()
	fi结束 = staticmethod(数据表.fi空行)
f物理地址表_v7 = F物理地址表_v7()
#===============================================================================
# 地址解析表
#===============================================================================
ca地址解析协议类型 = {
	"S": 信息.E地址解析协议类型.e静态,
	"D": 信息.E地址解析协议类型.e动态,
}
class F地址解析表_s5v7(数据表.I解析表格管线):
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
f地址解析表_s5v7 = F地址解析表_s5v7()
class F地址解析表_v7(数据表.I解析表格管线):
	"""display arp
	适用于: 华三msr3640(v7.1.070),
		华三s5560x(v7.1.070), 华三s6520x(v7.1.070), 华三s6900(v7.1.070), 华三s9850(v7.1.070)
		紫光s5600(v7.1.070)"""
	ca标题字段 = ("IP address", "MAC address", "VLAN", "Interface", "Aging", "Type")
	def __init__(self):
		数据表.I解析表格管线.__init__(self)
		self.m自动切割列 = 数据表.C自动切割列()
		self.f添加字段(数据表.E字段.e对端网络地址4, self.m自动切割列[0], 地址.S网络地址4.fc主机地址字符串)
		self.f添加字段(数据表.E字段.e对端物理地址, self.m自动切割列[1], 地址.S物理地址.fc字符串)
		self.f添加字段(数据表.E字段.e本端虚拟局域网, self.m自动切割列[2], 信息.f解析虚拟局域网)
		self.f添加字段(数据表.E字段.e本端接口, self.m自动切割列[3], 实现接口.f创建接口缩写v7)
		self.f添加字段(数据表.E字段.e本端寿命, self.m自动切割列[4], int)
		self.f添加字段(数据表.E字段.e本端地址解析协议类型, self.m自动切割列[5], ca地址解析协议类型.get)
	f初始处理 = 数据表.C自动切割列.F初始处理(*ca标题字段)
	fi有效行 = 数据表.C自动切割列.Fi有效行()
f地址解析表_v7 = F地址解析表_v7()
class F地址解析表_s9v7(数据表.I解析表格管线):
	"""display arp
	适用于: 华三s9810(v7.1.*)"""
	c标题行0 = "IP address      MAC address    VID        Interface/Link ID        Aging Type "
	c数据行0 = "xxx.xxx.xxx.xxx hhhh-hhhh-hhhh nnnn       XGE1/0/0/1               20    D    "
	ca列 = 数据表.f自动分列(c标题行0, c数据行0)
	c网络地址, c物理地址, c虚拟局域网, c接口, c寿命, c类型 = ca列.fe列位置()
	def __init__(self):
		数据表.I解析表格管线.__init__(self)
		self.f添加字段(数据表.E字段.e对端网络地址4, self.ca列[0], 地址.S网络地址4.fc主机地址字符串)
		self.f添加字段(数据表.E字段.e对端物理地址, self.ca列[1], 地址.S物理地址.fc字符串)
		self.f添加字段(数据表.E字段.e本端虚拟局域网, self.ca列[2], 信息.f解析虚拟局域网)
		self.f添加字段(数据表.E字段.e本端接口, self.ca列[3], 实现接口.f创建接口缩写s9v7)
		self.f添加字段(数据表.E字段.e本端寿命, self.ca列[4], int)
		self.f添加字段(数据表.E字段.e本端地址解析协议类型, self.ca列[5], ca地址解析协议类型.get)
	f初始处理 = staticmethod(数据表.F去标题行(c标题行0))
	fi有效行 = staticmethod(数据表.F有效长度(c类型))
f地址解析表_s9v7 = F地址解析表_s9v7()