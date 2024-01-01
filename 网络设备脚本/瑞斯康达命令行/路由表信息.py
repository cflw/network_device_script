import cflw代码库py.cflw字符串 as 字符串
import cflw代码库py.cflw网络地址 as 地址
from ..基础接口 import 数据表
from ..基础接口 import 信息
from ..基础接口 import 路由 as 北向路由
from . import 接口 as 实现接口
ca路由类型 = {
	"C": 北向路由.E路由类型.e直连,
	"S": 北向路由.E路由类型.e静态,
	"R": 北向路由.E路由类型.e路由信息协议,
	"O": 北向路由.E路由类型.e开放最短路径优先,
	"I": 北向路由.E路由类型.e中间系统到中间系统,
	"B": 北向路由.E路由类型.e边界网关协议,
}
class F路由表4_sv3(数据表.I解析表格管线):
	"""show ip route
	适用于: 浪潮s6550-24xq-ac/d(v3.60.*)"""
	c标志 = 0
	c网络号 = 4
	c管理距离度量值 = 23
	c下一跳 = 38
	c寿命 = 55
	c接口 = 66
	ca列 = 数据表.C切割列(c标志, c网络号, c管理距离度量值, c下一跳, c寿命, c接口)
	c标题行 = "P&s Destination/Mask   Dis/Metric     NextHop          Age        Interface"
	def __init__(self):
		数据表.I解析表格管线.__init__(self)
		self.f添加字段(数据表.E字段.e目的路由类型, lambda s: s[0], ca路由类型.get)
		self.f添加字段(数据表.E字段.e目的网络号, self.ca列[1], 地址.S网络地址4.fc地址前缀长度字符串)
		self.f添加字段(数据表.E字段.e目的管理距离, self.F取管理距离度量值(0), int)
		self.f添加字段(数据表.E字段.e目的度量值, self.F取管理距离度量值(1), int)
		self.f添加字段(数据表.E字段.e目的下一跳, self.ca列[3], 地址.S网络地址4.fc主机地址字符串)
		self.f添加字段(数据表.E字段.e本端出接口, self.ca列[5], 实现接口.f创建接口缩写_sv3)
	fi有效行 = staticmethod(数据表.F有效长度(c接口))
	f初始处理 = staticmethod(数据表.F去标题行(c标题行))
	def F取管理距离度量值(self, a序号: int):
		f取列 = self.ca列[2]
		def f(a行: str):
			v列 = f取列(a行)
			return v列.split("/")[a序号]
		return f
f路由表4_sv3 = F路由表4_sv3()
