import time
import cflw代码库py.cflw字符串 as 字符串
from ..基础接口 import 操作
from ..基础接口 import 异常
from ..基础接口 import 安全外壳 as 北向安全外壳
from ..命令行接口 import 命令
from ..命令行接口 import 模式
from ..命令行接口 import 安全外壳 as 南向安全外壳
from .常量 import *
class C安全外壳显示(北向安全外壳.I安全外壳显示, 模式.I显示模式):
	"""适用于:(模拟器)华为S5700-28C-HI(5.110 (S5700 V200R001C00))"""
	def __init__(self, a):
		模式.I显示模式.__init__(self, a)
	def fg服务状态(self):
		v输出 = self.m设备.f执行显示命令("display ssh server status")
		#  SSH version                         :1.99
		#  SSH connection timeout              :60 seconds
		#  SSH server key generating interval  :0 hours
		#  SSH authentication retries          :3 times
		#  SFTP server                         :Disable
		#  Stelnet server                      :Enable
		#  Scp server                          :Disable
		return v输出
	def fg版本(self):
		v服务状态 = self.fg服务状态()
		return 字符串.f提取字符串之间(v服务状态, " SSH version                         :", "\n", a结束严谨 = False)
	def fg访问列表(self):
		v输出 = self.m设备.f执行显示命令("display current-configuration | begin user-interface vty")
		# user-interface vty 0 4
		#  acl 3000 inbound
		#  protocol inbound all
		# #
		# return
		v分割 = v输出.split("user-interface vty")	#可能有多段
		for v节 in v分割[1:]:
			v允许协议 = 字符串.f提取字符串之间(v节, "protocol inbound ", "\n", a结束严谨 = False)
			if v允许协议 in ("all", "ssh"):
				return 字符串.f提取字符串之间(v节, "acl ", " ")	
class C安全外壳配置(南向安全外壳.I安全外壳配置, 模式.C同级模式):
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
	def fs会话超时(self, a时间, a操作 = 操作.E操作.e设置):
		"设置认证超时时间"
		v操作 = 操作.f解析操作(a操作)
		v命令 = 命令.C命令("ssh server timeout")
		if 操作.fi加操作(v操作):
			v命令 += a时间
		else:
			v命令.f前面添加(c不)
		self.f执行当前模式命令(v命令)
