import cflw代码库py.cflw字符串 as 字符串
import cflw代码库py.cflw工具_运算 as 运算
import cflw代码库py.cflw网络地址 as 地址
from ..基础接口 import 数据表
from ..基础接口 import 信息
from . import 接口 as 实现接口
#===============================================================================
# 接口表
#===============================================================================
class F物理接口表_nv7(数据表.I解析表格管线):
	"""show interface brief 的其中一部分
	适用于: 浪潮cn8672up(v7.3), 浪潮cn8696q(v7.3), 浪潮cn61108pcv(v9.2.3)"""
	c接口 = 0
	c虚拟局域网 = 14
	c类型 = 22	#eth
	c链路类型 = 27	#access/trunk/routed
	c状态 = 34	#up/down
	c原因 = 42
	c速率 = 67
	c聚合组 = 77
	ca列 = 数据表.C切割列(c接口, c虚拟局域网, c类型, c链路类型, c状态, c原因, c速率, c聚合组)
	c标题行0 = "Ethernet      VLAN    Type Mode   Status  Reason                   Speed     Port"
	c标题行1 = "Interface                                                                    Ch #"
	c标题行2 = "--------------------------------------------------------------------------------"
	c数据行0 = "Eth1/1        1       eth  trunk  up      none                       1000(D) --"
	def __init__(self):
		数据表.I解析表格管线.__init__(self)
		self.f添加字段(数据表.E字段.e本端接口, self.ca列[0], 实现接口.f创建接口_nv7)
		self.f添加字段(数据表.E字段.e本端虚拟局域网, self.ca列[1], 信息.f解析数字)
		self.f添加字段(数据表.E字段.e本端链路类型, self.ca列[3], 信息.f解析链路类型)
		self.f添加字段(数据表.E字段.e本端链路状态, self.ca列[4], 信息.f解析起宕状态)
		self.f添加字段(数据表.E字段.e本端速率, self.ca列[6], 信息.f解析速率)
		self.f添加字段(数据表.E字段.e本端链路聚合组, self.ca列[7], 信息.f解析数字)
	f初始处理 = staticmethod(数据表.F去标题行(c标题行0, c标题行1, c标题行2))
	fi结束 = staticmethod(数据表.fi空行)
f物理接口表_nv7 = F物理接口表_nv7()
class F链路聚合接口表_nv7(数据表.I解析表格管线):
	"""show interface brief 的其中一部分
	适用于: 浪潮cn8672up(v7.3), 浪潮cn8696q(v7.3), 浪潮cn61108pcv(v9.2.3)"""
	c接口 = 0
	c虚拟局域网 = 13
	c类型 = 21	#eth
	c链路类型 = 26	#access/trunk/routed
	c状态 = 33	#up/down
	c原因 = 41
	c速率 = 68
	c协议 = 78	#lacp/none
	ca列 = 数据表.C切割列(c接口, c虚拟局域网, c类型, c链路类型, c状态, c原因, c速率, c协议)
	c标题行0 = "Port-channel VLAN    Type Mode   Status  Reason                    Speed   Protocol"
	c标题行1 = "Interface                                                                  "
	c标题行2 = "--------------------------------------------------------------------------------"
	c数据行0 = "Po1          1       eth  trunk  up      none                       a-40G(D)  lacp"
	def __init__(self):
		数据表.I解析表格管线.__init__(self)
		self.f添加字段(数据表.E字段.e本端接口, self.ca列[0], 实现接口.f创建接口_nv7)
		self.f添加字段(数据表.E字段.e本端虚拟局域网, self.ca列[1], 信息.f解析数字)
		self.f添加字段(数据表.E字段.e本端链路类型, self.ca列[3], 信息.f解析链路类型)
		self.f添加字段(数据表.E字段.e本端链路状态, self.ca列[4], 信息.f解析起宕状态)
		self.f添加字段(数据表.E字段.e本端速率, self.ca列[6], 信息.f解析速率)
		self.f添加字段(数据表.E字段.e本端链路聚合协议, self.ca列[7], 信息.f解析链路聚合协议)
	f初始处理 = staticmethod(数据表.F去标题行(c标题行0, c标题行1, c标题行2))
	fi结束 = staticmethod(数据表.fi空行)
f链路聚合接口表_nv7 = F链路聚合接口表_nv7()
class F链路聚合接口表_nv9(F链路聚合接口表_nv7):
	"""适用于: 浪潮cn8696q(v7.3), 浪潮cn61108pcv(v9.2.3)"""
	c接口 = 0
	c虚拟局域网 = 13
	c类型 = 21	#eth
	c链路类型 = 26	#access/trunk/routed
	c状态 = 33	#up/down
	c原因 = 41
	c速率 = 77
	c协议 = 85	#lacp/none
	ca列 = 数据表.C切割列(c接口, c虚拟局域网, c类型, c链路类型, c状态, c原因, c速率, c协议)
	c标题行0 = "Port-channel VLAN    Type Mode   Status  Reason                              Speed   Protocol"
	c标题行1 = "Interface                                                                            "
	c标题行2 = "------------------------------------------------------------------------------------------"
	c数据行0 = "Po1          1       eth  trunk  up      none                                 a-40G(D)  lacp"	
	def __init__(self):
		F链路聚合接口表_nv7.__init__(self)
	f初始处理 = staticmethod(数据表.F去标题行(c标题行0, c标题行1, c标题行2))
f链路聚合接口表_nv9 = F链路聚合接口表_nv9()
class F管理接口表_nv7(数据表.I解析表格管线):
	"""show interface brief 的其中一部分
	适用于: 浪潮cn8672up(v7.3), 浪潮cn8696q(v7.3), 浪潮cn61108pcv(v9.2.3)"""
	c接口 = 0
	c虚拟路由转发 = 7
	c状态 = 20	#链路状态？up/down
	c网络地址 = 27
	c速率 = 67
	c最大传输单元 = 75
	ca列 = 数据表.C切割列(c接口, c虚拟路由转发, c状态, c网络地址, c速率, c最大传输单元)
	c标题行0 = "Port   VRF          Status IP Address                              Speed    MTU"
	c标题行1 = "--------------------------------------------------------------------------------"
	c数据行0 = "mgmt0  --           up     xxx.xxx.xxx.xxx                         1000     1500"
	def __init__(self):
		数据表.I解析表格管线.__init__(self)
		self.f添加字段(数据表.E字段.e本端接口, self.ca列[0], 实现接口.f创建接口_nv7)
		self.f添加字段(数据表.E字段.e本端虚拟路由转发, self.ca列[1], str)
		self.f添加字段(数据表.E字段.e本端链路状态, self.ca列[2], 信息.f解析起宕状态)
		self.f添加字段(数据表.E字段.e本端网络地址4, self.ca列[3], 信息.f解析网络地址4)
		self.f添加字段(数据表.E字段.e本端速率, self.ca列[4], int)
		self.f添加字段(数据表.E字段.e本端最大传输单元, self.ca列[5], int)
	f初始处理 = staticmethod(数据表.F去标题行(c标题行0, c标题行1))
	@staticmethod
	def fi结束(a行: str):
		return 数据表.fi空行(a行) or "---" in a行
f管理接口表_nv7 = F管理接口表_nv7()
class F虚拟局域网接口表_nv7(数据表.I解析表格管线):
	"""show interface brief 的其中一部分
	适用于: 浪潮cn8672up(v7.3), 浪潮cn8696q(v7.3), 浪潮cn61108pcv(v9.2.3)"""
	c接口 = 0
	c次要 = 10
	c类型 = 20
	c状态 = 50
	c原因 = 57
	ca列 = 数据表.C切割列(c接口, c次要, c类型, c状态, c原因)
	c标题行0 = "Interface Secondary VLAN(Type)                    Status Reason                 "
	c标题行1 = "-------------------------------------------------------------------------------"
	c数据行0 = "Vlan1     --                                      down   Administratively down  "
	def __init__(self):
		数据表.I解析表格管线.__init__(self)
		self.f添加字段(数据表.E字段.e本端接口, self.ca列[0], 实现接口.f创建接口_nv7)
		self.f添加字段(数据表.E字段.e本端协议状态, self.ca列[3], 信息.f解析起宕状态)
		self.f添加字段(数据表.E字段.e本端管理状态, self.ca列[4], 信息.f解析起宕状态)
	f初始处理 = staticmethod(数据表.F去标题行(c标题行0, c标题行1))
	fi结束 = staticmethod(数据表.fi空行)
f虚拟局域网接口表_nv7 = F虚拟局域网接口表_nv7()
#===============================================================================
# 接口状态表
#===============================================================================
class F接口状态表_nv7(数据表.I解析表格管线):
	"""show interface status
	适用于: 浪潮浪潮cn8696q(v7.3), 浪潮cn61108pcv(v9.2.3)"""
	c接口 = 0
	c描述 = 14
	c状态 = 33	#connected/notconnec/sfpAbsent/noOperMem/down
	c虚拟局域网 = 43	#数字/trunk/routed
	c双工 = 53	#full/auto
	c速率 = 61	#10G/40G/a-10G/1000/auto
	c类型 = 69	#10Gbase-SR/QSFP-40G-SR/--
	ca列 = 数据表.C切割列(c接口, c描述, c状态, c虚拟局域网, c双工, c速率, c类型)
	c标题行0 = "Port          Name               Status    Vlan      Duplex  Speed   Type"
	c标题行1 = "--------------------------------------------------------------------------------"
	c数据行0 = "Eth1/1        xxxxxxxxxxxxxxxxxx connected trunk     full    10G     10Gbase-SR "
	def __init__(self):
		数据表.I解析表格管线.__init__(self)
		self.f添加字段(数据表.E字段.e本端接口, self.ca列[0], 实现接口.f创建接口_nv7)
		self.f添加字段(数据表.E字段.e本端描述, self.ca列[1], str)
		self.f添加字段(数据表.E字段.e本端链路状态, self.ca列[2], lambda x: "connected" in x)
		self.f添加字段(数据表.E字段.e本端链路类型, self.ca列[3], 信息.f解析链路类型)
		self.f添加字段(数据表.E字段.e本端双工模式, self.ca列[4], 信息.f解析双工模式)
		self.f添加字段(数据表.E字段.e本端速率, self.ca列[5], 信息.f解析速率)
	f初始处理 = staticmethod(数据表.F去标题行(c标题行0, c标题行1))
	fi结束 = staticmethod(数据表.fi空行)
f接口状态表_nv7 = F接口状态表_nv7()
#===============================================================================
# 网络接口表4
#===============================================================================
class F网络接口表4_nv7(数据表.I解析表格管线):
	"""show ip interface brief
	适用于: 浪潮cn8672up(v7.*), 浪潮cn8696q(v7.3)"""
	c接口 = 0
	c地址 = 21
	c状态 = 37
	ca列 = 数据表.C切割列(c接口, c地址, c状态)
	c标题行 = "Interface            IP Address      Interface Status"
	def __init__(self):
		数据表.I解析表格管线.__init__(self)
		self.f添加字段(数据表.E字段.e本端接口, self.ca列[0], 实现接口.f创建接口_nv7)
		self.f添加字段(数据表.E字段.e本端网络地址4, self.ca列[1], 地址.S网络地址4.fc主机地址字符串)
		self.f添加字段(数据表.E字段.e本端协议状态, self.Fg状态(0), 信息.f解析起宕状态)
		self.f添加字段(数据表.E字段.e本端链路状态, self.Fg状态(1), 信息.f解析起宕状态)
		self.f添加字段(数据表.E字段.e本端管理状态, self.Fg状态(2), 信息.f解析起宕状态)
	f初始处理 = staticmethod(数据表.F去标题行(c标题行))
	f取状态列 = staticmethod(ca列[2])
	@staticmethod
	def Fg状态(a序号: int):
		def fg状态(a行: str):
			v状态s = F网络接口表4_nv7.f取状态列(a行)
			return v状态s.split("/")[a序号]
		return fg状态
f网络接口表4_nv7 = F网络接口表4_nv7()
class F网络接口表4全部_nv7(数据表.I解析表格列表管线):
	"""show ip interface brief vrf all
	适用于: 浪潮cn8696q(v7.3), 浪潮cn61108pcv(v9.2.*)"""
	def __init__(self):
		数据表.I解析表格列表管线.__init__(self)
		self.f添加表格(f网络接口表4_nv7)
		self.f添加字段(数据表.E字段.e本端虚拟路由转发, 数据表.F正则字段(r'IP Interface Status for VRF "(.+)"\((\d+)\)', 1), str)
	def f下一记录(self, a文本: str, a位置: int):
		v位置 = a文本.find("IP Interface Status for VRF", a位置 + 1)
		return v位置
f网络接口表4全部_nv7 = F网络接口表4全部_nv7()
#===============================================================================
# 地址解析表
#===============================================================================
def f解析寿命(a: str):
	if ":" in a:	#时:分:秒
		v时s, v分s, v秒s = a.split(":")
		return int(v时s) * 3600 + int(v分s) * 60 + int(v秒s)
	elif "." in a:	#小数
		return float(a)
	else:	#不是数字
		return 0
def f解析物理地址(a: str):
	if "." in a:
		return 地址.S物理地址.fc字符串(a)
	else:
		return None
class F地址解析表_nv7(数据表.I解析表格管线):
	"""show ip arp [vrf all]
	适用于: 浪潮cn8696q(v7.3), 浪潮cn61108pcv(v9.2.3)"""
	c网络地址 = 0
	c寿命 = 16
	c物理地址 = 26
	c接口 = 42
	c标志 = 59
	ca列 = 数据表.C切割列(c网络地址, c寿命, c物理地址, c接口, c标志)
	c标题行0 = "Address         Age       MAC Address     Interface"
	c数据行0 = "xxx.xxx.xxx.xxx 00:04:54  hhhh.hhhh.hhhh  Vlan****        "
	def __init__(self):
		数据表.I解析表格管线.__init__(self)
		self.f添加字段(数据表.E字段.e对端网络地址4, self.ca列[0], 地址.S网络地址4.fc主机地址字符串)
		self.f添加字段(数据表.E字段.e本端寿命, self.ca列[1], f解析寿命)
		self.f添加字段(数据表.E字段.e对端物理地址, self.ca列[2], f解析物理地址)
		self.f添加字段(数据表.E字段.e本端接口, self.ca列[3], 实现接口.f创建接口_nv7)
	f初始处理 = staticmethod(数据表.F去标题行(c标题行0))
f地址解析表_nv7 = F地址解析表_nv7()
#===============================================================================
# 物理地址表
#===============================================================================
class F物理地址表_nv7(数据表.I解析表格管线):
	"""show mac address-table
	适用于: 浪潮cn8672(v7.*), 浪潮cn8696q(v7.3), 浪潮cn61108pcv(v9.2.3)"""
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
		self.f添加字段(数据表.E字段.e本端虚拟局域网, self.ca列[1], 信息.f解析数字)
		self.f添加字段(数据表.E字段.e对端物理地址, self.ca列[2], 地址.S物理地址.fc字符串)
		self.f添加字段(数据表.E字段.e对端物理地址类型, self.ca列[3], 信息.f解析物理地址类型)
		self.f添加字段(数据表.E字段.e本端接口, self.ca列[7], 实现接口.f创建接口缩写_nv7)
	f初始处理 = staticmethod(数据表.F去标题行(c标题行0, c标题行1))
	@staticmethod
	def fi有效行(a行: str)->bool:
		return a行[0] in ('*', '+')
f物理地址表_nv7 = F物理地址表_nv7()
class F物理地址表_nv9(F物理地址表_nv7):
	"""show mac address-table
	适用于: 浪潮cn61108pcv(v9.2.3)"""
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
f物理地址表_nv9 = F物理地址表_nv9()