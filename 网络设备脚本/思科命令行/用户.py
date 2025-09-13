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
def f提取用户名(a行: str):
	"""从username行提取用户名"""
	return 字符串.f提取字符串之间(a行, "username ", " ")
def f提取密码(a行: str):
	v关键字位置 = a行.find("password")
	v加密级别位置 = a行.find(" ", v关键字位置) + 1
	v密码位置 = a行.find(" ", v加密级别位置) + 1
	return a行[v密码位置:].strip()
def f提取权限(a行: str):
	v关键字位置 = a行.find("privilege")
	if v关键字位置 == -1:
		return 北向用户.E用户权限.e最低
	v数字位置 = a行.find(" ", v关键字位置) + 1
	v数字结束 = a行.find(" ", v数字位置)
	v数字 = int(a行[v数字位置 : v数字结束])
	if v数字 == 15:
		return 北向用户.E用户权限.e最高
	return v数字
def fe配置用户名(a配置: str):
	"""show running-config | section username
	适用于: 思科c7200(15.2(4)M11)"""
	for v行 in 字符串.fe包含行(a配置, "username"):
		yield f提取用户名(v行)
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
#===============================================================================
# 用户显示
#===============================================================================
class C用户显示(模式.I显示模式, 北向用户.I用户显示):
	"""适用于: (模拟器)思科c7200"""
	def __init__(self, a, a用户名: str, a缓存: str = ""):
		模式.I显示模式.__init__(self, a)
		self.m用户名 = a用户名
		self.m缓存 = a缓存
	def fg配置(self)->str:
		if not self.m缓存:
			v命令 = f"show running-config | include username {self.m用户名} "
			self.m缓存 = self.m设备.f执行显示命令(v命令)	#只有一行
		return self.m缓存
	def fg用户名(self):
		return self.m用户名
	def fg密码(self):	#基本上只能显示密文密码
		return f提取密码(self.fg配置())
	def fg权限(self):
		return f提取权限(self.fg配置())
	def fg服务类型(self):
		pass	#无命令