import time
import cflw代码库py.cflw字符串 as 字符串
from ..基础接口 import 操作
from ..基础接口 import 异常
from ..基础接口 import 安全外壳 as 北向安全外壳
from ..命令行接口 import 命令
from ..命令行接口 import 模式
from ..命令行接口 import 安全外壳 as 南向安全外壳
from ..思科命令行.常量 import *
from . import 接口 as 实现接口
class C安全外壳显示(北向安全外壳.I安全外壳显示, 模式.I显示模式):
	"""适用于: 浪潮cn61108pc-v(7.0(3)I7(1)), 浪潮cn8696(7.3(0)N1(1c))"""
	def __init__(self, a):
		模式.I显示模式.__init__(self, a)
	def fg开关(self):
		v输出 = self.m设备.f执行显示命令("show ssh server")
		return "enabled" in v输出
	def fg密钥(self):
		v输出 = self.m设备.f执行显示命令("show ssh key")
		return v输出
	def fg版本(self):
		v输出 = self.m设备.f执行显示命令("show ssh server")
		return 字符串.f提取字符串之间(v输出, "version ", " ", a结束严谨 = False)
	def fg访问列表(self):
		v输出 = self.m设备.f执行显示命令("show running-config | section line.vty", a等待 = 5)
		v允许协议 = 字符串.f提取字符串之间(v输出, "transport input ", "\n", a结束严谨 = False)
		if v允许协议 in ("ssh", None):
			return 字符串.f提取字符串之间(v输出, "access-class ", " ")
class C安全外壳配置(南向安全外壳.I安全外壳配置, 模式.C同级模式):
	"""适用于: """
	def __init__(self, a):
		南向安全外壳.I安全外壳配置.__init__(self, a)
	def fs开关(self, a操作 = 操作.E操作.e开启):
		pass
	def f生成密钥(self, a长度 = 1024, a操作 = 操作.E操作.e设置):
		v操作 = 操作.f解析操作(a操作)
		v命令 = "ssh key rsa"
		if 操作.fi减操作(a操作):
			self.f执行当前模式命令(c不 + v命令)
			return
		v命令 += a长度
		v输出 = self.f执行当前模式命令(v命令)
		time.sleep(2)
		self.m设备.f输出(a等待 = True)
	def fs端口号(self, a端口号: int, a操作 = 操作.E操作.e设置):
		if a端口号 < 15001 or 65535 < a端口号:
			raise 异常.X命令("  <15001-65535>  Specify port number")	#ssh port ?得到的提示
		v命令 = 命令.C命令("ssh port")
		v命令 += a端口号
		self.f执行当前模式命令(v命令)
	def fs版本(self, a版本, a操作 = 操作.E操作.e设置):
		pass	#思科nexus系列无命令
	def fs源接口(self, a接口, a操作 = 操作.E操作.e设置):
		v操作 = 操作.f解析操作(a操作)
		v命令 = 命令.C命令("ssh source-interface")
		if 操作.fi加操作(v操作):
			v接口 = 实现接口.f创建接口(a接口)
			v命令 += v接口
		else:
			v命令.f前面添加(c不)
		self.f执行当前模式命令(v命令)
	def fs连接数(self, a数量 = 5, a操作 = 操作.E操作.e设置):
		pass	#思科nexus系列无命令
	def fs认证重试(self, a次数, a操作 = 操作.E操作.e设置):
		v操作 = 操作.f解析操作(a操作)
		v命令 = 命令.C命令("ssh login-attempts")
		if 操作.fi减操作(v操作):
			v命令.f前面添加(c不)
		else:
			v命令 += a次数
		self.f执行当前模式命令(v命令)
	def fs认证超时(self, a时间, a操作 = 操作.E操作.e设置):
		v操作 = 操作.f解析操作(a操作)
		v命令 = 命令.C命令("ssh login-gracetime")
		if 操作.fi减操作(v操作):
			v命令.f前面添加(c不)
		else:
			v命令 += a时间
		self.f执行当前模式命令(v命令)
