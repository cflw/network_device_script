import pandas	#pandas
import cflw代码库py.cflw网络地址 as 地址
from ..基础接口 import 协议
from ..基础接口 import 路由
from ..基础接口 import 数据表
from . import 模式
ca路由类型 = {
	"静态路由": 路由.E路由类型.e静态,
	"直接路由": 路由.E路由类型.e直连,
	"OSPF": 路由.E路由类型.e开放最短路径优先,
	"RIP": 路由.E路由类型.e路由信息协议,
	"BGP": 路由.E路由类型.e边界网关协议,
	"VPN路由": 路由.E路由类型.e本地,
	"SSL VPN路由": 路由.E路由类型.e本地,
}
def f解析路由条目4(a元素):	#<tr>
	"""适用于:v8.0.7~8.0.13"""
	v类型s, v目的s, v掩码s, v下一跳s, v度量值s, v接口s = map(lambda x: x.fg文本(), a元素.fe查找("td"))
	return {
		数据表.E字段.e目的路由类型: ca路由类型[v类型s],
		数据表.E字段.e目的网络号: 地址.S网络地址4.fc地址掩码(v目的s, v掩码s),
		数据表.E字段.e目的下一跳: 地址.S网络地址4.fc地址前缀长度(v下一跳s, 32),
		数据表.E字段.e目的度量值: int(v度量值s),
	}
class C查看路由:
	"""适用于:v8.0.7~8.0.13"""
	c表格路径 = "/html/body/div[2]/div[2]/div[2]/div/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div[2]/div/div[2]/div[3]/div"
	def __init__(self, a设备):
		self.m设备 = a设备
	def f显示_路由表(self, a网络协议 = 协议.E协议.e网络协议4, a路由类型 = 0):
		#未完成,现在只能取一页,不支持自动换页
		self.m设备.f切换模式(模式.C模式af8.c网络_路由_查看路由, C查看路由.c表格路径)
		w表格 = self.m设备.f查找(C查看路由.c表格路径)
		def fe行():
			for w行 in map(lambda x: x.f查找("table/tbody/tr"), w表格.fe查找("div")):
				yield f解析路由条目4(w行)
		return pandas.DataFrame(fe行())
