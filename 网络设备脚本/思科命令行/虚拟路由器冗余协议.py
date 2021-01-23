import cflw代码库py.cflw网络地址 as 地址
from ..基础接口 import 虚拟路由器冗余协议 as 北向协议
from ..基础接口 import 操作
from ..命令行接口 import 命令
from . import 接口 as 实现接口
from .常量 import *
class C冗余路由(北向协议.I冗余路由, 实现接口.I接口配置):
	def __init__(self, a, a接口, a组号):
		实现接口.I接口配置.__init__(self, a, a接口)
		self.m组号 = int(a组号)
	def fg命令前缀(self):
		return 命令.C命令(f"vrrp {self.m组号}")
	def fg组号(self):
		return self.m组号
	#配置
	def fs网络地址4(self, a地址, a操作 = 操作.E操作.e设置):
		"""命令: vrrp 组号 ip 地址"""
		v地址 = 地址.S网络地址4.fc自动(a地址)
		v命令 = self.fg命令前缀()
		v命令 += "ip", v地址.fg地址s()
		self.f执行当前模式命令(v命令)
	def fs网络地址6(self, a地址, a操作 = 操作.E操作.e设置):
		"""命令: vrrp 组号 ipv6 地址"""
		v地址 = 地址.S网络地址6.fc自动(a地址)
		v命令 = self.fg命令前缀()
		v命令 += "ipv6", v地址.fg地址s()
		self.f执行当前模式命令(v命令)
	def fs抢占(self, a开关 = True):
		"""命令: [no] vrrp 组号 preempt [delay minimum 抢占延时]"""
		v操作 = 操作.f解析操作(a开关)
		v命令 = self.fg命令前缀()
		v命令 += "preempt"
		v命令.f前置否定(操作.fi关操作(v操作), c不)
		self.f执行当前模式命令(v命令)
	def fs优先级(self, a优先级, a操作 = 操作.E操作.e设置):
		"""命令: vrrp 组号 priority 优先级"""
		v操作 = 操作.f解析操作(a操作)
		v优先级 = int(a优先级)
		v命令 = self.fg命令前缀()
		v命令 += "priority", v优先级
		v命令.f前置否定(操作.fi关操作(v操作), c不)
		self.f执行当前模式命令(v命令)