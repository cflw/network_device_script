from ..基础接口 import 操作
from ..基础接口 import 用户 as 北向用户
from ..命令行接口 import 模式
from ..命令行接口 import 命令
from ..命令行接口 import 用户 as 南向用户
from ..思科命令行.常量 import *
ca权限 = {
	北向用户.E用户权限.e最低: 1,
	北向用户.E用户权限.e最高: 15,
}
class C用户_sv3(模式.C同级模式, 南向用户.I用户配置):
	"""用户模式
	适用于: 浪潮s6550(v3.x)"""
	def __init__(self, a, a用户名):
		南向用户.I用户配置.__init__(self, a, a用户名)
	def fg命令前缀(self):
		return 命令.C命令(f"user name {self.m用户名}")
	def fg删除命令(self):
		"""没有命令"""
		return ""
	def fs密码(self, a密码, a操作 = 操作.E操作.e设置):
		"""命令: user name 用户名 password 密码"""
		v命令 = self.fg命令前缀()
		v命令 += "password", a密码
		v输出 = self.f执行当前模式命令(v命令)
		# User exist,if you want to modify the user information,please input 'yes' to confirm:
		if "confirm" in v输出:
			self.m设备.f执行命令("yes")
	def fs权限(self, a权限, a操作 = 操作.E操作.e设置):
		"""命令: user name 用户名 privilege 权限"""
		v命令 = self.fg命令前缀()
		if a权限 in 北向用户.E用户权限:
			v权限 = ca权限[a权限]
		else:
			v权限 = int(a权限)
		v命令 += "privilege", v权限
		self.f执行当前模式命令(v命令)
	def fs服务类型(self, a服务类型, a操作 = None):
		"""命令: user 用户名 service-type 服务类型"""
		pass