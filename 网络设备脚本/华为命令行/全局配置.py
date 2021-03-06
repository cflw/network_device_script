from ..基础接口 import 操作
from ..基础接口 import 协议
from ..基础接口 import 接口 as 北向接口
from ..命令行接口 import 全局配置
from .. import 华为
from . import 实用 as 华为实用
from . import 接口 as 实现接口
class C系统视图(全局配置.I全局配置):
	def __init__(self, a):
		全局配置.I全局配置.__init__(self, a)
	def fg进入命令(self):
		return "system-view"
	#模式
	def f模式_用户(self, a用户名, a操作 = 操作.E操作.e设置):
		from . import 用户
		return 用户.C用户配置(self, a用户名)
	def f模式_时间(self):
		from . import 时间
		return 时间.C时间(self.fg上级模式())
	def f模式_接口(self, a接口):
		v接口 = 实现接口.f创建接口(a接口)
		#检查值
		if v接口.fi属于分类(北向接口.E分类.e以太网):
			if v接口.fg主序号数() != 3:
				raise ValueError("在华为设备,接口序号有3段")
			elif v接口.fi范围():
				return C端口组(self, v接口)
		if v接口.fi属于分类(北向接口.E分类.e环回):
			if v接口.fg主序号数() != 1:
				raise ValueError("环回口的序号只有1段")
		return 实现接口.C接口视图(self, v接口)
	def f模式_登录(self, a方式, a范围 = 0, a操作 = 操作.E操作.e设置):
		return 登录.C登录(self, a方式, a范围)
	def f模式_虚拟局域网(self, a序号 = 0, a接口 = None, a操作 = 操作.E操作.e设置):	#vlan
		from . import 虚拟局域网 as 实现虚网
		def fc接口配置(a接口):
			if self.m设备.m版本 == 华为.E型号.s5700:
				return 实现虚网.C接口配置s5700(self, a接口)
			else:
				return 实现虚网.C接口配置(self, a接口)
		if a接口:
			v接口 = 实现接口.f创建接口(a接口)
			return fc接口配置(self, v接口)
		v类型 = type(a序号)
		if v类型 == int:
			return 实现虚网.C虚网配置(self, a序号)
		elif v类型 == 北向接口.S接口:
			return fc接口配置(self, a序号)
		elif isinstance(a序号, 南向接口.I接口配置基础):
			return fc接口配置(self, a序号.m接口)
		else:
			raise ValueError()
	#路由
	def f模式_静态路由(self, a版本 = 协议.E协议.e网络协议4, a虚拟路由转发 = None):
		from ..命令行接口 import 路由 as 南向路由
		from . import 静态路由 as 实现静态路由
		v版本 = 南向路由.f解析网络协议版本(a版本)
		if v版本 == 协议.E协议.e网络协议4:
			return 实现静态路由.C静态路由4(self, a虚拟路由转发 = a虚拟路由转发)
		elif v版本 == 协议.E协议.e网络协议6:
			raise NotImplementedError()
		else:
			raise ValueError("未知的版本")
	def f模式_开放最短路径优先(self, a进程号 = 1, a版本 = 协议.E协议.e开放最短路径优先, a接口 = None, a操作 = 操作.E操作.e设置):
		from . import 开放最短路径优先 as 实现开放最短路径优先
		if a接口:	#有接口
			v接口 = 实现接口.f创建接口(a接口)
			if a版本 == 协议.E协议.e开放最短路径优先2:
				return 实现开放最短路径优先.C接口4(self, a进程号, a接口)
			elif a版本 == 协议.E协议.e开放最短路径优先3:
				raise NotImplementedError()
			else:
				raise ValueError()
		#没有接口
		if a版本 == 协议.E协议.e开放最短路径优先2:
			return 实现开放最短路径优先.C路由4(self, a进程号)
		elif a版本 == 协议.E协议.e开放最短路径优先3:
			raise NotImplementedError()
		else:
			raise ValueError()
	def f模式_中间系统到中间系统(self, a进程号 = 1, a接口 = None, a操作 = 操作.E操作.e设置):
		from . import 中间系统到中间系统 as 实现路由协议
		#是接口
		if a接口:
			v接口 = 实现接口.f创建接口(a接口)
			return 实现路由协议.C接口配置(self, a进程号, a接口)
		#不是接口
		return 实现路由协议.C进程配置(self, a进程号)
	def f模式_边界网关协议(self, a自治系统号, a操作 = 操作.E操作.e设置):
		from . import 边界网关协议
		return 边界网关协议.C进程配置(self, a自治系统号)
	def f模式_路由策略(self, a名称, a操作 = 操作.E操作.e设置):
		from . import 路由策略
		return 路由策略.C组(self, a名称)
	#交换
	def f模式_生成树(self, a模式, a接口 = None, a操作 = 操作.E操作.e设置):
		from ..基础接口 import 生成树 as 北向生成树
		from . import 生成树 as 实现生成树
		if a接口:
			raise NotImplementedError()
		if a操作 == 操作.E操作.e设置:
			v命令 = f"stp mode {实现生成树.ca模式[a模式]}"
			self.f执行当前模式命令(v命令)
		if a模式 == 北向生成树.E模式.e多生成树:
			return 实现生成树.C多生成树(self)
		raise NotImplementedError()
	#数据结构
	def f模式_访问控制列表(self, a名称, a类型 = None, a操作 = 操作.E操作.e设置):
		from ..基础接口 import 访问控制列表 as 北向列表
		from ..命令行接口 import 访问控制列表 as 南向列表
		from . import 访问控制列表 as 实现列表
		v名称, v类型 = 南向列表.f解析名称和类型(a名称, a类型, 实现列表.C助手)
		if v类型 == 北向列表.E类型.e标准4:
			return 实现列表.C基本4(self, v名称)
		elif v类型 == 北向列表.E类型.e扩展4:
			return 实现列表.C高级4(self, v名称)
		elif v类型 == 北向列表.E类型.e标准6:
			return 实现列表.C基本6(self, v名称)
		elif v类型 == 北向列表.E类型.e扩展6:
			return 实现列表.C高级6(self, v名称)
		else:
			raise ValueError("错误的类型")
	def f模式_前缀列表(self, a名称, a类型 = 协议.E协议.e网络协议4):
		if a类型 == 协议.E协议.e网络协议4:
			return 前缀列表.C前缀列表(self, a名称, 前缀列表.c版本4, 地址.S网络地址4)
		elif a类型 == 协议.E协议.e网络协议6:
			return 前缀列表.C前缀列表(self, a名称, 前缀列表.c版本6, 地址.S网络地址6)
		else:
			raise ValueError("错误的类型")
	def f模式_虚拟路由转发(self, a名称 = "", a接口 = None, a操作 = 操作.E操作.e设置):
		from . import 虚拟路由转发
		if a接口:
			v模式 = 虚拟路由转发.C接口配置(self, a接口)
		else:
			v模式 = 虚拟路由转发.C资源配置(self, a名称)
		return v模式
	#服务
	def f模式_网络终端(self):
		from . import 登录协议
		return 登录协议.C网络终端(self)
	def f模式_安全外壳(self):
		from . import 登录协议
		return 登录协议.C安全外壳(self)
	def f模式_网络时间协议(self, a端, a操作 = 操作.E操作.e设置):
		from . import 网络时间协议
		if a端 == 操作.E端.e服务器:
			return 网络时间协议.C服务器(self)
		elif a端 == 操作.E端.e客户端:
			return 网络时间协议.C客户端(self)
		else:
			raise ValueError("a端 必需是服务器或客户端")
	def f模式_简单网络管理协议(self, a端 = 操作.E端.e代理, a操作 = 操作.E操作.e设置):
		from . import 简单网络管理协议
		if a端 == 操作.E端.e代理:
			return 简单网络管理协议.C代理(self)
		elif a端 == 操作.E端.e陷阱:
			return 简单网络管理协议.C陷阱(self)
		else:
			raise ValueError("a端 必需是代理或陷阱")
	#服务质量
	def f模式_流量分类(self, a名称, ai匹配全部 = False, a操作 = 操作.E操作.e设置):
		from . import 服务质量
		v类型 = type(a名称)
		if v类型 == 服务质量.C助手:
			self.f自动绑定流量策略(a名称)
			v模式 = self.f模式_流量分类1(a名称, ai匹配全部)
		elif v类型 == str:
			v模式 = self.f模式_流量分类0(a名称, ai匹配全部)
		else:
			raise TypeError()
		return v模式
	def f模式_流量分类0(self, a名称: str, ai匹配全部):
		from . import 服务质量
		return 服务质量.C分类(self, a名称, ai匹配全部)
	def f模式_流量分类1(self, a助手, ai匹配全部):
		if not a助手.m分类模式:
			a助手.m分类模式 = self.f模式_流量分类0(a助手.m分类名称, ai匹配全部)
		return a助手.m分类模式
	def f模式_流量行为(self, a名称, a操作 = 操作.E操作.e设置):
		from . import 服务质量
		v类型 = type(a名称)
		if v类型 == 服务质量.C助手:
			self.f自动绑定流量策略(a名称)
			v模式 = self.f模式_流量行为1(a名称)
		elif v类型 == str:
			v模式 = self.f模式_流量行为0(a名称)
		else:
			raise TypeError()
		return v模式
	def f模式_流量行为0(self, a名称: str):
		from . import 服务质量
		return 服务质量.C行为(self, a名称)
	def f模式_流量行为1(self, a助手):
		if not a助手.m行为模式:
			a助手.m行为模式 = self.f模式_流量行为0(a助手.m行为名称)
		return a助手.m行为模式
	def f模式_流量策略(self, a名称, a操作 = 操作.E操作.e设置):
		from . import 服务质量
		v类型 == type(a名称)
		if v类型 == 服务质量.C助手(a名称):
			v模式 = self.f模式_流量策略1(a名称)
		elif v类型 == str:
			v模式 = self.f模式_流量策略0(a名称)
		else:
			raise TypeError()
		return v模式
	def f模式_流量策略0(self, a名称: str):
		from . import 服务质量
		return 服务质量.C策略(self, a名称)
	def f模式_流量策略1(self, a助手):
		if not a助手.m策略模式:
			a助手.m策略模式 = self.f模式_流量策略0(a助手.m策略名称)
		return a助手.m策略模式
	def f自动绑定流量策略(self, a助手):
		if not a助手.mi自动绑定 or a助手.mi已绑定:
			return
		v分类 = self.f模式_流量分类1(a助手, False)
		v分类.f切换到当前模式()
		v行为 = self.f模式_流量行为1(a助手)
		v行为.f切换到当前模式()
		v策略 = self.f模式_流量策略1(a助手)
		v策略.fs绑定(a助手.m分类名称, a助手.m行为名称)
		a助手.mi已绑定 = True
	#配置
	def fs设备名(self, a名称):
		self.f执行当前模式命令("sysname " + str(a名称))
