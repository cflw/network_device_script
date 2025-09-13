import cflw代码库py.cflw字符串 as 字符串
import cflw代码库py.cflw工具_序列 as 序列
from ..基础接口 import 操作
from ..基础接口 import 用户 as 北向用户
from ..命令行接口 import 模式
from ..命令行接口 import 命令
#===============================================================================
# 常量
#===============================================================================
ca服务类型 = {
	北向用户.E服务类型.e终端: "terminal",
	北向用户.E服务类型.e网络终端: "telnet",
	北向用户.E服务类型.e安全外壳: "ssh",
	北向用户.E服务类型.e网页: "web",
	北向用户.E服务类型.e超文本: "http",
}
ca对应服务类型 = 序列.f字典键值反转(ca服务类型)
#===============================================================================
# 函数
#===============================================================================
def f提取用户名(a行: str):
	return 字符串.f提取字符串之间(a行, "local-user ", " ")
def f提取用户配置(a配置: str, a用户名: str):
	return 字符串.f提取多行包含行(a配置, f"local-user {a用户名}")
def f提取密码(a配置: str):
	#local-user test password simple test
	v关键字位置 = a配置.find("password")
	v加密级别位置 = a配置.find(" ", v关键字位置) + 1
	v密码位置 = a配置.find(" ", v加密级别位置) + 1
	v结束位置 = a配置.find("\n", v密码位置)
	return a配置[v密码位置:v结束位置].strip()
def f提取权限(a配置: str):
	#local-user test privilege level 15
	v关键字位置 = a配置.find("level")
	if v关键字位置 == -1:
		return 北向用户.E用户权限.e最低
	v数字位置 = a配置.find(" ", v关键字位置) + 1
	v数字结束 = a配置.find(" ", v数字位置)
	v数字 = int(a配置[v数字位置 : v数字结束])
	if v数字 == 15:
		return 北向用户.E用户权限.e最高
	return v数字
def f提取服务类型(a配置: str):
	#local-user test service-type telnet terminal ssh
	v字符串 = 字符串.f提取字符串之间(a配置, "service-type ", "\n", a结束严谨 = False)
	if not v字符串:
		return []
	return list(map(lambda x: ca对应服务类型.get(x), v字符串.split(" ")))
def fe配置用户名(a配置: str):
	va用户名 = set()	#一个用户可能有多行配置,需要去重
	for v行 in 字符串.fe包含行(a配置, "local-user"):
		v用户名 = f提取用户名(v行)
		if v用户名 not in va用户名:
			va用户名.add(v用户名)
			yield v用户名
#===============================================================================
# 用户配置
#===============================================================================
class C用户配置(北向用户.I用户配置, 模式.I模式):
	def __init__(self, a, a用户名: str):
		模式.I模式.__init__(self, a)
		self.m用户名 = a用户名
	def fg进入命令(self):
		return "aaa"
	def fg命令前缀(self):
		return 命令.C命令(f"local-user {self.m用户名}")
	def fs密码(self, a密码, a操作 = 操作.E操作.e设置):
		v命令 = self.fg命令前缀()
		v命令 += "password cipher", a密码
		self.f执行当前模式命令(v命令)
	def fs权限(self, a权限, a操作 = 操作.E操作.e设置):
		v命令 = self.fg命令前缀()
		if a权限 in 北向用户.E用户权限:
			v权限 = {
				北向用户.E用户权限.e最低: 0,
				北向用户.E用户权限.e最高: 15,
			}[a权限]
		else:
			v权限 = int(a权限)
		v命令 += "privilege level", v权限
		self.f执行当前模式命令(v命令)
	def fs服务类型(self, a服务类型, a操作 = 操作.E操作.e设置):
		va服务类型 = 北向用户.f解析服务类型(a服务类型)
		v命令 = self.fg命令前缀()
		v命令 += "service-type"
		v命令 += tuple(ca服务类型[v] for v in va服务类型)
		self.f执行当前模式命令(v命令)
#===============================================================================
# 用户显示
#===============================================================================
class C用户显示(模式.I显示模式, 北向用户.I用户显示):
	"""适用于: (模拟器)华为s5700(v5.110)"""
	def __init__(self, a, a用户名: str, a缓存: str = ""):
		模式.I显示模式.__init__(self, a)
		self.m用户名 = a用户名
		self.m缓存 = a缓存
	def fg配置(self)->str:
		if not self.m缓存:
			v命令 = f"display current-configuration | include local-user {self.m用户名} "
			self.m缓存 = self.m设备.f执行显示命令(v命令)
		return self.m缓存
	def fg用户名(self):
		return self.m用户名
	def fg密码(self):	#基本上只能显示密文密码
		return f提取密码(self.fg配置())
	def fg权限(self):
		return f提取权限(self.fg配置())
	def fg服务类型(self):
		return f提取服务类型(self.fg配置())