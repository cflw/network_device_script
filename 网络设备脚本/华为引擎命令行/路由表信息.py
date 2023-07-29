import cflw代码库py.cflw字符串 as 字符串
import cflw代码库py.cflw网络地址 as 地址
from ..基础接口 import 路由 as 北向路由
from ..基础接口 import 信息
from ..基础接口 import 数据表
from ..华为命令行 import 接口 as 实现接口
ca路由类型 = {
	"Direct": 北向路由.E路由类型.e直连,
	"Static": 北向路由.E路由类型.e静态,
	"RIP": 北向路由.E路由类型.e路由信息协议,
	"OSPF": 北向路由.E路由类型.e开放最短路径优先,
	"BGP": 北向路由.E路由类型.e边界网关协议,
}
class F路由表4(数据表.I解析表格管线):
	"""display ip routing-table
	适用于: 华为ne40e(v8.180), 华为ne9000(模拟器), 华为ce6800(模拟器)"""
	c网络号 = 0
	c协议 = 20
	c优先级 = 28
	c开销 = 33
	c标志 = 45
	c下一跳 = 51
	c接口 = 67
	ca列 = 数据表.C切割列(c网络号, c协议, c优先级, c开销, c标志, c下一跳, c接口)
	c标题行 = "Destination/Mask    Proto   Pre  Cost        Flags NextHop         Interface"
	def __init__(self):
		数据表.I解析表格管线.__init__(self)
		self.f添加字段(数据表.E字段.e目标网络号, F路由表4.ca列[0], 地址.S网络地址4.fc地址前缀长度字符串)
		self.f添加字段(数据表.E字段.e目标路由类型, F路由表4.ca列[1], ca路由类型.get)
		self.f添加字段(数据表.E字段.e目标管理距离, F路由表4.ca列[2], int)
		self.f添加字段(数据表.E字段.e目标度量值, F路由表4.ca列[3], int)
		self.f添加字段(数据表.E字段.e目标下一跳, F路由表4.ca列[5], 地址.S网络地址4.fc主机地址字符串)
		self.f添加字段(数据表.E字段.e本端出接口, F路由表4.ca列[6], 实现接口.f创建接口)
	fi有效行 = staticmethod(数据表.F有效长度(c接口))
	f初始处理 = staticmethod(数据表.F去标题行(c标题行))
f路由表4 = F路由表4()