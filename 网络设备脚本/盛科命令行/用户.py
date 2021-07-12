from ..基础接口 import 操作
from ..基础接口 import 用户 as 北向用户
from ..命令行接口 import 模式
from ..命令行接口 import 命令
from ..命令行接口 import 用户 as 南向用户
from .常量 import *
ca权限 = {
	北向用户.E用户权限.e最低: 1,
	北向用户.E用户权限.e最高: 4,
}
class C用户ev6(模式.C同级模式, 南向用户.I用户配置):
	"""适用于: 盛科e580(v6.x), 浪潮cn61108pcvh(v6.x), 浪潮s5350(v6.x)"""
	def __init__(self, a, a用户名):
		南向用户.I用户配置.__init__(self, a, a用户名)
	def fg命令前缀(self):
		return 命令.C命令(f"username {self.m用户名}")
	def fg删除命令(self):
		"""命令: no username 用户名"""
		return self.fg命令前缀().f前面添加(c不)
	def fs密码(self, a密码, a操作 = 操作.E操作.e设置):
		"""命令: username 用户名 password 密码"""
		v命令 = self.fg命令前缀()
		v命令 += "password", a密码
		self.f执行当前模式命令(v命令)
	def fs权限(self, a权限, a操作 = 操作.E操作.e设置):
		"""命令: username 用户名 privilege 权限
		最高4"""
		v命令 = self.fg命令前缀()
		if a权限 in 北向用户.E用户权限:
			v权限 = ca权限[a权限]
		else:
			v权限 = int(a权限)
		v命令 += "privilege", v权限
		self.f执行当前模式命令(v命令)
	def fs服务类型(self, a服务类型, a操作 = 操作.E操作.e设置):
		pass
