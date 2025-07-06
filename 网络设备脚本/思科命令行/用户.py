import cflw代码库py.cflw字符串 as 字符串
from ..基础接口 import 操作
from ..基础接口 import 异常
from ..基础接口 import 用户 as 北向用户
from ..命令行接口 import 命令
from ..命令行接口 import 模式
from ..命令行接口 import 用户 as 南向用户
from . import 密码
from .常量 import *
#===============================================================================
# 函数
#===============================================================================
def fe提取用户名(a配置: str):
	"""show running-config | section username
	适用于: 思科c7200(15.2(4)M11)"""
	for v行 in a配置.split("\n"):
		if v用户名 := 字符串.f提取字符串之间(v行, "username ", " "):
			yield v用户名
#===============================================================================
# 用户配置
#===============================================================================
class C用户配置(模式.C同级模式, 南向用户.I用户配置):
	def __init__(self, a, a用户名):
		南向用户.I用户配置.__init__(self, a, a用户名)
		self.m命令前缀 = 命令.C命令("username %s " % (self.m用户名,))
	def fg删除命令(self):
		return c不 + self.m命令前缀
	def fg命令前缀(self):
		return self.m命令前缀
	#显示
	def f显示_当前模式配置(self):
		v命令 = "show running-config | section " + self.m命令前缀
		return self.m设备.f执行显示命令(v命令)
	#执行
	def f执行用户命令(self, a命令):
		v命令 = self.m命令前缀 + a命令
		return self.f执行当前模式命令(v命令)
	def fs密码(self, a密码, a操作 = 操作.E操作.e设置):
		"""username 用户名 secret 密码
		username 用户名 password [级别] 密码"""
		v类型 = type(a密码)
		if v类型 == 密码.C包装:
			v输出 = self.f执行用户命令(a密码)
		else:
			v输出 = self.f执行用户命令("secret %s" % (a密码,))
			#ERROR: Can not have both a user password and a user secret.
			if "ERROR:" in v输出:
				# if self.m设备.m检测异常:
					# raise 异常.X执行(v输出)	#先抛异常, 以后改成修改命令并重新执行
				v输出 = self.f执行用户命令("password %s" % (a密码,))
	def fs权限(self, a权限, a操作 = 操作.E操作.e设置):
		"""username 用户名 privilege 权限"""
		if a权限 in 北向用户.E用户权限:
			v权限 = {
				北向用户.E用户权限.e最低: 0,
				北向用户.E用户权限.e最高: 15,
			}[a权限]
		else:
			v权限 = int(a权限)
		self.f执行用户命令("privildge %d" % (v权限,))
	def fs服务类型(self, a服务类型 = None, a操作 = 操作.E操作.e设置):
		pass	#无命令
