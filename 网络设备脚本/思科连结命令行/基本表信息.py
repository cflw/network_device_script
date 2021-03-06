import cflw代码库py.cflw字符串 as 字符串
import cflw代码库py.cflw工具_运算 as 运算
import cflw代码库py.cflw网络地址 as 地址
from ..基础接口 import 数据表
from ..基础接口 import 信息
from . import 接口 as 实现接口
#===============================================================================
# 接口表
#===============================================================================
class C物理接口表nv7:	#需重写
	"""show interface brief 的其中一部分
	适用于: 思科nexus9000(v7.x), 浪潮cn8672(v7.x),浪潮cn8696q(v7.x)"""
	c接口 = 0
	c虚拟局域网 = 14
	c类型 = 22	#eth
	c链路类型 = 27	#access/trunk/routed
	c状态 = 34	#up/down
	c原因 = 42
	c速率 = 67
	c聚合组 = 77
	c标题行0 = "Ethernet      VLAN    Type Mode   Status  Reason                   Speed     Port"
	c标题行1 = "Interface                                                                    Ch #"
	ca列开始 = (c接口, c虚拟局域网, c类型, c链路类型, c状态, c原因, c速率, c聚合组)
	@staticmethod
	def f解析行(a行):
		v接口s, v虚拟局域网s, v类型s, v链路类型s, v状态s, v原因s, v速率s, v聚合组s = 字符串.fe按位置分割(a行, *C物理接口表nv7.ca列开始)
class C链路聚合接口表nv7:
	"""show interface brief 的其中一部分
	适用于: 浪潮cn8672(v7.x),浪潮cn8696q(v7.x)"""
	c接口 = 0
	c虚拟局域网 = 14
	c类型 = 22	#eth
	c链路类型 = 27	#access/trunk/routed
	c状态 = 34	#up/down
	c原因 = 42
	c速率 = 67
	c协议 = 77	#lacp/none
	c标题行0 = "Port-channel VLAN    Type Mode   Status  Reason                    Speed   Protocol"
	c标题行1 = "Interface                                                                  "
	ca列开始 = (c接口, c虚拟局域网, c类型, c链路类型, c状态, c原因, c速率, c协议)
	@staticmethod
	def f解析行(a行):
		v接口s, v虚拟局域网s, v类型s, v链路类型s, v状态s, v原因s, v速率s, v协议s = 字符串.fe按位置分割(a行, *C物理接口表nv7.ca列开始)
class C管理口表nv7:
	"""show interface brief 的其中一部分
	适用于: 浪潮cn8672(v7.x),浪潮cn8696q(v7.x)"""
	c接口 = 0
	c虚拟路由转发 = 7
	c状态 = 20
	c网络地址 = 27
	c速率 = 67
	c最大传输单元 = 76
	ca列开始 = (c接口, c虚拟路由转发, c状态, c网络地址, c速率, c最大传输单元)
	c标题行 = "Port   VRF          Status IP Address                              Speed    MTU"
	@staticmethod
	def f解析行(a行):
		v接口s, v虚拟路由转发s, v状态s, v网络地址s, v速率s, v最大传输单元s = 字符串.fe按位置分割(a行, *C管理口表nv7.ca列开始)
class C虚拟局域网口表nv7:
	"""show interface brief 的其中一部分"""
	c接口 = 0
	c次要 = 10
	c类型 = 20
	c状态 = 50
	c原因 = 57
	ca列开始 = (c接口, c次要, c类型, c状态, c原因)
	c标题行 = "Interface Secondary VLAN(Type)                    Status Reason                 "
#===============================================================================
# 网络接口表
#===============================================================================
class F网络接口表nv7(数据表.I解析表格管线):
	"""show ip interface brief
	适用于: 浪潮cn8672(v7.x), 浪潮cn8696q(v7.x)"""
	c接口 = 0
	c地址 = 21
	c状态 = 37
	ca列 = 数据表.C切割列(c接口, c地址, c状态)
	c标题行 = "Interface            IP Address      Interface Status"
	def __init__(self):
		数据表.I解析表格管线.__init__(self)
		self.f添加字段(数据表.E字段.e本端接口, self.ca列[0], 实现接口.f创建接口nv7)
		self.f添加字段(数据表.E字段.e本端网络地址4, self.ca列[1], 地址.S网络地址4.fc主机地址字符串)
		self.f添加字段(数据表.E字段.e本端协议状态, self.Fg状态(0), 信息.f解析起宕状态)
		self.f添加字段(数据表.E字段.e本端链路状态, self.Fg状态(1), 信息.f解析起宕状态)
		self.f添加字段(数据表.E字段.e本端管理状态, self.Fg状态(2), 信息.f解析起宕状态)
	f初始处理 = staticmethod(数据表.F去标题行(c标题行))
	f取状态列 = staticmethod(ca列[2])
	@staticmethod
	def Fg状态(a序号: int):
		def fg状态(a行: str):
			v状态s = F网络接口表nv7.f取状态列(a行)
			return v状态s.split("/")[a序号]
		return fg状态
f网络接口表nv7 = F网络接口表nv7()
#===============================================================================
# 物理地址表
#===============================================================================
class F物理地址表nv7(数据表.I解析表格管线):
	"""show mac address-table
	适用于: 浪潮cn8672(v7.x),浪潮cn8696q(v7.x)"""
	c选项 = 0
	c虚拟局域网 = 2
	c物理地址 = 11
	c类型 = 29	#dynamic/static
	c寿命 = 39
	c安全 = 50
	nfty = 55	#不知道是什么
	c端口 = 58
	ca列 = 数据表.C切割列(c选项, c虚拟局域网, c物理地址, c类型, c寿命, c安全, nfty, c端口)
	c标题行0 = "   VLAN     MAC Address      Type      age     Secure NTFY   Ports/SWID.SSID.LID"
	c标题行1 = "---------+-----------------+--------+---------+------+----+------------------"
	def __init__(self):
		数据表.I解析表格管线.__init__(self)
		self.f添加字段(数据表.E字段.e本端虚拟局域网, self.ca列[1], int)
		self.f添加字段(数据表.E字段.e对端物理地址, self.ca列[2], 地址.S物理地址.fc字符串)
		self.f添加字段(数据表.E字段.e对端物理地址类型, self.ca列[3], 信息.f解析物理地址类型)
	f初始处理 = staticmethod(数据表.F去标题行(c标题行0, c标题行1))
class F物理地址表nv9(F物理地址表nv7):
	"""show mac address-table
	适用于: 浪潮cn61108pc-v(v9.2.3)"""
	c选项 = 0
	c虚拟局域网 = 2
	c物理地址 = 11
	c类型 = 28	#dynamic/static
	c寿命 = 37
	c安全 = 47
	nfty = 54	#不知道是什么
	c端口 = 59
	ca列 = 数据表.C切割列(c选项, c虚拟局域网, c物理地址, c类型, c寿命, c安全, nfty, c端口)
	c标题行0 = "   VLAN     MAC Address      Type      age     Secure NTFY Ports"
	c标题行1 = "---------+-----------------+--------+---------+------+----+------------------"
	f初始处理 = staticmethod(数据表.F去标题行(c标题行0, c标题行1))
f物理地址表nv7 = F物理地址表nv7()
f物理地址表nv9 = F物理地址表nv9()