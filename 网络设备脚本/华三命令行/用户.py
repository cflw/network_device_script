from ..基础接口 import 操作
from ..命令行接口 import 命令 as 命令
from ..基础接口 import 协议
from ..基础接口 import 接口
class C用户(设备.I用户配置):
	def __init__(self, a, a用户名):
		设备.I用户配置.__init__(self, a, a用户名)
	def fg模式参数(self):
		return self.m用户名
	def fg进入命令(self):
		v命令 = 命令.C命令("local-user")
		v命令 += self.fg模式参数()
		return v命令
	def fs密码(self, a密码):
		v命令 = 命令.C命令("password cipher")
		v命令 += a密码
		self.f执行当前模式命令(v命令)
	def fs权限(self, a权限):
		raise NotImplementedError()
	def fs服务类型(self, a服务类型):
		raise NotImplementedError()
class C用户s2126(C用户):
	def __init__(self, a, a用户名):
		C用户.__init__(self, a, a用户名)
class C用户v5(C用户):
	def __init__(self, a, a用户名):
		C用户.__init__(self, a, a用户名)
	def fs权限(self, a权限):
		v命令 = 命令.C命令("authorization-attribute level")
		v命令 += a权限
		self.f执行当前模式命令(v命令)
class C用户v7(C用户):
	def __init__(self, a, a用户名):
		C用户.__init__(self, a, a用户名)
	def fs权限(self, a权限):
		v命令 = 命令.C命令("authorization-attribute user-role level")
		v命令 += a权限
		self.f执行当前模式命令(v命令)
class C用户v7_1(C用户):
	def __init__(self, a, a用户名):
		C用户.__init__(self, a, a用户名)
	def fs权限(self, a权限):
		v命令 = 命令.C命令("authorization-attribute user-role")
		v类型 = type(a权限)
		if v类型 == int:
			v命令 += "level-%d" % (a权限,)
		else:
			v命令 += a权限
		self.f执行当前模式命令(v命令)
