from ..基础接口 import 操作
from ..基础接口 import 用户 as 北向用户
from ..命令行接口 import 模式
from ..命令行接口 import 命令
from ..命令行接口 import 用户 as 南向用户
ca服务类型 = {
	北向用户.E服务类型.e终端: "terminal",
	北向用户.E服务类型.e网络终端: "telnet",
	北向用户.E服务类型.e安全外壳: "ssh",
	北向用户.E服务类型.e网页: "web",
}
class C用户配置(南向用户.I用户配置):
	def __init__(self, a, a用户名):
		南向用户.I用户配置.__init__(self, a, a用户名)
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
		v命令 = self.fg命令前缀()
		v命令 += "service-type"
		v命令 += 南向用户.f生成服务类型(ca服务类型, a服务类型)
		self.f执行当前模式命令(v命令)
