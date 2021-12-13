from ..基础接口 import 操作
from ..基础接口 import 文件
from ..基础接口 import 简单网络管理协议 as 北向协议
from ..命令行接口 import 命令
from ..命令行接口 import 模式
class C代理(模式.C同级模式, 北向协议.I代理配置):
	def __init__(self, a):
		模式.C同级模式.__init__(self, a)
	def fs开关(self, a操作 = 操作.E操作.e设置):
		"""命令: snmp-agent protocol server ipv几 启用
		关闭后不再监听"""
		v操作 = 操作.f解析操作(a操作)
		v命令 = 命令.C命令("snmp-agent protocol server ipv4")
		v命令 += "enable" if 操作.fi开操作(v操作) else "disable"
		self.f执行当前模式命令(v命令)
	def fs团体字符串(self, a字符串, a权限 = 文件.E访问权限.e只读, a操作 = 操作.E操作.e设置):
		"""命令: snmp-agent community 权限 团体字"""
		v命令 = 命令.C命令("snmp-agent community")
		if 文件.fi含写(a权限):
			v命令 += "write"
		else:
			v命令 += "read"
		v命令 += a字符串
		self.f执行当前模式命令(v命令)
class C陷阱(模式.C同级模式, 北向协议.I陷阱配置):
	def __init__(self, a):
		模式.C同级模式.__init__(self, a)
	def fs开关(self, a操作 = 操作.E操作.e开启):
		"""命令: snmp-agent trap 启用"""
		v操作 = 操作.f解析操作(a操作)
		v命令 = 命令.C命令("snmp-agent trap")
		v命令 += "enable" if 操作.fi开操作(v操作) else "disable"
		v输出 = self.f执行当前模式命令(v命令)
		#Warning: All switches of SNMP trap/notification will be open. Continue? [Y/N]:
		if "[Y/N]" in v输出:
			self.m设备.f执行命令("y")
	def fs服务器(self, a地址, a字符串, a操作 = 操作.E操作.e添加):
		v命令 = 命令.C命令("snmp-agent target-host trap address udp-domain")
		v命令 += a地址
		v命令 += "params securityname", a字符串
		self.f执行当前模式命令(v命令)