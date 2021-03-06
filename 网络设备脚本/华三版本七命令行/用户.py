from ..基础接口 import 操作
from ..基础接口 import 用户 as 北向用户
from ..命令行接口 import 命令
from ..命令行接口 import 模式
ca服务类型 = {
	北向用户.E服务类型.e终端: "terminal",
	北向用户.E服务类型.e网络终端: "telnet",
	北向用户.E服务类型.e安全外壳: "ssh",
	北向用户.E服务类型.e网页: "web",
}
class C用户v7(北向用户.I用户配置, 模式.I模式):
	def __init__(self, a, a用户名: str):
		模式.I模式.__init__(self, a)
		self.m用户名 = a用户名
	def fg模式参数(self):
		return self.m用户名
	def fg进入命令(self):
		v命令 = 命令.C命令("local-user")
		v命令 += self.m用户名
		return v命令
	def fs密码(self, a密码, a操作 = 操作.E操作.e设置):
		v命令 = 命令.C命令("password cipher")
		v命令 += a密码
		self.f执行当前模式命令(v命令)
	def fs权限(self, a权限, a操作 = 操作.E操作.e设置):
		#未完成
		v命令 = 命令.C命令("authorization-attribute user-role level")
		v命令 += a权限
		self.f执行当前模式命令(v命令)
	def fs服务类型(self, a服务类型, a操作 = 操作.E操作.e设置):
		va服务类型 = 北向用户.f解析服务类型(a服务类型)
		v命令 = 命令.C命令("service-type")
		v命令 += tuple(ca服务类型[v] for v in va服务类型)
		self.f执行当前模式命令(v命令)
class C用户v7_1(C用户v7):
	def __init__(self, a, a用户名: str):
		C用户v7.__init__(self, a, a用户名)
	def fs权限(self, a权限, a操作 = 操作.E操作.e设置):
		#未完成
		v命令 = 命令.C命令("authorization-attribute user-role")
		v类型 = type(a权限)
		if v类型 == int:
			v命令 += "level-%d" % (a权限,)
		else:
			v命令 += a权限
		self.f执行当前模式命令(v命令)
