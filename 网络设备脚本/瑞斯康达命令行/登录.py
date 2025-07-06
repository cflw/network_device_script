import cflw代码库py.cflw字符串 as 字符串
import cflw代码库py.cflw工具_序列 as 序列
from ..基础接口 import 操作
from ..基础接口 import 登录 as 北向登录
from ..命令行接口 import 命令
from ..命令行接口 import 模式
from ..命令行接口 import 显示
#===============================================================================
# 前置
#===============================================================================
#字典
ca登录方式 = {
	北向登录.E登录方式.e控制台: "console",
	北向登录.E登录方式.e虚拟终端: "vty"
}
ca登录认证方式 = {
	北向登录.E登录认证方式.e无: "no login",
	北向登录.E登录认证方式.e密码: "login",
	北向登录.E登录认证方式.e账号: "login local",
	北向登录.E登录认证方式.e认证授权记账: "aaa new-model"
}
ca登录协议 = {
	北向登录.E登录协议.e无: "none",
	北向登录.E登录协议.e远程登录: "telnet",
	北向登录.E登录协议.e安全外壳: "ssh",
	北向登录.E登录协议.e全部: "all"
}
ca会话数量 = {
	北向登录.E登录方式.e控制台: 1,
	北向登录.E登录方式.e虚拟终端: 8,
}
def fi登录范围内(a登录方式, a范围: range):
	return 0 <= a范围.start and a范围.stop < ca会话数量[a登录方式]
def f解析配置头(a配置: str):
	"""show running-config 中的line部分
	适用于: 浪潮CN61108PC-V-H(v6.6.6.R1.23)"""
	#line vty 0 4
	va参数 = a配置.split(" ")
	v方式 = 序列.f字典按值找键(ca登录方式, va参数[1])
	v开始 = int(va参数[2])
	v结束 = int(va参数[3]) if len(va参数) >= 3 else v开始 + 1
	return v方式, range(v开始, v结束)
def f限制范围(a范围, a登录方式):
	v左 = a范围.start if a范围.start >= 0 else 0
	v上限 = ca会话数量[a登录方式]
	v右 = a范围.stop if a范围.stop < v上限 else v上限
	return range(v左, v右)
class S登录配置节:
	def __init__(self, a文本: str):	#文本应包含节头
		self.m文本 = a文本
		self.m登录方式 = None
		self.m登录认证方式 = None
		self.m权限级别 = None
		self.m访问列表 = None
	def fg文本(self):
		return self.m文本
	def fg登录方式(self):
		if self.m登录方式 == None:
			v行 = 字符串.f提取包含行(self.m文本, "line").strip()
			if v行:
				v方式s = v行.split()[1]
				self.m登录方式 = 序列.f字典按值找键(ca登录方式, v方式s)
			else:
				raise RuntimeError("未知错误")
		return self.m登录方式
	def fg认证方式(self):
		if self.m登录认证方式 == None:
			v行 = 字符串.f提取包含行(self.m文本, "login").strip()
			if v行:
				self.m登录认证方式 = 序列.f字典按值找键(ca登录认证方式, v行)
			else:
				raise RuntimeError("未知错误")
		return self.m登录认证方式
	def fg权限级别(self):
		if self.m权限级别 == None:
			v行 = 字符串.f提取字符串之间(self.m文本, "privilege level", "\n").strip()
			if v行:
				self.m权限级别 = int(v行)
			else:
				self.m权限级别 = 4
		return self.m权限级别
	def fg访问列表(self):
		if self.m访问列表 == None:
			v文本 = 字符串.f提取字符串之间(self.m文本, "access-class", "in").strip()
			self.m访问列表 = v文本
		return self.m访问列表
class C登录配置组:	#保存配置文本,只能有一种登录方式
	def __init__(self, a文本: str):
		self.ma节 = {}	#{int: S登录配置节}
		v位置 = 0
		while v切片 := 显示.f找单节选(a文本, "line", v位置):
			v节s = a文本[v切片]
			v登录方式, v范围 = f解析配置头(v节s)
			v位置 = v切片.stop
			v节 = S登录配置节(v节s)
			for i in v范围:
				self.ma节[i] = v节
	def __getitem__(self, a)->S登录配置节:
		return self.ma节[a]
	def __iter__(self):
		return self.ma节.values().__iter__()
#===============================================================================
# 模式
#===============================================================================
class C登录显示ssh_sv3(北向登录.I登录显示, 模式.I显示模式):
	"""适用于: """
	def __init__(self, a):
		模式.I显示模式.__init__(self, a)
		self.m配置文本 = None
		self.m配置组 = None
	def fg配置文本(self)->str:
		if not self.m配置文本:
			v输出 = self.m设备.f执行显示命令("show running-config")
			self.m配置文本 = 显示.F多节选("line " + ca登录方式[self.m登录方式])(v输出)
		return self.m配置文本
	def fg指定配置(self, a序号)->S登录配置节:
		if not self.m配置组:
			self.m配置组 = C登录配置组(self.fg配置文本())
		return self.m配置组[a序号]
	def fg首节序号(self)->int:
		return self.m范围.start
	def fg首节配置(self)->S登录配置节:
		return self.fg指定配置(self.fg首节序号())
	def fg认证方式(self):
		return self.fg首节配置().fg认证方式()
	def fg登录协议(self):
		raise NotImplementedError()
	def fg访问列表(self):
		raise NotImplementedError()
	def fg登录超时(self):
		pass
	def fg操作超时(self):
		raise NotImplementedError()
class C登录配置ssh_sv3(北向登录.I登录配置, 模式.C同级模式, C登录显示ssh_sv3):
	"""适用于: """
	def __init__(self, a):
		C登录显示ssh_sv3.__init__(self, a)
		模式.C同级模式.__init__(self, a)
	def fs认证方式(self, a认证方式, a操作 = 操作.E操作.e设置):
		v命令 = ca登录认证方式[a认证方式]
		self.f执行当前模式命令(v命令)
	def fs访问列表(self, a访问列表, a操作 = 操作.E操作.e设置):
		"""命令: ssh2 access-list 访问列表"""
		v命令 = f"ssh2 access-list {a访问列表}"
		self.f执行当前模式命令(v命令)
	def fs登录超时(self, a秒, a操作 = 操作.E操作.e设置):
		"""命令: ssh2 server authentication-timeout 秒"""
		v命令 = f"ssh2 server authentication-timeout {a秒}"
		self.f执行当前模式命令(v命令)
	def fs登录重试次数(self, a数量, a操作 = 操作.E操作.e设置):
		"""命令: ssh2 server authentication-retries 数量"""
		v命令 = f"ssh2 server authentication-retries {a数量}"
		self.f执行当前模式命令(v命令)
	def fs操作超时(self, a秒, a操作 = 操作.E操作.e设置):
		pass	#无命令
