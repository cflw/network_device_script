import pandas	#pandas
import cflw代码库py.cflw网络地址 as 地址
import cflw代码库py.cflw字符串 as 字符串
from ..基础接口 import 操作
from ..基础接口 import 协议
from ..基础接口 import 异常
from ..基础接口 import 数据表
from ..基础接口 import 访问控制列表 as 北向列表
from ..基础接口 import 文件
from ..命令行接口 import 命令
from ..命令行接口 import 模式
from ..命令行接口 import 访问控制列表 as 南向列表
from .常量 import *
#===============================================================================
# 生成&解析
#===============================================================================
#规则序号
def f生成规则序号4(a序号):
	if a序号 == None or a序号 < 0:
		return ""
	else:
		return a序号
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
#协议
ca协议到字符串4 = 南向列表.ca协议到字符串4 | {
	协议.E协议.ip: "any",
	协议.E协议.ipv4: "any",
}
f生成协议4 = 南向列表.F生成协议(ca协议到字符串4)
#允许
f生成允许 = 南向列表.f生成允许
#地址
def f生成地址4(a地址):
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
#===============================================================================
# 解析
#===============================================================================
def fe规则0(a列表: str, af解析规则):	#解析show access-list XXX [extend]的显示结果
	v位置 = 字符串.f连续找最后(a列表, "access-list ", "\n")
	for v行 in a列表[v位置+1:].split("\n"):
		if v行[0:2] != "  ":
			continue
		yield af解析规则(v行)
def f解析访问列表摘要(a文本: str):
	"""show running-config | include access-list
	得到"协议 access-list 名称 [extend]"的格式
	适用于: """
	def f摘要0():
		for v行 in a文本.split("\n"):
			yield f解析访问列表摘要开头(v行)
	return pandas.DataFrame(f摘要0())
def f解析访问列表摘要开头(a行: str):
	"""解析show access-lists summary每个列表开头的那一串"类型 access-list 名称" """
	v名称开始位置 = a行.find("access-list") + 12
	v名称结束位置 = a行.find(" ", v名称开始位置)
	v名称 = a行[v名称开始位置 : v名称结束位置]
	return {
		数据表.E字段.e本端名称: v名称,
		数据表.E字段.e本端访问控制列表类型: f解析访问控制列表类型(a行)
	}
def f解析访问控制列表类型(a行: str)->北向列表.E类型:
	"""解析"show running-config | include access-list 名称"的类型,如果有多个结果只取第一个
	适用于: 浪潮cn61108pcvh(v6.6.6)"""
	v协议结束位置 = a行.find("access-list") - 1
	if v协议结束位置 > 0:
		v协议s = a行[:v协议结束位置]
		if v协议s == "ip":
			v末尾单词位置 = a行.rfind(" ") + 1
			v末尾s = a行[v末尾单词位置:]
			if v末尾s == "extend":
				return 北向列表.E类型.e扩展4
			else:
				return 北向列表.E类型.e标准4
		elif v协议s == "ipv6":
			return 北向列表.E类型.e扩展6
		elif v协议s == "mac":
			return 北向列表.E类型.e物理
	else:
		return None	#输入空,列表不存在
#===============================================================================
# 显示
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
		if not hasattr(self, "m列表缓存") or not self.m列表缓存:
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
	"""适用于: 浪潮cn61108pcvh(v6.6.6)"""
	def fg显示命令(self, a序号 = None):
		"""show access-list ip 名称"""
		v命令 = 命令.C命令(f"show access-list ip {self.m名称}")
		if a序号 != None:
			v命令 += f"| include ^____{a序号}_"
		return v命令
	@staticmethod
	def f解析规则(a规则: str):
		v解析器 = C规则解析器(a规则)
		v规则 = 北向列表.S规则()
		v规则.m序号 = v解析器.f序号4()
		v规则.m允许 = v解析器.f允许()
		v规则.m协议 = v解析器.f协议()
		v规则.m源地址 = v解析器.f地址4()
		v规则.m目的地址 = v解析器.f地址4()
		return v规则
class C扩展4显示(I列表显示):
	"""适用于: """
	def fg显示命令(self, a序号 = None):
		"""show access-list ip 名称 extend"""
		v命令 = 命令.C命令(f"show access-list ip {self.m名称} extend")
		if a序号 != None:
			v命令 += f"| include ^____{a序号}_"
		return v命令
	@staticmethod
	def f解析规则(a规则: str):
		v解析器 = C规则解析器(a规则)
		v规则 = 北向列表.S规则()
		v规则.m序号 = v解析器.f序号4()
		v规则.m允许 = v解析器.f允许()
		v规则.m协议 = v解析器.f协议()
		v规则.m源地址 = v解析器.f地址4()
		v规则.m源端口 = v解析器.f端口号()
		v规则.m目的地址 = v解析器.f地址4()
		v规则.m目的端口 = v解析器.f端口号()
		return v规则
#===============================================================================
# 配置
#===============================================================================
class C扩展4配置(南向列表.I列表配置, C扩展4显示):
	"""适用于: 浪潮cn61108pcvh(v6.x), 浪潮s5350(v6.x)"""
	def __init__(self, a, a名称):
		南向列表.I列表配置.__init__(self, a)
		self.m名称 = a名称
	def fg进入命令(self):
		v命令 = f"ip access-list ip {self.m名称} extend"
		return v命令
	def f添加规则(self, a序号, a规则):
		v命令 = 命令.C命令()
		v命令 += f生成规则序号4(a序号)
		v命令 += f生成允许(a规则.m允许)
		#确定
		v命令 += ca协议到字符串4[a规则.m协议]
		v层 = 协议.f取协议层(a规则.m协议)
		#按层
		if v层 == 3:
			v命令 += f生成地址4(a规则.m源地址)
			v命令 += f生成地址4(a规则.m目的地址)
		elif v层 == 4:
			v命令 += f生成地址4(a规则.m源地址)
			if a规则.m源端口:
				v命令 += "src-port"
				v命令 += f生成端口(a规则.m源端口)
			v命令 += f生成地址4(a规则.m目的地址)
			if a规则.m目的端口:
				v命令 += "dst-port"
				v命令 += f生成端口(a规则.m目的端口)
		else:
			raise NotImplementedError("迷之逻辑")
		#执行命令
		self.f执行当前模式命令(v命令)
	def f删除规则_序号(self, a序号):
		v命令 = f"no sequence-num {a序号}"
		self.f执行当前模式命令(v命令)
	def f删除规则_规则(self, a规则):
		#需要开启读权限才能调用这个
		raise NotImplementedError()
	def fs规则(self, a序号 = None, a规则 = None, a操作 = 操作.E操作.e设置):
		v操作 = 操作.f解析操作(a操作)
		if v操作 == 操作.E操作.e设置:
			#不能直接覆盖,先删除旧规则再添加新规则
			if self.m设备.m访问权限 & 文件.E访问权限.e读:
				pass	#未实现
			self.f添加规则(a序号, a规则)
		elif v操作 == 操作.E操作.e修改:
			raise NotImplementedError()
		elif v操作 == 操作.E操作.e添加:
			self.f添加规则(a序号, a规则)
		elif v操作 == 操作.E操作.e删除:
			if a序号:
				self.f删除规则_序号(a序号)
			elif a规则:
				self.f删除规则_规则(a规则)
		else:
			raise NotImplementedError()
#===============================================================================
# 解析
#===============================================================================
class C规则解析器:
	def __init__(self, a文本):
		self.m取词 = 字符串.C推进取词(a文本)
	def f允许(self):
		return self.m取词.f取词推进() == "permit"
	def f协议(self):
		v词 = self.m取词.f取词推进()
		return 南向列表.ca字符串到协议.get(v词, None)
	def f序号4(self):
		return int(self.m取词.f取词推进())
	def f序号6(self):
		self.m取词.f推进()	#"sequence"
		return int(self.m取词.f取词推进())
	def f地址4(self):	#标准4
		"""出现的格式有: "any", "x.x.x.x m.m.m.m"(反掩码), "host x.x.x.x" """
		v词0 = self.m取词.f取词推进()
		if v词0 == "any":
			return None
		elif v词0 == "host":	#主机地址
			v词1 = self.m取词.f取词推进()	#地址
			return 地址.S网络地址4.fc主机地址字符串(v词1)
		else:	#ip地址,后面接通配符
			v词1 = self.m取词.f取词推进()
			v掩码 = 地址.S网络地址4.f反掩码字符串转前缀长度(v词1)
			return 地址.S网络地址4.fc地址前缀长度(v词0, v掩码)
	def f地址6(self):	#六
		v词0 = self.m取词.f取词推进()
		if v词0 == "any":
			return None
		elif v词0 == "host":
			v词1 = self.m取词.f取词推进()
			return 地址.S网络地址6.fc自动(v词1)
		return 地址.S网络地址6.fc自动(v词0)
	def f端口号(self):
		v词0 = self.m取词.f取词()
		if not v词0:	#文本结束,没词了
			return None
		if not "port" in v词0:	#src-port或dst-port
			return None	#不是端口号
		self.m取词.f推进()
		v词1 = self.m取词.f取词推进()	#端口运算符
		vf端口号 = C规则解析器.ca端口号运算函数[v词1]
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