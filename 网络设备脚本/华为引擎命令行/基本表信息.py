import cflw代码库py.cflw字符串 as 字符串
import cflw代码库py.cflw网络地址 as 地址
from ..基础接口 import 信息
from ..基础接口 import 接口 as 北向接口
from ..基础接口 import 数据表
from ..华为命令行 import 接口 as 实现接口
#===============================================================================
# 接口详细
#===============================================================================
class F接口详细ne(数据表.I解析列表管线):
	"""display interface
	适用于: 华为ne9000(模拟器)"""
	c接口状态正则 = r"current state : (.+?)\s"
	c协议状态正则 = r"Line protocol current state : (.+?)\s"
	c描述 = "Description"
	c最大传输单元 = "Maximum Transmit Unit is"
	c网络地址 = "Internet Address is"
	c物理地址 = "Hardware address is"
	c虚拟局域网 = "Vlan is "
	c速率正则 = r"Speed :\s+?(.+?),"	#需要修改
	c双工模式正则 = r"Duplex:\s+?(.+?),"	#需要修改
	c接收正则 = r"Last 300 seconds input rate:? (\d+) bits/sec, (\d+) packets/sec"
	c发送正则 = r"Last 300 seconds output rate:? (\d+) bits/sec, (\d+) packets/sec"
	c接收带宽 = "Last 300 seconds input utility rate"
	c发送带宽 = "Last 300 seconds output utility rate"
	def __init__(self):
		数据表.I解析列表管线.__init__(self)
		self.f添加字段(数据表.E字段.e本端接口, 数据表.F正则字段(北向接口.c接口正则, 0), 实现接口.f创建接口)
		self.f添加字段(数据表.E字段.e本端管理状态, 数据表.F正则字段(self.c接口状态正则, 1), 信息.f解析起宕状态)
		self.f添加字段(数据表.E字段.e本端协议状态, 数据表.F正则字段(self.c协议状态正则, 1), 信息.f解析起宕状态)
		self.f添加字段(数据表.E字段.e本端描述, 数据表.F列表字段(self.c描述), str)
		self.f添加字段(数据表.E字段.e本端最大传输单元, 数据表.F列表字段(self.c最大传输单元, a分隔符 = None), int)
		self.f添加字段(数据表.E字段.e本端网络地址4, 数据表.F列表字段(self.c网络地址, a分隔符 = None), self.f解析网络地址4)
		self.f添加字段(数据表.E字段.e本端物理地址, 数据表.F列表字段(self.c物理地址, a分隔符 = None), 地址.S物理地址.fc字符串)
		self.f添加字段(数据表.E字段.e本端虚拟局域网, 数据表.F列表字段(self.c虚拟局域网, a分隔符 = None, a结束 = ','), int)
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
	@staticmethod
	def f解析网络地址4(a文本: str):
		v括号位置 = a文本.find('(')
		if v括号位置 >= 0:	#有括号,可能使用了其他接口地址
			v结束位置 = a文本.find(')', v括号位置)
			v地址s = a文本[v括号位置+1 : v结束位置]
			return 地址.S网络地址4.fc地址前缀长度字符串(v地址s)
		else:	#无括号
			return 地址.S网络地址4.fc地址前缀长度字符串(a文本)
f接口详细ne = F接口详细ne()
class F接口详细ce(数据表.I解析列表管线):
	"""display interface
	适用于: 华为ce6800(模拟器)"""
	c接口状态正则 = r"current state : (.+?)\s"
	c协议状态正则 = r"Line protocol current state : (.+?)\s"
	c描述 = "Description"
	c物理地址正则 = r"Hardware address is (.+?)\s"
	c速率正则 = r"Speed :\s+?(.+?),"	#需要修改
	c双工模式正则 = r"Duplex:\s+?(.+?),"	#需要修改
	c接收正则 = r"Last 300 seconds input rate:? (\d+) bits/sec, (\d+) packets/sec"
	c发送正则 = r"Last 300 seconds output rate:? (\d+) bits/sec, (\d+) packets/sec"
	c接收带宽 = "Last 300 seconds input utility rate"
	c发送带宽 = "Last 300 seconds output utility rate"
	def __init__(self):
		数据表.I解析列表管线.__init__(self)
		self.f添加字段(数据表.E字段.e本端接口, 数据表.F正则字段(北向接口.c接口正则, 0), 实现接口.f创建接口缩写)
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
f接口详细ce = F接口详细ce()
#===============================================================================
# 物理接口表
#===============================================================================
class F接口表ne(数据表.I解析表格管线):
	"""display interface brief
	适用于: 华为ne40e(v8.180)"""
	c接口 = 0
	c物理 = 28
	c协议 = 35
	c输入率 = 44
	c输出率 = 50
	c输入错误 = 59
	c输出错误 = 69
	ca列 = 数据表.C切割列(c接口, c物理, c协议, c输入率, c输出率, c输入错误, c输出错误)
	c标题行0 = "Interface                   PHY   Protocol  InUti OutUti   inErrors  outErrors"
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
f接口表ne = F接口表ne()
class F接口表ce(数据表.I解析表格管线):
	"""display interface brief
	适用于: 华为ce6800(模拟器)"""
	c接口 = 0
	c物理 = 27
	c协议 = 36
	c输入率 = 46
	c输出率 = 52
	c输入错误 = 61
	c输出错误 = 71
	ca列 = 数据表.C切割列(c接口, c物理, c协议, c输入率, c输出率, c输入错误, c输出错误)
	c标题行0 = "Interface                  PHY      Protocol  InUti OutUti   inErrors  outErrors"
	def __init__(self):
		数据表.I解析表格管线.__init__(self)
		self.f添加字段(数据表.E字段.e本端接口, self.ca列[0], 实现接口.f创建接口缩写)
		self.f添加字段(数据表.E字段.e本端链路状态, self.ca列[1], 信息.f解析起宕状态)
		self.f添加字段(数据表.E字段.e本端协议状态, self.ca列[2], 信息.f解析起宕状态)
		self.f添加字段(数据表.E字段.e本端接收利用率, self.ca列[3], 信息.f解析数字)
		self.f添加字段(数据表.E字段.e本端发送利用率, self.ca列[4], 信息.f解析数字)
		self.f添加字段(数据表.E字段.e本端接收错误数, self.ca列[5], int)
		self.f添加字段(数据表.E字段.e本端发送错误数, self.ca列[6], int)
	f初始处理 = staticmethod(数据表.F去标题行(c标题行0))
	fi有效行 = staticmethod(数据表.F有效长度(len(c标题行0)))
f接口表ce = F接口表ce()
#===============================================================================
# 网络接口表
#===============================================================================
class F网络接口表4(数据表.I解析表格管线):
	"""display ip interface brief
	适用于: 华为ne40e(v8.180)"""
	c接口 = 0
	c地址 = 34
	c物理 = 55
	c协议 = 66
	c虚专网 = 75
	ca列 = 数据表.C切割列(c接口, c地址, c物理, c协议, c虚专网)
	c标题行0 = "Interface                         IP Address/Mask      Physical   Protocol VPN "
	def __init__(self):
		数据表.I解析表格管线.__init__(self)
		self.f添加字段(数据表.E字段.e本端接口, F网络接口表4.ca列[0], 实现接口.f创建接口)
		self.f添加字段(数据表.E字段.e本端网络地址4, F网络接口表4.ca列[1], 信息.f解析网络地址4)
		self.f添加字段(数据表.E字段.e本端链路状态, F网络接口表4.ca列[2], 信息.f解析起宕状态)
		self.f添加字段(数据表.E字段.e本端协议状态, F网络接口表4.ca列[3], 信息.f解析起宕状态)
		self.f添加字段(数据表.E字段.e本端虚拟路由转发, F网络接口表4.ca列[4], str)
	f初始处理 = staticmethod(数据表.F去标题行(c标题行0))
	fi有效行 = staticmethod(数据表.F有效长度(c虚专网))
f网络接口表4 = F网络接口表4()
#===============================================================================
# 地址解析表
#===============================================================================
ca地址解析类型 = {
	"D": 信息.E地址解析协议类型.e动态,
	"S": 信息.E地址解析协议类型.e静态,
	"I": 信息.E地址解析协议类型.e接口,
}
class F地址解析表ne(数据表.I解析多行表格管线):
	"""display arp all
	适用于: 华为ne40e(v8.180)"""
	c网络地址 = 0
	c物理地址 = 16
	c过期 = 32	#单位:分钟
	c类型 = 42
	c接口 = 47	#缩写
	c虚拟路由转发 = 62	#可能0个字符
	ca列 = 数据表.C切割列(c网络地址, c物理地址, c过期, c类型, c接口, c虚拟路由转发)
	c标题行0 = "IP ADDRESS      MAC ADDRESS     EXPIRE(M) TYPE        INTERFACE   VPN-INSTANCE"
	c标题行1 = "                                          VLAN/CEVLAN PVC"
	c标题行2 = "----------------------------------------------------------------------------------------"
	def __init__(self):
		数据表.I解析多行表格管线.__init__(self)
		self.m行0 = 数据表.C行()	#基础行
		self.m行0.f添加字段(数据表.E字段.e对端网络地址4, self.ca列[0], 地址.S网络地址4.fc主机地址字符串)
		self.m行0.f添加字段(数据表.E字段.e对端物理地址, self.ca列[1], 地址.S物理地址.fc字符串)
		self.m行0.f添加字段(数据表.E字段.e本端寿命, self.ca列[2], lambda x: 信息.f解析数字(x) * 60)
		self.m行0.f添加字段(数据表.E字段.e本端地址解析协议类型, self.fg类型, ca地址解析类型.get)
		self.m行0.f添加字段(数据表.E字段.e本端接口, self.ca列[4], 实现接口.f创建接口缩写)
		self.m行1 = 数据表.C行()	#vlan行
		self.m行1.f添加字段(数据表.E字段.e本端虚拟局域网, self.fg虚拟局域网, int)
		self.m行 = 0	#决定使用行0还是行1来解析
	def f解析行(self, a行: str):
		if self.m行:	#1
			return self.m行1.f解析(a行)
		else:	#0
			self.m行 += 1
			return self.m行0.f解析(a行)
	f初始处理 = staticmethod(数据表.F去标题行(c标题行0, c标题行1, c标题行2))
	fi结束 = staticmethod(lambda a行: "--" in a行)
	def fi有效行(self, a行: str):
		return len(a行) >= self.c类型
	def fi新记录(self, a行: str):
		v结果 = a行[0] != ' '
		if v结果:
			self.m行 = 0
		return v结果
	def fg类型(self, a行: str):
		return a行[self.c类型]
	def fg虚拟局域网(self, a行: str):
		return a行[self.c类型: a行.find("/", self.c类型)]
f地址解析表ne = F地址解析表ne()
class F地址解析表ce(数据表.I解析表格管线):
	"""display arp
	适用于: 华为ce6800(模拟器)"""
	c网络地址 = 0
	c物理地址 = 16
	c寿命 = 33	#可能空
	c类型 = 38
	c接口 = 48
	c虚专网 = 64	#可能空
	ca列 = 数据表.C切割列(c网络地址, c物理地址, c寿命, c类型, c接口, c虚专网)
	c标题行0 = "IP ADDRESS      MAC ADDRESS    EXP(M) TYPE/VLAN INTERFACE       VPN-INSTANCE"
	c标题行1 = "------------------------------------------------------------------------------"
	def __init__(self):
		数据表.I解析表格管线.__init__(self)
		self.f添加字段(数据表.E字段.e对端网络地址4, self.ca列[0], 地址.S网络地址4.fc主机地址字符串)
		self.f添加字段(数据表.E字段.e对端物理地址, self.ca列[1], 地址.S物理地址.fc字符串)
		self.f添加字段(数据表.E字段.e本端寿命, self.ca列[2], lambda x: int(x or 0) * 60)
		self.f添加字段(数据表.E字段.e本端地址解析协议类型, self.fg类型, ca地址解析类型.get)
		self.f添加字段(数据表.E字段.e本端虚拟局域网, self.fg虚拟局域网, int)
		self.f添加字段(数据表.E字段.e本端接口, self.ca列[4], 实现接口.f创建接口缩写)
		self.f添加字段(数据表.E字段.e本端虚拟路由转发, self.ca列[5], str)
	def fg类型(self, a行: str):
		v列 = self.ca列[3](a行)
		return v列.split('/')[0]
	def fg虚拟局域网(self, a行: str):
		v列 = self.ca列[3](a行)
		v分割 = v列.split('/')
		return v分割[1] if len(v分割) > 1 else 0
	f初始处理 = staticmethod(数据表.F去标题行(c标题行0, c标题行1))
	fi结束 = staticmethod(lambda a行: "--" in a行)
f地址解析表ce = F地址解析表ce()
#===============================================================================
# 物理地址表
#===============================================================================
class F物理地址表ce(数据表.I解析表格管线):
	"""display mac-address
	适用于: 华为ce6800(模拟器)"""
	c物理地址 = 0
	c虚拟局域网 = 15
	c接口 = 29
	c类型 = 49
	c寿命 = 69
	ca列 = 数据表.C切割列(c物理地址, c虚拟局域网, c接口, c类型, c寿命)
	c标题行0 = "MAC Address    VLAN/VSI/BD   Learned-From        Type                Age"
	c标题行1 = "-------------------------------------------------------------------------------"
	def __init__(self):
		数据表.I解析表格管线.__init__(self)
		self.f添加字段(数据表.E字段.e对端物理地址, self.ca列[0], 地址.S物理地址.fc字符串)
		self.f添加字段(数据表.E字段.e本端虚拟局域网, self.ca列[1], lambda x: int(x.split('/')[0]))
		self.f添加字段(数据表.E字段.e本端接口, self.ca列[2], 实现接口.f创建接口缩写)
		self.f添加字段(数据表.E字段.e对端物理地址类型, self.ca列[3], 信息.ca物理地址类型.get)
		self.f添加字段(数据表.E字段.e本端寿命, self.ca列[4], 信息.f解析数字)
	f初始处理 = staticmethod(数据表.F去标题行(c标题行0, c标题行1))
	fi结束 = staticmethod(lambda a行: "--" in a行)
f物理地址表ce = F物理地址表ce()