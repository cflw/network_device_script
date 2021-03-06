import cflw代码库py.cflw工具_序列 as 序列
import cflw代码库py.cflw网络地址 as 地址
from ..基础接口 import 异常
from ..基础接口 import 操作
from ..基础接口 import 静态路由
from ..基础接口 import 路由
from ..网页接口 import 元素
from . import 模式
class C静态路由配置(静态路由.I静态路由配置):
	"""适用于: mw155r"""
	def __init__(self, a设备):
		self.m设备 = a设备
	def f显示_路由表(self):
		self.m设备.f切换模式(模式.C模式.c路由功能_静态路由表)
		v元素 = self.m设备.f查找("/html/body/center/form/table/tbody/tr[2]/td/table/tbody/tr[1]/td[2]/table[2]/tbody")
		return C路由表(v元素)
	def fs路由(self, a网络号, a下一跳, a操作 = 操作.E操作.e设置):
		v网络号 = 地址.S网络地址4.fc自动(a网络号)
		v下一跳 = 地址.S网络地址4.fc自动(a下一跳)
		v操作 = 操作.f解析操作(a操作)
		self.m设备.f切换模式(模式.C模式.c路由功能_静态路由表)
		if 操作.fi加操作(v操作):
			w添加新条目 = self.m设备.f查找("/html/body/center/form/table/tbody/tr[2]/td/table/tbody/tr[1]/td[2]/table[3]/tbody/tr/td/input[1]")
			w添加新条目.f点击()
			w目的网络地址 = self.m设备.f查找("/html/body/center/form/table/tbody/tr[2]/td/table/tbody/tr[1]/td[2]/table[2]/tbody/tr[1]/td[2]/input")
			w目的网络地址.f输入(v网络号.fg网络号s())
			w子网掩码 = self.m设备.f查找("/html/body/center/form/table/tbody/tr[2]/td/table/tbody/tr[1]/td[2]/table[2]/tbody/tr[2]/td[2]/input")
			w子网掩码.f输入(v网络号.fg掩码s())
			w网关 = self.m设备.f查找("/html/body/center/form/table/tbody/tr[2]/td/table/tbody/tr[1]/td[2]/table[2]/tbody/tr[3]/td[2]/input")
			w网关.f输入(v下一跳.fg地址s())
			w保存 = self.m设备.f查找("/html/body/center/form/table/tbody/tr[2]/td/table/tbody/tr[3]/td/input[4]")
			w保存.f点击()
		else:
			raise NotImplementedError()
	def fs默认路由(self, a下一跳, a操作 = 操作.E操作.e设置):
		raise 异常.X执行("不支持设置默认路由")
class C路由表:
	"""适用于: mw155r"""
	def __init__(self, a元素):
		self.m元素 = a元素
	def __iter__(self):
		return self.fe路由()
	def fe路由(self):
		for v元素 in self.m元素.fe查找("./tr"):
			v标识s, v网络号s, v掩码s, v网关s, v状态s, v编辑s = 序列.f映射(元素.C元素.fg文本, v元素.fe查找("./td"))
			if v标识s == "ID":
				continue
			if v状态s == "失效":
				continue
			v网络号 = 地址.S网络地址4.fc地址掩码(v网络号s, v掩码s)
			v下一跳 = 地址.S网络地址4.fc地址前缀长度(v网关s, 32)
			yield 路由.S路由条目(a网络号 = v网络号, a下一跳 = v下一跳)