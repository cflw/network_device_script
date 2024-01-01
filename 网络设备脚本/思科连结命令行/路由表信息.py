import pandas	#pandas
import cflw代码库py.cflw字符串 as 字符串
import cflw代码库py.cflw网络地址 as 地址
from ..基础接口 import 数据表
from ..基础接口 import 协议
from ..基础接口 import 接口 as 北向接口
from ..基础接口 import 路由 as 北向路由
from ..命令行接口 import 命令
from . import 接口 as 实现接口
#===============================================================================
# 声明
#===============================================================================
ca路由类型 = {
	"local": 北向路由.E路由类型.e本地,
	"direct": 北向路由.E路由类型.e直连,
	"static": 北向路由.E路由类型.e静态,
	"hsrp": 北向路由.E路由类型.e热备份路由协议,
}
#===============================================================================
# 表
#===============================================================================
class F路由表4_nv7(数据表.I解析列表管线):
	"""show ip route
	适用于: 浪潮cn8696q(v7.3), 浪潮cn61108pcv(v9.2.3)"""
	def __init__(self):
		pass	#确定什么也不做
	def fe记录(self, a文本: str):
		for v记录s in self.fe记录文本(a文本):
			v结果 = {}
			va行s = v记录s.split("\n")	#有2行
			#第[0]行: 网络号, 单播数/组播数, 附加(可能没有)
			va字段0 = va行s[0].split(",")
			v结果[数据表.E字段.e目的网络号] = 地址.S网络地址4.fc地址前缀长度字符串(va字段0[0])
			#第[1]行: 下一跳, 接口(可能没有), 管理距离/度量值, 时间?, 路由类型
			va字段1 = va行s[1].split(",")
			v下一跳s = va字段1[0].split()[1]
			v结果[数据表.E字段.e目的下一跳] = 地址.S网络地址4.fc主机地址字符串(v下一跳s)
			v接口s = va字段1[1]
			if "/" in v接口s:	#不是接口,是管理距离和度量值
				v偏移 = 0
			else:
				v结果[数据表.E字段.e本端出接口] = 实现接口.f创建接口_nv7(v接口s)
				v偏移 = 1
			v管理距离和度量值s = va字段1[1 + v偏移]
			v管理距离s = 字符串.f提取字符串之间(v管理距离和度量值s, "[", "/")
			v结果[数据表.E字段.e目的管理距离] = int(v管理距离s)
			v度量值s = 字符串.f提取字符串之间(v管理距离和度量值s, "/", "]")
			v结果[数据表.E字段.e目的度量值] = int(v度量值s)
			v路由类型s = va字段1[3 + v偏移].strip()
			v结果[数据表.E字段.e目的路由类型] = ca路由类型.get(v路由类型s)
			yield v结果
	def f初始处理(self, a文本: str):
		v位置 = 字符串.f找下一行位置(a文本, a位置 = 0, a循环 = 6)
		if v位置 == -1:	#路由表是空的
			return ""
		return a文本[v位置:]
	def f下一记录(self, a文本: str, a开始位置: int):
		v位置 = 字符串.f找下一行位置(a文本, a位置 = a开始位置, a循环 = 2)
		return v位置
f路由表4_nv7 = F路由表4_nv7()
class F路由表4全部_nv7(数据表.I解析表格列表管线):
	"""show ip route vrf all
	适用于: 浪潮cn8696q(v7.3), 浪潮cn61108pcv(v9.2.3)"""
	def __init__(self):
		数据表.I解析表格列表管线.__init__(self)
		self.f添加表格(f路由表4_nv7)
		self.f添加字段(数据表.E字段.e本端虚拟路由转发, 数据表.F正则字段(r'IP Route Table for VRF "(.+)"', 1), str)
	def f下一记录(self, a文本: str, a位置: int):
		v位置 = a文本.find("IP Route Table for VRF", a位置 + 1)
		return v位置
f路由表4全部_nv7 = F路由表4全部_nv7()