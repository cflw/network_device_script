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
from ..思科命令行.常量 import *
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
#动作
f生成动作 = 南向列表.f生成动作
#地址
def f生成地址4(a地址):
	if not a地址:
		return "any"
	v地址 = 地址.S网络地址4.fc自动(a地址)
	if v地址.fi主机():
		return "host %s" % (v地址.fg地址s())
	elif v地址.fi空():
		return "any"
	else:
		return "%s %s" % (v地址.fg网络号s(), v地址.fg反掩码s())
def f生成规则_标准4(a序号, a规则: 北向列表.S规则):
	v序号 = f生成规则序号4(a序号)
	v动作 = f生成动作(a规则.m动作)
	v源地址 = f生成地址4(a规则.m源地址)
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
c网络标准范围 = range(1, 1001)	#ip standard
c网络扩展范围 = range(1001, 2001)	#ip extended
c物理标准范围 = range(2001, 3001)	#mac standard
c物理扩展范围 = range(3001, 4001)	#mac extended
c混合扩展范围 = range(5001, 6001)	#hybrid extended
c网络6标准范围 = range(6001, 7001)	#ipv6 standard
c网络6扩展范围 = range(7001, 8001)	#ipv6 extended
class F序号范围检查:
	def __init__(self, a范围, a异常文本):
		self.m范围 = a范围
		self.m异常文本 = a异常文本
	def __call__(self, a序号, a异常 = True):
		if type(a序号) == int:
			if a序号 in self.m范围:
				return True
			if a异常:
				raise ValueError(self.m异常文本)
			return False
		return False
fi标准范围 = F序号范围检查(c网络标准范围, "ip标准访问控制列表号码范围应为1~1000")
fi扩展范围 = F序号范围检查(c网络扩展范围, "ip扩展访问控制列表号码范围应为1001~2000")
def fe规则0(a文本: str, af解析规则):
	"""解析 show XXX access-list XXX 的输出结果"""
	v位置 = 字符串.f连续找最后(a文本, "access-list", "\n")
	for v行 in a文本[v位置+1:].split("\n"):
		if not bool(v行):	#判断空行
			continue
		if v行[0] != ' ':	#每行规则开头有个空格缩进
			continue
		yield af解析规则(v行)
def f解析规则_标准4(a规则: str):
	"""适用于: 迈普t6100(v9.3.4.45)"""
	v解析器 = C规则解析器(a规则)
	v规则 = 北向列表.S规则()
	v规则.m序号 = v解析器.f序号4()
	v规则.m动作 = v解析器.f动作()
	v规则.m源地址 = v解析器.f地址4()
	return v规则
def f解析规则_扩展4(a规则: str):
	"""适用于: 迈普t6100(v9.3.4.45)"""
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
def f解析规则_混合(a规则: str):
	"""适用于: 迈普t6100(v9.3.4.45)"""
	v解析器 = C规则解析器(a规则)
	v规则 = 北向列表.S规则()
	v规则.m序号 = v解析器.f序号4()
	v规则.m动作 = v解析器.f动作()
	v解析器.f跳过()	#源mac
	v解析器.f跳过()	#目的mac
	v解析器.f跳过()	#ether-type
	v解析器.f跳过() #ipv4
	v规则.m协议 = v解析器.f协议()	#ip
	v规则.m源地址 = v解析器.f地址4()
	v规则.m目的地址 = v解析器.f地址4()
	return v规则
#从文本创建本地列表对象
def fc本地列表_标准4(a配置: str):
	"""show ip access-list XXX
	适用于: 迈普t6100(v9.3.4.45)"""
	return 北向列表.C列表(fe规则0(a配置, f解析规则_标准4))
def fc本地列表_扩展4(a配置: str):
	"""show ip access-list XXX"""
	return 北向列表.C列表(fe规则0(a配置, f解析规则_扩展4))
def fc本地列表_混合(a配置: str):
	"""show hybrid access-list XXX"""
	return 北向列表.C列表(fe规则0(a配置, f解析规则_混合))
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
	"""适用于: 迈普t6100(v9.3.4.45)"""
	c协议 = "ip"
	c类型 = "standard"
	f解析规则 = staticmethod(f解析规则_标准4)
class C扩展4显示(I列表显示):
	"""适用于: 迈普t6100(v9.3.4.45)"""
	c协议 = "ip"
	c类型 = "extended"
	f解析规则 = staticmethod(f解析规则_扩展4)
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
	"""适用于: """
	c协议 = "ip"
	c类型 = "standard"
	f生成规则 = staticmethod(f生成规则_标准4)
class C扩展4配置(I列表配置, C扩展4显示):
	"""适用于: """
	c协议 = "ip"
	c类型 = "extended"
	f生成规则 = staticmethod(f生成规则_扩展4)
#===============================================================================
# 其它
#===============================================================================
class C助手(北向列表.I助手):
	def F计算(a起始):
		@staticmethod
		def f(n):
			return n + a起始
		return f
	def F反算(a起始):
		@staticmethod
		def f(n):
			return n - a起始
		return f
	f计算标准4 = F计算(1)
	f计算扩展4 = F计算(1001)
	f反算标准4 = F反算(1)
	f反算扩展4 = F反算(1001)
	@staticmethod
	def ft特定编号(n, a类型):
		if a类型 == 北向列表.E类型.e标准4:
			return C助手.f计算标准4(n)
		elif a类型 == 北向列表.E类型.e扩展4:
			return C助手.f计算扩展4(n)
		return n
	@staticmethod
	def ft统一编号(n, a类型):
		if a类型 == 北向列表.E类型.e标准4:
			return C助手.f反算标准4(n)
		elif a类型 == 北向列表.E类型.e扩展4:
			return C助手.f反算扩展4(n)
		return n
	@staticmethod
	def f判断类型(n):
		try:
			v = int(n)
			if v in c网络标准范围:
				return 北向列表.E类型.e标准4
			elif v in c网络扩展范围:
				return 北向列表.E类型.e扩展4
			else:
				return None
		except:
			return None
#===============================================================================
# 解析器
#===============================================================================
class C规则解析器:
	def __init__(self, a文本: str):
		self.m取词 = 字符串.C推进取词(a文本)
	def f跳过(self):
		self.m取词.f推进()
	def f动作(self):
		return self.m取词.f取词推进() == "permit"
	def f协议(self):
		return 南向列表.ca字符串到协议[self.m取词.f取词推进()]
	def f序号4(self):
		return int(self.m取词.f取词推进())
	def f序号6(self):
		self.m取词.f推进()	#"sequence"
		return int(self.m取词.f取词推进())
	def f地址4(self):	#扩展4
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