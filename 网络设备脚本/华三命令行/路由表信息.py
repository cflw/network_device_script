import cflw代码库py.cflw字符串 as 字符串
import cflw代码库py.cflw网络地址 as 地址
from ..基础接口 import 接口 as 北向接口
from ..基础接口 import 路由 as 北向路由
from . import 接口 as 实现接口
ca协议 = {
	"Direct": 北向路由.E路由协议.e直连,
	"Static": 北向路由.E路由协议.e静态,
	"RIP": 北向路由.E路由协议.e路由信息协议,
	"OSPF": 北向路由.E路由协议.e开放最短路径优先,
	"BGP": 北向路由.E路由协议.e边界网关协议,
}
class C路由表4:
	"""display ip routing-table
	适用于: msr36系列"""
	c网络号 = 0
	c协议 = 19
	c优先级 = 27
	c开销 = 31
	c下一跳 = 43
	c接口 = 59
	ca列开始 = (c网络号, c协议, c优先级, c开销, c下一跳, c接口)
	c标题行 = "Destination/Mask   Proto   Pre Cost        NextHop         Interface"
	def __init__(self, a文本):
		v位置 = 字符串.f连续找最后(a文本, C路由表4.c标题行, "\n")
		self.m文本 = a文本[v位置+1:]
	def __iter__(self):
		return self.fe行()
	def fe行(self):
		for v行 in self.m文本.split("\n"):
			if len(v行) < C路由表4.c接口:
				continue
			v网络号s, v协议s, v优先级s, v开销s, v下一跳s, v接口s = 字符串.fe按位置分割(v行, *C路由表4.ca列开始)
			if v网络号s:	#没有网络号是负载均衡
				v网络号 = 地址.S网络地址4.fc自动(v网络号s)
			v协议 = ca协议[v协议s]
			v优先级 = int(v优先级s)
			v开销 = int(v开销s)
			v下一跳 = 地址.S网络地址4.fc自动(v下一跳s)
			v接口 = 北向接口.S接口.fc字符串(v接口s, 实现接口.ca接口缩写, False)
			yield 北向路由.S路由条目(a网络号 = v网络号, a下一跳 = v下一跳, a出接口 = v接口, a路由协议 = v协议, a优先级 = v优先级, a度量值 = v开销)
