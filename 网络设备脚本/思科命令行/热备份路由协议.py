import cflw代码库py.cflw网络地址 as 地址
from ..基础接口 import 操作
from ..基础接口 import 热备份路由协议 as 北向协议
from ..命令行接口 import 命令
from .常量 import *
from . import 接口 as 实现接口
class C配置(北向协议.I冗余路由, 实现接口.I接口配置):
	def __init__(self, a, a接口, a组号):
		实现接口.I接口配置.__init__(self, a, a接口)
		self.m组号 = int(a组号)
	def fg前置命令(self):
		return 命令.C命令(f"stanby {self.fg组号()}")
	#显示
	def fg组号(self):
		return self.m组号
	#配置
	def fs版本(self, a版本, a操作 = 操作.E操作.e设置):
		v命令 = f"standby version {a版本}"
		self.f执行当前模式命令(v命令)
	def fs网络地址4(self, a地址, a操作 = 操作.E操作.e设置):
		v地址 = 地址.S网络地址4.fc自动(a地址)
		v命令 = self.fg前置命令()
		v命令 += "ip", v地址.fg地址s()
		self.f执行当前模式命令(v命令)
	def fs抢占(self, a操作 = 操作.E操作.e开启):
		v操作 = 操作.f解析操作(a操作)
		v命令 = self.fg前置命令()
		v命令 += "preempt"
		v命令.f前置肯定(操作.fi关操作(v操作), c不)
		self.f执行当前模式命令(v命令)
	def fs优先级(self, a优先级, a操作 = 操作.E操作.e设置):
		v命令 = self.fg前置命令()
		v命令 += "priority", a优先级
		self.f执行当前模式命令(v命令)
	def fs问候时间(self, a秒, a操作 = 操作.E操作.e设置):
		raise NotImplementedError()
	def fs维持时间(self, a秒, a操作 = 操作.E操作.e设置):
		raise NotImplementedError()
	def fs跟踪(self, a接口, a优先级, a操作 = 操作.E操作.e设置):
		v接口 = 实现接口.f创建接口(a接口)
		v命令 = self.fg前置命令()
		v命令 += "track", v接口, -a优先级
		self.f执行当前模式命令(v命令)
	def fs认证(self, a密码, a操作 = 操作.E操作.e设置):
		v命令 = self.fg前置命令()
		v命令 += "authentication md5 key-string", a密码
		self.f执行当前模式命令(v命令)
