import cflw代码库py.cflw字符串 as 字符串
import cflw代码库py.cflw工具_序列 as 序列
from ..基础接口 import 操作
from ..基础接口 import 用户 as 北向用户
from ..命令行接口 import 命令
from ..命令行接口 import 模式
from ..命令行接口 import 显示
#===============================================================================
# 常量
#===============================================================================
#服务类型
ca服务类型 = {
	北向用户.E服务类型.e终端: "terminal",
	北向用户.E服务类型.e网络终端: "telnet",
	北向用户.E服务类型.e安全外壳: "ssh",
	北向用户.E服务类型.e网页: "web",
	北向用户.E服务类型.e超文本: "http",
}
ca对应服务类型 = 序列.f字典键值反转(ca服务类型)
#角色
c网络操作员 = "network-operator"
c网络管理员 = "network-admin"
c安全审计员 = "security-audit"
ca角色 = {
	北向用户.E用户权限.e最低: c网络操作员,
	北向用户.E用户权限.e最高: c网络管理员,
}
ca名称对应角色 = 序列.f字典键值反转(ca角色)
#===============================================================================
# 函数
#===============================================================================
def f提取用户名(a行: str):
	#local-user test1 class manage
	return 字符串.f提取字符串之间(a行, "local-user ", " ")
def f提取用户配置(a配置: str, a用户名: str):
	v头 = f"local-user {a用户名} "
	return 显示.f取单节选(a配置, v头)
def f提取密码(a配置: str):
	# password hash $h$6$yvKwa1Nm6IBqj8iC$GHI6itV7uv9pst1KMxsnHCX+dzWperbfWRuOJE+CtzVSgzTHSkoyRxTqfvqOj1T+rpOIOKce7nukP/MFv9806Q==
	v关键字位置 = a配置.find("password")
	v加密级别位置 = a配置.find(" ", v关键字位置) + 1
	v密码位置 = a配置.find(" ", v加密级别位置) + 1
	v结束位置 = a配置.find("\n", v密码位置)
	return a配置[v密码位置 : v结束位置].strip()
def f提取权限(a配置: str):
	# authorization-attribute user-role network-operator
	#一个用户可能有多个角色,脚本只取第一个
	v关键字位置 = a配置.find("user-role")
	if v关键字位置 == -1:
		return 北向用户.E用户权限.e最低
	v角色位置 = a配置.find(" ", v关键字位置) + 1
	v角色结束 = a配置.find("\n", v角色位置)
	v角色 = a配置[v角色位置:] if v角色结束 == -1 else a配置[v角色位置:v角色结束]
	if "level-" in v角色:
		v级别 = int(v角色[6:])
		if v级别 == 0:
			return 北向用户.E用户权限.e最低
		elif v级别 == 15:
			return 北向用户.E用户权限.e最高
		else:
			return v级别
	if v角色 in ca名称对应角色:
		return ca名称对应角色.get(v角色)
	else:
		return v角色
def f提取服务类型(a配置: str):
	# service-type telnet ssh terminal
	v字符串 = 字符串.f提取字符串之间(a配置, "service-type ", "\n", a结束严谨 = False)
	if not v字符串:
		return []
	return list(map(lambda x: ca对应服务类型.get(x), v字符串.split(" ")))
def fe配置用户名(a配置: str):
	for v行 in 字符串.fe包含行(a配置, "local-user"):
		v用户名 = f提取用户名(v行)
		yield v用户名
def f生成权限_v7_1(a权限)->str:
	v类型 = type(a权限)
	if v类型 == 北向用户.E用户权限:
		return ca角色.get(a权限)
	elif v类型 == int:
		if a权限 <= 1:
			return c网络操作员
		elif a权限 == 15:
			return c网络管理员
		else:
			return f"level-{a权限}"
	else:
		raise ValueError("无法解析的类型")
#===============================================================================
# 配置模式
#===============================================================================
class C用户配置_v7(北向用户.I用户配置, 模式.I模式):
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
class C用户配置_v7_1(C用户配置_v7):
	def __init__(self, a, a用户名: str):
		C用户配置_v7.__init__(self, a, a用户名)
	def fs权限(self, a权限, a操作 = 操作.E操作.e设置):
		v命令 = 命令.C命令("authorization-attribute user-role")
		v命令 += f生成权限_v7_1(a权限)
		self.f执行当前模式命令(v命令)
#===============================================================================
# 显示模式
#===============================================================================
class C用户显示_v7_1(模式.I显示模式, 北向用户.I用户显示):
	"""适用于: (模拟器)华三s6850(v7.1.070)"""
	def __init__(self, a, a用户名: str, a配置: str = ""):
		模式.I显示模式.__init__(self, a)
		self.m用户名 = a用户名
		self.m缓存 = a配置
	def fg配置(self):
		if not self.m缓存:
			v命令 = f"display current-configuration | begin local-user {self.m用户名}"
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