import pandas	#pandas
import cflw代码库py.cflw字符串 as 字符串
import cflw代码库py.cflw网络地址 as 地址
from ..基础接口 import 操作
from ..基础接口 import 信息
from ..基础接口 import 数据表
from ..基础接口 import 协议
from ..基础接口 import 接口 as 北向接口
from ..基础接口 import 路由 as 北向路由
from ..命令行接口 import 命令
from ..命令行接口 import 路由 as 南向路由
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
	v = 字符串.f提取字符串之间(a文本, "[", "]")
	v管理距离s, v度量值s = v.split("/")
	return int(v管理距离s), int(v度量值s)
def f去逗号(a文本):
	if a文本[-1] == ",":
		return a文本[:-1]
	return a文本
#===============================================================================
# 表
#===============================================================================
class F路由表4:
	c协议 = 0
	c网络号 = 9
	def __call__(self, a文本: str):
		return self.f解析(a文本)
	def f解析(self, a文本: str):
		def fe行():
			v结果 = {}
			for v行 in a文本.split("\n"):
				if not self.fi有效行(v行):
					continue
				if self.fi新记录(v行):
					v结果 = {}
					v路由类型s = v行[F路由表4.c协议 : F路由表4.c网络号].strip()
					v详细开始 = v行.find(" ", F路由表4.c网络号)
					v网络号s = v行[F路由表4.c网络号 : v详细开始]
					v结果[数据表.E字段.e目标路由类型] = ca代码4[v路由类型s]
					v结果[数据表.E字段.e目标网络号] = 地址.S网络地址4.fc自动(v网络号s)
				for v词 in v行[v详细开始+1 : ].split(" "):
					v词 = f去逗号(v词)
					if "[" in v词:	#管理距离&度量值
						v管理距离, v度量值 = f解析距离(v词)
						v结果[数据表.E字段.e目标管理距离] = v管理距离
						v结果[数据表.E字段.e目标度量值] = v度量值
					elif v词.count(".") == 3:	#地址
						v下一跳 = 地址.S网络地址4.fc自动(v词)
						v结果[数据表.E字段.e目标下一跳] = v下一跳
					elif v词.count(":") == 2:	#存在时间
						pass
					elif 北向接口.c接口正则.fullmatch(v词):
						v出接口 = 实现接口.f创建接口(v词)
						v结果[数据表.E字段.e本端出接口] = v出接口
					else:	#无关词,跳过
						pass
				yield v结果
		v数据表 = pandas.DataFrame(fe行())
		return v数据表
	@staticmethod
	def fi有效行(a行: str):
		if len(a行) < 40:	#太短
			return False
		if "-" in a行:	#带横杠的是说明行
			return False
		if a行[6].isdigit():	#主类行没有能使用的信息
			return False
		return True
	@staticmethod
	def fi新记录(a行: str):
		return a行[0] != " " and a行[F路由表4.c网络号-1] == " "
f路由表4 = F路由表4()
class F路由表6:
	c协议 = 0
	c网络号 = 4
	def __call__(self, a行: str):
		return self.f解析(a行)
	def f解析(self, a文本: str):
		def fe行():
			v结果 = {}
			for v行 in a文本.split("\n"):
				if not self.fi有效行(v行):
					continue
				if self.fi新记录(v行):
					v结果 = {}
					v路由类型s = v行[F路由表6.c协议 : F路由表6.c网络号].strip()
					v距离开始 = v行.find(" ", F路由表6.c网络号)
					v网络号s = v行[F路由表6.c网络号 : v距离开始]
					v结果[数据表.E字段.e目标路由类型] = ca代码6[v路由类型s]
					v结果[数据表.E字段.e目标网络号] = 地址.S网络地址6.fc自动(v网络号s)
					v管理距离, v度量值 = f解析距离(v行[v距离开始+1 : ])
					v结果[数据表.E字段.e目标管理距离] = v管理距离
					v结果[数据表.E字段.e目标度量值] = v度量值
					continue
				for v词 in v行.strip().split(" "):
					v词 = f去逗号(v词)
					if v词.count(":") >= 2:	#地址
						v结果[数据表.E字段.e目标下一跳] = 地址.S网络地址6.fc自动(v词)
					elif 北向接口.c接口正则.fullmatch(v词):
						v结果[数据表.E字段.e本端出接口] = 实现接口.f创建接口(v词)
					else:
						pass
				yield v结果
		v数据表 = pandas.DataFrame(fe行())
		return v数据表
	@staticmethod
	def fi有效行(a行: str):
		if len(a行) < 16:	#太短
			return False
		if "-" in a行:	#说明行
			return False
		return True
	@staticmethod
	def fi新记录(a行: str):
		return a行[0] != " " and a行[F路由表6.c网络号-1] == " "
f路由表6 = F路由表6()