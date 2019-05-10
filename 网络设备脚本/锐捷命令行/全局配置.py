from ..命令行接口 import 全局配置
from ..基础接口 import 操作
from ..基础接口 import 协议
class C全局配置(全局配置.I全局配置):
	"""适用于: s5750(v11.4)"""
	def __init__(self, a):
		全局配置.I全局配置.__init__(self, a)
	#命令
	def fg进入命令(self):
		return "configure terminal"
	#模式
	def f模式_接口(self, a接口, a操作 = 操作.E操作.e设置):
		from ..思科命令行 import 接口
		v接口 = 接口.f创建接口(a接口)
		return 接口.C接口(self, v接口)
	def f模式_访问控制列表(self, a名称, a类型, a操作 = 操作.E操作.e设置):
		v名称, v类型 = 通用访问列表.f解析名称和类型(a名称, a类型, 访问控制列表.C助手)
		#创建访问控制列表对象
		if v类型 == 北向列表.E类型.e标准4:
			访问控制列表.fi标准范围(v名称)
			v模式 = 访问控制列表.C标准4(self, v名称)
		elif v类型 == 北向列表.E类型.e扩展4:
			访问控制列表.fi扩展范围(v名称)
			v模式 = 访问控制列表.C扩展4(self, v名称)
		elif v类型 in (北向列表.E类型.e标准6, 北向列表.E类型.e扩展6):
			v模式 = 访问控制列表.C六(self, v名称)
		else:
			raise ValueError("未知的访问控制列表类型")
		if a操作 == 操作.E操作.e删除:
			v命令 = c不 + v模式.fg进入命令()
			self.f执行当前模式命令(v命令)
		elif a操作 == 操作.E操作.e重置:
			v命令 = c默认 + v模式.fg进入命令()
			self.f执行当前模式命令(v命令)
		return v模式
	#路由
	def f模式_静态路由(self, a版本 = 协议.E协议.e网络协议4, a虚拟路由转发 = None):
		v版本 = f解析网络协议版本(a版本)
		if v版本 == 协议.E协议.e网络协议4:
			return 静态路由.C静态路由4(self)
		elif v版本 == 协议.E协议.e网络协议6:
			raise NotImplementedError()
		else:
			raise ValueError("未知的版本")
	def f模式_路由信息协议(self, a进程号 = 0, a版本 = 协议.E协议.e路由信息协议, a接口 = None, a操作 = 操作.E操作.e设置):	#rip
		v版本 = 南向路由.f解析路由信息协议版本(a版本)
		if v版本 == 协议.E协议.e路由信息协议:	#rip
			return 路由信息协议.C当代(self)
		elif v版本 == 协议.E协议.e下一代路由信息协议:	#ripng
			raise NotImplementedError()
		else:
			raise ValueError("未知的版本")
	def f模式_开放最短路径优先(self, a进程号 = 1, a版本 = 协议.E协议.e开放最短路径优先, a接口 = None, a操作 = 操作.E操作.e设置):
		v版本 = 南向路由.f解析开放最短路径优先版本(a版本)
		if a接口:	#有接口
			v接口 = 接口.f创建接口(a接口)
			if a版本 == 协议.E协议.e开放最短路径优先2:
				return 开放最短路径优先.C接口(self, a进程号, v接口)
			elif a版本 == 协议.E协议.e开放最短路径优先3:
				raise NotImplementedError()
			else:
				raise ValueError("未知的版本")
		#没有接口
		if a版本 == 协议.E协议.e开放最短路径优先2:
			return 开放最短路径优先.C路由配置(self, a进程号)
		elif a版本 == 协议.E协议.e开放最短路径优先3:
			raise NotImplementedError()
		else:
			raise ValueError("未知的版本")
