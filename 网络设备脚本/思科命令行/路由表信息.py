import pandas	#pandas
import cflw代码库py.cflw字符串 as 字符串
import cflw代码库py.cflw网络地址 as 地址
from ..基础接口 import 数据表
from ..基础接口 import 协议
from ..基础接口 import 接口 as 北向接口
from ..基础接口 import 路由 as 北向路由
from ..命令行接口 import 命令
from . import 接口 as 实现接口
#常量
ca代码4 = {
	"L": 北向路由.E路由类型.e本地,	#local
	"C": 北向路由.E路由类型.e直连,	#connected
	"S": 北向路由.E路由类型.e静态,	#static
	"R": 北向路由.E路由类型.e路由信息协议,	#RIP
	"M": 北向路由.E路由类型.e移动,	#mobile
	"B": 北向路由.E路由类型.e边界网关协议,	#BGP
	"D": 北向路由.E路由类型.e增强内部网关路由协议,	#EIGRP
	"EX": 北向路由.E路由类型.e增强内部网关路由协议,	#EIGRP external
	"O": 北向路由.E路由类型.e开放最短路径优先,	#OSPF
	"IA": 北向路由.E路由类型.e开放最短路径优先,	#OSPF inter area
	"N1": 北向路由.E路由类型.e开放最短路径优先,	#OSPF NSSA external type 1
	"N2": 北向路由.E路由类型.e开放最短路径优先,	#OSPF NSSA external type 2
	"E1": 北向路由.E路由类型.e开放最短路径优先,	#OSPF external type 1
	"E2": 北向路由.E路由类型.e开放最短路径优先,	#OSPF external type 2
	"i": 北向路由.E路由类型.e中间系统到中间系统,	#IS-IS
	"su": 北向路由.E路由类型.e中间系统到中间系统,	#IS-IS summary
	"L1": 北向路由.E路由类型.e中间系统到中间系统,	#IS-IS level-1
	"L2": 北向路由.E路由类型.e中间系统到中间系统,	#IS-IS level-2
	"ia": 北向路由.E路由类型.e中间系统到中间系统,	#IS-IS inter area
	"U": 北向路由.E路由类型.e静态,	#per-user static route
	"o": 北向路由.E路由类型.e按需路由,	#ODR
	"P": 北向路由.E路由类型.e静态,	#periodic downloaded static route
	"H": 北向路由.E路由类型.e下一跳解析协议,	#NHRP
	"l": 北向路由.E路由类型.e定位与身份分离协议	#LISP
}
ca代码6 = {
	"L": 北向路由.E路由类型.e本地,	#Local
	"LC": 北向路由.E路由类型.e本地,	#
	"C": 北向路由.E路由类型.e直连,	#Connected
	"S": 北向路由.E路由类型.e静态,	#Static
	"U": 北向路由.E路由类型.e静态,	#Per-user Static route
	"B": 北向路由.E路由类型.e边界网关协议,	#BGP
	"R": 北向路由.E路由类型.e路由信息协议,	#RIP
	"H": 北向路由.E路由类型.e下一跳解析协议,	#NHRP
	"IS": 北向路由.E路由类型.e中间系统到中间系统,	#ISIS summary
	"I1": 北向路由.E路由类型.e中间系统到中间系统,	#ISIS L1
	"I2": 北向路由.E路由类型.e中间系统到中间系统,	#ISIS L2
	"IA": 北向路由.E路由类型.e中间系统到中间系统,	#ISIS interarea
	"D": 北向路由.E路由类型.e增强内部网关路由协议,	#EIGRP
	"EX": 北向路由.E路由类型.e增强内部网关路由协议,	#EIGRP external
	"ND": 北向路由.E路由类型.e邻居发现协议,	#ND Default
	"NDp": 北向路由.E路由类型.e邻居发现协议,	#ND Prefix
	"DCE": 北向路由.E路由类型.e邻居发现协议,	#Destination
	"NDr": 北向路由.E路由类型.e邻居发现协议,	#Redirect
	"O": 北向路由.E路由类型.e开放最短路径优先,	#OSPF Intra
	"OI": 北向路由.E路由类型.e开放最短路径优先,	#OSPF Inter
	"OE1": 北向路由.E路由类型.e开放最短路径优先,	#OSPF ext 1
	"OE2": 北向路由.E路由类型.e开放最短路径优先,	#OSPF ext 2
	"ON1": 北向路由.E路由类型.e开放最短路径优先,	#OSPF NSSA ext 1
	"ON2": 北向路由.E路由类型.e开放最短路径优先,	#OSPF NSSA ext 2
	"l": 北向路由.E路由类型.e定位与身份分离协议	#LISP
}
ca协议字符串 = {
	北向路由.E路由类型.e直连: "connected",
	北向路由.E路由类型.e静态: "static",
	北向路由.E路由类型.e路由信息协议: "rip",
	北向路由.E路由类型.e开放最短路径优先: "ospf",
	北向路由.E路由类型.e增强内部网关路由协议: "eigrp",
	北向路由.E路由类型.e中间系统到中间系统: "isis",
	北向路由.E路由类型.e边界网关协议: "bgp"
}
#函数
def f生成显示路由表命令(a版本, *a参数, a虚拟路由转发 = None):
	v命令 = 命令.C命令("show")
	if a版本 == 协议.E协议.e网络协议4:
		v命令 += "ip"
	elif a版本 == 协议.E协议.e网络协议6:
		v命令 += "ipv6"
	for v参数 in a参数:
		if v参数 in 北向路由.E路由类型:
			v命令 += ca协议字符串[v参数]
		else:
			v命令 += v参数
	if a虚拟路由转发:
		v命令 += a虚拟路由转发
	return v命令
def f解析距离(a文本):
	"""必需是"[%d/%d]"格式"""
	if v := 字符串.f提取字符串之间(a文本, "[", "]"):
		v管理距离s, v度量值s = v.split("/")
		return int(v管理距离s), int(v度量值s)
	return 0, 0
#===============================================================================
# 路由表4
#===============================================================================
class F路由表4(数据表.I解析列表管线):
	"""show ip route
	适用于: 思科c7200(v15.2)"""
	c协议 = 0
	c主类 = 6
	c网络号 = 9
	def __init__(self):
		数据表.I解析列表管线.__init__(self)
	def fe记录(self, a文本):
		for v行s in self.fe记录文本(a文本):
			v记录 = {}
			#路由类型
			if v路由类型s := v行s[self.c协议 : self.c主类].strip():
				if v路由类型s[-1] == '*':	#默认路由
					v路由类型s = v路由类型s[:-1]
				v记录[数据表.E字段.e目的路由类型] = ca代码4[v路由类型s]
			else:
				v记录[数据表.E字段.e目的路由类型] = self.f上次结果(数据表.E字段.e目的路由类型)
			#网络号
			v网络号开始位置 = self.c主类 if v行s[self.c主类] != ' ' else self.c网络号
			v网络号结束位置 = v行s.find(" ", v网络号开始位置)
			if v网络号s := v行s[v网络号开始位置 : v网络号结束位置].strip():
				v记录[数据表.E字段.e目的网络号] = 地址.S网络地址4.fc自动(v网络号s)
			else:
				v记录[数据表.E字段.e目的网络号] = self.f上次结果(数据表.E字段.e目的网络号)
			#管理距离,度量值
			v记录[数据表.E字段.e目的管理距离], v记录[数据表.E字段.e目的度量值] = f解析距离(v行s)
			#下一跳地址
			v逗号位置0 = v行s.find(",")	#逗号前是下一跳地址
			v下一跳位置 = v行s.rfind(" ", 0, v逗号位置0) + 1
			v下一跳s = v行s[v下一跳位置 : v逗号位置0]
			if "." in v下一跳s:
				v记录[数据表.E字段.e目的下一跳] = 地址.S网络地址4.fc主机地址字符串(v下一跳s)
			#出接口
			v逗号位置1 = v行s.find(",", v逗号位置0 + 1)	#最后一个逗号后面是出接口
			if v逗号位置1 > 0:
				v接口s = v行s[v逗号位置1 + 1 :].strip()
			else:
				v接口s = v行s[v逗号位置0 + 1 :].strip()
			if not "." in v接口s:	#判断是否接口
				v记录[数据表.E字段.e本端出接口] = 实现接口.f创建接口(v接口s)
			yield v记录
	f下一记录 = staticmethod(数据表.f下一记录_下一行)
	def fi有效记录(self, a行: str):
		if len(a行) < 10:	#太短
			return False
		if "-" in a行:	#带横杠的是说明行
			return False
		if "subnet" in a行:	#是主类行
			return False
		if a行[self.c主类-1] != ' ':
			return False
		return True
f路由表4 = F路由表4()
#===============================================================================
# 路由表6
#===============================================================================
class F路由表6(数据表.I解析列表管线):
	"""show ipv6 route
	适用于: 思科c7200(v15.2)"""
	c协议 = 0
	c网络号 = 4
	c标题行6 = "       OE2 - OSPF ext 2, ON1 - OSPF NSSA ext 1, ON2 - OSPF NSSA ext 2, l - LISP"
	def __init__(self):
		数据表.I解析列表管线.__init__(self)
	def fe记录(self, a文本: str):
		for v行s in self.fe记录文本(a文本):
			#新记录行
			if self.fi新记录(v行s):
				v记录0 = self.f解析网络号行(v行s)
				continue
			#详细行
			v记录1 = v记录0 | self.f解析下一跳行(v行s)
			yield v记录1
	def f解析网络号行(self, a行: str):
		v记录 = {}
		v路由类型s = a行[F路由表6.c协议 : self.c网络号].strip()
		v距离开始 = a行.find(" ", self.c网络号)
		v网络号s = a行[F路由表6.c网络号 : v距离开始]
		v记录[数据表.E字段.e目的路由类型] = ca代码6[v路由类型s]
		v记录[数据表.E字段.e目的网络号] = 地址.S网络地址6.fc自动(v网络号s)
		v记录[数据表.E字段.e目的管理距离], v记录[数据表.E字段.e目的度量值] = f解析距离(a行[v距离开始+1 : ])
		return v记录
	def f解析下一跳行(self, a行: str):
		v记录 = {}
		v逗号位置0 = a行.find(",")
		v下一跳位置0 = a行.rfind(" ", 0, v逗号位置0)	#逗号前的空格
		v下一跳s = a行[v下一跳位置0 + 1 : v逗号位置0].strip()
		if ":" in v下一跳s:	#是地址
			v记录[数据表.E字段.e目的下一跳] = 地址.S网络地址6.fc主机地址字符串(v下一跳s)
			v接口s = a行[v逗号位置0 + 1 :].strip()
			v记录[数据表.E字段.e本端出接口] = 实现接口.f创建接口(v接口s)
		else:	#是接口
			v记录[数据表.E字段.e本端出接口] = 实现接口.f创建接口(v下一跳s)
		return v记录
	f下一记录 = staticmethod(数据表.f下一记录_下一行)
	f初始处理 = staticmethod(数据表.F去标题行(c标题行6))
	@staticmethod
	def fi有效行(a行: str):
		if len(a行) < 16:	#太短
			return False
		if "-" in a行:	#说明行
			return False
		return True
	def fi新记录(self, a行: str):
		return a行[0] != ' ' and a行[self.c网络号-1] == ' ' and a行[self.c网络号] != ' '
f路由表6 = F路由表6()