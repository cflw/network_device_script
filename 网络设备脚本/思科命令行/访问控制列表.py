import pandas	#pandas
import cflw代码库py.cflw网络地址 as 地址
import cflw代码库py.cflw字符串 as 字符串
from ..基础接口 import 操作
from ..基础接口 import 协议
from ..基础接口 import 异常
from ..基础接口 import 数据表
from ..基础接口 import 访问控制列表 as 北向列表
from ..命令行接口 import 命令
from ..命令行接口 import 模式
from ..命令行接口 import 访问控制列表 as 南向列表
from .常量 import *
#===============================================================================
# 生成
#===============================================================================
#端口号
class F生成端口(北向列表.I生成端口):
	def f大于(self, a值):
		return "gt " + str(a值)
	def f小于(self, a值):
		return "lt " + str(a值)
	def f等于(self, a序列):
		return "eq " + " ".join(字符串.ft字符串序列(a序列))
	def f不等于(self, a序列):
		return "neq " + " ".join(字符串.ft字符串序列(a序列))
	def f范围(self, a值: range):
		return "range %d %d" % (a值.start, a值.stop - 1)
f生成端口 = F生成端口()
#规则序号
def f生成规则序号4(a序号):
	if a序号 == None or a序号 < 0:
		return ""
	else:
		return a序号
def f生成规则序号6(a序号):
	if a序号 == None or a序号 < 0:
		return ""
	else:
		return "sequence " + str(a序号)
#协议
#动作
f生成动作 = 南向列表.f生成动作
#地址
def f生成地址标准4(a地址):
	if not a地址:
		return "any"
	v地址 = 地址.S网络地址4.fc自动(a地址)
	if v地址.fi主机():
		return v地址.fg地址s()
	elif v地址.fi空():
		return "any"
	else:
		return "%s %s" % (v地址.fg网络号s(), v地址.fg反掩码s())
def f生成地址扩展4(a地址):
	"转成字符串"
	if not a地址:
		return "any"
	v地址 = 地址.S网络地址4.fc自动(a地址)
	if v地址.fi主机():
		return "host %s" % (v地址.fg地址s())
	elif v地址.fi空():
		return "any"
	else:
		return "%s %s" % (v地址.fg网络号s(), v地址.fg反掩码s())
def f生成地址6(a地址):
	if not a地址:
		return "any"
	v地址 = 地址.S网络地址6.fc自动(a地址)
	if v地址.fi主机():
		return "host %s" % (v地址.fg地址s())
	elif v地址.fi空():
		return "any"
	else:
		return str(v地址)
def f生成规则_标准4(a序号, a规则: 北向列表.S规则):
	v序号 = f生成规则序号4(a序号)
	v动作 = f生成动作(a规则.m动作)
	v源地址 = f生成地址标准4(a规则.m源地址)
	v命令 = f"{v序号} {v动作} {v源地址}"
	return v命令
def f生成规则_扩展4(a序号, a规则: 北向列表.S规则):
	v命令 = 命令.C命令()
	v命令 += f生成规则序号4(a序号)
	v命令 += f生成动作(a规则.m动作)
	#确定
	v命令 += 南向列表.ca协议到字符串4[a规则.m协议]
	v层 = 协议.f取协议层(a规则.m协议)
	#按层
	if v层 == 3:
		v命令 += f生成地址扩展4(a规则.m源地址)
		v命令 += f生成地址扩展4(a规则.m目的地址)
	elif v层 == 4:
		v命令 += f生成地址扩展4(a规则.m源地址)
		v命令 += f生成端口(a规则.m源端口)
		v命令 += f生成地址扩展4(a规则.m目的地址)
		v命令 += f生成端口(a规则.m目的端口)
	else:
		raise NotImplementedError("其他层未实现")
	return v命令
def f生成规则_6(self, a序号, a规则: 北向列表.S规则):
	v命令 = 命令.C命令()
	v命令 += f生成规则序号6(a序号)
	v命令 += f生成动作(a规则.m动作)
	#确定
	v命令 += 南向列表.ca协议到字符串6[a规则.m协议]
	v层 = 协议.f取协议层(a规则.m协议)
	#按层
	if v层 == 3:
		v命令 += f生成地址6(a规则.m源地址)
		v命令 += f生成地址6(a规则.m目的地址)
	elif v层 == 4:
		v命令 += f生成地址6(a规则.m源地址)
		v命令 += f生成端口(a规则.m源端口)
		v命令 += f生成地址6(a规则.m目的地址)
		v命令 += f生成端口(a规则.m目的端口)
	else:
		raise NotImplementedError("其他层未实现")
	return v命令
#===============================================================================
# 解析
#===============================================================================
#范围
ca标准范围 = (range(1, 100), range(1300, 2000))
ca扩展范围 = (range(100, 200), range(2000, 2700))
class F序号范围检查:
	def __init__(self, aa范围, a异常文本):
		self.ma范围 = aa范围
		self.m异常文本 = a异常文本
	def __call__(self, a序号, a异常 = True):
		if type(a序号) == int:
			for v in self.ma范围:
				if a序号 in v:
					return True
			if a异常:
				raise ValueError(self.m异常文本)
			return False
		return False
fi标准范围 = F序号范围检查(ca标准范围, "标准访问控制列表号码范围应为1~99,1300~1999")
fi扩展范围 = F序号范围检查(ca扩展范围, "扩展访问控制列表号码范围应为100~199,2000~2699")\
#类型字符串
ca字符串到类型 = {	#show_access-lists显示的类型
	"Standard IP": 北向列表.E类型.e标准4,
	"Extended IP": 北向列表.E类型.e扩展4,
	"IPv6": 北向列表.E类型.e扩展6,
	"MAC": 北向列表.E类型.e物理,
}
#解析规则
def fe规则0(a文本: str, af解析规则):
	"""解析show access-list XXX的输出结果"""
	v位置 = 字符串.f连续找最后(a文本, "access list", "\n")
	for v行 in a文本[v位置+1:].split("\n"):
		if v行[0:4] != "    ":
			continue
		yield af解析规则(v行)
def f解析访问列表摘要(a文本: str):
	"""show access-lists | include access list
	适用于: 浪潮cn61108pcv(9.2.3)"""
	def f摘要0():
		for v行 in a文本.split("\n"):
			yield f解析访问列表摘要开头(v行)
	return pandas.DataFrame(f摘要0())
def f解析访问列表摘要开头(a行: str):
	"""解析show access-lists每个列表开头的那一串"类型 access list 名称" """
	v类型结束位置 = a行.find("access list") - 1
	v名称开始位置 = a行.rfind(" ") + 1
	v类型s = a行[:v类型结束位置]
	v名称s = a行[v名称开始位置:]
	return {
		数据表.E字段.e本端名称: v名称s,
		数据表.E字段.e本端访问控制列表类型: ca字符串到类型[v类型s]
	}
def f解析访问控制列表类型(a行: str)->北向列表.E类型:
	"""解析show access-lists 名称 的类型,如果有多个结果只取第一个"""
	v类型结束位置 = a行.find("access list") - 1
	if v类型结束位置 > 0:
		v类型s = a行[:v类型结束位置]
		return ca字符串到类型[v类型s]
	else:
		return None	#输入空,列表不存在
def f解析规则_标准4(a规则: str):
	v解析器 = C规则解析器(a规则)
	v规则 = 北向列表.S规则()
	v规则.m序号 = v解析器.f序号4()
	v规则.m动作 = v解析器.f动作()
	v规则.m源地址 = v解析器.f地址标准4()
	return v规则
def f解析规则_扩展4(a规则: str):
	v解析器 = C规则解析器(a规则)
	v规则 = 北向列表.S规则()
	v规则.m序号 = v解析器.f序号4()
	v规则.m动作 = v解析器.f动作()
	v规则.m协议 = v解析器.f协议()
	v规则.m源地址 = v解析器.f地址扩展4()
	v规则.m源端口 = v解析器.f端口号()
	v规则.m目的地址 = v解析器.f地址扩展4()
	v规则.m目的端口 = v解析器.f端口号()
	return v规则
def f解析规则_6(a规则: str):
	v解析器 = C规则解析器(a规则)
	v规则 = 北向列表.S规则()
	v规则.m动作 = v解析器.f动作()
	v规则.m协议 = v解析器.f协议()
	v规则.m源地址 = v解析器.f地址6()
	v规则.m源端口 = v解析器.f端口号()
	v规则.m目的地址 = v解析器.f地址6()
	v规则.m目的端口 = v解析器.f端口号()
	v规则.m序号 = v解析器.f序号6()
	return v规则
class C全局列表配置解析:
	def __init__(self, a配置):
		self.m配置 = a配置
	def fe列表(self):
		pass
class C单列表配置解析:
	def __init__(self, a配置):
		self.m配置 = a配置
	def fg类型(self):
		pass
	def fe规则(self, af解析规则):
		pass
#本地列表
def fc本地列表_标准4(a配置: str):
	return 北向列表.C列表(fe规则0(a配置, f解析规则_标准4))
def fc本地列表_扩展4(a配置: str):
	return 北向列表.C列表(fe规则0(a配置, f解析规则_扩展4))
def fc本地列表_6(a配置: str):
	return 北向列表.C列表(fe规则0(a配置, f解析规则_6))
#===============================================================================
# 显示模式
#===============================================================================
class I列表显示(北向列表.I列表显示, 模式.I显示模式):
	def __init__(self, a, a名称, a列表缓存: str = None):
		模式.I显示模式.__init__(self, a)
		self.m名称 = a名称
		self.m列表缓存 = a列表缓存	#外面执行显示命令确定类型后传进来作为缓存
	def __bool__(self):
		return self.fi存在()
	def fi存在(self):
		v列表 = self.fg列表文本()
		return bool(v列表)	#不存在则什么都不显示
	def fg列表文本(self):
		if not self.m列表缓存:
			v命令 = self.fg显示命令()
			self.m列表缓存 = self.m设备.f执行显示命令(v命令)
		return self.m列表缓存
	def fg显示命令(self, a序号 = None):
		v命令 = 命令.C命令("show", self.c协议, "access-list", self.m名称)
		if a序号 != None:
			v命令 += f"| include ^____{a序号}_"
		return v命令
	def fe规则(self):
		v列表 = self.fg列表文本()
		return fe规则0(v列表, self.f解析规则)
	def fg规则(self, a序号):
		v命令 = self.fg显示命令(a序号)
		v输出 = self.m设备.f执行显示命令(v命令)
		v规则 = self.f解析规则(v输出)
		return v规则
class C标准4显示(I列表显示):
	c协议 = "ip"
	c类型 = "standard"
	f解析规则 = staticmethod(f解析规则_标准4)
class C扩展4显示(I列表显示):
	c协议 = "ip"
	c类型 = "extended"
	f解析规则 = staticmethod(f解析规则_扩展4)
class C六显示(I列表显示):
	c协议 = "ipv6"
	c类型 = ""
	f解析规则 = staticmethod(f解析规则_6)
	def fg显示命令(self, a序号 = None):
		v命令 = 命令.C命令("show", self.c协议, "access-list", self.m名称)
		if a序号 != None:
			v命令 += f"| include sequence_{a序号}$"
		return v命令
#===============================================================================
# 配置模式
#===============================================================================
class I列表配置(南向列表.I列表配置):
	def __init__(self, a, a名称, a列表缓存: str = None):
		南向列表.I列表配置.__init__(self, a)
		self.m名称 = a名称
		self.m列表缓存 = a列表缓存
	def fg模式参数(self):
		return (self.c类型, self.m名称)
	def fg进入命令(self):
		return 命令.C命令(self.c协议, "access-list", self.c类型, self.m名称)
	def f删除规则(self, a序号: int):
		self.f执行当前模式命令(c不 + str(a序号))
	def f添加规则(self, a序号, a规则: 北向列表.S规则):
		v命令 = self.f生成规则(a序号, a规则)
		self.f执行当前模式命令(v命令)
	def fs规则(self, a序号, a规则 = None, a操作 = 操作.E操作.e设置):
		v操作 = 操作.f解析操作(a操作)
		if v操作 in (操作.E操作.e设置, 操作.E操作.e新建, 操作.E操作.e添加):
			self.f添加规则(a序号, a规则)
		elif v操作 == 操作.E操作.e修改:
			v规则 = self.fg规则(a序号)
			v规则.f更新_规则(a规则)
			self.f删除规则(a序号)	#不能直接覆盖,需要先删除再添加
			self.f添加规则(a序号, v规则)
		elif v操作 == 操作.E操作.e删除:
			self.f删除规则(a序号)
		else:
			raise 异常.X操作()
class C标准4配置(I列表配置, C标准4显示):
	c协议 = "ip"
	c类型 = "standard"
	f生成规则 = staticmethod(f生成规则_标准4)
class C扩展4配置(I列表配置, C扩展4显示):
	"""适用于: 浪潮s6650(v11.12.1) 浪潮s5960(v12.2)"""
	c协议 = "ip"
	c类型 = "extended"
	f生成规则 = staticmethod(f生成规则_扩展4)
class C六配置(I列表配置, C六显示):
	c模式名 = "互联网协议第6版命名访问控制列表"
	c协议 = "ipv6"
	c类型 = ""
	f生成规则 = staticmethod(f生成规则_6)
#===============================================================================
class C助手(北向列表.I助手):
	#元组结构含意:(序号开始, 序号结束（不包含）, 到目标序号的增加值)
	c计算标准4 = [(0, 99, 1), (99, 799, 1200)]
	c计算扩展4 = [(0, 99, 100), (99, 799, 1900)]
	c反算标准4 = [(1, 100, -1), (1300, 2000, -1200)]
	c反算扩展4 = [(100, 200, -100), (2000, 2700, -1900)]
	def F计算(a0, a1):
		@staticmethod
		def f(n):
			v类型 = type(n)
			if v类型 == int:
				if n in range(a0[0], a0[1]):
					return n + a0[2]
				elif n in range(a1[0], a1[1]):
					return n + a1[2]
				else:
					raise ValueError("n超出范围")
			else:
				return n
		return f
	f计算标准4 = F计算(*c计算标准4)
	f计算扩展4 = F计算(*c计算扩展4)
	f反算标准4 = F计算(*c反算标准4)
	f反算扩展4 = F计算(*c反算扩展4)
	def F判断类型(a0, a1, a类型):
		@staticmethod
		def f(n):
			try:
				v = int(n)
				if v in range(a0[0], a0[1]):
					return a类型
				elif v in range(a1[0], a1[1]):
					return a类型
				else:
					return None
			except:
				return None
		return f
	f判断标准4 = F判断类型(*c反算标准4, 北向列表.E类型.e标准4)
	f判断扩展4 = F判断类型(*c反算扩展4, 北向列表.E类型.e扩展4)
	#实现
	@staticmethod
	def ft特定编号(n, a类型):
		if a类型 == 北向列表.E类型.e标准4:
			return C助手.f计算标准4(n)
		elif a类型 == 北向列表.E类型.e扩展4:
			return C助手.f计算扩展4(n)
		else:
			raise ValueError("类型错")
	@staticmethod
	def ft统一编号(n, a类型):
		if a类型 == 北向列表.E类型.e标准4:
			return C助手.f反算标准4(n)
		elif a类型 == 北向列表.E类型.e扩展4:
			return C助手.f反算扩展4(n)
		else:
			raise ValueError("类型错")
	@staticmethod
	def f判断类型(n):
		v = C助手.f判断标准4(n)
		if v:
			return v
		v = C助手.f判断扩展4(n)
		return v
#===============================================================================
# 解析器
#===============================================================================
class C规则解析器:
	def __init__(self, a文本: str):
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
	def f地址标准4(self):	#标准4
		v词0 = self.m取词.f取词推进()
		if v词0 == "any":
			return None
		if v词0[-1] == ",":	#有通配符
			v词0 = v词0[:-1]
			self.m取词.f推进()
			self.m取词.f推进()
			v词1 = self.m取词.f取词推进()
			v掩码 = 地址.S网络地址4.c全f - 地址.S网络地址4.f地址字符串转整数(v词1)
			return 地址.S网络地址4.fc地址掩码(v词0, v掩码)
		else:	#主机地址
			return 地址.S网络地址4.fc主机地址字符串(v词0)
	def f地址扩展4(self):	#扩展4
		v词0 = self.m取词.f取词推进()
		if v词0 == "any":
			return None
		elif v词0 == "host":
			v词1 = self.m取词.f取词推进()	#地址
			return 地址.S网络地址4.fc主机地址字符串(v词1)
		v词1 = self.m取词.f取词()	#通配符
		if not v词1:
			return 地址.S网络地址4.fc主机地址字符串(v词0)
		self.m取词.f推进()
		v掩码 = 地址.S网络地址4.c全f - 地址.S网络地址4.f地址字符串转整数(v词1)
		return 地址.S网络地址4.fc地址掩码(v词0, v掩码)
	def f地址6(self):	#六
		v词0 = self.m取词.f取词推进()
		if v词0 == "any":
			return None
		elif v词0 == "host":
			v词1 = self.m取词.f取词推进()
			return 地址.S网络地址6.fc自动(v词1)
		return 地址.S网络地址6.fc自动(v词0)
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