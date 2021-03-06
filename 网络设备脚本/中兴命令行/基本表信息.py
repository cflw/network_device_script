import cflw代码库py.cflw字符串 as 字符串
import cflw代码库py.cflw网络地址 as 地址
from ..基础接口 import 信息
from ..基础接口 import 数据表
from . import 接口 as 实现接口
#===============================================================================
# 网络接口表
#===============================================================================
def f解析网络地址4(a地址: str):
	if "unassigned" in a地址:
		return None
	else:
		return 地址.S网络地址4.fc地址掩码(*a地址.split())
class F网络接口表4(数据表.I解析表格管线):
	"""show ip interface brief
	适用于: ZXR10 M6000(V3.00.10(2.70.1))"""
	c接口 = 0
	c地址 = 32
	c掩码 = 48
	c管理 = 64
	c物理 = 70
	c协议 = 75
	ca列 = 数据表.C切割列(c接口, c地址, c管理, c物理, c协议)
	c标题行 = "Interface                       IP-Address      Mask            Admin Phy  Prot"
	def __init__(self):
		数据表.I解析表格管线.__init__(self)
		self.f添加字段(数据表.E字段.e本端接口, F网络接口表4.ca列[0], 实现接口.f创建接口m6000)
		self.f添加字段(数据表.E字段.e本端网络地址4, F网络接口表4.ca列[1], f解析网络地址4)
		self.f添加字段(数据表.E字段.e本端管理状态, F网络接口表4.ca列[2], 信息.f解析起宕状态)
		self.f添加字段(数据表.E字段.e本端链路状态, F网络接口表4.ca列[3], 信息.f解析起宕状态)
		self.f添加字段(数据表.E字段.e本端协议状态, F网络接口表4.ca列[4], 信息.f解析起宕状态)
	f初始处理 = staticmethod(数据表.F去标题行(c标题行))
	@staticmethod
	def fi有效行(a行):
		if len(a行) < F网络接口表4.c协议:
			return False
		elif a行[F网络接口表4.c地址-1] != " ":
			return False
		elif a行[F网络接口表4.c协议-1] != " ":
			return False
		return True
f网络接口表4 = F网络接口表4()
#===============================================================================
# 接口表
#===============================================================================
class F接口表(数据表.I解析表格管线):
	"""show interface brief
	适用于: ZXR10 M6000(V3.00.10(2.70.1))"""
	c接口 = 0	#Interface
	c光电属性 = 15	#Portattribute
	c模式 = 26	#Mode
	c速率 = 39	#BW(Mbps)
	c管理 = 46	#Admin
	c物理 = 52	#Phy
	c协议 = 58	#Prot
	c描述 = 64	#Description
	ca列 = 数据表.C切割列(c接口, c光电属性, c模式, c速率, c管理, c物理, c协议, c描述)
	c标题行 = "Interface      Portattribute  Mode  BW(Mbps)  Admin Phy   Prot  Description"
	def __init__(self):
		数据表.I解析表格管线.__init__(self)
		self.f添加字段(数据表.E字段.e本端接口, F接口表.ca列[0], 实现接口.f创建接口m6000)
		self.f添加字段(数据表.E字段.e本端双工模式, F接口表.ca列[2], 信息.f解析双工模式)
		self.f添加字段(数据表.E字段.e本端速率, F接口表.ca列[3], int)
		self.f添加字段(数据表.E字段.e本端管理状态, F接口表.ca列[4], 信息.f解析起宕状态)
		self.f添加字段(数据表.E字段.e本端链路状态, F接口表.ca列[5], 信息.f解析起宕状态)
		self.f添加字段(数据表.E字段.e本端协议状态, F接口表.ca列[6], 信息.f解析起宕状态)
		self.f添加字段(数据表.E字段.e本端描述, F接口表.ca列[7], str)
	f初始处理 = staticmethod(数据表.F去标题行(c标题行))
	@staticmethod
	def fi有效行(a行):
		if len(a行) < F接口表.c描述:
			return False
		elif a行[F接口表.c光电属性-1] != " ":
			return False
		elif a行[F接口表.c模式-1] != " ":
			return False
		return True
f接口表 = F接口表()
#===============================================================================
# 地址解析表
#===============================================================================
def f解析时间(a时间: str):	#hh:mm:ss 格式
	v时, v分, v秒 = (int(x) for x in a时间.split(":"))
	return v时 * 3600 + v分 * 60 + v秒
def f解析虚拟局域网(a: str):
	if "N/A" in a:
		return 0
	else:
		return int(a)
class F地址解析表(数据表.I解析表格管线):
	"""show arp
	适用于: ZXR10 M6000(V3.00.10(2.70.1))"""
	c网络地址 = 0
	c寿命 = 16
	c物理地址 = 25
	c接口 =  40
	c外部虚拟局域网 = 53
	c内部虚拟局域网 = 60
	c子接口 = 67
	ca列 = 数据表.C切割列(c网络地址, c寿命, c物理地址, c接口, c外部虚拟局域网, c内部虚拟局域网, c子接口)
	c标题行0 = "IP                       Hardware                    Exter  Inter  Sub"
	c标题行1 = "Address         Age      Address        Interface    VlanID VlanID Interface"
	c标题行2 = "--------------------------------------------------------------------------------"
	def __init__(self):
		数据表.I解析表格管线.__init__(self)
		self.f添加字段(数据表.E字段.e对端网络地址4, F地址解析表.ca列[0], 地址.S网络地址4.fc主机地址字符串)
		self.f添加字段(数据表.E字段.e对端物理地址, F地址解析表.ca列[2], 地址.S物理地址.fc字符串)
		self.f添加字段(数据表.E字段.e对端寿命, F地址解析表.ca列[1], f解析时间)
		self.f添加字段(数据表.E字段.e本端接口, F地址解析表.ca列[3], 实现接口.f创建接口m6000)
		self.f添加字段(数据表.E字段.e本端虚拟局域网, F地址解析表.ca列[4], f解析虚拟局域网)
	f初始处理 = staticmethod(数据表.F去标题行(c标题行0, c标题行1, c标题行2))
	@staticmethod
	def fi有效行(a行):
		if len(a行) < F地址解析表.c子接口:
			return False
		if "H" in a行:	#寿命列有H表示接口自已
			return False
		return True
f地址解析表 = F地址解析表()