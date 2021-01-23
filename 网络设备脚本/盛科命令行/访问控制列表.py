import functools
import cflw代码库py.cflw网络地址 as 地址
import cflw代码库py.cflw字符串 as 字符串
from ..基础接口 import 操作
from ..基础接口 import 协议
from ..基础接口 import 异常
from ..基础接口 import 访问控制列表 as 北向列表
from ..基础接口 import 文件
from ..命令行接口 import 命令
from ..命令行接口 import 访问控制列表 as 南向列表
from .常量 import *
#===============================================================================
# 生成&解析
#===============================================================================
#规则序号
def f生成规则序号4(a序号):
	if a序号 == None or a序号 < 0:
		return ""
	else:
		return a序号
#端口号
class C端口号到字符串(北向列表.I端口号到字符串):
	def f大于(self, a值):
		return "gt " + str(a值)
	def f小于(self, a值):
		return "lt " + str(a值)
	def f等于(self, a序列):
		return "eq " + " ".join(字符串.ft字符串序列(a序列))
	def f不等于(self, a序列):
		return "neq " + " ".join(字符串.ft字符串序列(a序列))
	def f范围(self, a值: range):
		return "range %d %d" % (a值.start, a值.stop - 1)
g端口号到字符串 = C端口号到字符串()
f生成端口 = functools.partial(南向列表.f生成端口, g端口号到字符串)
#协议
ca协议到字符串4 = 南向列表.ca协议到字符串4 | {
	协议.E协议.ip: "any",
	协议.E协议.ipv4: "any",
}
#允许
f生成允许 = functools.partial(南向列表.f生成允许, 南向列表.c允许元组)
#地址
def f生成地址4(a地址):
	"转成字符串"
	if not a地址:
		return "any"
	v地址 = 地址.S网络地址4.fc自动(a地址)
	if v地址.fi主机():
		return "host %s" % (v地址.fg地址s())
	elif v地址.fi空():
		return "any"
	else:
		return "%s %s" % (v地址.fg网络号s(), v地址.fg反掩码s())
#===============================================================================
# 类
#===============================================================================
class C网络4(南向列表.I列表配置):
	"""适用于: 浪潮cn61108pcvh(v6.x), 浪潮s5350(v6.x)"""
	def __init__(self, a, a名称):
		南向列表.I列表配置.__init__(self, a)
		self.m名称 = a名称
	def fg进入命令(self):
		v命令 = f"ip access-list {self.m名称}"
		return v命令
	def f添加规则(self, a序号, a规则):
		v命令 = 命令.C命令()
		v命令 += f生成规则序号4(a序号)
		v命令 += f生成允许(a规则.m允许)
		#确定
		v命令 += ca协议到字符串4[a规则.m协议]
		v层 = 协议.f取协议层(a规则.m协议)
		#按层
		if v层 == 3:
			v命令 += f生成地址4(a规则.m源地址)
			v命令 += f生成地址4(a规则.m目的地址)
		elif v层 == 4:
			v命令 += f生成地址4(a规则.m源地址)
			if a规则.m源端口:
				v命令 += "src-port"
				v命令 += f生成端口(a规则.m源端口)
			v命令 += f生成地址4(a规则.m目的地址)
			if a规则.m目的端口:
				v命令 += "dst-port"
				v命令 += f生成端口(a规则.m目的端口)
		else:
			raise NotImplementedError("迷之逻辑")
		#执行命令
		self.f执行当前模式命令(v命令)
	def f删除规则_序号(self, a序号):
		v命令 = f"no sequence-num {a序号}"
		self.f执行当前模式命令(v命令)
	def f删除规则_规则(self, a规则):
		#需要开启读权限才能调用这个
		raise NotImplementedError()
	def fs规则(self, a序号 = None, a规则 = None, a操作 = 操作.E操作.e设置):
		v操作 = 操作.f解析操作(a操作)
		if v操作 == 操作.E操作.e设置:
			#不能直接覆盖,先删除旧规则再添加新规则
			if self.m设备.m访问权限 & 文件.E访问权限.e读:
				pass	#未实现
			self.f添加规则(a序号, a规则)
		elif v操作 == 操作.E操作.e修改:
			raise NotImplementedError()
		elif v操作 == 操作.E操作.e添加:
			self.f添加规则(a序号, a规则)
		elif v操作 == 操作.E操作.e删除:
			if a序号:
				self.f删除规则_序号(a序号)
			elif a规则:
				self.f删除规则_规则(a规则)
		else:
			raise NotImplementedError()