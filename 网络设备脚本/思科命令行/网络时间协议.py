from ..基础接口 import 操作
from ..命令行接口 import 网络时间协议 as 南向协议
from ..命令行接口 import 模式
from ..命令行接口 import 命令
from .常量 import *
class C服务器(模式.C同级模式, 南向协议.I服务器配置):
	def __init__(self, a):
		南向协议.I服务器配置.__init__(self, a)
	def fs开关(self, a操作 = 操作.E操作.e开启):
		self.fs层数(a操作 = a操作)
	def fs层数(self, a层数 = 8, a操作 = 操作.E操作.e设置):
		v操作 = 操作.f解析操作(a操作)
		v命令 = 命令.C命令("ntp master")
		if 操作.fi加操作(v操作):
			v命令 += a层数
		else:
			v命令.f前面添加(c不)
		self.f执行当前模式命令(v命令)
	def fs发送广播(self, a操作 = 操作.E操作.e开启):
		v命令 = 命令.C命令("ntp broadcast")
		v命令.f前置肯定(操作.fi开操作(a操作))
		self.f执行当前模式命令(v命令)
class C客户端(模式.C同级模式, 南向协议.I客户端配置):
	def __init__(self, a):
		南向协议.I客户端配置.__init__(self, a)
	def f模式_远端(self, a地址, a端 = 操作.E端.e服务器, a操作 = 操作.E操作.e新建):
		v模式 = C远端(self, a地址)
		if a操作 == 操作.E操作.e新建:
			v模式.f执行当前模式命令(v模式.fg命令前缀())
		return v模式
	def fs开关(self, a操作 = None):
		pass
	def fs接收广播(self, a操作 = 操作.E操作.e开启):
		v操作 = 操作.f解析操作(a操作)
		v命令 = 命令.C命令("ntp broadcast client")
		v命令.f前置肯定(操作.fi关操作(v操作))
		self.f执行当前模式命令(v命令)
class C远端(模式.C同级模式, 南向协议.I远端配置):
	def __init__(self, a, a地址):
		南向协议.I远端配置.__init__(self, a, a地址)
	def fg命令前缀(self):
		return 命令.C命令(f"ntp server {self.fg地址()}")
	def fs版本(self, a版本, a操作 = 操作.E操作.e设置):
		v命令 = self.fg命令前缀()
		v命令 += "version", a版本
		self.f执行当前模式命令(v命令)
	def fs优先(self, a操作 = 操作.E操作.e设置):
		pass
	def fs认证(self, a钥匙 = 0, a操作 = 操作.E操作.e设置):
		v命令 = self.fg命令前缀()
		v命令 += "key", a钥匙
		self.f执行当前模式命令(v命令)
	def fs源(self, a源, a操作 = 操作.E操作.e设置):
		raise NotImplementedError()