import enum
import cflw代码库py.cflw字符串 as 字符串
import cflw代码库py.cflw工具_运算 as 运算
from . import 协议
#===============================================================================
# 枚举&结构
#===============================================================================
class E类型(enum.IntEnum):
	e类型 = 0x1000
	e物理 = 0x2000
	mac = e物理
	e标准4 = 0x3040
	e扩展4 = 0x3041
	e标准6 = 0x3060
	e扩展6 = 0x3061
	e多协议标签交换 = 0x4000
	mpls = e多协议标签交换
class I端口号到字符串:
	def f等于(self, a序列):
		raise NotImplementedError()
	def f不等于(self, a序列):
		raise NotImplementedError()
	def f大于(self, a值):
		raise NotImplementedError()
	def f大于等于(self, a值):
		return self.f大于(a值 - 1)
	def f小于(self, a值):
		raise NotImplementedError()
	def f小于等于(self, a值):
		return self.f小于(a值 + 1)
	def f范围(self, a值):
		raise NotImplementedError()
class C端口号到字符串(I端口号到字符串):
	def f大于(self, a值):
		return ">" + str(a值)
	def f大于等于(self, a值):
		return "≥" + str(a值)
	def f小于(self, a值):
		return "<" + str(a值)
	def f小于等于(self, a值):
		return "≤" + str(a值)
	def f等于(self, a序列):
		return "=" + " ".join(字符串.ft字符串序列(a序列))
	def f不等于(self, a序列):
		return "≠" + " ".join(字符串.ft字符串序列(a序列))
	def f范围(self, a值: range):
		return "%d~%d" % (a值.start, a值.stop - 1)
c端口号到字符串 = C端口号到字符串()
class S端口号:
	def __init__(self, a值, a运算):
		self.m运算 = a运算
		self.m值 = a值
	def __str__(self):
		return self.ft字符串()
	@staticmethod
	def fc自动(a):
		v类型 = type(a)
		if v类型 == S端口号:
			return a
		elif v类型 == int:
			return S端口号.fc等于(a)
		elif v类型 == range:
			return S端口号.fc范围(a)
		elif v类型 in (tuple, list):
			return S端口号.fc等于(*v类型)
		elif v类型 == str:
			return S端口号.fc字符串(a)
		else:
			raise TypeError("无法解析的类型")
	@staticmethod
	def fc字符串(a: str):
		#纯数字
		if a.isdigit():
			return S端口号.fc等于(int(a))
		#区间
		if 字符串.fi连续范围(a) or 字符串.fi区间范围(a):
			return S端口号.fc范围(字符串.ft范围(a))
		#"符号 数字"的格式
		ca符号表 = {
			"==": S端口号.fc等于,
			">=": S端口号.fc大于等于,
			"<=": S端口号.fc小于等于,
			"!=": S端口号.fc不等于,
			"<>": S端口号.fc不等于,
			">": S端口号.fc大于,
			"≥": S端口号.fc大于等于,
			"<": S端口号.fc小于,
			"≤": S端口号.fc小于等于,
			"=": S端口号.fc等于,
			"≠": S端口号.fc不等于,
		}
		for k, v in ca符号表.items():
			v符号长度 = len(k)
			v符号 = a[0 : v符号长度]
			if k == v符号:
				v数字 = int(a[v符号长度 : ])
				return v(v数字)
		#其它
		raise ValueError("无法解析的格式")
	@staticmethod
	def fc大于(a值):
		return S端口号(a值, 运算.f大于)
	@staticmethod
	def fc大于等于(a值):
		return S端口号(a值, 运算.f大于等于)
	@staticmethod
	def fc小于(a值):
		return S端口号(a值, 运算.f小于)
	@staticmethod
	def fc小于等于(a值):
		return S端口号(a值, 运算.f小于等于)
	@staticmethod
	def fc范围(a值):
		return S端口号(a值, 运算.f包含)
	@staticmethod
	def fc等于(*a值):	#慎用多值,只有思科ipv4扩展访问控制列表支持多值
		return S端口号(a值, 运算.f包含)
	@staticmethod
	def fc不等于(*a值):	#慎用,只有思科支持不等于
		return S端口号(a值, 运算.f不包含)
	def fi范围内(self, a):
		return self.m运算(self.m值, a)
	def ft字符串(self, a接口 = c端口号到字符串):
		if self.m运算 == 运算.f大于:
			return a接口.f大于(self.m值)
		elif self.m运算 == 运算.f大于等于:
			return a接口.f大于等于(self.m值)
		elif self.m运算 == 运算.f小于:
			return a接口.f小于(self.m值)
		elif self.m运算 == 运算.f小于等于:
			return a接口.f小于等于(self.m值)
		elif self.m运算 == 运算.f包含:
			if type(self.m值) == range:
				return a接口.f范围(self.m值)
			else:
				return a接口.f等于(self.m值)
		elif self.m运算 == 运算.f不包含:
			return a接口.f不等于(self.m值)
		else:
			return ""
class S规则:
	"""成员&参数:\n
	允许: bool, 决定动作是permit还是deny\n
	协议: int, 值来自E协议\n
	源地址: S网络地址4\n
	目标地址: S网络地址4\n
	源端口: S端口\n
	目标端口: S端口"""
	#方法	--------------------------------------------------------------------
	def __init__(self, **a):
		self.m序号 = -1	#添加规则时不使用该序号,解析规则时赋值
		self.m允许 = None
		self.m协议 = 协议.E协议.ip
		self.m源地址 = None
		self.m目的地址 = None
		self.m源端口 = None
		self.m目的端口 = None
		self.f更新(**a)
	def f更新(self, a规则 = None, **a字典):
		if a规则:
			self.f更新_规则(a规则)
		self.f更新_字典(a字典)
	def f更新_规则(self, a规则):
		self.m允许 = a规则.m允许 if a规则.m允许 else self.m允许
		self.m协议 = a规则.m协议 if a规则.m协议 else self.m协议
		self.m源地址 = a规则.m源地址 if a规则.m源地址 else self.m源地址
		self.m目的地址 = a规则.m目的地址 if a规则.m目的地址 else self.m目的地址
		self.m源端口 = a规则.m源端口 if a规则.m源端口 else self.m源端口
		self.m目的端口 = a规则.m目的端口 if a规则.m目的端口 else self.m目的端口
	def f更新_字典(self, a字典):
		for k, v in S规则.ca更新函数.items():
			if k in a字典:
				v(self, a字典[k])
	def __str__(self):
		v = ""
		#序号
		if self.m序号 >= 0:
			v += "序号%d, " % (self.m序号,)
		#允许
		if self.m允许:
			v += "允许, "
		else:
			v += "拒绝, "
		#协议
		v += S规则.ca协议到字符串[self.m协议] + ", "
		#地址
		if self.m源地址:
			v += "源地址%s, " % (self.m源地址,)
		if self.m源端口:
			v += "源端口%s, " % (self.m源端口,)
		if self.m目的地址:
			v += "目的地址%s, " % (self.m目的地址,)
		if self.m目的端口:
			v += "目的端口%s, " % (self.m目的端口,)
		return v
	#属性
	def fs允许(self, a):
		self.m允许 = bool(a)
	def fs协议(self, a协议):
		self.m协议 = a协议
	def fs源地址(self, a地址):
		self.m源地址 = a地址
	def fs目的地址(self, a地址):
		self.m目的地址 = a地址
	def fs源端口(self, a端口):
		self.m源端口 = a端口
	def fs目的端口(self, a端口):
		self.m目的端口 = a端口
	#计算
	def f匹配(self, a源地址 = None, a源端口 = None, a目的地址 = None, a目的端口 = None):
		def f匹配0(a成员, a匹配):
			if a成员 != None and a匹配 != None:
				return a成员.fi范围内(a匹配)
			else:
				return True
		v匹配源地址 = f匹配0(self.m源地址, a源地址)
		v匹配目的地址 = f匹配0(self.m目的地址, a目的地址)
		v匹配源端口 = f匹配0(self.m源端口, a源端口)
		v匹配目的端口 = f匹配0(self.m目的端口, a目的端口)
		v匹配 = v匹配源地址 and v匹配目的地址 and v匹配源端口 and v匹配目的端口
		if v匹配:
			return self.m允许
		else:
			return None
	def f匹配源地址(self, a地址):
		return self.m源地址.fi范围内(a地址) if self.m源地址 else True
	def f匹配目的地址(self, a地址):
		return self.m目的地址.fi范围内(a地址) if self.m目的地址 else True
	def f匹配源端口(self, a端口):
		return self.m源端口.fi范围内(a端口) if self.m源端口 else True
	def f匹配目的端口(self, a端口):
		return self.m目的端口.fi范围内(a端口) if self.m目的端口 else True
	#后置常量
	ca更新函数 = {
		"a允许": fs允许,
		"a协议": fs协议,
		"a源地址": fs源地址,
		"a目的地址": fs目的地址,
		"a源端口": fs源端口,
		"a目的端口": fs目的端口,
	}
	ca协议到字符串 = {
		协议.E协议.ip: "互联网协议第4版",
		协议.E协议.ipv6: "互联网协议第6版",
		协议.E协议.tcp: "传输控制协议",
		协议.E协议.udp: "用户数据报协议",
	}
c空序号 = -1
c空规则 = S规则(a允许 = False)	#拒绝所有
class S统一序号:
	def __init__(self, a统一, a特定 = None, a类型 = None):
		self.m统一序号 = a统一
		self.m特定序号 = a特定
		self.m类型 = a类型
	def __str__(self):
		if self.m特定序号:
			return str(self.m特定序号)
		else:
			return str(self.m统一序号)
	@staticmethod
	def fc特定序号(n, a类型 = None):
		return S统一序号(None, n, a类型)
	@staticmethod
	def fc统一序号(n, a类型 = None):
		return S统一序号(n, None, a类型)
#===============================================================================
# 接口
#===============================================================================
class I列表配置:
	c模式名 = "访问控制列表配置模式"
	def fs规则(self, a序号, a规则, a操作):
		raise NotImplementedError()
	def fe规则(self):
		raise NotImplementedError()
	def fg规则(self, a序号):
		raise NotImplementedError()
	def f应用到(self, a模式, a方向, a操作):
		raise NotImplementedError()
class I助手:
	"用来计算到目标设备的访问控制列表序号, 原始参数的n从0开始"
	@staticmethod
	def ft特定序号(n, a类型):
		return n
	@staticmethod
	def ft统一序号(n, a类型 = None):
		return n
	@staticmethod
	def f判断类型(n):
		"根据特定序号判断类型"
		raise NotImplementedError()