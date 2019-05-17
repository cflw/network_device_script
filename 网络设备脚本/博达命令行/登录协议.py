from ..基础接口 import 操作
from ..基础接口 import 协议
from ..基础接口 import 接口 as 北向接口
from ..命令行接口 import 命令
from ..命令行接口 import 模式
from ..命令行接口 import 设备 as 南向设备
from ..命令行接口 import 网络终端 as 南向网络终端
from ..命令行接口 import 安全外壳 as 南向安全外壳
from .常量 import *
from . import 接口 as 实现接口
class C网络终端(南向网络终端.I网络终端配置, 模式.C同级模式):
	def __init__(self, a):
		南向网络终端.I网络终端配置.__init__(self, a)
	def fs开关(self, a操作 = 操作.E操作.e设置):
		v操作 = 操作.f解析操作(a操作):
		if 操作.fi开操作(v操作):
			self.fs连接数(a操作 = 操作.E操作.e删除)
		else:
			self.fs连接数(0)
	def fs端口号(self, a端口号, a操作 = 操作.E操作.e设置):
		v操作 = 操作.f解析操作(a操作)
		v命令 = 命令.C命令("ip telnet listen-port")
		v命令 += a端口号
		if 操作.fi减操作(v操作):
			v命令.f前面添加(c不)
		self.f执行当前模式命令(v命令)
	def fs源接口(self, a接口, a操作 = 操作.E操作.e设置):
		v操作 = 操作.f解析操作(a操作)
		v命令 = 命令.C命令("ip telnet source-interface")
		if 操作.fi加操作(v操作):
			v接口 = 实现接口.f创建接口(a接口)
			v命令 += v接口
		else:
			v命令.f前面添加(c不)
		self.f执行当前模式命令(v命令)
	def fs连接数(self, a数量 = 5, a操作 = 操作.E操作.e设置):
		v操作 = 操作.f解析操作(a操作)
		v命令 = 命令.C命令("ip telnet max-user")
		if 操作.fi加操作(v操作):
			v命令 += a数量
		else:
			v命令.f前面添加(c不)
		self.f执行当前模式命令(v命令)
class C安全外壳(南向安全外壳.I安全外壳配置, 模式.C同级模式):
	def __init__(self, a):
		南向安全外壳.I安全外壳配置.__init__(self, a)
	def fs开关(self, a操作 = 操作.E操作.e设置):
		v操作 = 操作.f解析操作(a操作)
		v命令 = 命令.C命令("ip sshd enable")
		if 操作.fi关操作(v操作):
			v命令.f前面添加(c不)
		self.f执行当前模式命令(v命令)
		time.sleep(2)
		self.m设备.f输出(a等待 = True)
	def f生成密钥(self, a长度 = 1024, a操作 = 操作.E操作.e设置):
		pass	#没命令
	def fs超时时间(self, a时间, a操作 = 操作.E操作.e设置):
		v操作 = 操作.f解析操作(a操作)
		v命令 = 命令.C命令("ip sshd timeout")
		v命令 += a时间
		if 操作.fi减操作(v操作):
			v命令.f前面添加(c不)
		self.f执行当前模式命令(v命令)