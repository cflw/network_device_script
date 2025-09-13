import cflw代码库py.cflw字符串 as 字符串
import cflw代码库py.cflw工具_序列 as 序列
from ..基础接口 import 用户 as 北向用户
from ..基础接口 import 操作
from ..命令行接口 import 命令
from ..命令行接口 import 模式
from ..命令行接口 import 显示
from ..命令行接口 import 用户 as 南向用户
from ..思科命令行.常量 import *
#===============================================================================
# 常量
#===============================================================================
ca角色 = {
	北向用户.E用户权限.e最低: "network-operator",
	北向用户.E用户权限.e最高: "network-admin",
}
ca名称对应角色 = 序列.f字典键值反转(ca角色)
#===============================================================================
# 函数
#===============================================================================
def f提取用户名(a配置: str):
	"""从username行提取用户名"""
	return 字符串.f提取字符串之间(a配置, "username ", " ")
def f提取用户配置(a配置: str, a用户名: str):
	v配置 = 显示.f换行拼接_固定开头(a配置, "username")	#可能存在断行,先拼接
	v配置 = 字符串.f提取多行包含行(v配置, f"username {a用户名}")
	return v配置
def f提取密码(a配置: str):
	v关键字位置 = a配置.find("password")
	v加密级别位置 = a配置.find(" ", v关键字位置) + 1
	v密码位置 = a配置.find(" ", v加密级别位置) + 1
	v结束位置 = a配置.find(" ", v密码位置)
	return a配置[v密码位置:v结束位置].strip()
def f提取权限(a配置: str):
	#username admin password 5 xxx  role network-admin
	#一个用户可能有多个角色,脚本只取第一个
	v关键字位置 = a配置.find("role")
	if v关键字位置 == -1:
		return 北向用户.E用户权限.e最低
	v角色位置 = a配置.find(" ", v关键字位置) + 1
	v角色结束 = a配置.find("\n", v角色位置)
	v角色 = a配置[v角色位置:] if v角色结束 == -1 else a配置[v角色位置:v角色结束]
	if "priv-" in v角色:
		v级别 = int(v角色[5:])
		if v级别 <= 1:
			return 北向用户.E用户权限.e最低
		elif v级别 == 15:
			return 北向用户.E用户权限.e最高
		else:
			return v级别
	if v角色 in ca名称对应角色:
		return ca名称对应角色.get(v角色)
	else:
		return v角色
def fe配置用户名(a配置: str):
	"""适用于: 浪潮cn8696q(v7.3(5)N1(1))"""
	va用户名 = set()	#一个用户可能有多行配置,需要去重
	for v行 in 字符串.fe包含行(a配置, "username"):
		v用户名 = f提取用户名(v行)
		if v用户名 not in va用户名:
			va用户名.add(v用户名)
			yield v用户名
#===============================================================================
# 配置模式
#===============================================================================
class C用户配置_nv7(模式.C同级模式, 南向用户.I用户配置):
	"""适用于: 思科nexus系列(v7.*), 浪潮cn系列(v7.*)"""
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
		"""命令: username 用户名 role 角色
		最高network-admin"""
		v命令 = self.fg命令前缀()
		if a权限 in 北向用户.E用户权限:
			v权限 = ca角色[a权限]
		else:
			v权限 = int(a权限)
		v命令 += "role", v权限
		self.f执行当前模式命令(v命令)
	def fs服务类型(self, a服务类型, a操作 = 操作.E操作.e设置):
		pass
#===============================================================================
# 显示模式
#===============================================================================
class C用户显示_nv7(模式.I显示模式, 北向用户.I用户显示):
	"""适用于: 浪潮cn8696q(v7.3(5)N1(1)), 浪潮cn61108pcv(v9.2(3iE2))"""
	def __init__(self, a, a用户名: str, a配置: str = ""):
		模式.I显示模式.__init__(self, a)
		self.m用户名 = a用户名
		self.m缓存 = a配置
	def fg配置(self)->str:
		if not self.m缓存:
			v命令 = f"show running-config | include username {self.m用户名} "
			self.m缓存 = self.m设备.f执行显示命令(v命令)
		return self.m缓存
	def fg用户名(self):
		return self.m用户名
	def fg密码(self):	#基本上只能显示密文密码
		return f提取密码(self.fg配置())
	def fg权限(self):
		return f提取权限(self.fg配置())
	def fg服务类型(self):
		pass	#无命令