import cflw代码库py.cflw字符串 as 字符串
import cflw代码库py.cflw工具_序列 as 序列
import cflw代码库py.cflw工具_运算 as 运算
import cflw代码库py.cflw网络地址 as 地址
from ..基础接口 import 数据表
from ..基础接口 import 信息
from . import 接口 as 实现接口
class C物理接口表nv7:
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
class C网络接口表nv7:
	"""show ip interface brief
	适用于: 浪潮cn8672(v7.x),浪潮cn8696q(v7.x)"""
	c接口 = 0
	c地址 = 21
	c状态 = 37
	ca列开始 = (c接口, c地址, c状态)
	c标题行 = "Interface            IP Address      Interface Status"
	def __init__(self, a文本):
		v位置 = 字符串.f连续找最后(a文本, C网络接口表nv7.c标题行, "\n")
		self.m文本 = a文本[v位置 + 1 :]
	def __iter__(self):
		return self.fe行()
	def fe行(self):
		for v行 in self.m文本.split("\n"):
			v接口s, v地址s, v状态s = 字符串.fe按位置分割(v行, *C网络接口表nv7.ca列开始)
			v协议状态s, v链路状态s, v管理状态s = 序列.f映射(str.strip, v状态s.split("/"))
			v接口 = 实现接口.f创建接口nv7(v接口s)
			v地址 = 地址.S网络地址4.fc自动(v地址s)
			v协议状态 = "-up" in v协议状态s
			v链路状态 = "-up" in v链路状态s
			v管理状态 = "-up" in v管理状态s
			yield 数据表.C记录({
				数据表.E字段.e本端接口: v接口,
				数据表.E字段.e本端网络地址4: v地址,
				数据表.E字段.e本端协议状态: v协议状态,
				数据表.E字段.e本端链路状态: v链路状态,
				数据表.E字段.e本端管理状态: v管理状态,
			})
class C物理地址表nv7:
	"""show mac address-table
	适用于: 浪潮cn8672(v7.x),浪潮cn8696q(v7.x)"""
	c选项 = 0
	c虚拟局域网 = 2
	c物理地址 = 11
	c类型 = 21	#dynamic/static
	c寿命 = 39
	c安全 = 50
	nfty = 55	#不知道是什么
	c端口 = 58
	ca列开始 = (c选项, c虚拟局域网, c物理地址, c类型, c安全, nfty, c端口)
	c标题行0 = "   VLAN     MAC Address      Type      age     Secure NTFY   Ports/SWID.SSID.LID"
	c标题行1 = "---------+-----------------+--------+---------+------+----+------------------"
	def __init__(self, a文本):
		v位置 = 字符串.f连续找最后(a文本, C物理地址表nv7.c标题行0, C物理地址表nv7.c标题行1, "\n")
		self.m文本 = a文本[v位置 + 1 :]
	def __iter__(self):
		return self.fe行()
	def fe行(self):
		for v行 in self.m文本.split("\n"):
			v选项s, v虚拟局域网s, v物理地址s, v类型s, v寿命s, v安全s, v6_, v端口s = 字符串.fe按位置分割(v行, *C物理地址表nv7.ca列开始)
			v虚拟局域网 = int(v虚拟局域网s)
			v物理地址 = 地址.S物理地址.fc自动(v物理地址s)
			yield 数据表.C记录({
				数据表.E字段.e本端虚拟局域网: v虚拟局域网,
				数据表.E字段.e本端物理地址: v物理地址,
			})
