import time
import cflw代码库py.cflw字符串 as 字符串
from ..基础接口 import 操作
from ..基础接口 import 安全外壳 as 北向安全外壳
from ..命令行接口 import 命令
from ..命令行接口 import 模式
from ..命令行接口 import 安全外壳 as 南向安全外壳
from .常量 import *
from . import 接口 as 实现接口
class C安全外壳显示(北向安全外壳.I安全外壳显示, 模式.I显示模式):
	"""适用于: 浪潮s5350(6.2.27.R5.66T3), 浪潮cn61108pcvh(6.2.28, 6.6.6)"""
	def __init__(self, a):
		模式.I显示模式.__init__(self, a)
		self.m状态缓存 = None
	def fg服务状态(self):
		if not self.m状态缓存:
			self.m状态缓存 = self.m设备.f执行显示命令("show ip ssh server status")
		#  SSH server enabled
		#  Version: 2.0
		#  Authentication timeout: 60 second(s)
		#  Authentication retries: 5 time(s)
		#  Server key lifetime: 60 minute(s)
		#  Authentication type: password, public-key
		return self.m状态缓存
	def fg开关(self):
		v服务状态 = self.fg服务状态()
		return "SSH server enabled" in v服务状态
	def fg认证超时(self):
		v服务状态 = self.fg服务状态()
		v秒s = 字符串.f提取字符串之间(v服务状态, "Authentication timeout: ", " ")
		return int(v秒s)
	def fg认证重试(self):
		v服务状态 = self.fg服务状态()
		v次数s = 字符串.f提取字符串之间(v服务状态, "Authentication retries: ", " ")
		return int(v次数s)
	def fg访问列表(self):
		v输出 = self.m设备.f执行显示命令("show running-config | begin line vty")
		# line vty 0 4
		#  privilege level 4
		#  access-class ssh in 
		#  transport input ssh 
		#  no line-password
		# line vty 5 7
		v分割 = v输出.split("line vty")	#可能有多段line vty
		for v节 in v分割[1:]:
			v允许协议 = 字符串.f提取字符串之间(v节, "transport input ", " ", a结束严谨 = False)
			if v允许协议 in ("ssh", None):
				return 字符串.f提取字符串之间(v节, "access-class ", " ")
class C安全外壳配置(南向安全外壳.I安全外壳配置, 模式.C同级模式):
	def __init__(self, a):
		南向安全外壳.I安全外壳配置.__init__(self, a)
	def fs开关(self, a操作 = 操作.E操作.e开启):
		"""ip ssh server {enable|disable}"""
		if 操作.fi开操作(a操作):
			v命令 = "ip ssh server enable"
		else:
			v命令 = "ip ssh server disable"
		self.f执行当前模式命令(v命令)
	def fs版本(self, a版本, a操作 = 操作.E操作.e设置):
		v命令 = 命令.C命令("ip ssh server version")
		if a版本 == True:
			v命令 += "all"
		else:
			v命令 += a版本
		self.f执行当前模式命令(v命令)
	def fs源接口(self, a接口, a操作 = 操作.E操作.e设置):	#从思科复制过来,需要修改
		v操作 = 操作.f解析操作(a操作)
		v命令 = 命令.C命令("ip ssh source-interface")
		if 操作.fi加操作(v操作):
			v接口 = 实现接口.f创建接口(a接口)
			v命令 += v接口
		else:
			v命令.f前面添加(c不)
		self.f执行当前模式命令(v命令)
	def fs连接数(self, a数量 = 5, a操作 = 操作.E操作.e设置):	#从思科复制过来,需要修改
		v操作 = 操作.f解析操作(a操作)
		v命令 = 命令.C命令("ip ssh maxstartups")
		if 操作.fi加操作(v操作):
			v命令 += a数量
		else:
			v命令.f前面添加(c不)
		self.f执行当前模式命令(v命令)
	def fs会话超时(self, a时间, a操作 = 操作.E操作.e设置):	#从思科复制过来,需要修改
		v操作 = 操作.f解析操作(a操作)
		v命令 = 命令.C命令("ip ssh time-out")
		v命令 += a时间
		if 操作.fi减操作(v操作):
			v命令.f前面添加(c不)
		self.f执行当前模式命令(v命令)
	def fs认证重试(self, a次数, a操作 = 操作.E操作.e设置):
		"""ip ssh server authentication-retries 次数"""
		v命令 = 命令.C命令("ip ssh server authentication-retries")
		v命令 += a次数
		self.f执行当前模式命令(v命令)
	def fs认证超时(self, a时间, a操作 = 操作.E操作.e设置):
		"""ip ssh server authentication-timeout 秒"""
		v命令 = 命令.C命令("ip ssh server authentication-timeout")
		v命令 += a时间
		self.f执行当前模式命令(v命令)
	def fs认证类型(self, a类型, a操作 = 操作.E操作.e设置):
		"""ip ssh server authentication-type {all|password|public-key|rsa}"""
		v命令 = 命令.C命令("ip ssh server authentication-type")
		v命令 += a类型
		self.f执行当前模式命令(v命令)