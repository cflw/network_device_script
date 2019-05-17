import cflw代码库py.cflw工具_序列 as 序列
import enum
import copy
import re
#===============================================================================
# 接口基础
#===============================================================================
c接口正则 = re.compile(r"\w+\d+(\/\d+)*(\.\d+)?")	#字母加数字就是接口
class E接口(enum.IntEnum):#为保证取接口全名有个优先级顺序，高位16位为优先级
	e无 = 0x00000000	#没有接口名的无接口
	e空 = 0x00000001	#只丢包的空接口
	e管理 = 0x00000002
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
class E接口分类(enum.IntEnum):
	e空 = 0
	e环回 = 1
	e以太网 = 2
	e串行 = 3
	e虚拟局域网 = 4
	e隧道 = 5
ca接口名称 = {
	E接口.e空: "Null",
	E接口.e环回: "Loopback",
	E接口.e以太网: "Ethernet",
	E接口.e快速以太网: "FastEthernet",
	E接口.e吉以太网: "GigabitEthernet",
	E接口.e十吉以太网: "TenGigabitEthernet",
	E接口.e串行: "Serial",
	E接口.e虚拟局域网: "Vlan",
	E接口.e隧道: "Tunnel",
	E接口.e以无源光网络: "EPON",
	E接口.e吉无源光网络: "GPON",
	E接口.e无线电: "Radio",
	E接口.e局域网: "LAN",
	E接口.e广域网: "WAN",
}
def fc接口名称字典(a字典 = None):
	v字典 = copy.copy(ca接口名称)
	if a字典:
		v字典.update(a字典)
	return v字典
#接口结构
class S接口:
	"表示一个接口"
	def __init__(self, a类型: int, a名称: str, aa序号: tuple, a子序号 = 0):
		self.m类型 = int(a类型)
		self.m名称 = str(a名称)
		self.ma序号 = tuple(aa序号)
		self.m子序号 = int(a子序号)
	def __str__(self):
		if self.m名称:
			return self.m名称 + self.fg序号字符串()
		else:
			return self.ft字符串(ca接口名称)
	def __eq__(self, a):
		if isinstance(a, S接口):
			return (self.m类型 == a.m类型) and (self.ma序号 == a.ma序号)
		else:
			return False
	@staticmethod
	def fc字符串(a字符串, a全称字典 = ca接口名称, ai字典字符串在右 = True):
		if ai字典字符串在右:
			v字典 = a全称字典
		else:
			v字典 = 序列.f字典键值反转(a全称字典)	#字典左右对调
		v类型, v名称 = S接口.f解析_取全称(a字符串, v字典)
		v序号, v子序号 = S接口.f解析_取序号(a字符串)
		return S接口(v类型, v名称, v序号, v子序号)
	@staticmethod
	def fc标准(a类型, *a序号, a子序号 = 0):
		"(类型,*序号,子序号)"
		return S接口(a类型, "", a序号, a子序号)
	def fg序号字符串(self):
		"包含子序号"
		#转成字符串列表
		v列表 = list(self.ma序号)
		v子序号 = self.m子序号
		for i in range(len(v列表)):
			v = v列表[i]
			if type(v) == range:
				v列表[i] = str(v.start) + "-" + str(v.stop - 1)
			else:
				v列表[i] = str(v)
		s = '/'.join(v列表)
		if v子序号:
			s += '.' + str(v子序号)
		return s
	@staticmethod
	def f解析_取全称(a: str, a字典 = ca接口名称.items()):
		"提取接口字符串的名称部分,根据字典取全称"
		v类型 = type(a字典)
		if hasattr(a字典, "__iter__"):
			v列表 = a字典
		else:
			raise TypeError()
		v名称 = S接口.f解析_取名称(a)
		#找前面匹配, 无优先级版本见 cflw字符串.f找前面匹配
		v正则 = re.compile(r"^" + v名称, re.IGNORECASE)
		v目标 = None
		v优先级 = -1
		for k, v in a字典.items():	#k=E接口,v=字符串
			if type(v) != str:
				raise TypeError("元素类型必须是字符串")
			if a == v:	#完全相等
				return (k, v)
			elif re.search(v正则, v):
				v匹配优先级 = k // 0x10000
				if v匹配优先级 > v优先级:
					v优先级 = v匹配优先级
					v目标 = (k, v)
		if v目标:
			return v目标
		else:
			raise RuntimeError("未找到")
	@staticmethod
	def f解析_取名称(a):
		"提取接口字符串的名称部分"
		return re.split(r"\d", a)[0].strip()
	@staticmethod
	def f解析_取序号(a):
		"提取接口字符串的序号部分,返回列表,包含子序号"
		c数字正则 = re.compile(r"\d+.*")
		if not c数字正则.search(a):	#找不到数字,返回0
			return [0], 0
		v列表 = a.split("/")
		#[0]去字符,保留数字
		v列表[0] = c数字正则.findall(v列表[0])[0]
		#[-1]判断子序号
		if "." in v列表[-1]:
			v分割 = v列表[-1].split(".")
			v列表[-1] = v分割[0]
			v子序号 = int(v分割[1])
		else:
			v子序号 = 0
		#转成int,range
		v长度 = len(v列表)
		for i in range(v长度):
			v = v列表[i]
			if "-" in v:
				v分割 = v.split("-")
				v列表[i] = range(int(v分割[0]), int(v分割[1])+1)
			else:
				v列表[i] = int(v)
		return v列表, v子序号
	def fi范围(self):
		for v序号 in self.ma序号:
			if type(v序号) == range:
				return True
		if type(self.m子序号) == range:
			return True
		return False
	def fs名称(self, a):
		v类型 = type(a)
		if v类型 == str:
			self.m名称 = a
		elif v类型 == dict:
			self.m名称 = a[self.m类型]
		else:
			raise TypeError("无法识别的参数")
	def fg名称(self, a字典 = None):
		"根据类型值查字典取名称"
		if a字典:
			return a字典[self.m类型]
		elif self.m名称:
			return self.m名称
		else:
			return ca接口名称[self.m类型]
	def ft字符串(self, a字典 = ca接口名称):
		return self.fg名称(a字典) + self.fg序号字符串()
	def fg主序号数(self):
		return len(self.ma序号) - 1
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
					v接口0 = S接口(self.m类型, self.m名称, self.ma序号, j)
					yield v接口0
			else:
				v接口0 = self
				yield v接口0
		else:	#递归
			v指定序号 = self.ma序号[i]
			if type(v指定序号) == range:
				for j in v指定序号:
					va新序号 = self.ma序号[:i] + (j,) + self.ma序号[i+1:]
					v接口0 = S接口(self.m类型, self.m名称, va新序号, self.m子序号)
					for v接口1 in v接口0.fe接口(i+1):
						yield v接口1
			else:
				v接口0 = self
				for v接口1 in v接口0.fe接口(i+1):
					yield v接口1
	def fg指定序号接口(self, af取值):
		va序号 = []
		for v in self.ma序号:
			va序号.append(af取值(v))
		v子序号 = af取值(self.m子序号)
		return S接口(self.m类型, self.m名称, va序号, v子序号)
	def fg头接口(self):
		return self.fg指定序号接口(lambda a: a.start if type(a) == range else a)
	def fg尾接口(self):
		return self.fg指定序号接口(lambda a: (a.stop - 1) if type(a) == range else a)
class F创建接口:
	def __init__(self, a全称字典 = ca接口名称):
		self.m全称字典 = a全称字典
	def __call__(self, a):
		v类型 = type(a)
		if v类型 == S接口:
			v = copy.copy(a)
			v.m名称 = self.m全称字典[v.m类型]
			return v
		elif isinstance(a, I接口配置):
			v = copy.copy(a.m接口)
			v.m名称 = self.m全称字典[v.m类型]
			return v
		elif v类型 == str:
			return S接口.fc字符串(a, self.m全称字典)
		else:
			raise TypeError("无法解析的类型")
#===============================================================================
# 接口配置
#===============================================================================
class I接口配置:	#常见的接口配置
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