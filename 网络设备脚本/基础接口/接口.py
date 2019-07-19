import cflw代码库py.cflw工具_序列 as 序列
import enum
import copy
import re
#===============================================================================
# 接口基础
#===============================================================================
c接口正则 = re.compile(r"\w+\d+(\/\d+)*(\.\d+)?")	#字母加数字就是接口
c数字正则 = re.compile(r"\d+.*")
class E类型(enum.IntEnum):#为保证取接口全名有个优先级顺序，高位16位为优先级
	e无 = 0x00000000	#没有接口名的无接口
	e空 = 0x00000001	#只丢包的空接口
	e管理 = 0x00000002
	e堆叠 = 0x00000003
	e环回 = 0x00000100
	e内部 = 0x00000101	#inloop,在华三中出现
	e十兆以太网 = 0x00000210	#10M=10'000'000
	e以太网 = e十兆以太网
	e百兆以太网 = 0x00000220	#100M=100'000'000
	e快速以太网 = e百兆以太网
	e吉以太网 = 0x00000230	#1G=1'000M=1'000'000'000
	e千兆以太网 = e吉以太网
	e十吉以太网 = 0x00000240	#10G=10'000M=10'000'000'000
	e万兆以太网 = e十吉以太网
	e四万兆以太网 = 0x00000244
	e百吉以太网 = 0x00000250	#100G=100'000M=100'000'000'000
	e十万兆以太网 = 0x00000250
	e太以太网 = 0x00000260	#1T=1'000G=1'000'000'000'000
	e百万兆以太网 = 0x00000260
	e十太以太网 = 0x00000270	#10T=10'000G=10'000'000'000'000
	e百太以太网 = 0x00000280	#100T=100'000G=10'000'000'000'000
	e拍以太网 = 0x00000290	#1P=1'000T
	e串行 = 0x00000400
	e虚拟局域网 = 0x00000500
	e聚合 = 0x00000501
	e隧道 = 0x00000600
	e注册隧道 = 0x00000601	#在华三中出现
	qx = 0x000f0700	#在中兴m6000中出现
	qx以太网 = 0x00000701	#在中兴m6000中出现
	e无源光网络 = 0x00000800	#pon
	e以无源光网络 = 0x00000801	#epon
	e吉无源光网络 = 0x00000802	#gpon
	e无线电 = 0x00000900
	e局域网 = 0x00001010
	e广域网 = 0x00001011
class E分类(enum.IntEnum):
	e空 = 0
	e环回 = 1
	e以太网 = 2
	e串行 = 3
	e虚拟局域网 = 4
	e隧道 = 5
ca接口名称 = {
	E类型.e空: "Null",
	E类型.e环回: "Loopback",
	E类型.e以太网: "Ethernet",
	E类型.e快速以太网: "FastEthernet",
	E类型.e吉以太网: "GigabitEthernet",
	E类型.e十吉以太网: "TenGigabitEthernet",
	E类型.e四万兆以太网: "FortyGigabitEthernet",
	E类型.e串行: "Serial",
	E类型.e虚拟局域网: "Vlan",
	E类型.e隧道: "Tunnel",
	E类型.e以无源光网络: "EPON",
	E类型.e吉无源光网络: "GPON",
	E类型.e无线电: "Radio",
	E类型.e局域网: "LAN",
	E类型.e广域网: "WAN",
}
def fc接口名称字典(a字典 = None):
	v字典 = copy.copy(ca接口名称)
	if a字典:
		v字典.update(a字典)
	return v字典
#===============================================================================
# 接口结构&类
#===============================================================================
class S接口:
	"表示一个接口"
	def __init__(self, a类型: int, aa序号: tuple, a子序号 = 0):
		self.m类型 = int(a类型)
		self.ma序号 = tuple(aa序号)
		self.m子序号 = int(a子序号)
	def __str__(self):
		return f"""{self.m类型} {"/".join(self.ma序号)} .{self.m子序号}"""
	def __repr__(self):
		return f"S接口({self.m类型}, {self.ma序号}, {self.m子序号})"
	def __eq__(self, a):
		if isinstance(a, S接口):
			return (self.m类型 == a.m类型) and (self.ma序号 == a.ma序号)
		elif isinstance(a, C接口):
			return self == a.m接口
		else:
			return False
	@staticmethod
	def fc标准(a类型, *a序号, a子序号 = 0):
		"(类型,*序号,子序号)"
		return S接口(a类型, "", a序号, a子序号)
	def fi范围(self):
		for v序号 in self.ma序号:
			if type(v序号) == range:
				return True
		if type(self.m子序号) == range:
			return True
		return False
	def fg序号数(self):
		return len(self.ma序号)
	def fg序号(self, i):
		return self.ma序号[i]
	def fg序号组(self):
		return self.ma序号
	def fg分类(self):
		#取类型的16进制的低3,4位
		return self.m类型 % 0x10000 // 0x10
	def fi属于分类(self, *a分类):
		v值 = self.fg分类()
		for v in a分类:
			v分类 = int(v)
			if v值 == v分类:
				return True
		return False
	def fi只有末尾序号是范围(self):
		for v序号 in self.ma序号[:-1]:
			if type(v序号) == range:
				return False
		return type(self.ma序号[-1]) == range
	def fe接口(self, i = 0):
		if i == len(self.ma序号):	#结束
			v指定序号 = self.m子序号
			if type(v指定序号) == range:
				for j in v指定序号:
					v接口0 = S接口(self.m类型, self.ma序号, j)
					yield v接口0
			else:
				v接口0 = self
				yield v接口0
		else:	#递归
			v指定序号 = self.ma序号[i]
			if type(v指定序号) == range:
				for j in v指定序号:
					va新序号 = self.ma序号[:i] + (j,) + self.ma序号[i+1:]
					v接口0 = S接口(self.m类型, va新序号, self.m子序号)
					for v接口1 in v接口0.fe接口(i+1):
						yield v接口1
			else:
				v接口0 = self
				for v接口1 in v接口0.fe接口(i+1):
					yield v接口1
	def fg指定序号接口(self, af取值):
		va序号 = list(af取值(v) for v in self.ma序号)
		v子序号 = af取值(self.m子序号)
		return S接口(self.m类型, va序号, v子序号)
	def fg头接口(self):
		return self.fg指定序号接口(S接口.f头序号)
	def fg尾接口(self):
		return self.fg指定序号接口(S接口.f尾序号)
	@staticmethod
	def f头序号(a):
		if type(a) == range:
			return a.start
		else:
			return a
	@staticmethod
	def f尾序号(a):
		if type(a) == range:
			return a.stop - 1
		else:
			return a
class C接口:
	"""复杂接口类, 包含接口的各种详细信息"""
	def __init__(self, a接口, a名称, af生成接口):
		self.m接口 = a接口
		if a名称:
			self.m名称 = a名称
		else:
			self.m名称 = aa接口名称[a接口.m类型]
		self.mf生成接口 = af生成接口
	def __str__(self):
		return self.mf生成接口(self.m接口)
	def __eq__(self, a):
		if isinstance(a, S接口):
			return self.m接口 == a
		elif isinstance(a, C接口):
			return self.m接口 == a.m接口
		else:
			return False
	def f新基(self, a基接口: S接口):
		"""创建一个新的 C接口 对象, 其中只有 self.m接口 不同"""
		return C接口(a基接口, self.m名称, self.mf生成接口)
	def fe接口(self):
		for v基接口 in self.m接口.fe接口():
			yield self.f新基(v基接口)
	def fg序号数(self):
		return self.m接口.fg序号数()
	def fg序号(self, i):
		return self.m接口.fg序号(i)
	def fg序号组(self):
		return self.m接口.fg序号组()
	def fi范围(self):
		return self.m接口.fi范围()
	def fi属于分类(self, *a分类):
		return self.m接口.fi属于分类(*a分类)
#===============================================================================
# 处理接口字符串
#===============================================================================
class F创建接口:
	"""把字符串转换成接口对象的类"""
	def __init__(self, aa接口名称, af生成接口 = None):
		self.ma接口名称 = aa接口名称
		if af生成接口:
			self.mf生成接口 = af生成接口
		else:
			self.mf生成接口 = F生成接口(aa接口名称)
	def __call__(self, a):
		v类型 = type(a)
		if v类型 == S接口:
			return C接口(a接口 = a, a名称 = None, aa接口名称 = self.ma接口名称)
		elif isinstance(a, C接口):
			return a
		elif hasattr(a, "fg接口"):
			return a.fg接口()
		elif v类型 == str:
			return self.f创建(a)
		else:
			raise TypeError("无法解析的类型")
	def f创建(self, a字符串):
		v名称s, v总序号s = self.f提取名称和序号(a字符串)
		v类型, v名称 = self.f解析名称(v名称s)
		va序号s = self.f分隔序号(v总序号s)
		va序号s[-1], v子序号s = self.f提取尾序号和子序号(va序号s[-1])
		va序号 = list(self.f解析序号(v) for v in va序号s)
		v子序号 = self.f解析子序号(v子序号s)
		v接口值 = S接口(v类型, va序号, v子序号)
		v接口对象 = C接口(v接口值, v名称, self.mf生成接口)
		return v接口对象
	def f提取名称和序号(self, a字符串):
		va数字 = c数字正则.findall(a字符串)
		if not va数字:	#找不到数字
			v名称 = a字符串
			v序号 = ""
		else:
			v数字位置 = a字符串.find(va数字[0])
			v名称 = a字符串[: v数字位置]
			v序号 = a字符串[v数字位置 :]
		return v名称.strip(), v序号
	def f提取尾序号和子序号(self, a字符串):
		v点位置 = a字符串.find(".")
		if v点位置 < 0:
			return a字符串, "0"
		else:
			return a字符串[: v点位置], a字符串[v点位置+1 :]
	def f解析名称(self, a字符串):
		v正则 = re.compile(r"^" + a字符串, re.IGNORECASE)
		v目标 = None
		v优先级 = -1
		for k, v in self.ma接口名称.items():	#k=E类型,v=字符串
			if type(v) != str:
				raise TypeError("元素类型必须是字符串")
			if a字符串 == v:	#完全相等
				return (k, v)
			elif re.search(v正则, v):
				v匹配优先级 = k // 0x10000
				if v匹配优先级 > v优先级:
					v优先级 = v匹配优先级
					v目标 = (k, v)
		if v目标:
			return v目标
		else:
			raise RuntimeError("找不到名称\"" + a字符串 + "\"")
	def f分隔序号(self, a字符串):
		if not a字符串:
			return [0]
		return a字符串.split(self.f分隔符())
	def f解析序号(self, a字符串):
		if "-" in a字符串:
			v分割 = a字符串.split("-")
			return range(int(v分割[0]), int(v分割[1])+1)
		else:
			return int(a字符串)
	def f解析子序号(self, a字符串):
		return self.f解析序号(a字符串)
	def f分隔符(self):
		return "/"
class F生成接口:
	"""把接口对象转换成字符串的类"""
	def __init__(self, aa接口名称):
		self.ma接口名称 = aa接口名称
	def __call__(self, a):
		v类型 = type(a)
		if isinstance(a, S接口):
			return self.f生成(a)
		if isinstance(a, C接口):
			return self.f生成(a.m接口)
		elif hasattr(a, "fg接口"):
			v接口 = a.fg接口()
			return self.f生成(v接口.m接口)
		else:
			raise TypeError("无法解析的类型")
	def f生成(self, a接口: S接口):
		v名称 = self.f生成名称(a接口.m类型)
		va序号 = list(self.fe生成序号组(a接口.ma序号))
		if a接口.m子序号:
			v子序号s = self.f生成子序号(a接口.m子序号)
		else:
			v子序号s = ""
		return v名称 + self.f分隔符().join(va序号) + v子序号s
	def f生成名称(self, a类型):
		return self.ma接口名称[a类型]
	def fe生成序号组(self, a序号组):
		for v序号 in a序号组:
			v序号类型 = type(v序号)
			if v序号类型 == int:
				v序号s = self.f生成序号(v序号)
			elif v序号类型 == range:
				v序号s = self.f生成范围(v序号)
			else:
				raise TypeError()
			yield v序号s
	def f生成序号(self, a序号):
		return str(a序号)
	def f生成范围(self, a范围):
		return f"{a范围.start}-{a范围.stop - 1}"
	def f生成子序号(self, a序号):
		return "." + str(a序号)
	def f分隔符(self):
		return "/"
f生成接口 = F生成接口(ca接口名称)
f创建接口 = F创建接口(ca接口名称, f生成接口)
#===============================================================================
# 接口配置
#===============================================================================
class I接口配置:	#常见的接口配置
	def fg接口(self):
		"必需返回 C接口 对象"
		raise NotImplementedError()
	#模式
	def f模式_虚拟局域网(self):
		raise NotImplementedError()
	def f模式_端口安全(self):
		raise NotImplementedError()
	def f模式_生成树(self):
		raise NotImplementedError()
	def f模式_路由信息协议(self, a进程号, a版本):
		raise NotImplementedError()
	def f模式_开放最短路径优先(self, a进程号, a版本):
		raise NotImplementedError()
	def f模式_增强内部网关路由协议(self, a版本):
		raise NotImplementedError()
	def f模式_中间系统到中间系统(self, a版本):
		raise NotImplementedError()
	#接口
	def fs开关(self, a操作):	#可以填True/False,也可以填 E操作 值
		raise NotImplementedError()
	def fs描述(self, a描述, a操作):
		raise NotImplementedError()
	#以太网
	def fs速率(self, a速率, a操作):
		raise NotImplementedError()
	def fs双工模式(self, a全双工, a操作):
		raise NotImplementedError()
	def fs巨帧(self, a操作):
		raise NotImplementedError()
	#三层
	def fs网络地址4(self, a地址, a操作):
		raise NotImplementedError()
	def fe网络地址4(self):
		"返回这个接口拥有的所有地址"
		raise NotImplementedError()
	def fs网络地址6(self, a地址, a操作):
		raise NotImplementedError()
	def fe网络地址6(self):
		raise NotImplementedError()
	#主机接口
	def fs默认网关4(self, a地址, a操作):
		raise NotImplementedError()
	def fs默认网状6(self, a地址, a操作):
		raise NotImplementedError()
	def fs域名服务器4(self, *a地址, a操作):
		raise NotImplementedError()
	def fs域名服务器6(self, *a地址, a操作):
		raise NotImplementedError()
	#串行口
	def fs时钟频率(self, a频率, a操作):
		raise NotImplementedError()
	#流量控制
	def fs访问控制列表(self, a访问控制列表, a方向, a操作):
		raise NotImplementedError()
	def fs服务质量(self, a, a方向, a操作):
		raise NotImplementedError()