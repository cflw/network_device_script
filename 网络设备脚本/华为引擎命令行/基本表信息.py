import cflw代码库py.cflw字符串 as 字符串
import cflw代码库py.cflw网络地址 as 地址
from ..基础接口 import 信息
from ..基础接口 import 数据表
from ..华为命令行 import 接口 as 实现接口
#===============================================================================
# 物理接口表
#===============================================================================
class F接口表(数据表.I解析表格管线):
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
		self.f添加字段(数据表.E字段.e本端接口, F接口表.ca列[0], 实现接口.f创建接口)
		self.f添加字段(数据表.E字段.e本端链路状态, F接口表.ca列[1], 信息.f解析起宕状态)
		self.f添加字段(数据表.E字段.e本端协议状态, F接口表.ca列[2], 信息.f解析起宕状态)
		self.f添加字段(数据表.E字段.e本端接收利用率, F接口表.ca列[3], 信息.f解析数字)
		self.f添加字段(数据表.E字段.e本端发送利用率, F接口表.ca列[4], 信息.f解析数字)
		self.f添加字段(数据表.E字段.e本端接收错误数, F接口表.ca列[5], int)
		self.f添加字段(数据表.E字段.e本端发送错误数, F接口表.ca列[6], int)
	f初始处理 = staticmethod(数据表.F去标题行(c标题行0))
	fi有效行 = staticmethod(数据表.F有效长度(len(c标题行0)))
f接口表 = F接口表()
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
class F地址解析表(数据表.I解析多行表格管线):
	"""display arp
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
		self.m行0.f添加字段(数据表.E字段.e对端网络地址4, F地址解析表.ca列[0], 地址.S网络地址4.fc主机地址字符串)
		self.m行0.f添加字段(数据表.E字段.e对端物理地址, F地址解析表.ca列[1], 地址.S物理地址.fc字符串)
		self.m行0.f添加字段(数据表.E字段.e本端寿命, F地址解析表.ca列[2], lambda x: 信息.f解析数字(x) * 60)
		self.m行0.f添加字段(数据表.E字段.e本端地址解析协议类型, F地址解析表.fg类型, ca地址解析类型.get)
		self.m行0.f添加字段(数据表.E字段.e本端接口, F地址解析表.ca列[4], 实现接口.f创建接口缩写)
		self.m行1 = 数据表.C行()	#vlan行
		self.m行1.f添加字段(数据表.E字段.e本端虚拟局域网, F地址解析表.fg虚拟局域网, int)
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
	fg虚拟局域网 = staticmethod(lambda x: x[F地址解析表.c类型: x.find("/", F地址解析表.c类型)])
f地址解析表 = F地址解析表()
