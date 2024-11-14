import cflw代码库py.cflw字符串 as 字符串
from ..基础接口 import 操作
from ..基础接口 import 安全外壳 as 北向安全外壳
from ..命令行接口 import 命令
from ..命令行接口 import 模式
from ..命令行接口 import 安全外壳 as 南向安全外壳
from ..华三命令行.常量 import *
from . import 接口 as 实现接口
#===============================================================================
# 显示
#===============================================================================
class C安全外壳显示_v7(北向安全外壳.I安全外壳显示, 模式.I显示模式):
	"""适用于: (模拟器)华三S5820V2-54QS-GE(7.1.075),
		华三s5560x(7.1.070), 华三s6900(7.1.070), 华三s9810(7.1.045),
		紫光s5200(7.1.070), 紫光s5600(7.1.070), 紫光s6600x(7.1.070), 紫光s7800xp(7.1.070), 紫光s8600x(7.1.070)"""
	def __init__(self, a):
		模式.I显示模式.__init__(self, a)
		self.m状态缓存 = None
	def fg服务状态(self):
		if not self.m状态缓存:
			self.m状态缓存 = self.m设备.f执行显示命令("display ssh server status")
		#  Stelnet server: Enable
		#  SSH version : 2.0
		#  SSH authentication-timeout : 60 second(s)
		#  SSH server key generating interval : 0 hour(s)
		#  SSH authentication retries : 3 time(s)
		#  SFTP server: Disable
		#  SFTP Server Idle-Timeout: 10 minute(s)
		#  NETCONF server: Disable
		#  SCP server: Disable
		return self.m状态缓存
	def fg开关(self):
		v服务状态 = self.fg服务状态()
		return "Stelnet server: Enable" in v服务状态
	def fg版本(self):
		v服务状态 = self.fg服务状态()
		return 字符串.f提取字符串之间(v服务状态, "SSH version : ", "\n")
	def fg访问列表(self):
		v输出 = self.m设备.f执行显示命令("display current-configuration | include ssh.server.acl", a等待 = 8)	#中低端交换机较长时间出结果,所以多等待一段时间
		# ssh server acl 3000
		if v输出:
			return 字符串.f提取字符串之间(v输出, "ssh server acl ", "\n", a结束严谨 = False)
#===============================================================================
# 配置
#===============================================================================
class C安全外壳配置_v7(南向安全外壳.I安全外壳配置, 模式.C同级模式):
	"""适用于: (模拟器)华三S5820V2-54QS-GE(7.1.075)"""
	def __init__(self, a):
		南向安全外壳.I安全外壳配置.__init__(self, a)
	def fs开关(self, a操作 = 操作.E操作.e开启):
		"""ssh server {enable|disable}"""
		if 操作.fi开操作(a操作):
			v命令 = "ssh server enable"
		else:
			v命令 = "undo ssh server enable"
		self.f执行当前模式命令(v命令)
	def fs版本(self, a版本, a操作 = 操作.E操作.e设置):
		pass	#没有命令
	def fs认证重试(self, a次数, a操作 = 操作.E操作.e设置):
		"""ssh server authentication-retries 次数"""
		v命令 = 命令.C命令("ssh server authentication-retries")
		v命令 += a次数
		self.f执行当前模式命令(v命令)
	def fs认证超时(self, a时间, a操作 = 操作.E操作.e设置):
		"""ssh server authentication-timeout 秒"""
		v命令 = 命令.C命令("ssh server authentication-timeout")
		v命令 += a时间
		self.f执行当前模式命令(v命令)
	def fs认证类型(self, a用户名, a服务类型, a认证类型, a操作 = 操作.E操作.e设置):
		"""ssh user 用户名 service-type 服务类型 authentication-type 认证类型"""
		v命令 = f"ssh user {a用户名} service-type {a服务类型} authentication-type {a认证类型}"
		self.f执行当前模式命令(v命令)