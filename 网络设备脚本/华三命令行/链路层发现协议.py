import cflw代码库py.cflw字符串 as 字符串
import cflw代码库py.cflw网络地址 as 地址
from ..基础接口 import 操作
from ..基础接口 import 数据表
from ..基础接口 import 接口 as 北向接口
from ..基础接口 import 链路层发现协议 as 北向协议
from ..命令行接口 import 命令
from ..命令行接口 import 模式
from ..命令行接口 import 链路层发现协议 as 南向协议
from .常量 import *
from . import 接口 as 实现接口
#===============================================================================
# 配置模式
#===============================================================================
class C进程配置v7(模式.C同级模式, 南向协议.I进程配置):
	def __init__(self, a):
		南向协议.I进程配置.__init__(self, a)
	def f模式_接口(self, a接口):
		v接口 = 实现接口.f创建接口(a接口)
		return C接口配置v7(self.fg上级模式(), v接口)
	def fs开关(self, a操作 = 操作.E操作.e开启):
		v操作 = 操作.f解析操作(a操作)
		v命令 = 命令.C命令("lldp global enable")
		v命令.f前置肯定(操作.fi关操作(v操作), c不)
		self.f执行当前模式命令(v命令)
class C接口配置v7(南向协议.I接口配置):
	def __init__(self, a, a接口):
		南向协议.I接口配置.__init__(self, a, a接口)
	def fs开关(self, a操作 = 操作.E操作.e开启):
		v操作 = 操作.f解析操作(a操作)
		v命令 = 命令.C命令("lldp enable")
		v命令.f前置肯定(操作.fi关操作(v操作), c不)
		self.f执行当前模式命令(v命令)
#===============================================================================
# 数据表
#===============================================================================
class C邻居表v7:
	c值开始 = 23
	def __init__(self, a文本):
		self.m文本 = str(a文本)
	def __iter__(self):
		return self.fe行()
	def fe行(self):
		v表项 = None
		for v行 in self.m文本.split("\n"):
			if len(v行) < C邻居表v7.c值开始:
				continue
			#LLDP neighbor-information of port 2[GigabitEthernet1/0/1]:
			if "neighbor-information" in v行:
				if v表项:
					yield v表项
				v表项 = 数据表.C记录()
				v接口s = 字符串.f提取字符串之间(v行, "[", "]")
				v接口 = 实现接口.f创建接口(v接口s)
				v表项[数据表.E字段.e本端接口] = v接口
			#LLDP agent nearest-bridge:
			if v行[0] == " ":
				v键 = v行[:C邻居表v7.c值开始-2].strip()
				v值 = v行[C邻居表v7.c值开始:].strip()
			else:
				v键 = ""
			# LLDP neighbor index : 1
			# ChassisID/subtype   : 5e0b-be09-0200/MAC address
			if v键 == "ChassisID/subtype":
				v物理地址s = 字符串.f提取字符串之间(v值, None, "/", a反向查找 = True)
				v物理地址 = 地址.S物理地址.fc字符串(v物理地址s)
				v表项[数据表.E字段.e对端物理地址] = v物理地址
			# PortID/subtype      : GigabitEthernet1/0/1/Interface name
			if v键 == "PortID/subtype":
				v接口s = 字符串.f提取字符串之间(v值, None, "/", a反向查找 = True)
				v接口 = 北向接口.S接口.fc字符串(v接口s)
				v表项[数据表.E字段.e对端接口] = v接口
			# Capabilities        : Bridge, Router, Customer Bridge
		if v表项:
			yield v表项
