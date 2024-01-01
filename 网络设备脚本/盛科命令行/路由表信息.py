import cflw代码库py.cflw字符串 as 字符串
import cflw代码库py.cflw网络地址 as 地址
from ..基础接口 import 数据表
from ..基础接口 import 信息
from ..基础接口 import 路由 as 北向路由
from . import 接口 as 实现接口
ca路由类型 = {
	"loopback": 北向路由.E路由类型.e本地,
	"connected": 北向路由.E路由类型.e直连,
	"static": 北向路由.E路由类型.e静态,
}
class F路由表4_ev6(数据表.I解析列表管线):	#只有直连路由,缺少静态路由和动态路由,以后再改
	"""show ip route
	适用于: 浪潮cn61108pcvh(v6.2.27.13), 浪潮s5350(v6.2.27)"""
	c代码 = 0
	c网络号 = 9
	def __init__(self):
		数据表.I解析列表管线.__init__(self)
	def fe记录(self, a文本: str):
		for v记录s in self.fe记录文本(a文本):
			v记录 = {}
			v代码s = v记录s[0: self.c网络号].strip()
			v是位置 = v记录s.find("is")
			v网络号s = v记录s[self.c网络号 : v是位置].strip()
			v记录[数据表.E字段.e目的网络号] = 地址.S网络地址4.fc地址前缀长度字符串(v网络号s)
			v逗号位置 = v记录s.find(",")
			v空格位置 = v记录s.rfind(" ", 0, v逗号位置)
			v路由类型s = v记录s[v空格位置+1 : v逗号位置].strip()
			v记录[数据表.E字段.e目的路由类型] = ca路由类型.get(v路由类型s)
			v接口s = v记录s[v逗号位置+1 :].strip()
			v记录[数据表.E字段.e本端出接口] = 实现接口.f创建接口_ev6(v接口s)
			yield v记录
	def f下一记录(self, a文本: str, a位置: int):
		v位置 = a文本.find("\n", a位置+1)
		return v位置
	def f初始处理(self, a文本: str)->str:
		v位置 = 字符串.f找下一行位置(a文本, 0, a循环 = 8)
		return a文本[v位置:]
f路由表4_ev6 = F路由表4_ev6()