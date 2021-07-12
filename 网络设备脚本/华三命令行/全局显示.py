import cflw代码库py.cflw字符串 as 字符串
from ..命令行接口 import 全局显示
from ..命令行接口 import 模式
from . import 基本表信息
class C全局显示(全局显示.I全局显示, 模式.I显示模式):
	def __init__(self, a):
		模式.I显示模式.__init__(self, a)
	#模式
	def f模式_设备(self):
		from . import 设备模式
		return 设备模式.C设备显示v5(self)
	def f模式_时间(self):
		from . import 时间
		return 时间.C时间显示(self)
	#配置
	def f显示_当前配置(self):	#需重写
		from . import 系统信息
		v输出 = self.m设备.f执行命令("display current-configuration", a自动换页 = True)
		v输出 = 字符串.f去头尾行(v输出)
		return 系统信息.C配置信息(v输出)
	#基本表信息
	def f显示_路由表(self):	#未完成
		v输出 = self.m设备.f执行命令("display ip routing-table", a自动换页 = True)
		v输出 = 字符串.f去头尾行(v输出, a转列表 = True)
		raise NotImplementedError()
	def f显示_默认路由(self):	#需重写
		v输出 = self.m设备.f执行命令("display ip routing-table 0.0.0.0")
		v输出 = 字符串.f去头尾行(v输出, a转列表 = True)
		v输出 = v输出[5]
		return (ipaddress.IPv4Network("0.0.0.0/0"), v输出[20:25], int(v输出[27:30]), int(v输出[32:42]), ipaddress.IPv4Address(v输出[45:61]), v输出[61:70])
	def f显示_链路层发现协议(self):	#未完成
		v输出 = self.m设备.f执行命令("display lldp neighbor-information", a自动换页 = True)
		raise NotImplementedError()
