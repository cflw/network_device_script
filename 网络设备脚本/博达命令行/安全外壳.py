import time
from ..基础接口 import 操作
from ..命令行接口 import 命令
from ..命令行接口 import 模式
from ..命令行接口 import 安全外壳 as 南向安全外壳
from ..思科命令行.常量 import *
class C安全外壳配置(南向安全外壳.I安全外壳配置, 模式.C同级模式):
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
	def fs会话超时(self, a时间, a操作 = 操作.E操作.e设置):
		v操作 = 操作.f解析操作(a操作)
		v命令 = 命令.C命令("ip sshd timeout")
		v命令 += a时间
		if 操作.fi减操作(v操作):
			v命令.f前面添加(c不)
		self.f执行当前模式命令(v命令)