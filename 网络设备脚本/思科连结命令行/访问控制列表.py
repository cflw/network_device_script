import pandas	#pandas
import cflw代码库py.cflw网络地址 as 地址
import cflw代码库py.cflw字符串 as 字符串
from ..基础接口 import 协议
from ..基础接口 import 数据表
from ..基础接口 import 访问控制列表 as 北向列表
from ..命令行接口 import 命令
from ..命令行接口 import 访问控制列表 as 南向列表
from ..思科命令行.常量 import *
from ..思科命令行 import 访问控制列表 as 旧列表
#===============================================================================
# 生成
#===============================================================================
f生成规则序号4 = 旧列表.f生成规则序号4
f生成动作 = 旧列表.f生成动作
def f生成地址4(a地址):
	if not a地址:
		return "any"
	v地址 = 地址.S网络地址4.fc自动(a地址)
	return v地址.ft字符串()
f生成端口 = 旧列表.f生成端口
def f生成规则4(a序号, a规则: 北向列表.S规则):
	v命令 = 命令.C命令()
	v命令 += f生成规则序号4(a序号)
	v命令 += f生成动作(a规则.m动作)
	#确定
	v命令 += 南向列表.ca协议到字符串4[a规则.m协议]
	v层 = 协议.f取协议层(a规则.m协议)
	#按层
	if v层 == 3:
		v命令 += f生成地址4(a规则.m源地址)
		v命令 += f生成地址4(a规则.m目的地址)
	elif v层 == 4:
		v命令 += f生成地址4(a规则.m源地址)
		v命令 += f生成端口(a规则.m源端口)
		v命令 += f生成地址4(a规则.m目的地址)
		v命令 += f生成端口(a规则.m目的端口)
	else:
		raise NotImplementedError("其他层未实现")
	return v命令
#===============================================================================
# 解析
#===============================================================================
ca字符串到类型 = {	#show_access-list_summary显示的类型
	"IP": 北向列表.E类型.e扩展4,	#浪潮cn61108pcv(v9.2.3)显示"IP"
	"IPv4": 北向列表.E类型.e扩展4,
	"IPV4": 北向列表.E类型.e扩展4,	#浪潮cn8696q(v7.3)显示"IPV4"
	"IPv6": 北向列表.E类型.e扩展6,
	"IPV6": 北向列表.E类型.e扩展6,
	"MAC": 北向列表.E类型.e物理,
}
def f解析访问列表摘要(a文本: str):
	"""show access-lists summary | include ACL
	得到"类型 ACL 名称"的格式
	适用于: 浪潮cn61108pcv(9.2.3)"""
	def f摘要0():
		for v行 in a文本.split("\n"):
			yield f解析访问列表摘要开头(v行)
	return pandas.DataFrame(f摘要0())
def f解析访问列表摘要开头(a行: str):
	"""解析show access-lists summary每个列表开头的那一串"类型 ACL 名称" """
	va列 = a行.split(" ")
	return {
		数据表.E字段.e本端名称: va列[2],
		数据表.E字段.e本端访问控制列表类型: ca字符串到类型[va列[0]]
	}
def f解析访问控制列表类型_nv7(a行: str)->北向列表.E类型:
	"""解析show access-lists 名称 的类型
	适用于: 浪潮cn8696q(v7.3)"""
	v行 = 字符串.f提取包含行(a行, "ACL")
	v类型结束位置 = v行.find("ACL") - 1
	if v类型结束位置 > 0:
		v类型s = v行[:v类型结束位置]
		return ca字符串到类型[v类型s]
	else:
		return None	#输入空,列表不存在
def f解析访问控制列表类型_nv9(a行: str)->北向列表.E类型:
	"""解析show access-lists 名称 的类型
	适用于: 浪潮cv61108pcv(v9.2.3)"""
	v行 = 字符串.f提取包含行(a行, "access list")
	v类型结束位置 = v行.find("access list") - 1
	if v类型结束位置 > 0:
		v类型s = v行[:v类型结束位置]
		return ca字符串到类型[v类型s]
	else:
		return None	#输入空,列表不存在
def f解析规则4(a规则: str):
	v解析器 = C规则解析器(a规则)
	v规则 = 北向列表.S规则()
	v规则.m序号 = v解析器.f序号4()
	v规则.m动作 = v解析器.f动作()
	v规则.m协议 = v解析器.f协议()
	v规则.m源地址 = v解析器.f地址4()
	v规则.m源端口 = v解析器.f端口号()
	v规则.m目的地址 = v解析器.f地址4()
	v规则.m目的端口 = v解析器.f端口号()
	return v规则
def fc本地列表_4(a配置: str):
	"""show access-list XXX
	适用于: 浪潮cn8696q(v7.3)"""
	return 北向列表.C列表(旧列表.fe规则0(a配置, f解析规则4))
fc本地列表_6 = 旧列表.fc本地列表_6
#===============================================================================
# 显示
#===============================================================================
class C四显示(旧列表.I列表显示):
	"""适用于: 浪潮cn8696q(v7.3), 浪潮cv61108pcv(v9.2.3)"""
	c协议 = "ip"
	c类型 = ""
	f解析规则 = staticmethod(f解析规则4)
#===============================================================================
# 配置
#===============================================================================
class C四配置(旧列表.I列表配置, C四显示):
	"""适用于: 浪潮cn8696q(v7.3), 浪潮cv61108pcv(v9.2.3)"""
	c协议 = "ip"
	c类型 = ""
	f生成规则 = staticmethod(f生成规则4)
#===============================================================================
# 解析器
#===============================================================================
class C规则解析器:
	def __init__(self, a文本):
		self.m取词 = 字符串.C推进取词(a文本)
	def f动作(self):
		return self.m取词.f取词推进() == "permit"
	def f协议(self):
		return 南向列表.ca字符串到协议[self.m取词.f取词推进()]
	def f序号4(self):
		return int(self.m取词.f取词推进())
	def f序号6(self):
		self.m取词.f推进()	#"sequence"
		return int(self.m取词.f取词推进())
	def f地址4(self):
		v词0 = self.m取词.f取词推进()
		if v词0 == "any":
			return None
		elif "/" in v词0:	#x.x.x.x/n
			return 地址.S网络地址4.fc地址前缀长度字符串(v词0)
		else:	#x.x.x.x m.m.m.m
			v词1 = self.m取词.f取词推进()
			return 地址.S网络地址4(地址.S网络地址4.f地址字符串转整数(v词0), 地址.S网络地址4.f掩码字符串转前缀长度(v词1))
	def f地址6(self):	#未测试
		v词0 = self.m取词.f取词推进()
		if v词0 == "any":
			return None
		else:	#x:x:x:x:x:x:x:x/n
			return 地址.S网络地址6.fc地址前缀长度字符串(v词0)
	def f端口号(self):
		v词 = self.m取词.f取词()
		if not v词 in C规则解析器.ca端口号运算函数:
			return None	#不是端口号
		self.m取词.f推进()
		vf端口号 = C规则解析器.ca端口号运算函数[v词]
		return vf端口号(self)
	def f端口号_大于(self):
		return 北向列表.S端口号.fc大于(int(self.m取词.f取词推进()))
	def f端口号_小于(self):
		return 北向列表.S端口号.fc小于(int(self.m取词.f取词推进()))
	def f端口号_等于(self):
		va端口号 = []
		while True:
			v词 = self.m取词.f取词()
			if v词 and v词.isdigit():
				self.m取词.f推进()
				va端口号.append(int(v词))
			else:
				break
		return 北向列表.S端口号.fc等于(*va端口号)
	def f端口号_不等于(self):
		va端口号 = []
		while True:
			v词 = self.m取词.f取词()
			if v词.isdigit():
				self.m取词.f推进()
				va端口号.append(int(v词))
			else:
				break
		return 北向列表.S端口号.fc不等于(*va端口号)
	def f端口号_范围(self):
		v词1 = self.m取词.f取词推进()
		v词2 = self.m取词.f取词推进()
		return 北向列表.S端口号.fc范围(range(int(v词1), int(v词2) + 1))
	ca端口号运算函数 = {
		"eq": f端口号_等于,
		"neq": f端口号_不等于,
		"gt": f端口号_大于,
		"lt": f端口号_小于,
		"range": f端口号_范围,
	}