import enum
import copy
from typing import *
import cflw代码库py.cflw字符串 as 字符串
import cflw代码库py.cflw工具_运算 as 运算
from . import 协议
#===============================================================================
# 枚举&结构
#===============================================================================
class E字段(enum.Enum):	#访问控制列表摘要表字段
	e列表编号 = 0
	e列表名称 = 1
	e列表类型 = 2
	e是否使用 = 3
	e规则数量 = 10
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
#===============================================================================
# 端口
#===============================================================================
class I生成端口:
	"""把 S端口号 转换成字符串的接口"""
	def __init__(self):
		self.f自动生成运算()
	def __call__(self, a端口)->str:
		v端口 = S端口号.fc自动(a端口)
		if v端口.m运算 == 运算.f大于:
			return self.f大于(v端口.m值)
		elif v端口.m运算 == 运算.f大于等于:
			return self.f大于等于(v端口.m值)
		elif v端口.m运算 == 运算.f小于:
			return self.f小于(v端口.m值)
		elif v端口.m运算 == 运算.f小于等于:
			return self.f小于等于(v端口.m值)
		elif v端口.m运算 == 运算.f包含:
			if type(v端口.m值) == range:
				return self.f范围(v端口.m值)
			else:
				return self.f等于(v端口.m值)
		elif v端口.m运算 == 运算.f不包含:
			return self.f不等于(v端口.m值)
		elif v端口.fi空():
			return self.f空()
		else:
			return self.f其他(v端口.m值)
	def f空(self)->str:
		return ""
	def f等于(self, a序列)->str:
		raise NotImplementedError()
	def f不等于(self, a序列)->str:
		raise NotImplementedError()
	def f大于(self, a值: int)->str:
		raise NotImplementedError()
	def f大于等于(self, a值: int)->str:
		raise NotImplementedError()
	def f小于(self, a值: int)->str:
		raise NotImplementedError()
	def f小于等于(self, a值: int)->str:
		raise NotImplementedError()
	def f范围(self, a值: range)->str:
		raise NotImplementedError()
	def f其他(self, a值)->str:
		return ""
	def f自动生成运算(self):	#在__init__中调用
		c等于 = 0
		c不等于 = 1
		c大于 = 2
		c大于等于 = 3
		c小于 = 4
		c小于等于 = 5
		c范围 = 6
		va重写表 = [	#根据缺少的函数自动生成其它函数, 需要覆盖的为True
			self.__class__.f等于 == I生成端口.f等于,	#0
			self.__class__.f不等于 == I生成端口.f不等于,	#1
			self.__class__.f大于 == I生成端口.f大于,	#2
			self.__class__.f大于等于 == I生成端口.f大于等于,	#3
			self.__class__.f小于 == I生成端口.f小于,	#4
			self.__class__.f小于等于 == I生成端口.f小于等于,	#5
			self.__class__.f范围 == I生成端口.f范围,	#6
		]
		if va重写表[c大于]:
			if not va重写表[c大于等于]:
				self.f大于 = lambda a值: self.f大于等于(a值 + 1)
			elif not va重写表[c范围]:
				self.f大于 = lambda a值: self.f范围(range(a值 + 1, 65536))
		if va重写表[c大于等于]:
			if not va重写表[c大于]:
				self.f大于等于 = lambda a值: self.f大于(a值 - 1)
			elif not va重写表[c范围]:
				self.f大于等于 = lambda a值: self.f范围(range(a值, 65536))
		if va重写表[c小于]:
			if not va重写表[c小于等于]:
				self.f小于 = lambda a值: self.f小于等于(a值 - 1)
			elif not va重写表[c范围]:
				self.f小于 = lambda a值: self.f范围(range(1, a值))
		if va重写表[c小于等于]:
			if not va重写表[c小于]:
				self.f小于等于 = lambda a值: self.f小于(a值 + 1)
			elif not va重写表[c范围]:
				self.f小于等于 = lambda a值: self.f范围(range(1, a值 + 1))
class C生成端口(I生成端口):
	"""把 S端口号 转换成字符串的实现"""
	def f空(self):
		return "∅"
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
c生成端口 = C生成端口()
class S端口号:
	"""一个端口范围"""
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
		elif a == None:
			return S端口号.c空
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
		for k, v in ca端口号符号表.items():
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
	def fi空(self):
		return self.m运算 == None
	def ft字符串(self, a接口 = c生成端口):
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
S端口号.c空 = S端口号(0, None)
ca端口号符号表 = {
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
#===============================================================================
# 规则
#===============================================================================
class S规则:
	"""成员&参数:\n
	动作: bool, 决定动作是permit还是deny\n
	协议: int, 值来自E协议\n
	源地址: S网络地址4\n
	目的地址: S网络地址4\n
	源端口: S端口\n
	目的端口: S端口"""
	#方法
	def __init__(self, a序号 = -1, a动作 = None, a协议 = 协议.E协议.ipv4, a源地址 = None, a目的地址 = None, a源端口 = None, a目的端口 = None, a源虚拟路由 = None, a目的虚拟路由 = None):
		self.m序号 = a序号	#添加规则时不使用该序号,只在解析规则时赋值
		self.m动作 = a动作
		self.m协议 = a协议
		self.m源地址 = a源地址
		self.m目的地址 = a目的地址
		self.m源端口 = a源端口
		self.m目的端口 = a目的端口
		self.m源虚拟路由 = a源虚拟路由	#在华三acl出现过
		self.m目的虚拟路由 = a目的虚拟路由
	def __eq__(self, a):
		"""严格比较两个规则是否完全一样(除了序号)"""
		v类型 = type(a)
		if v类型 == S规则:
			return self.m动作 == a.m动作 and \
				self.m协议 == a.m协议 and \
				self.m源地址 == a.m源地址 and \
				self.m目的地址 == a.m目的地址 and \
				self.m源端口 == a.m源端口 and \
				self.m目的端口 == a.m目的端口 and \
				self.m源虚拟路由 == a.m源虚拟路由 and \
				self.m目的虚拟路由 == a.m目的虚拟路由
		else:
			return False
	def __ior__(self, a规则: "S规则"):
		self.f更新_规则(a规则)
		return self
	def __or__(self, a规则: "S规则"):
		v = copy.copy(self)
		v.__ior__(a规则)
		return v
	def f更新_规则(self, a规则):
		self.m动作 = a规则.m动作 or self.m动作
		self.m协议 = a规则.m协议 or self.m协议
		self.m源地址 = a规则.m源地址 or self.m源地址
		self.m目的地址 = a规则.m目的地址 or self.m目的地址
		self.m源端口 = a规则.m源端口 or self.m源端口
		self.m目的端口 = a规则.m目的端口 or self.m目的端口
		self.m源虚拟路由 = a规则.m源虚拟路由 or self.m源虚拟路由
		self.m目的虚拟路由 = a规则.m目的虚拟路由 or self.m目的虚拟路由
	def __str__(self):
		v = ""
		#序号
		if self.m序号 >= 0:
			v += "序号%d, " % (self.m序号,)
		#允许
		if self.m动作:
			v += "允许, "
		else:
			v += "拒绝, "
		#协议
		if self.m协议:
			v += S规则.ca协议到字符串[self.m协议] + ", "
		#地址
		if self.m源虚拟路由:
			v += f"源虚拟路由{self.m源虚拟路由}, "
		if self.m源地址:
			v += f"源地址{self.m源地址}, "
		if self.m源端口:
			v += f"源端口{self.m源端口}, "
		if self.m目的虚拟路由:
			v += f"目的虚拟路由{self.m目的虚拟路由}, "
		if self.m目的地址:
			v += f"目的地址{self.m目的地址}, "
		if self.m目的端口:
			v += f"目的端口{self.m目的端口}, "
		return v
	#属性
	def fs动作(self, a):
		self.m动作 = bool(a)
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
	def f匹配(self, a协议 = None, a源地址 = None, a源端口 = None, a目的地址 = None, a目的端口 = None):
		"""匹配元组,匹配到返回规则动作,没匹配到返回None"""
		v匹配 = f匹配协议(self.m协议, a协议) and \
			f匹配地址(self.m源地址, a源地址) and \
			f匹配地址(self.m目的地址, a目的地址) and \
			f匹配端口(self.m源端口, a源端口) and \
			f匹配端口(self.m目的端口, a目的端口)
		if v匹配:
			return self.m动作
		else:
			return None
	def f匹配协议(self, a协议)->bool:
		return f匹配协议(self.m协议, a协议)
	def f匹配源地址(self, a地址)->bool:
		return f匹配地址(self.m源地址, a地址)
	def f匹配目的地址(self, a地址)->bool:
		return f匹配地址(self.m目的地址, a地址)
	def f匹配源端口(self, a端口)->bool:
		return f匹配地址(self.m源端口, a端口)
	def f匹配目的端口(self, a端口)->bool:
		return f匹配地址(self.m目的端口, a端口)
	#后置常量
	ca协议到字符串 = {
		协议.E协议.ipv4: "互联网协议第4版",
		协议.E协议.ipv6: "互联网协议第6版",
		协议.E协议.tcp: "传输控制协议",
		协议.E协议.udp: "用户数据报协议",
	}
def f匹配协议(a成员, a匹配)->bool:
	if a成员 == None or a匹配 == None:
		return True
	else:
		return a成员 == a匹配 or 协议.fi包含(a成员, a匹配)
def f匹配地址(a成员, a匹配)->bool:
	if a成员 == None or a匹配 == None:
		return True
	else:
		return a成员.fi范围内(a匹配)
def f匹配端口(a成员, a匹配)->bool:
	if a成员 == None or a匹配 == None:
		return True
	else:
		return a成员.fi范围内(a匹配)
class S统一编号:
	def __init__(self, a统一, a特定 = None, a类型 = None):
		self.m统一编号 = a统一
		self.m特定编号 = a特定
		self.m类型 = a类型
	def __str__(self):
		if self.m特定编号:
			return str(self.m特定编号)
		else:
			return str(self.m统一编号)
	@staticmethod
	def fc特定编号(n, a类型 = None):
		return S统一编号(None, n, a类型)
	@staticmethod
	def fc统一编号(n, a类型 = None):
		return S统一编号(n, None, a类型)
#===============================================================================
# 访问控制列表类
#===============================================================================
class C列表:
	"""一个设备无关的本地的访问控制列表类, 可以从 I列表显示 构造列表对象
	C列表 提供和 I列表显示, I列表配置 一样的函数, 可以当缓存使用"""
	def __init__(self, aa规则 = None):
		if aa规则:
			self.ma规则 = list(aa规则)
		else:	#无参数,创建空列表
			self.ma规则 = []
	def __str__(self):
		return "\n".join(str(x) for x in self.ma规则)
	#读
	def fe规则(self):
		"""遍历规则"""
		return iter(self.ma规则)
	def fg规则(self, a序号)->S规则:
		"""根据规则序号返回规则对象.
		可能存在未排序情况,将遍历全部"""
		for v规则 in self.ma规则:
			if v规则.m序号 == a序号:
				return v规则
		return None
	def f匹配(self, a协议 = None, a源地址 = None, a源端口 = None, a目的地址 = None, a目的端口 = None):
		"""访问控制列表所有规则和数据包匹配,返回匹配到的规则"""
		for v规则 in self.ma规则:
			if v规则.f匹配(a协议, a源地址, a源端口, a目的地址, a目的端口):
				return v规则
	def fe存在序号(self)->Generator[int, None, None]:
		for v规则 in self.ma规则:
			yield v规则.m序号
	def fg空序号(self)->int:
		"""返回一个空序号. 从性能考虑多次获取空序号应调用 fe空序号()"""
		return next(self.fe空序号())
	def fe空序号(self)->Generator[int, None, None]:
		"""返回一个可以不断获得空序号的空序号生成器,从1开始"""
		va存在序号 = list(self.fe存在序号())
		return fe空序号(va存在序号)
	#写
	def f添加规则(self, a序号: int, a规则: S规则):
		"""添加规则, 返回规则引用"""
		v复制规则 = copy.copy(a规则)
		v复制规则.m序号 = a序号
		self.ma规则.append(v复制规则)
		return v复制规则
	def f删除规则(self, a序号: int):
		for v规则 in self.ma规则:
			if v规则.m序号 == a序号:
				self.ma规则.remove(v规则)
				return True
		return False
	def fs规则(self, a序号: int, a规则: S规则, a操作):
		"""添加/设置/删除规则,序号应是必须参数"""
		from . import 操作
		if 操作.fi加操作(a操作):
			self.f添加规则(a序号, a规则)
		else:
			self.f删除规则(a序号)
	#本地列表专用函数
	def f排序(self):	#按照序号排序
		self.ma规则 = sorted(self.ma规则, key = lambda a规则: a规则.m序号)
	def fg索引(self, a序号)->int:
		for i in range(0, len(self.ma规则)):
			v规则 = self.ma规则[i]
			if v规则.m序号 == a序号:
				return i
		return None
#辅助函数
def fe空序号(aa存在序号)->Generator[int, None, None]:
	"""返回一个可以不断获得空序号的空序号生成器,从1开始"""
	v数量 = len(aa存在序号)
	if v数量 == 0:	#没规则
		yield from range(1, 65535)	#华三序号范围0~65534,网络设备脚本保留0,从1开始
	#有规则
	v当前空序号 = 1
	i = 0
	v最后存在序号 = aa存在序号[-1]
	while aa存在序号[i] < v当前空序号:	#可能存在序号从<1数字开始的情况,先递增存在序号
		i += 1
		if i == v数量:
			break
	while v当前空序号 < v最后存在序号:
		while v当前空序号 < aa存在序号[i]:	#和下一存在序号比较
			yield v当前空序号
			v当前空序号 += 1
		if aa存在序号[i] == v当前空序号:
			v当前空序号 += 1
			i += 1
			continue
	yield from range(v最后存在序号 + 1, 65535)
#===============================================================================
# 接口
#===============================================================================
class I列表显示:
	c模式名 = "访问控制列表显示模式"
	def fc本地列表(self)->C列表:
		"""从当前模式构造本地访问控制列表对象"""
		return C列表(self.fe规则())
	def fe规则(self)->Generator[S规则, None, None]:
		"""遍历规则"""
		raise NotImplementedError()
	def fg规则(self, a序号)->S规则:
		"""根据规则序号返回规则对象"""
		raise NotImplementedError()
	def f匹配(self, a协议 = None, a源地址 = None, a源端口 = None, a目的地址 = None, a目的端口 = None):
		"""访问控制列表所有规则和数据包匹配,返回匹配到的规则"""
		for v规则 in self.fe规则():
			if v规则.f匹配(a协议, a源地址, a源端口, a目的地址, a目的端口):
				return v规则
	def fe存在序号(self)->Generator[int, None, None]:
		"""生成已存在规则的序号"""
		for v规则 in self.fe规则():
			yield v规则.m序号
	def fg空序号(self)->int:
		"""返回一个空序号. 仅限每次登录设备只获取一次空序号时使用, 多次获取空序号应调用 fe空序号()"""
		return next(self.fe空序号())
	def fe空序号(self)->Generator[int, None, None]:
		"""返回一个可以不断获得空序号的空序号生成器,从1开始"""
		va存在序号 = list(self.fe存在序号())
		return fe空序号(va存在序号)
class I列表配置:
	c模式名 = "访问控制列表配置模式"
	def fs规则(self, a序号, a规则, a操作):
		"""添加/设置/删除规则,序号应是必须参数"""
		raise NotImplementedError()
	def f应用到(self, a模式, a方向, a操作):
		"""当前访问控制列表应用到其他模式"""
		raise NotImplementedError()
class I助手:
	"用来计算到目的设备的访问控制列表编号, 原始参数的n从0开始"
	@staticmethod
	def ft特定编号(n, a类型):
		return n
	@staticmethod
	def ft统一编号(n, a类型 = None):
		return n
	@staticmethod
	def f判断类型(n):
		"根据特定编号判断类型"
		raise NotImplementedError()
