import enum
import cflw代码库py.cflw字符串 as 字符串
import cflw代码库py.cflw工具_运算 as 运算
class E路由协议(enum.IntEnum):
	#网络层
	e本地 = 0
	e直连 = 1
	e静态 = 2
	e邻居发现协议 = 3	#ndp
	#动态路由协议
	e路由信息协议 = 10	#rip
	e开放最短路径优先 = 11	#ospf
	e边界网关协议 = 12	#bgp
	e增强内部网关路由协议 = 13	#eigrp
	e中间系统到中间系统 = 14	#isis
	#其它
	e按需路由 = 20	#odr
	e下一跳解析协议 = 21	#nhrp
	e移动 = 22
	e定位与身份分离协议 = 23	#lisp
class S路由条目:
	"表示一条路由条目"
	def __init__(self, a网络号, a下一跳, a出接口 = None, a路由协议 = None, a优先级 = None, a度量值 = None, a路由类型 = None):
		self.m网络号 = a网络号
		self.m下一跳 = a下一跳
		self.m出接口 = a出接口
		self.m路由协议 = a路由协议
		self.m优先级 = a优先级
		self.m度量值 = a度量值
		self.m路由类型 = a路由类型
	def __str__(self):
		return 字符串.ft字符串(self.m网络号, self.m下一跳, self.m出接口, self.m路由协议, self.m优先级, self.m度量值, self.m路由类型)
	def f目的相等(self, a路由条目):
		return self.m网络号 == a路由条目.m网络号 
	def f比较优(self, a路由条目):
		"比较优先级和度量值,返回-1,0,1"
		if not self.f目的相等(a路由条目):
			raise ValueError("只有目的相等的2条路由才能比较")
		if self.m优先级 != a路由条目.m优先级:
			return 运算.f反比较(self.m优先级, a路由条目.m优先级)
		if self.m度量值 != a路由条目.m度量值:
			return 运算.f反比较(self.m度量值, a路由条目.m度量值)
		return 0
	def f匹配地址(self, a地址):
		return self.m网络号.fi范围内(a地址)
