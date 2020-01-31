import cflw代码库py.cflw字符串 as 字符串
import cflw代码库py.cflw网络地址 as 地址
from ..基础接口 import 路由 as 北向路由
from . import 接口 as 实现接口
ca类型 = {
	"Direct": 北向路由.E路由类型.e直连,
	"Static": 北向路由.E路由类型.e静态,
	"RIP": 北向路由.E路由类型.e路由信息类型,
	"OSPF": 北向路由.E路由类型.e开放最短路径优先,
	"BGP": 北向路由.E路由类型.e边界网关类型,
}
class C路由表4:
	"""display ip routing-table"""
	c网络号 = 0
	c类型 = 20
	c优先级 = 28
	c开销 = 33
	c标志 = 43
	c下一跳 = 49
	c接口 = 65
	ca列开始 = (c网络号, c类型, c优先级, c开销, c标志, c下一跳, c接口)
	c标题行 = "Destination/Mask    Proto   Pre  Cost      Flags NextHop         Interface"
	def __init__(self, a文本):
		v位置 = 字符串.f连续找最后(a文本, C路由表4.c标题行, "\n")
		self.m文本 = a文本[v位置+1:]
	def __iter__(self):
		return self.fe行()
	def fe行(self):
		for v行 in self.m文本.split("\n"):
			if len(v行) < C路由表4.c接口:
				continue
			v网络号s, v类型s, v优先级s, v开销s, v标志s, v下一跳s, v接口s = 字符串.fe按位置分割(v行, *C路由表4.ca列开始)
			if v网络号s:	#没有网络号是负载均衡
				v网络号 = 地址.S网络地址4.fc自动(v网络号s)
			v类型 = ca类型[v类型s]
			v优先级 = int(v优先级s)
			v开销 = int(v开销s)
			v下一跳 = 地址.S网络地址4.fc自动(v下一跳s)
			v接口 = 实现接口.f创建接口(v接口s)
			yield 北向路由.S路由条目(a网络号 = v网络号, a下一跳 = v下一跳, a出接口 = v接口, a路由类型 = v类型, a优先级 = v优先级, a度量值 = v开销)
