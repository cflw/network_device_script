import time
import cflw代码库py.cflw字符串 as 字符串
from ..基础接口 import 操作
from ..基础接口 import 安全外壳 as 北向安全外壳
from ..命令行接口 import 命令
from ..命令行接口 import 模式
from ..命令行接口 import 显示
from ..命令行接口 import 安全外壳 as 南向安全外壳
from ..思科命令行.常量 import *
#===============================================================================
# 解析
#===============================================================================
def f提取访问列表(a多节: str):
	"""从show running-config | begin line vty提取acl名称
	适用于: 迈普t6100(v9.3.4.45)"""
	#line vty 0 4
	# access-class 100 in
	# privilege level 15
	# login local
	# exit
	v分割 = a多节.split("line vty")	#可能有多段line vty
	for v节 in v分割[1:]:
		return 字符串.f提取字符串之间(v节, "access-class ", " ")
#===============================================================================
# 显示
#===============================================================================
class C安全外壳显示_v9(北向安全外壳.I安全外壳显示, 模式.I显示模式):
	"""适用于: 迈普t6100(v9.3.4.45)"""
	def __init__(self, a):
		模式.I显示模式.__init__(self, a)
	def fg开关(self):
		v输出 = self.m设备.f执行显示命令("show running-config | include ip ssh server", a等待 = 5)
		return "ip ssh server" in v输出
	def fg访问列表(self):
		v输出 = self.m设备.f执行显示命令("show running-config | begin line vty", a等待 = 5)
		return f提取访问列表(v输出)
	def fg版本(self):
		v输出 = self.m设备.f执行显示命令("show running-config | include ip ssh server", a等待 = 5)
		if "sshv1-compatible" in v输出:
			return 1
		else:
			return 2
	def fg日志记录(self):
		pass	#无命令
