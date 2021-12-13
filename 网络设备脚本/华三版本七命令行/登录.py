import cflw代码库py.cflw字符串 as 字符串
from ..基础接口 import 登录 as 北向登录
from ..基础接口 import 操作
from ..基础接口 import 协议
from ..命令行接口 import 模式
from ..命令行接口 import 命令
from ..华三命令行 import 登录 as 旧登录
#===============================================================================
# 常量
#===============================================================================
c命令_登录配置v7 = "line"
#===============================================================================
# 解析
#===============================================================================
class C登录配置表v7:
	def __init__(self, a文本):
		self.m文本 = a文本
	def __iter__(self):
		return self.fe节()
	def fe节(self):
		v位置0 = 0
		for v位置1 in 字符串.f重复找(self.m文本, c命令_登录配置v7):
			if v位置0 != v位置1:
				v文本 = self.m文本[v位置0 : v位置1]
				v位置0 = v位置1
				if not c命令_登录配置v7 in v文本:
					continue
				yield 旧登录.S登录配置(v文本)
		yield 旧登录.S登录配置(self.m文本[v位置1:])
#===============================================================================
# 模式
#===============================================================================
class C登录v7(旧登录.C登录):	#废弃
	def __init__(self, a, a方式, a范围 = None):
		旧登录.C登录.__init__(self, a, a方式, a范围)
		self.t登录配置表 = C登录配置表v7
	def fg进入命令(self):
		v命令 = 命令.C命令(c命令_登录配置v7)
		v命令 += self.fg模式参数()
		return v命令
	def fs访问列表(self, a访问列表):
		pass	#没有命令
	def fg访问列表(self):
		v命令 = "display current-configuration configuration system | include .+server.+acl"
		v输出 = self.m设备.f执行显示命令(v命令)
		v名称 = 字符串.f提取字符串之间(v输出, "acl ", "\n", a结束严谨 = False)
		return v名称
class C远程登录显示v7(北向登录.I远程登录显示, 模式.I显示模式):
	def __init__(self, a):
		模式.I显示模式.__init__(self, a)
	def fg认证方式(self):
		raise NotImplementedError()
	def fg登录超时(self):
		raise NotImplementedError()
	def fg操作超时(self):
		raise NotImplementedError()
	def fg登录协议(self):
		raise NotImplementedError()
	def fg访问列表(self):
		v命令 = "display current-configuration configuration system | include .+server.+acl"
		v输出 = self.m设备.f执行显示命令(v命令)
		v名称 = 字符串.f提取字符串之间(v输出, "acl ", "\n", a结束严谨 = False)
		return v名称
class C远程登录配置v7(北向登录.I远程登录配置, 模式.I模式):
	def __init__(self, a, a协议, a范围):
		模式.I模式.__init__(self, a)
		self.m协议 = a协议
		self.m范围 = a范围
	#模式
	def fg进入命令(self):
		"""命令: line vty 范围"""
		v命令 = 命令.C命令("line vty")
		v命令 += self.m范围.start, self.m范围.stop - 1
		return v命令
	#操作
	def fs认证方式(self, a认证方式, a操作 = 操作.E操作.e设置):
		"""命令: authentication-mode 方式"""
	def fs登录超时(self, a秒, a操作 = 操作.E操作.e设置):
		pass	#无命令
	def fs登录重试次数(self, a数量, a操作 = 操作.E操作.e设置):
		pass	#无命令
	def fs操作超时(self, a秒: int, a操作 = 操作.E操作.e设置):
		"""命令: idle-timeout 分钟"""
		v分钟 = a秒 // 60
		v命令 = f"idle-timeout {v分钟}"
		self.f执行当前模式命令(v命令)
	def fs登录协议(self, a登录协议, a操作 = 操作.E操作.e设置):
		pass	#无命令
	def fs访问列表(self, a访问列表, a操作 = 操作.E操作.e设置):
		"""命令: telnet server [ipv6] acl 访问列表\n
			ssh server [ipv6] acl 访问列表"""
		if self.m协议 == 协议.E协议.telnet:
			v命令 = 命令.C命令("telnet server")
		elif self.m协议 == 协议.E协议.ssh:
			v命令 = 命令.C命令("ssh server")
		else:
			raise RuntimeError("不支持的协议")
		v命令 += "acl", a访问列表
		self.fg上级模式().f执行当前模式命令(v命令)