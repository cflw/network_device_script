import cflw代码库py.cflw字符串 as 字符串
import cflw代码库py.cflw网络地址 as 地址
from ..基础接口 import 信息
from ..基础接口 import 接口 as 北向接口
from ..基础接口 import 数据表
from . import 接口 as 实现接口
#===============================================================================
# 接口详细
#===============================================================================
class F接口详细(数据表.I解析列表管线):
	"""display interface
	适用于: 华为s3700(v5.110~5.70), 华为ar201(模拟器)"""
	c接口状态正则 = r"current state : (.+?)\s"
	c协议状态正则 = r"Line protocol current state : (.+?)\s"
	c描述 = "Description"
	c物理地址正则 = r"Hardware address is (.+?)\s"
	c速率正则 = r"Speed :\s+?(.+?),"
	c双工模式正则 = r"Duplex:\s+?(.+?),"
	c接收正则 = r"Last 300 seconds input rate (\d+) bits/sec, (\d+) packets/sec"
	c发送正则 = r"Last 300 seconds output rate (\d+) bits/sec, (\d+) packets/sec"
	c接收带宽 = "Input bandwidth utilization"
	c发送带宽 = "Output bandwidth utilization"
	def __init__(self):
		数据表.I解析列表管线.__init__(self)
		self.f添加字段(数据表.E字段.e本端接口, 数据表.F正则字段(北向接口.c接口正则, 0), 实现接口.f创建接口)
		self.f添加字段(数据表.E字段.e本端管理状态, 数据表.F正则字段(self.c接口状态正则, 1), 信息.f解析起宕状态)
		self.f添加字段(数据表.E字段.e本端协议状态, 数据表.F正则字段(self.c协议状态正则, 1), 信息.f解析起宕状态)
		self.f添加字段(数据表.E字段.e本端物理地址, 数据表.F正则字段(self.c物理地址正则, 1), 地址.S物理地址.fc字符串)
		self.f添加字段(数据表.E字段.e本端描述, 数据表.F列表字段(self.c描述), str)
		self.f添加字段(数据表.E字段.e本端速率, 数据表.F正则字段(self.c速率正则, 1), 信息.f解析速率)
		self.f添加字段(数据表.E字段.e本端双工模式, 数据表.F正则字段(self.c双工模式正则, 1), 信息.f解析双工模式)
		self.f添加字段(数据表.E字段.e本端每秒接收比特数, 数据表.F正则字段(self.c接收正则, 1), int)
		self.f添加字段(数据表.E字段.e本端每秒接收包数, 数据表.F正则字段(self.c接收正则, 2), int)
		self.f添加字段(数据表.E字段.e本端每秒发送比特数, 数据表.F正则字段(self.c发送正则, 1), int)
		self.f添加字段(数据表.E字段.e本端每秒发送包数, 数据表.F正则字段(self.c发送正则, 2), int)
		self.f添加字段(数据表.E字段.e本端接收利用率, 数据表.F列表字段(self.c接收带宽), 信息.f解析数字)
		self.f添加字段(数据表.E字段.e本端发送利用率, 数据表.F列表字段(self.c发送带宽), 信息.f解析数字)
	@staticmethod
	def f下一记录(a文本: str, a开始位置: int)->int:
		v开始位置 = a开始位置
		for i in range(3):	#往下找第3个"current state"
			v开始位置 = a文本.find("current state", v开始位置+1)
			if v开始位置 > 0:
				pass
			else:
				return -1
		v切片 = 字符串.f找当前行切片(a文本, v开始位置)
		return v切片.start
f接口详细 = F接口详细()
#===============================================================================
# 物理接口表
#===============================================================================
class F接口表(数据表.I解析表格管线):
	"""display interface brief
	适用于: 华为s3700(v5.70), 华为ar201(模拟器)"""
	c标题行0 = "Interface                   PHY   Protocol InUti OutUti   inErrors  outErrors"
	c接口 = 0
	c物理 = 28
	c协议 = 34
	c输入率 = 43
	c输出率 = 49
	c输入错误 = 58
	c输出错误 = 68
	ca列 = 数据表.C切割列(c接口, c物理, c协议, c输入率, c输出率, c输入错误, c输出错误)
	def __init__(self):
		数据表.I解析表格管线.__init__(self)
		self.f添加字段(数据表.E字段.e本端接口, self.ca列[0], 实现接口.f创建接口)
		self.f添加字段(数据表.E字段.e本端链路状态, self.ca列[1], 信息.f解析起宕状态)
		self.f添加字段(数据表.E字段.e本端协议状态, self.ca列[2], 信息.f解析起宕状态)
		self.f添加字段(数据表.E字段.e本端接收利用率, self.ca列[3], 信息.f解析数字)
		self.f添加字段(数据表.E字段.e本端发送利用率, self.ca列[4], 信息.f解析数字)
		self.f添加字段(数据表.E字段.e本端接收错误数, self.ca列[5], int)
		self.f添加字段(数据表.E字段.e本端发送错误数, self.ca列[6], int)
	f初始处理 = staticmethod(数据表.F去标题行(c标题行0))
	fi有效行 = staticmethod(数据表.F有效长度(len(c标题行0)))
f接口表 = F接口表()
#===============================================================================
# 网络接口表
#===============================================================================
class F网络接口表4(数据表.I解析表格管线):
	"""display ip interface brief"""
	c标题行0 = "Interface                         IP Address/Mask      Physical   Protocol  "
	c接口 = 0
	c地址 = 34
	c物理 = 55
	c协议 = 66
	ca列 = 数据表.C切割列(c接口, c地址, c物理, c协议)
	def __init__(self):
		数据表.I解析表格管线.__init__(self)
		self.f添加字段(数据表.E字段.e本端接口, F网络接口表4.ca列[0], 实现接口.f创建接口)
		self.f添加字段(数据表.E字段.e本端网络地址4, F网络接口表4.ca列[1], 信息.f解析网络地址4)
		self.f添加字段(数据表.E字段.e本端链路状态, F网络接口表4.ca列[2], 信息.f解析起宕状态)
		self.f添加字段(数据表.E字段.e本端协议状态, F网络接口表4.ca列[3], 信息.f解析起宕状态)
	f初始处理 = staticmethod(数据表.F去标题行(c标题行0))
	fi有效行 = staticmethod(数据表.F有效长度(c协议))
f网络接口表4 = F网络接口表4()
#===============================================================================
# 地址解析表
#===============================================================================
ca地址解析类型 = {
	"D": 信息.E地址解析协议类型.e动态,
	"S": 信息.E地址解析协议类型.e静态,
	"I": 信息.E地址解析协议类型.e接口,
}
class F地址解析表(数据表.I解析多行表格管线):
	"""display arp
	适用于: 华为s5700(v5.110)"""
	c网络地址 = 0
	c物理地址 = 16
	c过期 = 32	#单位:分钟
	c类型 = 42
	c接口 = 47	#缩写
	c虚拟路由 = 62	#可能0个字符
	ca列 = 数据表.C切割列(c网络地址, c物理地址, c过期, c类型, c接口, c虚拟路由)
	c标题行0 = "IP ADDRESS      MAC ADDRESS     EXPIRE(M) TYPE INTERFACE      VPN-INSTANCE    "
	c标题行1 = "                                          VLAN "
	c标题行2 = "------------------------------------------------------------------------------"
	def __init__(self):
		数据表.I解析多行表格管线.__init__(self)
		self.m行0 = 数据表.C行()	#基础行
		self.m行0.f添加字段(数据表.E字段.e对端网络地址4, self.ca列[0], 地址.S网络地址4.fc主机地址字符串)
		self.m行0.f添加字段(数据表.E字段.e对端物理地址, self.ca列[1], 地址.S物理地址.fc字符串)
		self.m行0.f添加字段(数据表.E字段.e本端寿命, self.ca列[2], lambda x: 信息.f解析数字(x) * 60)
		self.m行0.f添加字段(数据表.E字段.e本端地址解析协议类型, self.fg类型, ca地址解析类型.get)
		self.m行0.f添加字段(数据表.E字段.e本端接口, self.ca列[4], 实现接口.f创建接口缩写)
		self.m行1 = 数据表.C行()	#vlan行
		self.m行1.f添加字段(数据表.E字段.e本端虚拟局域网, self.ca列[3], int)
		self.m行 = 0	#决定使用行0还是行1来解析
	def f解析行(self, a行: str):
		if self.m行:	#1
			return self.m行1.f解析(a行)
		else:	#0
			self.m行 += 1
			return self.m行0.f解析(a行)
	f初始处理 = staticmethod(数据表.F去标题行(c标题行0, c标题行1, c标题行2))
	@staticmethod
	def fi有效行(a行: str):
		if len(a行) < F地址解析表.c类型:	#太短
			return False
		return True
	@staticmethod
	def fi结束(a行: str):
		return "--" in a行
	def fi新记录(self, a行: str):
		v结果 = a行[0] != ' '
		if v结果:
			self.m行 = 0
		return v结果
	fg类型 = staticmethod(lambda x: x[F地址解析表.c类型])
f地址解析表 = F地址解析表()
class F地址解析表ar(F地址解析表):
	"""display arp
	适用于: 华为ar201(模拟器)"""
	c网络地址 = 0
	c物理地址 = 16
	c过期 = 32	#单位:分钟
	c类型 = 42
	c接口 = 54	#缩写
	c虚拟路由 = 66	#可能0个字符
	ca列 = 数据表.C切割列(c网络地址, c物理地址, c过期, c类型, c接口, c虚拟路由)
	c标题行0 = "IP ADDRESS      MAC ADDRESS     EXPIRE(M) TYPE        INTERFACE   VPN-INSTANCE "
	c标题行1 = "                                          VLAN/CEVLAN PVC                      "
	c标题行2 = "------------------------------------------------------------------------------"
	def __init__(self):
		数据表.I解析多行表格管线.__init__(self)
		self.m行0 = 数据表.C行()	#基础行
		self.m行0.f添加字段(数据表.E字段.e对端网络地址4, self.ca列[0], 地址.S网络地址4.fc主机地址字符串)
		self.m行0.f添加字段(数据表.E字段.e对端物理地址, self.ca列[1], 地址.S物理地址.fc字符串)
		self.m行0.f添加字段(数据表.E字段.e本端寿命, self.ca列[2], lambda x: 信息.f解析数字(x) * 60)
		self.m行0.f添加字段(数据表.E字段.e本端地址解析协议类型, self.fg类型, ca地址解析类型.get)
		self.m行0.f添加字段(数据表.E字段.e本端接口, self.ca列[4], 实现接口.f创建接口缩写)
		self.m行1 = 数据表.C行()	#vlan行
		self.m行1.f添加字段(数据表.E字段.e本端虚拟局域网, self.ca列[3], lambda x: int(x.split('/')[0]))
		self.m行 = 0	#决定使用行0还是行1来解析
	f初始处理 = staticmethod(数据表.F去标题行(c标题行0, c标题行1, c标题行2))
f地址解析表ar = F地址解析表ar()
#===============================================================================
# 物理地址表
#===============================================================================
class F物理地址表(数据表.I解析表格管线):
	"""display mac-address
	适用于: 华为s5700(v5.110)"""
	c物理地址 = 0
	c虚拟局域网 = 15
	c接口 = 49
	c类型 = 69
	ca列 = 数据表.C切割列(c物理地址, c虚拟局域网, c接口, c类型)
	c标题行0 = "MAC Address    VLAN/VSI                          Learned-From        Type      "
	c标题行1 = "-------------------------------------------------------------------------------"
	def __init__(self):
		数据表.I解析表格管线.__init__(self)
		self.f添加字段(数据表.E字段.e对端物理地址, self.ca列[0], 地址.S物理地址.fc字符串)
		self.f添加字段(数据表.E字段.e本端虚拟局域网, self.ca列[1], lambda x: int(x[:x.find("/")]))
		self.f添加字段(数据表.E字段.e本端接口, self.ca列[2], 实现接口.f创建接口缩写)
		self.f添加字段(数据表.E字段.e对端物理地址类型, self.ca列[3], 信息.ca物理地址类型.get)
	f初始处理 = staticmethod(数据表.F去标题行(c标题行0, c标题行1))
	fi有效行 = staticmethod(数据表.F有效长度(c类型))	
	@staticmethod
	def fi结束(a行: str):
		return "--" in a行
f物理地址表 = F物理地址表()
class F物理地址表2(数据表.I解析表格管线):
	"""display mac-address
	适用于: 华为s5700(模拟器)"""
	c物理地址 = 0
	c虚拟局域网 = 15
	PEVLAN = 27	#?
	CEVLAN = 34	#?
	c接口 = 41
	c类型 = 57
	LSP = 67	#?
	ca列 = 数据表.C切割列(c物理地址, c虚拟局域网, PEVLAN, CEVLAN, c接口, c类型, LSP)
	c标题行0 = "MAC Address    VLAN/       PEVLAN CEVLAN Port            Type      LSP/LSR-ID  "
	c标题行1 = "               VSI/SI                                              MAC-Tunnel  "
	c标题行2 = "-------------------------------------------------------------------------------"
	def __init__(self):
		数据表.I解析表格管线.__init__(self)
		self.f添加字段(数据表.E字段.e对端物理地址, self.ca列[0], 地址.S物理地址.fc字符串)
		self.f添加字段(数据表.E字段.e本端虚拟局域网, self.ca列[1], int)
		self.f添加字段(数据表.E字段.e本端接口, self.ca列[4], 实现接口.f创建接口缩写)
		self.f添加字段(数据表.E字段.e对端物理地址类型, self.ca列[5], 信息.ca物理地址类型.get)
	f初始处理 = staticmethod(数据表.F去标题行(c标题行0, c标题行1, c标题行2))
	fi有效行 = staticmethod(数据表.F有效长度(LSP))	
	@staticmethod
	def fi结束(a行: str):
		return "--" in a行
f物理地址表2 = F物理地址表2()
class F物理地址表ar(F物理地址表):
	"""display mac-address
	适用于: 华为ar201(模拟器)"""
	c物理地址 = 0
	c虚拟局域网 = 18
	c接口 = 42
	c类型 = 69
	ca列 = 数据表.C切割列(c物理地址, c虚拟局域网, c接口, c类型)
	c标题行0 = "MAC Address       VLAN/Bridge             Learned-From               Type      "
	c标题行1 = "-------------------------------------------------------------------------------"
	f初始处理 = staticmethod(数据表.F去标题行(c标题行0, c标题行1))
f物理地址表ar = F物理地址表ar()