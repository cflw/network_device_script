import time
import cflw代码库py.cflw字符串 as 字符串
from ..命令行接口 import 全局显示
from . import 基本表信息
class C全局显示(全局显示.I全局显示):
	"""适用于: 迈普sm4120(v6.6.4.1.3)"""
	#显示
	def f显示_启动配置(self):
		v输出 = self.m设备.f执行显示命令("show startup-config")
		return v输出
	def f显示_当前配置(self):
		v输出 = self.m设备.f执行显示命令("show running-config")
		return v输出
	def f显示_时间(self):
		v命令 = "show clock"
		v输出 = self.m设备.f执行显示命令(v命令)	#beijing(UTC+08:00) THU APR 04 11:11:12 2019
		#解析
		v空格位置 = 字符串.f全部找(v输出, " ")
		v行结束 = v输出.find("\n", v空格位置[0])
		if v行结束 > 0:	#如果有换行符,截取到行结束
			v输出 = v输出[v空格位置[0]+1 : v行结束]
		else:	#如果没有换行符,截取到字符串结束
			v输出 = v输出[v空格位置[0]+1:]	#THU APR 04 11:11:12 2019
		v时间 = time.strptime(v输出, "%a %b %d %H:%M:%S %Y")
		return v时间
	def f显示_设备名(self):
		v命令 = "show running-config | include hostname"
		v输出 = self.m设备.f执行显示命令(v命令)
		v位置 = v输出.find("hostname")
		v行结束 = v输出.find("\n", v位置)
		return v输出[v位置 + 9 : v行结束]
	#显示具体
	def f显示_接口表(self):
		v命令 = "show interface switchport"
		v输出 = self.m设备.f执行显示命令(v命令)
		return 基本表信息.f交换接口表(v输出)
	def f显示_网络接口表4(self):
		v命令 = "show ip interface brief"
		v输出 = self.m设备.f执行显示命令(v命令)
		return 基本表信息.f网络接口表4(v输出)
class C全局显示_v9(C全局显示):
	"""适用于: 迈普t6100(v9.3.4.45)"""
	#服务
	def f模式_安全外壳(self):
		"""适用于: 迈普t6100(v9.3.4.45)"""
		from . import 安全外壳
		return 安全外壳.C安全外壳显示_v9(self)
	def f模式_访问控制列表(self, a名称, a类型 = None):
		"""适用于: 迈普t6100(v9.3.4.45)"""
		from ..基础接口 import 访问控制列表 as 北向列表
		from ..命令行接口 import 访问控制列表 as 南向列表
		from . import 访问控制列表 as 实现列表
		v名称, v类型 = 南向列表.f解析名称和类型(a名称, a类型, 实现列表.C助手)
		if v类型 == 北向列表.E类型.e标准4:
			return 实现列表.C标准4显示(self, v名称)
		elif v类型 == 北向列表.E类型.e扩展4:
			return 实现列表.C扩展4显示(self, v名称)
		elif v类型 == 北向列表.E类型.e标准6:
			raise NotImplementedError()
		elif v类型 == 北向列表.E类型.e扩展6:
			raise NotImplementedError()
		else:
			raise ValueError("错误的类型")
