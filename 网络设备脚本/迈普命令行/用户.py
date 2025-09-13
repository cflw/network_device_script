import cflw代码库py.cflw字符串 as 字符串
import cflw代码库py.cflw工具_序列 as 序列
from ..基础接口 import 用户 as 北向用户
from ..命令行接口 import 模式
#===============================================================================
# 常量
#===============================================================================
#服务类型
ca服务类型 = {
	北向用户.E服务类型.e终端: "console",
	北向用户.E服务类型.e网络终端: "telnet",
	北向用户.E服务类型.e安全外壳: "ssh",
}
ca对应服务类型 = 序列.f字典键值反转(ca服务类型)
#===============================================================================
# 函数
#===============================================================================
def f提取用户名(a配置: str):
	return 字符串.f提取字符串之间(a配置, "user ", " ")
def f提取用户配置(a配置: str, a用户名: str):
	v配置 = 字符串.f提取多行包含行(a配置, f"user {a用户名}")
	return v配置
def f提取密码(a配置: str):
	v关键字位置 = a配置.find("password")
	v加密级别位置 = a配置.find(" ", v关键字位置) + 1
	v密码位置 = a配置.find(" ", v加密级别位置) + 1
	v结束位置 = a配置.find("\n", v密码位置)
	return a配置[v密码位置:v结束位置].strip()
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
def f提取服务类型(a配置: str):
	#user xxx service-type console ssh
	v字符串 = 字符串.f提取字符串之间(a配置, "service-type ", "\n", a结束严谨 = False)
	if not v字符串:
		return []
	return list(map(lambda x: ca对应服务类型.get(x), v字符串.split(" ")))
def fe配置用户名(a配置: str):
	"""适用于: 迈普t6100(v9.3.4.45)"""
	va用户名 = set()	#一个用户可能有多行配置,需要去重
	for v行 in 字符串.fe包含行(a配置, "user"):
		v用户名 = f提取用户名(v行)
		if v用户名 not in va用户名:
			va用户名.add(v用户名)
			yield v用户名
#===============================================================================
# 用户显示模式
#===============================================================================
class C用户显示_v9(模式.I显示模式, 北向用户.I用户显示):
	"""适用于: 迈普t6100(v9.3.4.45)"""
	def __init__(self, a, a用户名: str, a配置: str = ""):
		模式.I显示模式.__init__(self, a)
		self.m用户名 = a用户名
		self.m缓存 = a配置
	def fg配置(self):
		if not self.m缓存:
			v命令 = f"show running-config | include user {self.m用户名} "
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