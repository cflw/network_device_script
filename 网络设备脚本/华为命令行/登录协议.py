from ..基础接口 import 操作
from ..基础接口 import 协议
from ..基础接口 import 接口 as 北向接口
from ..命令行接口 import 命令
from ..命令行接口 import 模式
from ..命令行接口 import 设备 as 南向设备
from ..命令行接口 import 网络终端 as 南向网络终端
from ..命令行接口 import 安全外壳 as 南向安全外壳
from .常量 import *
class C网络终端(南向网络终端.I网络终端配置, 模式.C同级模式):
	def __init__(self, a):
		南向网络终端.I网络终端配置.__init__(self, a)
	def fs开关(self, a操作 = 操作.E操作.e开启):
		v操作 = 操作.f解析操作(a操作)
		v命令 = 命令.C命令("telnet server enable")
		v命令.f前置否定(操作.fi关操作(v操作), c不)
		self.f执行当前模式命令(v命令)
	def fs端口号(self, a):
		v命令 = 命令.C命令("telnet server port")
		v命令 += a
		self.f执行当前模式命令(v命令)
class C安全外壳(南向安全外壳.I安全外壳配置, 模式.C同级模式):
	def __init__(self, a):
		南向安全外壳.I安全外壳配置.__init__(self, a)
	def fs开关(self, a操作 = 操作.E操作.e开启):
		v操作 = 操作.f解析操作(a操作)
		v命令 = 命令.C命令("stelnet server enable")
		if 操作.fi关操作(v操作):
			v命令.f前面添加(c不)
		v输出 = self.f执行当前模式命令(v命令)
		#Warning: The operation will stop the STelnet server. Continue? [Y/N]:
		if "Continue" in v输出:
			self.m设备.f执行命令("y")
	def f生成密钥(self, a长度 = 1024, a操作 = 操作.E操作.e设置):
		v操作 = 操作.f解析操作(a操作)
		if 操作.fi减操作(v操作):
			raise 异常.X操作(v操作, "华为不支持删除密钥")
		v命令 = 命令.C命令("rsa local-key-pair create")
		v输出 = self.f执行当前模式命令(v命令)
		#The key name will be: Huawei_Host
		#% RSA keys defined for Huawei_Host already exist.
		#Confirm to replace them? [y/n]:
		if "replace" in v输出:
			if v操作 in (操作.E操作.e设置, 操作.E操作.e修改):
				v输出 = self.m设备.f执行命令("y")
			else:
				v输出 = self.m设备.f执行命令("n")
				return
		#The range of public key size is (512 ~ 2048). 
		#NOTES: If the key modulus is greater than 512, 
		#       it will take a few minutes.
		#Input the bits in the modulus[default = 512]:
		if "modulus" in v输出:
			v输出 = self.m设备.f执行命令(a长度)
		#Generating keys...
		#..........++++++++++++
		#.........++++++++++++
		#........................++++++++
		#..............++++++++
		time.sleep(2)
		self.m设备.f输出(a等待 = True)
	def fs端口号(self, a端口号 = 22, a操作 = 操作.E操作.e设置):
		v操作 = 操作.f解析操作(a操作)
		v命令 = 命令.C命令("ssh server port")
		if 操作.fi加操作(v操作):
			v命令 += a端口号
		else:
			v命令.f前面添加(c不)
		self.f执行当前模式命令(v命令)
	def fs超时时间(self, a时间, a操作 = 操作.E操作.e设置):
		"设置认证超时时间"
		v操作 = 操作.f解析操作(a操作)
		v命令 = 命令.C命令("ssh server timeout")
		if 操作.fi加操作(v操作):
			v命令 += a时间
		else:
			v命令.f前面添加(c不)
		self.f执行当前模式命令(v命令)
